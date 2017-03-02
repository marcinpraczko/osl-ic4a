# -*- coding: utf-8 -*-

"""
Template module from IC4A
"""

import argparse
import textwrap

# IC4A modules
from ic4amodule_main import IC4AModuleMain


class Ic4aModuleTemplate(IC4AModuleMain):
    """
    Template Class module from IC4A
    """

    def create_parser(self):
        """ArgParser for module: template"""
        parser = argparse.ArgumentParser(
            prog=self.progname,
            # formatter_class=argparse.RawDescriptionHelpFormatter,
            usage='%(prog)s [options] template [<command>]',
            epilog=textwrap.dedent(
                '''For help on any individual command run `%(prog)s template COMMAND -h`'''
            ),
            description="Description about template module",
        )
        print ""
        print "DEBUG: HERE - Template"
        print ""

        parser.add_argument('-h', '--help',
                            action='store_true', dest='module_help')
        parser.add_argument('templ_command', help=argparse.SUPPRESS)
        return parser

    def parse_cmdline_arguments(self, parser):
        """
        Parse command line arguments from provided parser

        :param parser: argparse.ArgumentParser
        :return: args: from parse_args()
        """
        args = parser.parse_args()
        print "You are in template module"
        # if args.module_help:
        #     parser.print_help()
        return args
