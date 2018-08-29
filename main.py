# Welcome to Proxy Pool System
# /random 获取随机代理
#
# /count 当前代理池总量
#
# 检查周期20s
# 爬取周期300s
#
# 调用与测试方法:


# -*- coding: utf-8 -*-
import requests

PROXY_POOL_URL = 'http://65.49.228.122/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def try_proxy():
    proxy = get_proxy()
    print('随机选择的代理', proxy)

    res = requests.get('http://httpbin.org/get')
    print('真实ip', res.json().get('origin'))

    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print('使用代理后的ip', response.json().get('origin'))
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    try_proxy()