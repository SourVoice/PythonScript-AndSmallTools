import requests
import urllib.request
import json
import time
import sys


# 动态加载网站
class Download(object):
    def __init__(self):
        self.serve = 'https://www.lagou.com/gongsi/searchPosition.json'

        # 副请求
        self.url = 'https://gate.lagou.com/v1/neirong/positions/mark_info?positionIds=8395615%2C7697412%2C7697621' \
                   '%2C7697705%2C5634731%2C8370756%2C8186990%2C8371550%2C8370795%2C7085366 '
        self.headers = {
            'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/89.0.4389.90 Safari/537.36',
            'cookies': 'user_trace_token=20210306135628-751a18b8-f063-4151-9213-4f6cd377e7b6; '
                       'LGUID=20210306135631-e84d5edb-d360-4fb7-b839-e581cbe8ee37; _ga=GA1.2.2052635484.1615010192; '
                       '__lg_stoken__'
                       '=d094d948cd857076ba815d9b4b9771b69012e87d12b6df96181ecbcfc4149a281f1cf40c706e3cd1dedd444f6a7367d1a59b7fb54c58f4a5a596688b9fb58dbb4bd64c43a379; JSESSIONID=ABAAAECABFAACEABE0F6686C06EA109C4827DAFB83C481F; WEBTJ-ID=20210317下午9:35:30213530-178406600e4850-08a3993cfd6466-5771031-1327104-178406600e5b9f; X_HTTP_TOKEN=66e4e54fd793bd7892188951618433cd8c86dd7adb; sensorsdata2015session={}; sensorsdata2015jssdkcross={"distinct_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151","first_id":"","props":{"$latest_traffic_source_type":"引荐流量","$latest_search_keyword":"未取到值","$latest_referrer":"https://www.jianshu.com/","$os":"Windows","$browser":"Chrome","$browser_version":"89.0.4389.90"},"$device_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151"}; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615010192,1615010203,1615886408,1615988130; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615988130; _gat=1; PRE_UTM=; PRE_LAND=https://www.lagou.com/gongsi/j94.html; _gid=GA1.2.252747310.1615988130; LGSID=20210317213529-597f80d3-1853-4806-a065-7b1545620cdd; PRE_HOST=www.jianshu.com; PRE_SITE=https://www.jianshu.com/; TG-TRACK-CODE=hpage_code; LGRID=20210317213706-3ec3e9af-c766-43bd-8da9-0c5f5c7d0585',
            'origin': 'https://www.lagou.com',
            'referer': 'https: // www.lagou.com / gongsi / j94.html',
            'pragma': 'no - cache',
            'accept': 'application / json, text / javascript, * / *; q = 0.01',
            'accept - language': 'zh - CN, zh - TW;q = 0.9, zh; q = 0.8, en - US;q = 0.7, en;q = 0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        # 请求参数
        """"""
        self.pragma = {
            'companyId': '94',
            'positionFirstType': '%E5%85%A8%E9%83%A8',
            'city': '',
            'salary': '',
            'workYour': '',
            'schoolJob': 'false',
            'pageNo': [],
            'pageSize': '10'
        }
        # 加入代理IP
        self.proxy = {
            'https': '202.46.38.11'
        }

    def get_text(self):
        for n in range(1, 5):
            self.pragma['pageNo'].append(n)
            reponse = requests.post(url=dl.serve, params=self.pragma, proxies=self.proxy, timeout=2)
            print(reponse.text.encode('UTF-8'))
            json_data = json.loads(reponse.text)
            print(json_data)
            self.pragma['pageNo'].clear()


# if __name__ == '__main__':
dl = Download()
dl.get_text()
"""
pragma = json.dumps(dl.pragma)
headers = json.dumps(dl.headers)  # str类型
req = requests.post(url=dl.serve, json=dl.pragma, data=dl.headers)
print(json_data)
"""
