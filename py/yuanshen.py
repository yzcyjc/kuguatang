# -*- coding: utf-8 -*-
import sqlite3


def cailiao():
    sql = r'SELECT * FROM yuanshen WHERE Status=1 AND Type="材料" ORDER BY Number DESC'
    conn = sqlite3.connect('E:/yuanshen.sqlite3')
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    for i in result:
        print(i[1], encoding='utf-8')

    conn.close()


if __name__ == "__main__":
    cailiao()
