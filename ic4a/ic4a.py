#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2016 by Marcin Praczko for OSSL

IC4A - Quick console for automation (from different subjects)
"""

# TODO: Fix Not interactive

import sys
# import ic4amainapp
import ic4amodule_main

if __name__ == '__main__':
    IC4A = ic4amodule_main.IC4AModuleMain(sys.argv[0])

    if len(sys.argv) > 1:
        IC4A.non_interactive()
    else:
        IC4A.interactive()
