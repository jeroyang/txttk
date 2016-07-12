#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

from txttk import nlptools, retools, feature

__all__ = ['feature', 'nlptools', 'retools']
__author__ = 'Chia-Jung, Yang'
__email__ = 'jeroyang@gmail.com'

with open('VERSION') as f:
    __version__ = f.read().strip()
