# -*- coding: utf-8 -*-
import sqlite3


def cailiao():
    sql = r'SELECT name,Number,LastDate,Refresh,Position FROM yuanshen WHERE Status=1 AND Type="材料" ORDER BY Number ASC'
    conn = sqlite3.connect('E:/yuanshen.sqlite3',
                           detect_types=sqlite3.PARSE_DECLTYPES)
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    for i in result:
        if int(i[2]) == 911:
            pass
        else:
            '''
            默认情况下，print() 函数输出后会自动换行，即把输出信息放在下一行。
            如果不想换行，可以使用 end='' 参数。
            此外，使用 flush=True 参数可以实时刷新输出结果。
            '''
            print(i)
    conn.close()


if __name__ == "__main__":
    cailiao()
