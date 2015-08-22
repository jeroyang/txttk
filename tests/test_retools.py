#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""
test_retools
----------------------------------

Tests for `retools` module.
"""

import unittest
from txttk import retools
import re

class RetoolsTestCase(unittest.TestCase):
    def test_condense(self):
        words = ['hello', 'hellokitty', 'hellomonkey', 'goodbye', 'hell', 
                 'he', 'his', 'hi', 'bye', 'history', 'story', 'condense',
                 'hematoma', 'lymphoma']
        regex = retools.condense(words)
        condensed = re.compile(regex)
        for word in words:
            self.assertTrue(condensed.match(word))
            
        negative_words = ['akkk', 'adadkjkl ', 'avxnbcjn']
        for word in negative_words:
            self.assertFalse(condensed.match(word))


