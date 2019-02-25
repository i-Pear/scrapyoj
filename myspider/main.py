#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.cmdline import execute
import os
import sys

# 添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'ojlist', '-o', 'oj.xml'])


def runScrapy(username,password):
    # execute(['scrapy', 'crawl', 'ojlist'])
    execute(['scrapy', 'crawl', 'ojlist', '-o', 'oj.xml'])
