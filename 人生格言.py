import requests
from lxml import etree  

# def get_content(url):
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
#     }
#     respone=requests.get(url,headers=headers).content.decode('utf-8')
#     title=etree.HTML(respone).xpath("//div[@class='lside']/div/h1/text()")
#     content=etree.HTML(respone).xpath("//div[@class='lside']/div/div/p/text()")
#     return title,content
# def get_next(url='https://www.mingyannet.com/mingyan/257311586'):
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
#     }
#     base_url='https://www.mingyannet.com'
#     respone=requests.get(url).content.decode('utf-8')
#     url_list=etree.HTML(respone).xpath("//div[@class='pager clearfix']//a[4]/@href")
#     return url_list
# if __name__ == '__main__':
#     s=get_next()
#     if s == None:
#         print("it is over")
#     else:
#         title,content=get_content(s)
#         print(title,content)

    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }