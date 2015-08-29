===============================
Text Toolkit: txttk
===============================

.. image:: https://img.shields.io/travis/jeroyang/txttk.svg
        :target: https://travis-ci.org/jeroyang/txttk

.. image:: https://img.shields.io/pypi/v/txttk.svg
        :target: https://pypi.python.org/pypi/txttk


Text Toolkit: manipulate text  & regular expression

* Free software: BSD license
* Documentation: https://txttk.readthedocs.org.

Features
--------
* NLP tools

### nlptools.sent_tokenize(text)
A rule based sentence tokenizer desiged for biomedical papers. It will not cut the text in paired symbols such as '(', ')' and '[', ']'. 

    >>> from nlptoolkit import nlp
    >>> text = """A rule based sentence tokenizer desiged for biomedical papers. (Fig. 1a, we did a good job in this. The accuracy is about 0.9431.)"""
    >>> nlp.sent_tokenize(text)
    ['A rule based sentence tokenizer desiged for biomedical papers.', '(Fig. 1a, we did a good job on this. The accuracy is about 0.94.)']
    
- input: text containing multi-sentences
- output: a list of sentences

### nlptools.sent_count(text)
Segment the give text by sent_tokenzie, and then return its length

    >>> nlp.sent_count(text)
    2

### nlptools.clause_tokenize(sentence)
Split on comma or parenthesis, if there are more then three words for each clause

    >>> nlp.clause_tokenize(sentence)

### nlptools.word_tokenize(sentence)
Cut the sentence in into tokens without deleting anything

### nlptools.slim_stem(token)
A very simple stemmer, for entity of GO stemming

### nlptools.powerset(iterable)
powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

### nlptools.ngram(n, iter_tokens)
Return a generator of n-gram from an iterable

### nlptools.power_ngram(iter_tokens)
Generate unigram, bigram, trigram ... and the max-gram, different from powerset(), this function will not generate skipped combinations such as (1,3)

* RE tools

* TODO
