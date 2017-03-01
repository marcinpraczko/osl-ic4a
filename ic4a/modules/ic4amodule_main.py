# -*- coding: utf-8 -*-

"""
Main module from IC4A

This is module which should be used for others modules as a base code.
"""

import argparse
import textwrap

# IC4A modules
from ic4amainapp import IC4A


class IC4AModuleMain(IC4A):
    """
    Main Class module from IC4A
    """

    def create_parser(self):
        """Generate 'Argparser' for Main (default) module

        Default main parser has disabled help, and help must be provided
        with others modules. Otherwise the same help is displayed over and
        over.
        """
        # TODO: Move this to mainapp and overwrite once module is loaded
        parser = argparse.ArgumentParser(
            prog=self.progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            usage='%(prog)s [options] <command> [<args>]',
            epilog=textwrap.dedent(
                '''For help on any individual command run `%(prog)s COMMAND -h`'''
            ),
            description=textwrap.dedent(
                self.format_commands_short_help()
            ),
            add_help=False
        )
        parser.add_argument('-h', '--help',
                            action='store_true', dest='module_help')
        parser.add_argument('command', help=argparse.SUPPRESS)
        return parser

    def parse_cmdline_arguments(self, parser):
        """
        Parse command line arguments from provided parser

        :param parser: argparse.ArgumentParser
        :return: args: from parse_args()
        """
        args = parser.parse_args()
        if args.module_help:
            parser.print_help()
        return args

    def format_commands_short_help(self):
        """Format short help display for main commands"""
        # TODO: Add more info about interactive mode to this help
        help_info = ""
        if not self.interactive_mode:
            help_info += "IC4A - Interactive Console For Automation\n\n"
        help_info += "Common commands:\n"
        for key, value in self.main_commands.iteritems():
            # Do not display help when
            if not self.interactive_mode and key in ['cmd_help', 'cmd_exit']:
                continue
            help_info += "  {0:<14}    {1:}\n".format(value['cmd'], value['help'])
        help_info += "\n"
        return help_info
