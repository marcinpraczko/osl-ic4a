#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2016 by Marcin Praczko for OSSL

IC4A - Quick console for automation (from different subjects)
"""

import sys
import ic4amainapp

if __name__ == '__main__':
    IC4A = ic4amainapp.IC4A(sys.argv[0])

    if len(sys.argv) > 1:
        IC4A.non_interactive()
    else:
        IC4A.interactive()
