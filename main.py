# -*- coding:utf-8 -*-
from parser import Parser
from crawler import Crawler

if __name__ == "__main__":
    #用户名
    #usrnames = ["ruitao","loviselu","laiyonghao","fenng"]
    usrnames = ["litten"]
    for name in usrnames:
        cwl = Crawler(name)
        cwl.start()
        parser = Parser(cwl)
        parser.run()
