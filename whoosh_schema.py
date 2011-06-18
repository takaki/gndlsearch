#!/usr/bin/python
# -*- coding: utf-8 -*-


from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import NgramTokenizer

schema = Schema(
    book_id=ID(stored=True, unique=True),
    number_type=TEXT(),
    number=TEXT(stored=True),
    title=NGRAM(stored=True,minsize=1,maxsize=4),
    volume=TEXT(stored=True,
                analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    author=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    version=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    publisher=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    year_month=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    series_title=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    price=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    office=TEXT(stored=True,
               analyzer=NgramTokenizer(minsize=1,maxsize=4)), 
    date=DATETIME(stored=True)
    )


if __name__ == '__main__':
    import os
    try:
        os.mkdir('db')
    except OSError:
        pass
    create_in("db", schema)

