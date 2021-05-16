import requests

headers = {

    'cookie': 'user_trace_token=20210306135628-751a18b8-f063-4151-9213-4f6cd377e7b6; '
              'LGUID=20210306135631-e84d5edb-d360-4fb7-b839-e581cbe8ee37; _ga=GA1.2.2052635484.1615010192; '
              '__lg_stoken__'
              '=5069b14dbe3e12e91a85838e9b78870731e12736e5a1e3b7d81b6ed57e0aae6ff668f6af63b7ff1f5f8dae1f56eb3c948c2deb1a3d4234b435f77136d6d9fb8764f059fddc1b; _gid=GA1.2.6347202.1616990864; sensorsdata2015session={}; X_MIDDLE_TOKEN=03fb630aa64db94170ef53ddad05f15b; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617007601,1617007615,1617007639,1617012845; PRE_UTM=; PRE_HOST=; PRE_LAND=https://www.lagou.com/gongsi/j94.html; LGSID=20210329181404-dd7f15d5-3ed6-4958-8d68-d450f3b7e57e; PRE_SITE=; _gat=1; X_HTTP_TOKEN=66e4e54fd793bd7888041071618433cd8c86dd7adb; sensorsdata2015jssdkcross={"distinct_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$os":"Windows","$browser":"Chrome","$browser_version":"89.0.4389.90"},"$device_id":"178061bda2edc-00c39d7d02de21-53e356a-1327104-178061bda2f151"}; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1617014090; LGRID=20210329183520-d0c0ce97-8e34-40ac-ab52-253a6135be30 ',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

}

req = requests.post('https://www.lagou.com/gongsi/searchPosition.json', headers)
print(req.content.decode('UTF-8'))
