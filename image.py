import requests
from   hyper.contrib import HTTPConnection
def image_list(url,headers):
    response=requests.get(f'{url}+"4kmeinv/"',headers=headers)
    
def image_url():
    pass

if __name__ == "__main__":
    base_url="https://pic.netbian.com"
    headers={
        ":authority":"pic.netbian.com",
        "referer":"https://pic.netbian.com/4k/index_61.html",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0, (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
with  HTTPConnection(host="https://pic.netbian.com/",secure=True) as con:
    response=con.request("GET","/4kmeinv/",headers=headers)
    rsp=con.get_response(response)
    rsp_code=rsp.status()
    rsp_text=rsp.read().decode()
    print(rsp_code)
    print(rsp_text)