# -*- coding: utf-8 -*-

"""
Main module from IC4A
"""

import argparse
import textwrap

# IC4A modules
from ic4amainapp import IC4A

class IC4AModuleMain(IC4A):
    """
    Main Class module from IC4A
    """

    def argparser(self):
        """ArgParser for module: Main

        Default main parser has disabled help, and help must be provided
        with others modules. Otherwise the same help is displayed over and
        over.
        """
        # TODO: Move this to mainapp and overwrite once module is loaded
        # TODO: Maybe is worth to return parser and not only args,
        #       this will allow run commands from parser as well.
        parser = argparse.ArgumentParser(
            prog=self.progname,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            usage='%(prog)s [options] <command> [<args>]',
            epilog=textwrap.dedent(
                '''For help on any individual command run `%(prog)s COMMAND -h`'''
            ),
            description=textwrap.dedent(
                self.format_main_commands_short_help()
            ),
            add_help=False
        )
        parser.add_argument('-h', '--help',
                            action='store_true', dest='module_help')
        parser.add_argument('command', help=argparse.SUPPRESS)
        args = parser.parse_args()
        return args
