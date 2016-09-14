# -*- coding: utf-8 -*-

"""
This module deliver code for utilities operations:
Create folders / Copy files / Run commands
"""

import os
import subprocess
import errno


class IC4AUtils(object):
    """
    IC4A class for utilities
    """

    def __init__(self):
        self.test = "This is a test message"
        print self.test

    def os_create_directory(self, path):
        """Create directory based on path argument"""
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    # TODO: From some reason return from wget is display faster then message about download (run init to see)
    def os_run_command(self, command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print "{0}".format(output)
