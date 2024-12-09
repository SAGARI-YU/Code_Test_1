import requests
import fake_useragent
from lxml import etree
from bs4 import BeautifulSoup
import re

def get_next_url(url,headers):
    response=requests.get(url,headers=headers)
    res=BeautifulSoup(response.text,'lxml')
    next_url=res.xpath("//div[@class='pager clearfix']/li/a[4]/@href")
    return next_url[0]

# def get_next_url(url,headers):
#     response=requests.get(url,headers=headers)
#     res=etree.HTML(response.content.decode("utf8"))
#     next_url=res.xpath("//div[@class='pager clearfix']/li/a[4]/@href")
#     return next_url[0]

# def get_content(url,headers):
#     response=requests.get(url,headers=headers)
#     res=etree.HTML(response.content.decode("utf8"))
#     title=(res.xpath("//div[@id='article']/h1/text()"))
#     motto=res.xpath("//div[@id='article']/div[2]/p/text()")
#     return title,motto

def get_content(url,headers):
    response=requests.get(url,headers=headers)
    res=BeautifulSoup(response.text,'lxml')
    title=(res.find_all('#article'))
    motto=res.find_all('div','txt')
    return title,motto

def write_motto(title,motto):
    with open(f'{title}.txt','w') as f:
        f.write(title)
        for i in motto:
            f.write(i.encode('utf-8'))   
if __name__ == "__main__":
    base_url="https://www.mingyannet.com"
    url="https://www.mingyannet.com/mingyan/257311586"
    next_url=True
    headers={
        "referer":"https://cn.bing.com/",
        "upgrade-insecure-requests":"1",
        "user-agent":fake_useragent.FakeUserAgent().edge,
        }
    flag=True
    while flag:
        if next_url:
            title,content=get_content(url,headers)
            #write_motto(title,content)
            next_url=get_next_url(url,headers)
            url=base_url+next_url
        else:
            flag=False
    # print(response.content.decode('utf8'))

