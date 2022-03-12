# -*- coding = utf-8 -*-
# @Time : 2022/3/7 1:38
# @File : DataSource.py
# @Software : PyCharm
import datetime
import getData.read_data as result


class Data:
    def __init__(self, date):
        # 标题
        # self.title = date + '数据概览'
        # 左中部营收柱状图
        self.res = result.get_live_history(date)
        self.mid_left_data = {
            'title': '营收TOP10',
            'xAxis': result.get_live_history(date)[0],
            'values': result.get_live_history(date)[1]
        }
        # 中部数据总览
        self.mid_center_data = {
            'goldCoin': result.summary_data(date)[0],
            'goldUser': result.summary_data(date)[1],
            'participants': result.summary_data(date)[2],
            'realDanmaku': result.summary_data(date)[3]
        }
        # 右中部互动人数柱状图
        self.mid_right_data = {
            'title': '互动人数TOP10',
            'xAxis': result.get_live_history(date)[0],
            'values': result.get_live_history(date)[2],
        }
        # 左下占比图
        self.bottom_left_data = {
            'title': '营收TOP10占比',
            'data': [
                {"name": result.get_live_history(date)[0][0], "value": result.get_live_history(date)[1][0]},
                {"name": result.get_live_history(date)[0][1], "value": result.get_live_history(date)[1][1]},
                {"name": result.get_live_history(date)[0][2], "value": result.get_live_history(date)[1][2]},
                {"name": result.get_live_history(date)[0][3], "value": result.get_live_history(date)[1][3]},
                {"name": result.get_live_history(date)[0][4], "value": result.get_live_history(date)[1][4]},
                {"name": result.get_live_history(date)[0][5], "value": result.get_live_history(date)[1][5]},
                {"name": result.get_live_history(date)[0][6], "value": result.get_live_history(date)[1][6]},
                {"name": result.get_live_history(date)[0][7], "value": result.get_live_history(date)[1][7]},
                {"name": result.get_live_history(date)[0][8], "value": result.get_live_history(date)[1][8]},
                {"name": result.get_live_history(date)[0][9], "value": result.get_live_history(date)[1][9]},
            ]
        }
        # 中下部分人气榜单
        self.bottom_center_data = {
            'title': '人气TOP10',
            'xAxis': result.get_live_history(date)[0],
            'values': result.get_live_history(date)[4]
        }
        # 右下散点分布图
        self.bottom_right_data = {
            'series': [[result.get_live_history(date)[1][i], result.get_live_history(date)[4][i]] for i in range(len(result.get_live_history(date)[1]))],
            type: 'scatter'
        }

    @property
    def mid_left(self):
        data = self.mid_left_data
        ml = {
            'title': data.get('title'),
            'xAxis': data.get('xAxis'),
            'series': data.get('values')
        }
        return ml

    @property
    def mid_center(self):
        data = self.mid_center_data
        md = {
            't1': data.get('goldCoin'),
            't2': data.get('goldUser'),
            't3': data.get('participants'),
            't4': data.get('realDanmaku')
        }
        return md

    @property
    def mid_right(self):
        data = self.mid_right_data
        mr = {
            'title': data.get('title'),
            'xAxis': data.get('xAxis'),
            'series': data.get('values')
        }
        return mr

    @property
    def bottom_left(self):
        data = self.bottom_left_data
        bl = {
            'title': data.get('title'),
            'name': [item.get("name") for item in data.get('data')],
            'series': [item.get("values") for item in data.get('values')]
        }
        return bl

    @property
    def bottom_center(self):
        data = self.bottom_center_data
        bc = {
            'title': data.get('title'),
            'xAxis': data.get('xAxis'),
            'series': data.get('values')
        }
        return bc

    @property
    def bottom_right(self):
        data = self.bottom_right_data
        br = {
            'title': data.get('title'),
            'xAxis': data.get('series')
        }
        return br


# 继承Data类
class Demo(Data):
    def __init__(self, date):
        # super().__init__(str(datetime.datetime.today().date()))
        super().__init__(date)
