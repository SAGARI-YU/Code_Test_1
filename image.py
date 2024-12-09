import requests
from lxml import etree

def image(url,headers):
    pass
    
# def image_url():
#     response=requests.get(base_url,headers=headers)
#     res=etree.HTML(response.text,'lxml')
#     url=res.xpath('//dl[@class="egeli_pic_dl"]//a/@href')
#     return url

if __name__ == "__main__":
    base_url="https://www.enterdesk.com/zhuomianbizhi"
    headers={
        "cookie":"t=5756b273e2ac119003f306f847b59c1d; r=6102; Hm_lvt_86200d30c9967d7eda64933a74748bac=1733733802; HMACCOUNT=2677EC9453ECBF9C; Hm_lpvt_86200d30c9967d7eda64933a74748bac=1733733934",
        "user-agent":"Mozilla/5.0, (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
    response=requests.get("https://www.enterdesk.com/bizhi/64549.html",headers=headers)
    res=etree.HTML(response.text)
    url=res.xpath('//div[@class="swiper-wrapper"]//a/@src')
    title=res.xpath('//div[@id="images_show_zoom"]//a/@title')
    print(title)