# -*- coding: utf-8 -*-

"""
Template module from IC4A
"""

import argparse
import textwrap

# IC4A modules
from ic4amainapp import IC4A


class Ic4aModuleTemplate(IC4A):
    """
    Template Class module from IC4A
    """

    def argparser(self):
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
        print "DEBUG: HERE - Template"
        print ""
        parser.add_argument('command')
        parser.add_argument('-o')
        return parser
