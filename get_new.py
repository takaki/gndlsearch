#!/usr/bin/python

import urllib2
from HTMLParser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs = dict(attrs)
            if "href" in attrs:
                self.links.append(attrs["href"])

resp = urllib2.urlopen('http://iss.ndl.go.jp/pbs/news/')

lp = LinkParser()
lp.feed(resp.read().decode('utf-8'))
for i in [ l for l in lp.links if l.find(r'.txt') >= 0]:
    fname = i.split('/')[-1]
    import os
    try:
        os.mkdir('data')
    except OSError:
        pass
    file('data/' + fname, 'w').write(urllib2.urlopen(i).read())
    

