#!/usr/bin/python
# -*- coding: utf8 -*-

import sqlite3
import sys

QUERIES = {'init_tables':'CREATE TABLE Users(Id INT, Name TEXT,Surname TEXT, Mail TEXT)'}

def init():
    try:
        con = sqlite3.connect('santa_secret.db')
        cur = con.cursor()
        cur.execute(QUERIES['init_tables'])
        print('DB initialized')

    except sqlite3.Error, e:
        print("SQLITE3 has returned :%s" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()

if __name__ == '__main__':
    init()
