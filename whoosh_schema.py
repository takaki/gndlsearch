#!/usr/bin/python
# -*- coding: utf-8 -*-


from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import NgramTokenizer

schema = Schema(
    book_id=ID(stored=True, unique=True),
    number_type=TEXT(),
    number=NGRAM(stored=True),
    title=NGRAM(stored=True,minsize=1,maxsize=4),
    volume=NGRAM(stored=True,minsize=1,maxsize=4), 
    author=NGRAM(stored=True,minsize=1,maxsize=4), 
    version=NGRAM(stored=True, minsize=1,maxsize=4), 
    publisher=NGRAM(stored=True, minsize=1,maxsize=4), 
    year_month=NGRAM(stored=True, minsize=1,maxsize=4), 
    series_title=NGRAM(stored=True, minsize=1,maxsize=4), 
    price=NGRAM(stored=True, minsize=1,maxsize=4), 
    office=NGRAM(stored=True, minsize=1,maxsize=4), 
    date=DATETIME(stored=True)
    )


if __name__ == '__main__':
    import os
    try:
        os.mkdir('db')
    except OSError:
        pass
    create_in("db", schema)

