# -*- coding = utf-8 -*-
# @Time : 2022/2/4 17:43
# @File : connect.py
# @Software : PyCharm
import pymysql


def update_data(data, live_type):
    connection = connect_to_mysql()
    # 获取游标
    cursors = connection.cursor()
    if live_type == 'day':
        sql = "INSERT INTO livehistoryday_total (uid, roomID, name, startTime, hourOfLive, realDanmaku, goldCoin, maxPopularity, goldUser, goldUserGreaterThen9, goldUserGreaterThen99, realDanmakuUser, silverUser, participants)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    if live_type == 'month':
        sql = "INSERT INTO livehistorymonth_total (uid, roomID, name, liveMonth, hourOfLive, realDanmaku, goldCoin, maxPopularity, goldUser, goldUserGreaterThen9, goldUserGreaterThen99, realDanmakuUser, silverUser, participants)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # 插入数据
    cursors.execute(sql, data)
    # 提交sql语句
    connection.commit()
    # 关闭游标和数据库连接
    cursors.close()
    connection.close()


def update_summary(data, summary_type):
    connection = connect_to_mysql()
    cursors = connection.cursor()
    if summary_type == 'day':
        sql = "INSERT INTO summary_day (date, realDanmaku, goldCoin, goldUser, goldUserGreaterThen9, realDanmakuUser, silverUser, participants)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    if summary_type == 'month':
        sql = "INSERT INTO summary_month (month, realDanmaku, goldCoin, goldUser, goldUserGreaterThen9, realDanmakuUser, silverUser, participants)"\
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursors.execute(sql, data)
    connection.commit()
    cursors.close()
    connection.close()


def connect_to_mysql():
    return pymysql.connect(host='localhost', user='root', password='0663', database='virtual_data')
