#!/usr/bin/python
# -*- coding: utf-8 -*-

from whoosh_schema import schema
import csv
import glob

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.analysis import NgramTokenizer

from StringIO import StringIO
from datetime import datetime

ix = open_dir('db')
writer = ix.writer()

for f in sorted(glob.glob("data/*")):
    print f
    cr = csv.reader(file(f),delimiter='\t')
    cr.next()
    for i in cr:
        try:
            writer.update_document(
                book_id=unicode(i[0]),
                number_type=unicode(i[1],'cp932'),
                number=unicode(i[2]),
                title=unicode(i[3],'cp932'),
                volume=unicode(i[4],'cp932'),
                author=unicode(i[5],'cp932'),
                version=unicode(i[6],'cp932'),
                publisher=unicode(i[7],'cp932'),
                year_month=unicode(i[8],'cp932'),
                series_title=unicode(i[9],'cp932'),
                price=unicode(i[10],'cp932'),
                office=unicode(i[11],'cp932'),
                date=datetime.strptime(i[12], '%Y/%m/%d')
                )
        except IndexError:
            pass
writer.commit()



