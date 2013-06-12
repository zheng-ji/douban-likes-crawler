# -*- coding:utf-8 -*-
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup
from parse import Parser

#爬虫类
class Crawler():
    def __init__(self,usrname):
        self._usrname = usrname
        self._linklist = []
        if (os.path.exists(os.path.abspath(os.curdir) + "/tmp/") == False):
            os.mkdir(os.path.abspath(os.curdir) + "/tmp/")
        self.localdir =  os.path.abspath(os.curdir) + "/tmp/" + self._usrname + "/"


    def get_content(self):
        link = "http://www.douban.com/people/" + self._usrname + "/likes"
        if (os.path.exists(self.localdir) == False):
            os.mkdir(self.localdir)
        localfile = self.localdir + "list.html"
        urllib.urlretrieve(link,localfile)

    def fill_list(self):
        localfile = self.localdir + "list.html"
        _html = open(localfile)
        content = _html.read()
        soup = BeautifulSoup(content)
        arr = soup.findAll(name="div", attrs={"class":"fav-main"})
        _html.close()
        self._linklist = []
        for item in arr:
           self._linklist.append(item.h3.a.attrs[0][1])

    def start(self):
        self.get_content()
        self.fill_list()

