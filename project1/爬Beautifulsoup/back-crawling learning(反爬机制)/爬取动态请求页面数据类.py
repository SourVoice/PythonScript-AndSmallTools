import requests
import urllib.request
import json
import time
import sys


# 动态加载网站


class Download(object):
    def __init__(self):
        self.serve = 'https://www.lagou.com/utrack/trackMid.html?f=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2Fj94.html&t=1615886582&_ti=3'
        self.headers = {
            'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/89.0.4389.82 Safari/537.36',
            'cookies': 'user_trace_token=20210306135628-751a18b8-f063-4151-9213-4f6cd377e7b6; '
                       'LGUID=20210306135631-e84d5edb-d360-4fb7-b839-e581cbe8ee37; _ga=GA1.2.2052635484.1615010192; '
                       '__lg_stoken__'
                       '=d094d948cd857076ba815d9b4b9771b69012e87d12b6df96181ecbcfc4149a281f1cf40c706e3cd1dedd444f6a7367d1a59b7fb54c58f4a5a596688b9fb58dbb4bd64c43a379; JSESSIONID=ABAAAECAAEBABII4BA19AA4C5563974F0CE1757DEB550A4; WEBTJ-ID=20210316下午5:20:02172002-1783a55c58b1ae-0c034176262ab6-5771133-1327104-1783a55c58c750; sensorsdata2015session={}; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615010192,1615010203,1615886408; _gat=1; _gid=GA1.2.1181560578.1615886408; LGSID=20210316172008-b3111e8c-a667-4911-ac0b-2c7e5c241c72; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https://www.lagou.com/gongsi/j94.html; TG-TRACK-CODE=hpage_code; X_MIDDLE_TOKEN=03fb630aa64db94170ef53ddad05f15b; sensorsdata2015jssdkcross={"distinct_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151","first_id":"","props":{"$latest_traffic_source_type":"引荐流量","$latest_search_keyword":"未取到值","$latest_referrer":"https://www.jianshu.com/","$os":"Windows","$browser":"Chrome","$browser_version":"89.0.4389.82"},"$device_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151"}; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1615886573; LGRID=20210316172253-5838dcb1-2af2-4aa3-9e78-880a4000dc40; X_HTTP_TOKEN=66e4e54fd793bd7828568851618433cd8c86dd7adb '
                       '=RDR6VWI4ZmdVSmdLL3V6cTVWTW9tMkMwb2kvNzk4WElQQksvL0VYcWhZMDE2QjZ6MmxUeTRPSDg1TEFxOHlPeVNiajlPU3ZPNTdCYkdTRUZ0MXVQbkgrVk5UMHlsZUpkeHBWYmRudjI0eVhacUFCMXVhNEJVcnAwdFVLRkRPL1dlVUpsVW02VW5RMzEzQ081KzRIcGVSSHUvY2hXaEVuQkJ6VkExNy9jS0ZpRjBDQndZK0VlRjkvOENMaDJ6dEZaZ0wraGU0alpONXUwbHhmVkxLWW9QeU5zYjY4S0EwSnR2Nm9OU3hTMCtYWXRqYmVVN0lQVDgxcGZxR3NXaDJ6bU9XUFl4Q3IxRjY3anE1ZGZIaXNxQ0hWbzdFRmxiTXVVTlJ5T3U5VXE4SHM9LS0wUTA4OGxaOHRvMWpRL3RIYVBETlRBPT0=--80cc9ab04b0eab1283a5338253245810dbad2d29; _gid=GA1.2.2109834900.1615854168; lux_uid=161585416760100511; _sp_ses.0295=*; _sp_id.0295=6ee6b685-6efc-4cc0-8e01-ed0a4ba00fc3.1615008782.3.1615854210.1615114751.b4021ea9-ed22-4d17-88ec-ff9bf0d4f9e2 '

        }


if __name__ == '__main__':
    dl = Download()
    req = requests.get(url=dl.serve, headers=dl.headers)
    json_data = json.loads(req.text.encode('utf-8'))
    print(json_data)
