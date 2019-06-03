#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
import logging

log = logging.getLogger("Gxdb")
log.setLevel(logging.DEBUG)

class Gxdb:

    def __init__(self):
        log.info("初始化db")

    def addInfo(self,info):
        db = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="test",charset="utf8")
        cursor = db.cursor()
        args = (info.zuuid,info.type,info.belong,info.locality,info.talent,info.address,info.phone,info.mail,info.web_url)
        sql_1 = "INSERT INTO gx_info(uuid,type,belong,locality,talent,address,phone,mail,web_url) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % \
            args
        cursor.execute(sql_1)
        db.commit()
        db.close()

    def addLine(self,line):
        db = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="test",charset="utf8")
        cursor = db.cursor()
        sql_1 = "INSERT INTO gx_line(v1,v2,v3,v4,v5,v6,v7,v8) VALUES('%s','%s','%s','%s','%s','%s','%s','%s');" % \
                (line.v1,line.v2,line.v3,line.v4,line.v5,line.v6,line.v7,line.v8)
        cursor.execute(sql_1)
        db.commit()
        db.close()