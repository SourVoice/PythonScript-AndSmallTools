import time
import traceback
from multiprocessing.pool import ThreadPool
import requests
from db import MongoDB


def valid_many(proxy_list, method):
    pool = ThreadPool(16)
    for proxy in proxy_list:
        pool.apply_async(valid_one, args=(proxy, method))
    pool.close()
    pool.join()


def valid_one(proxy, method, url='https://www.baidu.com'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    proxies = {
        'http': 'http://' + proxy['proxy'],
        'https': 'http://' + proxy['proxy']
    }
    try:
        start_time = time.time()
        # requests.packages.urllib3.disable_warnings()
        resp = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
        delay = round(time.time() - start_time, 2)
        if resp.status_code == 200:
            proxy['delay'] = delay
        if method == 'insert':
            MongoDB().insert(proxy)
        elif method == 'check':
            MongoDB().update({'proxy': proxy['proxy']}, {'delay': proxy['delay']})
        else:
            if method == 'check':
                MongoDB().delete({'proxy': proxy['proxy']})
    except (ProxyError, ConnectionError):
        if method == 'check':
            MongoDB().delete({'proxy': proxy['proxy']})
    except Exception:
        traceback.print_exc()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        proxies = {
            'http': 'http://' + proxy['proxy'],
            'https': 'http://' + proxy['proxy']
        }
    try:
        start_time = time.time()
        # requests.packages.urllib3.disable_warnings()
        resp = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
        delay = round(time.time() - start_time, 2)
        if resp.status_code == 200:
            proxy['delay'] = delay
        if method == 'insert':
            MongoDB().insert(proxy)
        elif method == 'check':
            MongoDB().update({'proxy': proxy['proxy']}, {'delay': proxy['delay']})
        else:
            if method == 'check':
                MongoDB().delete({'proxy': proxy['proxy']})
    except (ProxyError, ConnectionError):
        if method == 'check':
            MongoDB().delete({'proxy': proxy['proxy']})
    except Exception:
        traceback.print_exc()
