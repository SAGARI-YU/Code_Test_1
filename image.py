import requests
from lxml import etree
import os
def get_content(url,headers):
    response=requests.get(url,headers=headers)
    links=etree.HTML(response.text).xpath('//div[@class="swiper-wrapper"]//img/@src')
    titles=etree.HTML(response.text).xpath('//div[@class="swiper-wrapper"]//img/@title')
    return titles,links
    
def image_url(url,headers):
    response=requests.get(url,headers=headers)
    res=etree.HTML(response.text).xpath('//div[@class="egeli_pic_li"]//a/@href')
    return res

def download_image(url,headers):
    titles,links=get_content(url,headers)
    title=titles[0]
    if not os.path.exists(f"/ZYH/CODE/图片/{title}"):
        os.makedirs(f"/ZYH/CODE/图片/{title}")
        for num,link in enumerate(links):
            num +=1
            pic_content=requests.get(link,headers=headers).content
            with open(f"/ZYH/CODE/图片/{title}/{title}{num}.jpg","wb") as f:
                f.write(pic_content)
                print(f"已下载....{title}..编号..{num}")

if __name__ == "__main__":
    headers={
        "cookie":"t=8de4c8cd41c9156be468fdbe7368eff8; r=2103; Show_Size=images_show_zoom2; Hm_lvt_86200d30c9967d7eda64933a74748bac=1733733802,1733794814,1733796308; HMACCOUNT=2677EC9453ECBF9C; Hm_lpvt_86200d30c9967d7eda64933a74748bac=1733799082",
        "user-agent":"Mozilla/5.0, (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }
    for i in range(1,5):
        next_url=f"https://www.enterdesk.com/zhuomianbizhi/{i}.html"
        image_url_lists=image_url(next_url,headers)
        for image_url in image_url_lists:
            download_image(image_url,headers)
