import requests
from lxml import etree
import os
def get_content(url,headers):
    response=requests.get(url,headers=headers)
    res=etree.HTML(response.text)
    url=res.xpath('//div[@class="swiper-wrapper"]//a/@src')
    title=res.xpath('//div[@id="images_show_zoom"]//a/@title')
    return url,title
    
def image_url(url,headers):
    response=requests.get(url,headers=headers)
    res=etree.HTML(response.text)
    url=res.xpath('//dl[@class="egeli_pic_dl"]//a/@href')
    return url

def write_content(url,headers):
    links,titles=get_content(url,headers)
    title=titles[0]
    if not os.path.exists("E:\\skill leaner\\pythoncode\\class1\\图片"):
        os.chdir("E:\\skill leaner\\pythoncode\\class1")
        os.mkdir(f"//图片//{title}")
    for num,link in enumerate(links):
         num +=1
         pic_content=requests.get(link,headers=headers).content
         with open(f"//图片//{title}//{title}{num}.jpg","wb") as f:
              f.write(pic_content)
              print(f"已下载....{title}..编号..{num}")

if __name__ == "__main__":
        headers={
        "cookie":"Hm_lvt_86200d30c9967d7eda64933a74748bac=1733744278; HMACCOUNT=35E8DAA113C64D64; t=10f9355e14d6dc2f18b8ff614526fdc6; r=8989; Hm_lpvt_86200d30c9967d7eda64933a74748bac=1733744970",
        "user-agent":"Mozilla/5.0, (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
        for i in range(1,10):
            base_url=f"https://www.enterdesk.com/zhuomianbizhi/{i}.html"
            url_list=image_url(base_url,headers)
            for url in url_list:
                write_content(url,headers)
