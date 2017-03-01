# -*- coding: utf-8 -*-

"""
Unit test for testing IC4A Application Main Module

Links:
- http://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
- http://stackoverflow.com/questions/18325211/argparse-fails-when-called-from-unittest-test
- http://dustinrcollins.com/testing-python-command-line-apps
- http://docs.python-guide.org/en/latest/writing/tests/   -> This is nice and worth to use it

"""

# IMPORTANT:
# This line is important as described on this issue:
# - https://youtrack.jetbrains.com/issue/PY-20171
from __future__ import absolute_import

import unittest
from ic4a import ic4amodule_main


class MainModule_CommandLineTestCase(unittest.TestCase):
    def setUp(self):
        self.IC4A = ic4amodule_main.IC4AModuleMain('test_ic4a')
        self.parser = self.IC4A.create_parser()

    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_help_args(self):
        """
        User passes help, should display valid usage message
        """
        parsed = self.parser.parse_args(['--help'])
        print "<S>{0}<E>".format(parsed)

if __name__ == '__main__':
    unittest.main()


#     def test_something(self):
#         parsed = self.parser.parse_args(['--something', 'test'])
#         self.assertEqual(parsed.something, 'test')