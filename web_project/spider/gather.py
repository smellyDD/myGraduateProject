# -*- coding = utf-8 -*-
# @Time : 2022/1/7 16:41
# @File : get_data.py
# @Software : PyCharm
import datetime
import json
import re
from time import sleep
import requests
import save
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_data(urls, live_type):
    # 发送请求，获取响应
    payload = {}
    files = {}
    proxies = {}
    headers = {
        'User-Agent': 'PostmanRuntime/7.29.0'
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    response = requests.request("GET", urls, headers=headers, data=payload, files=files, proxies=proxies, verify=False)
    # response = requests.get(url=urls, headers=headers)
    # 获取响应数据
    response.content.decode('utf-8')
    context = json.loads(response.text)
    for i in range(len(context['list'])):
        live_data = list()
        # 获取主播uid
        live_data.append(str(context['list'][i]['liver']['uid']))
        # 获取主播房间号吗
        live_data.append(str(context['list'][i]['liver']['roomId']))
        # 获取主播名称
        live_data.append(context['list'][i]['liver']['name'])
        if live_type == 'day':
            # 获取开播日期
            live_data.append(re.compile(r'^\d{4}-\d{1,2}-\d{1,2}').search(context['updateTime']).group())
            # live_data.append(re.match(pattern=r'^\d{4}-\d{1,2}-\d{1,2}', string=context['list'][i]['data']['startTime']).group())
        if live_type == 'month':
            # 获取最后一次直播的日期
            live_data.append(re.compile(r'^\d{4}-\d{1,2}').search(context['list'][i]['data']['lastLiveTime']).group())
        # 获取直播时长
        live_data.append(format(context['list'][i]['data']['hourOfLive'], '.1f'))
        # 获取弹幕数量
        live_data.append(str(context['list'][i]['data']['realDanmaku']))
        # 获取营收金额
        live_data.append(str(context['list'][i]['data']['goldCoin'] / 1000))
        # 获取人气峰值
        live_data.append(str(context['list'][i]['data']['maxPopularity']))
        # 获取付费人数
        live_data.append(str(context['list'][i]['data']['goldUser']))
        # 获取付费金额超过9人民币的人数
        live_data.append(str(context['list'][i]['data']['goldUserGreaterThen9']))
        # 获取付费金额超过99人民币的人数
        live_data.append(str(context['list'][i]['data']['goldUserGreaterThen99']))
        # 获取发送弹幕的人数
        live_data.append(str(context['list'][i]['data']['realDanmakuUser']))
        # 获取赠送免费礼物的人数
        live_data.append(str(context['list'][i]['data']['silverUser']))
        # 获取互动人数
        live_data.append(str(context['list'][i]['data']['participants']))
        save.update_data(live_data, live_type)


def get_summary(urls, summary_type, renew):
    payload = {}
    files = {}
    proxies = {}
    headers = {
        'User-Agent': 'PostmanRuntime/7.29.0'
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    response = requests.request("GET", urls, headers=headers, data=payload, files=files, proxies=proxies, verify=False)
    # response = requests.get(url=urls, headers=headers)
    # 获取响应数据
    response.content.decode('utf-8')
    context = json.loads(response.text)
    summary_list = list()
    if summary_type == 'day':
        summary_list.append(renew)
        # summary_list.append(re.compile(r'^\d{4}-\d{1,2}-\d{2}').search(context['updateTime']).group())
        # live_data.append(re.match(pattern=r'^\d{4}-\d{1,2}-\d{1,2}', string=context['list'][i]['data']['startTime']).group())
    if summary_type == 'month':
        summary_list.append(renew)
        # summary_list.append(re.compile(r'^\d{4}-\d{1,2}').search(context['updateTime']).group())
    summary_list.append(str(context['data']['realDanmaku']))
    summary_list.append(str(context['data']['goldCoin'] / 1000))
    summary_list.append(str(context['data']['goldUser']))
    summary_list.append(str(context['data']['goldUserGreaterThen9']))
    summary_list.append(str(context['data']['realDanmakuUser']))
    summary_list.append(str(context['data']['silverUser']))
    summary_list.append(str(context['data']['participants']))
    print(summary_list)
    save.update_summary(summary_list, summary_type)
