# -*-coding:utf-8-*-

import requests
import json
import sys
import time
import uuid


'''
    拉勾网爬虫程序
    2018.1.25
'''


def main():

    # 以utf-8为默认处理字符集（python2默认ascii）
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 西刺代理上采集的免费高可匿代理
    proxies = {
        "http": "http://122.114.31.177:808"
    }

    # 设置爬取url地址
    ajax_url = "https://www.lagou.com/jobs/positionAjax.json"

    # pn为页数
    pn = 1

    while True:

        # 生成动态uuid
        uid = uuid.uuid1()

        # 设置请求头，利用实时生成的uuid伪造cookie
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Origin": "https://www.lagou.com",
            "Host": "www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "Cookie": "_ga=GA1.2.753392604.1516803640; user_trace_token=201801"+str(uid)+"; LGUID=201801"+str(uid)+"-1d03a66c-0112-11e8-ab93-5254005c3644; "+
                      "index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.2037548825.1516968188; X_HTTP_TOKEN=c32c81c0809445229ec3d5b42f331c8a; JSESSIONID=ABAAABAACEBACDGA011945EB2093D529F4A119C2E2FBD54; _gat=1; "+
                      "LGSID=201801"+str(uid)+"; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJmfdC2dOCdNhHd6kwlPwZMvSz6MnICIsiC9NG3T02Ya%26wd%3D%26eqid%3Db6e77cef00039841000000035a6b57d2; "+
                      "PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516803640,1516968188,1516984127; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516984141; "+
                      "LGRID=201801"+str(uid)+"; SEARCH_ID=7bb3b9a282b449d1aca062b7deddb5e4"
        }

        # first设置为false，pn表示第几页，kd表示搜索关键词
        post_param = {"first": "true", "pn": pn, "kd": "java"}

        # 使用post方式，data里存放参数
        r = requests.post(ajax_url, data=post_param, headers=headers, proxies=proxies)

        # json.dumps()方法要禁用ascii编码输出
        result = json.loads(r.text)

        with open(r'C:\Users\Administrator\Desktop\lagou.txt', 'a+') as f:
            # 数据整理格式化
            for num in range(15):
                message = "职位名称：" + result["content"]["positionResult"]["result"][num]["positionName"] + "  " + "公司简称："+result["content"]["positionResult"]["result"][num]["companyShortName"]+ "  " + \
                        "薪资：" + result["content"]["positionResult"]["result"][num]["salary"] + "  " + "所在城市：" + result["content"]["positionResult"]["result"][num]["city"] + "  " + \
                        "经验要求：" + result["content"]["positionResult"]["result"][num]["workYear"] + "  " + "学历要求：" + result["content"]["positionResult"]["result"][num]["education"] + "  " + \
                        "公司规模：" + result["content"]["positionResult"]["result"][num]["companySize"]+"\n"
                # 终端实时打印爬取结果
                print(message)
                f.write(message)

        # 页数自增1
        pn += 1

        # 延时3秒避免ip被封锁
        time.sleep(3)


# 程序入口
if __name__ == '__main__':
    main()