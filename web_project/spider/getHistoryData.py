# -*- coding = utf-8 -*-
# @Time : 2022/2/21 13:48
# @File : getHistoryData.py
# @Software : PyCharm
import datetime
from time import sleep
import gather
import re


# 获取每日数据
def get_history_data_day(start):
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d').date()
    # 获取当前日期
    end_date = datetime.datetime.today().date()
    while start_date != end_date:
        url_date = str(start_date).replace('-', '/')
        urls = 'https://vup.darkflame.ga/api/ranking/' + url_date + '?datatype=total'
        gather.get_data(urls, live_type='day')
        print(str(start_date) + '数据更新完成')
        start_date = start_date + datetime.timedelta(days=1)


# 获取每月数据
def get_history_data_month(start_month):
    # 正则表达式匹配出年份和月份
    end_month = re.match(pattern=r'^\d{4}-\d{1,2}', string=str(datetime.datetime.today())).group()
    while start_month != end_month:
        url_month = start_month.replace('-', '/')
        urls = 'https://vup.darkflame.ga/api/ranking/' + url_month
        gather.get_data(urls, live_type='month')
        print(start_month + '数据更新完成')
        if int(start_month.split('-')[1]) < 12:
            if int(start_month.split('-')[1]) < 9:
                start_month = start_month.split('-')[0] + '-0' + str(int(start_month.split('-')[1]) + 1)
            else:
                start_month = start_month.split('-')[0] + '-' + str(int(start_month.split('-')[1]) + 1)
        else:
            start_month = str(int(start_month.split('-')[0]) + 1) + '-1'


# 获取每日总结数据
def get_summary_day(start_day):
    start_date = datetime.datetime.strptime(start_day, '%Y-%m-%d').date()
    end_date = datetime.datetime.today().date()
    while start_date != end_date:
        url_date = str(start_date).replace('-', '/')
        urls = 'https://vup.darkflame.ga/api/summary/' + url_date
        gather.get_summary(urls, 'day', start_date)
        print(str(start_date) + '数据更新完成')
        start_date = start_date + datetime.timedelta(days=1)
        sleep(10)


# 获取每月总结数据
def get_summary_month(start_month):
    end_month = re.match(pattern=r'^\d{4}-\d{1,2}', string=str(datetime.datetime.today())).group()
    while start_month != end_month:
        url_month = start_month.replace('-', '/')
        urls = 'https://vup.darkflame.ga/api/summary/' + url_month
        gather.get_summary(urls, 'month', start_month)
        print(start_month + '数据更新完成')
        if int(start_month.split('-')[1]) < 12:
            if int(start_month.split('-')[1]) < 9:
                start_month = start_month.split('-')[0] + '-0' + str(int(start_month.split('-')[1]) + 1)
            else:
                start_month = start_month.split('-')[0] + '-' + str(int(start_month.split('-')[1]) + 1)
        else:
            start_month = str(int(start_month.split('-')[0]) + 1) + '-01'
