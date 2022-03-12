# -*- coding = utf-8 -*-
# @Time : 2022/3/5 14:19
# @File : read_date.py
# @Software : PyCharm
import datetime
import pymysql


# 根据日期获取当天或当月数据，返回主播名称列表，营收额列表，付费人数列表，互动人数列表，最高人气列表
def get_live_history(date):
    connection = connect_to_mysql()
    cur = connection.cursor()
    sql_day = "SELECT name, goldCoin, goldUser, participants, maxPopularity FROM livehistoryday_total WHERE startTime= " + "'" + date + "'"
    sql_month = "SELECT name, goldCoin, goldUser, participants, maxPopularity FROM livehistorymonth_total WHERE liveMonth=" + "'" + date + "'"
    try:
        if len(date) > 9:
            cur.execute(sql_day)
        else:
            cur.execute(sql_month)
        result = cur.fetchall()
        name_list = list()
        gold_list = list()
        user_list = list()
        participants_list = list()
        popularity_list = list()
        for item in result:
            name_list.append(item[0])
            gold_list.append(item[1])
            user_list.append(item[2])
            participants_list.append(item[3])
            popularity_list.append(item[4])
    except Exception:
        print('获取当天数据发生异常', Exception)
        connection.rollback()
    finally:
        cur.close()
        connection.close()
    return name_list, gold_list, user_list, participants_list, popularity_list


# 根据月份获取当月数据
# def get_live_history_month(month):
#     connection = connect_to_mysql()
#     cur = connection.cursor()
#     sql = 'SELECT name, goldCoin, goldUser, participants, maxPopularity FROM livehistorymonth_total WHERE liveMonth=' + month
#     name_list = list()
#     gold_list = list()
#     user_list = list()
#     participants_list = list()
#     popularity_list = list()
#     try:
#         cur.execute(sql)
#         result = cur.fetchall()
#         for item in result:
#             name_list.append(item[0])
#             gold_list.append(item[1])
#             user_list.append(item[2])
#             participants_list.append(item[3])
#             popularity_list.append(item[4])
#     except Exception:
#         print('获取当月数据发生异常', Exception)
#         connection.rollback()
#     finally:
#         cur.close()
#         connection.close()
#     return name_list, gold_list, user_list, participants_list, popularity_list


# 获取数据总览
def summary_data(date):
    connection = connect_to_mysql()
    cur = connection.cursor()
    sql_day = "SELECT goldCoin, goldUser, participants, realDanmaku FROM summary_day WHERE date=" + "'" + date + "'"
    sql_month = "SELECT goldCoin, goldUser, participants, realDanmaku FROM summary_month WHERE month=" + "'" + date + "'"
    if len(date) > 9:
        cur.execute(sql_day)
    else:
        cur.execute(sql_month)
    result = cur.fetchone()
    return result


# 获取数据库内最新数据
def get_last_date(data_type):
    connection = connect_to_mysql()
    cur = connection.cursor()
    sql_month = "SELECT liveMonth FROM livehistorymonth_total ORDER BY liveMonth DESC LIMIT 1"
    sql_day = "SELECT startTime FROM livehistoryday_total ORDER BY startTime DESC LIMIT 1"
    if data_type == 'day':
        cur.execute(sql_day)
    if data_type == 'month':
        cur.execute(sql_month)
    return cur.fetchone()


# 连接数据库
def connect_to_mysql():
    conn = pymysql.connect(host='localhost', user='root', password='0663', database='virtual_data')
    return conn

