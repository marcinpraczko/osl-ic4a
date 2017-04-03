# -*- coding: utf-8 -*-

"""
This is main module for IC4A
"""

import os
import sys

# IC4A modules
import cli
import ic4autils

# TODO: Add help for commands - is not supported yet
#       Example ic4a.py command -h

class IC4A(object):
    """
    Main IC4A (Interactive Console For Automation)
    """

    def __init__(self):
        self.APPNAME = "ic4a"
        self.active_module = None

        self.interactive_mode = False
        self.version = "0.1"
        self.release = "0.1.0"
        self.console_prompt = "ic4a_console> "

        # TODO: Make sure that valid path is implemented when code is running from python package
        # TODO: On OSX seems that absolute path = relative
        self.appdir = os.path.dirname(__file__)
        self.ic4a_scripts = self.__ic4a_scripts__()
        self.ic4a_templates_boilr = self.__ic4a_templates_boilr__()

        self.homedir = os.path.expanduser("~")
        self.home_appdir = os.path.join(self.homedir, ".{0}".format(self.APPNAME))
        self.home_bindir = os.path.join(self.homedir, "bin")
        self.home_workspace_dirs = self.__home_appdirs__()
        self.arguments_parser = None

        # NOTE: Load dynamically 'Main module' only from this module
        #       do not following code from inherited classes
        if self.__module__ == 'ic4amainapp':
            # print ""
            # print "DEBUG: TODEL: Module Name: {0}".format(self.__module__)
            # print ""
            self.__import_main_module__()

        # NOTE: http://programmers.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
        # NOTE: http://stackoverflow.com/questions/9168340/python-using-a-dictionary-to-select-function-to-execute
        # TODO: This commands should be taken from modules folder - just option to consider
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
                'help': '(WIP: Under development) Initial configuration',
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
                'run': self.command_template,
                'module_name': 'ic4amodule_template',
                'module_class': 'Ic4aModuleTemplate',
            },
        }

    # TODO: Disabled this - seems be no longer required
    # def __import_main_module__(self):
    #     module_name = 'ic4amodule_main'
    #     class_module = 'IC4AModuleMain'
    #     self.__import_module__(module_name, class_module)

    # TODO: Disabled this - seems be no longer required
    # def __import_module__(self, module_name, class_name):
    #     """Import dynamically module from 'modules' dir"""
    #     try:
    #         module = importlib.import_module('modules.{0}'.format(module_name))
    #         loaded_class = getattr(module, class_name)
    #         # TODO: Loaded module is using progname / add module name to change prompt?
    #         self.active_module = loaded_class(self.progname)
    #         self.arguments_parser = self.active_module.create_parser()
    #     except Exception as e:
    #         print "ERROR: {0}".format(e.message)
    #         sys.exit(2)

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

    def __ic4a_templates_boilr__(self):
        """Directories with templates for boilr"""
        templates_boilr = {
            # TODO: Make this dynamic based on sub-folders
            # NOTE: Do not use underscore - boilr is not like this for template TAG
            'ic4atesttemplate': os.path.join(self.appdir, "..", "templates/boilr/ic4a-test-template"),
            'ic4avagrantsimple': os.path.join(self.appdir, "..", "templates/boilr/ic4a-vagrant-simple")
        }
        return templates_boilr

    def banner(self):
        """
        Generated with http://patorjk.com/software/taag/#p=display&f=Big&t=IC4A
        Plus my own modification (Add spaced between characters)
        """
        nice_banner = r"""
============================================================

      --==<< OSL (Open Solutions Lab) >>==--
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

    def command_help(self, args=None):
        """Display help from active (imported) module"""
        # TODO: Disabled this - seems be no longer required
        # help_details = self.active_module.format_commands_short_help()
        # print help_details
        pass

    def command_init(self, args=None):
        """Initial setup for IC4A"""
        IC4AUtils = ic4autils.IC4AUtils()

        print "Creating initial folder if not exists: {0}".format(self.home_appdir)
        IC4AUtils.os_create_directory(self.home_appdir)
        for dir in self.home_workspace_dirs:
            appdir = os.path.join(self.home_appdir, dir)
            IC4AUtils.os_create_directory(appdir)

    def command_exit(self, args=None):
        """Exit from application"""
        if self.interactive_mode:
            print "Exiting from console - See you soon :) ..."
            print ""
        sys.exit(0)

    def command_template(self, args=None):
        """Run template module"""
        print "In template module"

    def run_commands(self, args=None):
        """
        This function runs command based on input

        :param args: 'ArgParse Namespace' from not-interactive mode or 'List' from interactive mode
        """
        if self.interactive_mode:
            command = args[0]
        else:
            command = args.command

        command_exists = False
        for key, value in self.main_commands.iteritems():
            if command == value['cmd']:
                command_exists = True
                if value['run']:
                    value['run'](args)
                else:
                    msg = "[{0}]: {1}".format(value['cmd'], value['help'])
                    print "Only INFO: {0}".format(msg)

        if not command_exists:
            print "\nERROR: Unknown command: {0}\n".format(command)

        if not self.interactive_mode:
            sys.exit(2)

    def parse_cmdline_arguments(self):
        """Parse arguments from module"""
        # TODO: Add error message if active_module is not valid
        args = None
        if self.active_module:
            args = self.active_module.parse_cmdline_arguments(self.arguments_parser)
        print args
        if args.command:
            print "Detected command"
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
        cli.main()
