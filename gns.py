#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys  

from whoosh_schema import schema
from whoosh.query import *
from whoosh.index import open_dir

import os.path  
try:  
    import pygtk  
    pygtk.require("2.0")  
except:  
    pass  
try:  
    import gtk  
except:  
    sys.exit(1)  
  
class sample2:  
    def __init__(self):  
        gladefile = 'gndlsearch.glade'  
        self.wTree = gtk.Builder()  
        self.wTree.add_from_file(os.path.dirname(os.path.abspath(__file__)) + "/"+gladefile)  
        self.wTree.connect_signals(self)  
        b = self.wTree.get_object("button1")
        b.connect("clicked", self.on_button1_clicked)
        b = self.wTree.get_object("button2")
        b.connect("clicked", self.on_button2_clicked)

        self.textView = self.wTree.get_object("textview1")  
        self.MainWindow = self.wTree.get_object("window1")  
        self.MainWindow.connect("delete-event", gtk.main_quit)
        self.MainWindow.show_all()

  
    def on_button1_clicked(self, widget, event=None):
        self.wTree.get_object('entry1').set_text('')
        self.wTree.get_object('entry2').set_text('')
        self.wTree.get_object('entry3').set_text('')

    def on_button2_clicked(self, widget, event=None):
        ix = open_dir("db")
        with ix.searcher () as searcher:
            # print "AND"
            q = []

            e = self.wTree.get_object('entry1')
            s = e.get_text()
            if s:
                q.append(Term("author", unicode(s,'utf-8')))

            e = self.wTree.get_object('entry2')
            s = e.get_text()
            if s:
                q.append(Term("publisher", unicode(s,'utf-8')))

            e = self.wTree.get_object('entry3')
            s = e.get_text()
            if s:
                q.append(Term("title", unicode(s,'utf-8')))

            results = searcher.search(And(q), limit=300)

            # results.filter(results_2)
            s = ''
            for r in results:
                s += "%s; %s; %s\n" % (r['author'], r['publisher'], r['title'])

            t = self.textView
            b = t.get_buffer()
            b.set_text(s)

    def on_MainWindow_destroy(self,widget):  
        gtk.main_quit()  
  
    def on_btAdd_clicked(self,widget):  
        pass  
  
    def on_btOK_clicked(self,widget):  
        gtk.main_quit()  
  
    def on_btClose_clicked(self,widget):  
        gtk.main_quit()  
  
  
if __name__ == "__main__":  
    sample2()  
    gtk.main()
