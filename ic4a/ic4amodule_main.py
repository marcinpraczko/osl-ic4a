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
        """ArgParser for module: main"""
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
