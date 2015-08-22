#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import re
from itertools import chain, combinations, cycle, islice
from collections import namedtuple

def sent_tokenize(context):
    """Cut the given context into sentences. 
    Avoid a linebreak in between paried symbols, float numbers, and some abbr.
    Nothint will be discard after sent_tokeinze, simply ''.join(sents) will get the original context.
    Evey whitespace, tab, linebreak will be kept."""
    
    # Define the regular expression
    paired_symbols = [("(", ")"),
                  ("[", "]"),
                  ("{", "}")]
    paired_patterns = ["%s.*?%s" % (re.escape(lt), re.escape(rt)) for lt, rt in paired_symbols]
    number_pattern = ['\d+\.\d+']
    arr_pattern = ['(?: \w\.){2,3}|(?:\A|\s)(?:\w\.){2,3}|[A-Z]\. [a-z]|\svs\. |et al\.|Fig\. \d|approx\.|(?:Prof|Dr)\. (?:[A-Z]\.)?']
    
    # Find the string which matches the above pattern, and remove than from the context, to get a stem string
    escape_re = re.compile("|".join(paired_patterns + number_pattern + arr_pattern))
    escapes = escape_re.findall(context)
    escaped_stem = escape_re.sub('{}', context)

    escaped_escaped_stem = escaped_stem.replace('{','{{').replace('}', '}}')
    
    # Find the linebreaks 
    sent_re = re.compile(r'([A-Z0-9]..+?(?:[.!?]\s|[\n$]))')
    linebreaks = sent_re.findall(escaped_escaped_stem)
    sent_stem = sent_re.sub(r'\1###linebreak###', escaped_escaped_stem)
    recovered_sent_stem = sent_stem.replace('{{}}', '{}')
    result = recovered_sent_stem.format(*escapes)
    return [r for r in result.split('###linebreak###') if r is not '']

def sent_count(context):
    return len(sent_tokenize(context))

def clause_tokenize(sentence):
    """Split on comma or parenthesis, if there are more then three words for each clause"""
    clause_re = re.compile(r'((?:\S+\s){2,}\S+,|(?:\S+\s){3,}(?=\((?:\S+\s){2,}\S+\)))')
    clause_stem = clause_re.sub(r'\1###clausebreak###', sentence)
    return [c for c in clause_stem.split('###clausebreak###') if c != '']

def word_tokenize(sentence):
    """Cut the sentence in into tokens without deleting anything"""
    number_pattern = r'[\+-]?(\d+\.\d+|\d)'
    arr_pattern = r'(?: \w\.){2,3}|(?:\A|\s)(?:\w\.){2,3}|[A-Z]\. [a-z]'
    word_pattern = r'[\w]+'.format(re.escape('!"#$%&()*,./:;<=>?@[\]^_-`{|}~'))
    non_space_pattern = r'[{}]|\w'.format(re.escape('!"#$%&()*,./:;<=>?@[\]^_-`{|}~'))
    space_pattern = r'\s'
    patterns = [number_pattern, arr_pattern, word_pattern, non_space_pattern, space_pattern]
    big_pattern = r'|'.join([('(' + pattern + ')') for pattern in patterns])
    for match in re.finditer(big_pattern, sentence):
        yield match.group(0)

def slim_stem(token):
    """A very simple stemmer, for entity of GO stemming"""
    target_sulfixs = ['ic', 'tic', 'e', 'ive', 'ing', 'ical', 'nal', 'al', 'ism', 'ion', 'ation', 'ar', 'sis', 'us', 'ment']
    for sulfix in sorted(target_sulfixs, key=len, reverse=True):
        if token.endswith(sulfix):
            return token[0:-len(sulfix)]
    return token  

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def ngram(n, iter_tokens):
    """Return a generator of n-gram from an iterable"""
    z = len(iter_tokens)
    return (iter_tokens[i:i+n] for i in range(z-n+1))

def power_ngram(iter_tokens):
    """Generate unigram, bigram, trigram ... and the max-gram,
     different from powerset(), this function will not generate skipped combinations such as (1,3)"""
    return chain.from_iterable(ngram(j, iter_tokens) for j in range(1, len(iter_tokens) + 1))


