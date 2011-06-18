#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys  

from whoosh_schema import schema

from whoosh.index import open_dir

from whoosh.query import *


ix = open_dir("db")
from whoosh.qparser import QueryParser
with ix.searcher () as searcher:
    query = QueryParser("title", ix.schema).parse(u"あ")
    results = searcher.search(query)
    for r in results:
        print r['title'],r['publisher']
    print len(results)

    query = QueryParser("publisher", ix.schema).parse(u"神")
    results2 = searcher.search(query)
    for r in results2:
        print r['title'],r['publisher']

    print "AND"
    q = And([Term("title", u"あ"), Term("publisher",u"神")])
    rs = searcher.search(q)
    for r in rs:
        print r['title'],r['publisher']
        
