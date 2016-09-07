# -*- coding: utf-8 -*-

"""
This is main module for IC4A
"""

import os
import sys
import argparse
import textwrap

import errno

# TODO: Add help for commands - is not suppored yet
#       Example ic4a.py command -h

class IC4A(object):
    """
    Main IC4A (Interactive Console For Automation)
    """

    def __init__(self, progname):
        self.APPNAME = "ic4a"

        self.interactive_mode = False
        self.version = "0.1"
        self.release = "0.1.0"
        self.console_prompt = "ic4a_console> "

        # TODO: Make sure that valid path is implemented when code is running from python package
        # TODO: On OSX seems that absolute path = relative
        self.appdir = os.path.dirname(__file__)
        self.ic4a_scripts = self.__ic4a_scripts__()

        self.homedir = os.path.expanduser("~")
        self.home_appdir = os.path.join(self.homedir, ".{0}".format(self.APPNAME))
        self.home_workspace_dirs = self.__home_appdirs__()
        # NOTE: http://programmers.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
        # NOTE: http://stackoverflow.com/questions/9168340/python-using-a-dictionary-to-select-function-to-execute
        self.main_commands = {
            'cmd_help': {
                'cmd': 'help',
                'help': 'Display help in interactive section',
                'run': self.command_help
            },
            'cmd_exit': {
                'cmd': 'exit',
                'help': 'Exit from interactive console',
                'run': self.command_exit
            },
            'cmd_init': {
                'cmd': 'init',
                'help': '(To Be Develop) Initial configuration',
                'run': self.command_init
            },
            'cmd_check': {
                'cmd': 'check',
                'help': '(To Be Develop) Check configuration',
                'run': None
            },
            'cmd_template': {
                'cmd': 'template',
                'help': '(To Be Develop) Generate files based on templates',
                'run': None
            },
        }
        self.parser_main = argparse.ArgumentParser(
            prog=progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            usage='%(prog)s [options] <command> [<args>]',
            epilog=textwrap.dedent(
                '''For help on any individual command run `%(prog)s COMMAND -h`'''
            ),
            description=textwrap.dedent(
                self.format_main_commands_short_help()
            )
        )

    def banner(self):
        """
        Generated with http://patorjk.com/software/taag/#p=display&f=Big&t=IC4A
        Plus my own modification (Add spaced between characters)
        """
        nice_banner = r"""
============================================================

  --==<< OSSL (Open Source Solutions Lab) >>==--
       ______     _____    _  _
      |_   _/    / ____|  | || |       /\
        | |     | |       | || |__    /  \
        | |     | |       |__   _/   / /\ \
       _| |_    | |____      | |    / /__\ \
      |_____\    \_____|     |_/   /_/    \_\
    Interactive  Console    For    Automation

============================================================
"""
        print nice_banner
        print ""
        print "Version: {0}".format(self.release)
        print ""
        print "[*] Write 'help' for more details"
        print ""
        print ""

    def format_main_commands_short_help(self):
        """Format main commands short help"""
        help_info = ""
        if not self.interactive_mode:
            help_info += "IC4A - Interactive Console For Automation\n\n"
        help_info += "Common commands:\n"
        for key, value in self.main_commands.iteritems():
            # Do not display help when
            if not self.interactive_mode and key in [ 'cmd_help', 'cmd_exit']:
                continue
            help_info += "  {0:<14}    {1:}\n".format(value['cmd'], value['help'])
        help_info += "\n"
        return help_info

    def command_help(self, args=None):
        """Display help"""
        print self.format_main_commands_short_help()

    def __home_appdirs__(self):
        """Directories which will be created in IC4A config folder"""
        dirs = [ 'download', 'tmp' ]
        return dirs

    def __ic4a_scripts__(self):
        """Directories which IC4A has build in"""
        scripts = {
            'jobs': {
                'ic4a_init_shell_boilr_install':
                    os.path.join(self.appdir, "..", "jobs/ic4a_init/shell/boilr_install.sh")
            }
        }
        return scripts

    # TODO: Move this to another class with this kind of methos (for example utils)
    def os_create_directory(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def command_init(self, args=None):
        """Initial setup for IC4A"""
        print "Creating initial folder if not exists: {0}".format(self.home_appdir)
        self.os_create_directory(self.home_appdir)
        for dir in self.home_workspace_dirs:
            appdir = os.path.join(self.home_appdir, dir)
            self.os_create_directory(appdir)

        # TODO: Replace this to run automatically
        print "Running script for installing boilr"
        print "TODO: Please run this script manually (so far)"
        print "Run script:"
        print "  {0}".format(self.ic4a_scripts['jobs']['ic4a_init_shell_boilr_install'])

    def command_exit(self, args=None):
        """Exit from application"""
        if self.interactive_mode:
            print "Exiting from console - See you soon :) ..."
            print ""
        sys.exit(0)

    def run_commands(self, args=None):
        """
        This function runs command based on input

        :param args: 'ArgParse Namespace' from not-interactive mode or 'List' from interactive mode
        """
        if self.interactive_mode:
            command = args[0]
        else:
            command = args.main_command

        command_exists = False
        for key, value in self.main_commands.iteritems():
            if command == value['cmd']:
                command_exists = True
                if value['run']:
                    # TODO: Add passing arguments here for commands
                    # NOTE: run function from dict with arguments (so far no ARGS: None)
                    value['run'](None)
                else:
                    msg = "[{0}]: {1}".format(value['cmd'], value['help'])
                    print "Only INFO: {0}".format(msg)

        if not command_exists:
            print "\nERROR: Unknown command: {0}\n".format(command)

        if not self.interactive_mode:
            sys.exit(2)

    def parse_cmdline_arguments(self):
        """
        Parse arguments with subcommands
        Taken from examples: http://stackoverflow.com/questions/6394328/only-one-command-line-option-with-argparse
        """

        # NOTE: Have multi commands options - like: git <cmd>, vagrant <cmd>
        self.parser_main.add_argument('main_command', help=argparse.SUPPRESS)
        args = self.parser_main.parse_args()
        self.run_commands(args)

    def read_user_commands(self):
        """
        Read and parse user commands (from interactive mode)
        """
        while True:
            user_command = raw_input(self.console_prompt)
            user_command = user_command.strip().split()

            # Empty command
            if not user_command:
                continue

            self.run_commands(user_command)

    def interactive(self):
        """Interactive session"""

        self.interactive_mode = True
        self.banner()
        self.read_user_commands()

    def non_interactive(self):
        """Not interactive session"""

        self.parse_cmdline_arguments()
