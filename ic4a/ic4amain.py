# -*- coding: utf-8 -*-

import argparse

class IC4A(object):
    """
    Main IC4A (Interactive Console For Automation
    """

    def __init__(self):
        self.version = "0.1"
        self.release = "0.1.0"
        self.console_prompt = "ic4a_console> "
        self.parser_main = argparse.ArgumentParser(
            description='IC4A options - TODO write much more better desc')


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


    def parse_arguments(self):
        """
        Parse arguments with subcommands

        Taken from examples: http://stackoverflow.com/questions/6394328/only-one-command-line-option-with-argparse
        """
        subparsers_main_commands = self.parser_main.add_subparsers(title='Main commands',
                                                                   description='Actions based on commands',
                                                                   help='Main commands help')
        parser_check = subparsers_main_commands.add_parser('check', help='Checking different things')
        parser_todo = subparsers_main_commands.add_parser('todo', help='TODO list')

        # Testing multiple commands - so far is not working as expected, all 3 args are required
        # Is called in argparse - positional arguments
        parser_check.add_argument('arg01', nargs=1)
        parser_check.add_argument('arg02')
        parser_check.add_argument('arg03')

        args = self.parser_main.parse_args()
        print args


    def read_user_commands(self):
        # TODO: Replace me with list or dictionary of commands
        cmd_exit = 'exit'
        while True:
            user_command = raw_input(self.console_prompt)
            user_command = user_command.strip().split()

            # Empty command
            if not user_command:
                continue

            # Run command
            if user_command[0] == cmd_exit:
                print "Exiting from console - See you soon :) ..."
                print ""
                break
            elif user_command[0] == 'help':
                print "For exit - type: 'exit'"
                print "Not implemented yet"
            else:
                print "ERROR: Unknown command"


    def interactive(self):
        """Interactive session"""

        self.banner()
        self.read_user_commands()


    def non_interactive(self):
        """Not interactive session"""

        self.parse_arguments()
