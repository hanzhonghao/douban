# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import codecs
import MySQLdb
class DoubanPipeline(object):
    def __init__(self):
        self.file = codecs.open('doubandata.json', 'w', encoding='utf-8')
        # 取个变量名，连接数据库,依次是: host,user,password,dbname
        self.conn = MySQLdb.connect("127.0.0.1", "root", "123456", "douban",charset='utf8')
        # 通过cursor()的方法获取游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # conn = MySQLdb.connect(
        #     host='localhost',
        #     port=3306,
        #     user='root',
        #     passwd='123456',
        #     db='douban',
        # )
        # 通过获取到的数据库连接conn下的cursor()方法来创建游标。
        # cur = conn.cursor()

        # 要执行的插入sql语句

        insert_sql = """
            insert into doubanmovie(moviename,introduce,star,serialnumber,evaluates,describes)
             VALUES(%s,%s,%s,%s,%s,%s)
              """
        # 执行sql语句,注意后面是元组，将Item中的数据格式化填充到插入语句中
        self.cursor.execute(insert_sql, (item["movie_name"], item["introduce"], item["star"],
                                         item["serial_number"], item["evaluate"], item["describe"]))

        # 将sql语句提交到数据库执行
        self.conn.commit()

        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)
        # return item

    def spider_closed(self, spider):
        self.file.close()
