import requests
from lxml import etree
import threading
from queue import Queue

def url_list(url,headers,q):
    response=requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    res=etree.HTML(response.text)
    list_url=res.xpath('//div[@id="list"]//a/@href')
    list_title=res.xpath('//div[@id="list"]//a/text()')
    for link in list_url:
        q.put(link)

def get_content(url,headers):
    pass

def main():
    headers={
        "cookie":"cf_clearance=kuAEUGhHJIHarAI.wVPghwTvktwLlzsvulNw0zFW73k-1733831197-1.2.1.1-BfBO9WTpy5UvqhSoFCdnNiIr6rlOS35UyH5ii.4M70E.lt8gKLNbXIFv97lnjsWlcCwQQv6oPkmRPhDz.XYeaVrq6yKgOgGEK2GKePmRLUozfNamK6hV3FqWTODjUMfXYt1ToVsguwXtabiIz_rHGHJTKBT2GknkyMgHDLl6vp0boLjw1zVTbR87cPJRcZ4nShBmR3D1Uoa8M21EiHNp1m6t59n8qRfT0uYijoceOHPOMiNJOZXo7CGEgpoN3LlTSqUAavIM5Tw_6mxLURQz.JT5ahdYEco5hGyQ2YcVaDDa_wm7B3Zj5lxZfKg3dFIEwiqr2JlZCn4xWxwrHNvJzO7AzuWXhN813N2SvQgBhhGEfALZqUoLMJ6JV.nSQp0veSNe2EwD2xvrIMQzEJNOSU9KPLB1ARLX2Mh_JnH5IMSni7HZBgRQLpXBrQ84iwnSWEV4w9O62avQmAO2yZ0x5w; jieqiVisitId=article_articleviews%3D1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }
    index_url="https://www.biqooge.com/0_1/"
    q=Queue(maxsize=3000)
    th1=threading.Thread(target=url_list,args=(index_url,headers,q))
    th1.start()

if __name__ == "__main__":
    main()