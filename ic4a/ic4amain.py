# -*- coding: utf-8 -*-

import argparse
import textwrap

# TODO: Add displaying help from interactive
# TODO: Add help for commands - is not suppored yet

class IC4A(object):
    """
    Main IC4A (Interactive Console For Automation
    """

    def __init__(self, progname):
        self.version = "0.1"
        self.release = "0.1.0"
        self.console_prompt = "ic4a_console> "
        # TODO: Change this dict to main keys as 'cmd_XXX' and add attribute 'cmd'
        #       This will allow add aliases and compare command easier in code instead of hardcoded
        self.main_commands = {
            'cmd_help': {
                'cmd': 'help',
                'help': 'Display help in interactive section',
                'run': None
            },
            'cmd_exit': {
                'cmd': 'exit',
                'help': 'Exit from interactive console',
                'run': None
            },
            'cmd_init': {
                'cmd': 'init',
                'help': '(To Be Develop) Initial configuration',
                'run': None
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
                self.format_main_commands_short_help(interactive_mode=False))
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

    def format_main_commands_short_help(self, interactive_mode=True):
        """Format main commands short help"""
        help=""
        if not interactive_mode:
            help += "IC4A - Interactive Console For Automation\n\n"
        help += "Common commands:\n"
        for key, value in self.main_commands.iteritems():
            # Do not display help when
            if not interactive_mode and key in [ 'cmd_help', 'cmd_exit']:
                continue
            help += "  {0:<14}    {1:}\n".format(value['cmd'], value['help'])
        help += "\n"
        return help

    def parse_arguments(self):
        """
        Parse arguments with subcommands

        Taken from examples: http://stackoverflow.com/questions/6394328/only-one-command-line-option-with-argparse
        """
        # TODO: Have multi commands options - like: git <cmd>, vagrant <cmd>

        self.parser_main.add_argument('main_command', help=argparse.SUPPRESS)
        args = self.parser_main.parse_args()

        # TODO: This is temporary - find different solution
        for key, value in self.main_commands.iteritems():
            if args.main_command == value['cmd']:
                msg = "[{0}]: {1}".format(value['cmd'], value['help'])
                self.run_commands(msg)

    def run_commands(self, command):
        print "Run command: {0}".format(command)

    # TODO: This function should be connected with parse_arguments - somehow - to use the same code
    def read_user_commands(self):
        while True:
            user_command = raw_input(self.console_prompt)
            user_command = user_command.strip().split()

            # Empty command
            if not user_command:
                continue

            # Run command
            if user_command[0] == self.main_commands['cmd_help']['cmd']:
                help = self.format_main_commands_short_help(interactive_mode=True)
                print "{0}".format(help)
            elif user_command[0] == self.main_commands['cmd_exit']['cmd']:
                print "Exiting from console - See you soon :) ..."
                print ""
                break
            else:
                print "ERROR: Unknown command"

    def interactive(self):
        """Interactive session"""

        self.banner()
        self.read_user_commands()

    def non_interactive(self):
        """Not interactive session"""

        self.parse_arguments()
