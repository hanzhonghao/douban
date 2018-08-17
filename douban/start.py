# coding=utf-8
import time

from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute('scrapy crawl asahi_spider -a ch=1 -a cr=6 -a l=1 -a k=南海 -a t=100 -a o=1'.split())  # 这就是我们在命令行中的代码
    # cmdline.execute("scrapy crawl whoscored_spider".split())  # 这就是我们在命令行中的代码
    cmdline.execute("scrapy crawl douban_spider".split())  # 这就是我们在命令行中的代码
