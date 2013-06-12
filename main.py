# -*- coding:utf-8 -*-
from parse import Parser
from crawler import Crawler

if __name__ == "__main__":
    #用户名
    usrnames = ["cloudwu","fenng"]
    for name in usrnames:
        cwl = Crawler(name)
        cwl.start()
        parser = Parser(cwl)
        parser.run()
