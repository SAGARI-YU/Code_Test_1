import requests
from bs4 import BeautifulSoup
import re

def get_content(session,link):
    response = session.get(link)
    soup=BeautifulSoup(response.content,'html.parser')
    title = soup.find('div', class_='c_l_title').h1.text
    contents=soup.find('div',class_='noveContent').text
    try:
        contents = re.sub("十一.*\n|立即.*\n",'',contents).strip()
    except:
        contents = contents
    return title,contents

def get_info(session,index_url):
    response = session.get(index_url)
    soup=BeautifulSoup(response.content,'html.parser')
    filename=soup.find('div',class_='TitleDiv zpxg').h2.text
    filename=re.sub("作品相关",'',filename).strip()
    links=soup.find_all('div',class_='DivTd3') #link = 'https:'+link.a.get('href')
    return filename,links
def download(session,index_url,path):
    filename,links =get_info(session,index_url)
    with open(f'{path}\\{filename}.txt','a',encoding='utf-8') as f:
        for link in links[:10]:
            link='https:'+link.a.get('href')
            # print(link)
            title,content=get_content(session,link)
            f.write(title.strip()+'\n\n')
            f.write(content+'\n\n')
            f.write('--'*40)
            print(f'已完成{title}的下载')

if __name__ =='__main__':
    session=requests.Session()
    index_url="https://b.faloo.com/1448637.html"
    path=r"E:\skill leaner\pythoncode\文档"
    download(session,index_url,path)
    # get_info(session,index_url)

