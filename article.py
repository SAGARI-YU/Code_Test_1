import requests
from lxml import etree
import threading
from queue import Queue
import time
import os


flag=False
file_list=[]
def url_list(url,headers,q):
    global flag,file_list
    response=requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    res=etree.HTML(response.text)
    list_url=res.xpath('//div[@id="list"]//a/@href')[:10]
    title_list=res.xpath('//div[@id="list"]//a/text()')[:10]
    file_list=title_list
    for link in list_url:
        link="https://www.biqooge.com"+link
        q.put(link)
    flag =True
def get_content(q,headers,path):
    while True:
        if q.empty() and flag:
            print('已完成全部下载')
            break
        else:
            url=q.get()
            response=requests.get(url,headers=headers)
            response.encoding = response.apparent_encoding
            res=etree.HTML(response.text)
            content=res.xpath('//div[@class="content_read"]/div/div[3]/text()')
            title=res.xpath('//div[@class="bookname"]/h1/text()')[0].replace(', ',"").replace("?","")
            content="".join(content).strip()
            with open(f'{path}/{title}.txt','w',encoding='utf-8') as f:
                f.write(title+'\n\n')
                f.write(content+'\n\n')
                print(f'{threading.current_thread().name}已完成{title}的下载')

def combine(path):
    while not file_list:
        print('未发现file list，等待0.5s')
        time.sleep(0.5)
    fp=open(f'{path}/{time.time()}.txt','a',encoding='utf-8')
    for filename in file_list:
        while True:
            filename=filename[0].replace(', ',"").replace("?","")
            if os.path.isfile(f'{path}/{filename}.txt'):
                with open(f'{path}/{filename}.txt','r',encoding='utf-8') as f:
                    content=f.read()
                    fp.write(content)
                    print(f'已完成{filename}的合并')
                break
            else:
                print(f"为发现{filename},等待0.5s")
                time.sleep(0.5)
    fp.close()
    print('已完成全部文件合并')
                       
        


def main():
    headers={
        "cookie":"jieqiVisitId=article_articleviews%3D1; cf_clearance=zOEatSnr_z6zmB6vRkN8lggzbBr5j.8tmCSZGwRWDc4-1733901876-1.2.1.1-1woc0mQgjPMUSyFEb5MNjbg.esEdIunVuSt11JESnRAy5k2fY62z9fx7C8QsYHEp8QdQIlduYD0VnPxCS0SrS99aXOYZcJX9wZ3.pgvj_ErLrbxlxy8I8qMuXHButujxJX7dZwZRzGNbfynyohb4iv7oSdrePMQ.BnhKE1UlWQV7uutuKHiTBREMetbZp1_K9hkWbfDRteRI376Tq2Y1zcgx.c0I12SUasrbRbyIWzPRhlpihynG.Lkc7YE5BxOL8NP1ASoufKtmlt3Uxqm90bOM.UUflWAheqOUVDLAD8H9OgEv4npOX3bVr8pt4e1yyiScFBK0255OuPoqFzG6ejpFxqEy4TlsweGfe8VK8CMV031O36MzUZQIdalhgLuoeCpH_hlsmoqZ9Bsz73G0lN7iQC3pR7Ghrdjl8gn6lZSQk5I6Bmwzy2HDjzg1F20rTI6QRB6cH.5GKotH2hn_uw",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    index_url="https://www.biqooge.com/0_1/"
    path=r"F:\ZYH\CODE\article"
    q=Queue(maxsize=3000)
    th1=threading.Thread(target=url_list,args=(index_url,headers,q))
    th1.start()
    for i in range(4):
        th2=threading.Thread(target=get_content,args=(q,headers,path),name=f'线程{i}')
        th2.start()
    th3=threading.Thread(target=combine,args=(path,))
    th3.start()
if __name__ == "__main__":
    main()