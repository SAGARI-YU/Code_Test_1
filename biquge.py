import requests
import fake_useragent
from lxml import etree

def get_article_list(url_headers):
    url='https://www.bqg128.com/'
    resp=requests.get(url,headers=url_headers).text
    html=etree.HTML(resp)
    title_name=html.xpath("//div[@class='wrap']/div[@class='type']/div/ul/li/span[2]/a/text()")
    title_person=html.xpath("//div[@class='wrap']/div[@class='type']/div/ul/li/span[3]/text()")
    title_https=html.xpath("//div[@class='wrap']/div[@class='type']/div/ul/li/span[2]/a/@href")
    for i in range(0,len(title_https)):
        title_https[i] ='https://www.bqg128.com/'+title_https[i]
    return dict(zip(title_name,title_person)),dict(zip(title_name,title_https))

def get_article_content(atricl_name,article_dict,headers=None):
    if atricl_name in article_dict[0].keys():
        resp = requests.get(article_dict[1][atricl_name], headers=headers).text
        html = etree.HTML(resp)
        article_content=html.xpath("//div[@class='listmain']/dl/dd/text()")
        return article_content
    else:
        print("没有这个书名")
def main():
    pass

if __name__ == '__main__':
    headers={
       'user - agent':fake_useragent.UserAgent().random
    }
    url_list=get_article_list(headers)
    print(url_list[0].keys())
    name=input('选择你想要的小说:')
    article_content=get_article_content(name,url_list,headers)
    print(article_content)

