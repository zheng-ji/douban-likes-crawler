# -*- coding:utf-8 -*-
import urllib
import os
import re
from BeautifulSoup import BeautifulSoup
import StringIO
import Image, ImageFont, ImageDraw

#unicode function
def u(s, encoding):
    if isinstance(s, unicode):
        return s
    else:
        return unicode(s, encoding)

class Parser():
    def __init__(self,crawler):
        self._crawler = crawler
        self._txt = ''
        self._title = ''

    def _download(self,item):
        self._txt = ''
        self._title = ''

        if (item.find("note") != -1):
            localfile = self._crawler.localdir + item[-10:-1]
            urllib.urlretrieve(item,localfile)

            _html = open(localfile)
            content = _html.read()
            soup = BeautifulSoup(content)
            header = soup.findAll(name="div",attrs={"class":"note-header"})

            if not header:
                header = soup.findAll(name="div",attrs={"class":"note-hd"})
                date_str = soup.findAll(name="span",attrs={"class":"datetime"})[0].string
            else:
                date_str = header[0].span.string

            title =  header[0].h1.string
            post = soup.findAll(name="div",attrs={"id":"link-report"})[0]
            body = post.renderContents().replace("<br />","\n")

            self._txt = str(title) + "\n\n" + str(date_str) + "\n\n" + body
            self._title = title
            _html.close()
            
    #转化为文本    
    def _str_2_txt(self,item):
        output = open(self._crawler.localdir + self._title, 'w+')
        output.write(self._txt)
        output.close()

         
    def run(self):
        for item in self._crawler._linklist:
            if (item.find("note") != -1):
                self._download(item)
                self._str_2_txt(item);
                os.remove(self._crawler.localdir + item[-10:-1])
        os.remove(self._crawler.localdir + "list.html")

        
