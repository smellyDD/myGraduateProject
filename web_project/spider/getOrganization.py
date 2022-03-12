# -*- coding = utf-8 -*-
# @Time : 2022/2/24 18:06
# @File : getOrganization.py
# @Software : PyCharm
import pymysql
import requests
import json


def get_organization():
    urls = 'https://vup.darkflame.ga/api/orgs'
    headers = {
        'User-Agent': 'PostmanRuntime/7.29.0'
    }
    response = requests.get(urls, headers)
    response.content.decode('utf-8')
    context = json.loads(response.text)
    for i in range(len(context)):
        for j in range(len(context[i]['livers'])):
            org_list = list()
            org_list.append(context[i]['livers'][j]['uid'])
            org_list.append(context[i]['livers'][j]['roomId'])
            org_list.append(context[i]['livers'][j]['retire'])
            org_list.append(context[i]['name'])
            org_list.append(context[i]['label'])
            save_data(org_list)
    print('数据更新完成')


def save_data(data):
    connection = pymysql.connect(host='localhost', user='root', password='0663', database='virtual_data')
    cursors = connection.cursor()
    sql = "INSERT INTO organizationLivers_list (livers_uid, livers_roomId, retire, orgs_name, orgs_label)" \
          "VALUES (%s, %s, %s, %s, %s)"
    cursors.execute(sql, data)
    connection.commit()
    cursors.close()
    connection.close()


get_organization()
