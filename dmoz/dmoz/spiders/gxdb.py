#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
import logging

log = logging.getLogger("Gxdb")
log.setLevel(logging.DEBUG)

class Gxdb:

    def __init__(self):
        log.info("初始化db")

    config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456',
        'port': 3306,
        'database': 'test',
        'charset': 'utf8'
    }

    def addInfo(self):
        db = mysql.connector.connect(self.config)
        cursor = db.cursor()
        cursor.execute("select 1")