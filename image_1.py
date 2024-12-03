import requests
import fake_useragent
from lxml import etree

def get_url_list(url,headers):
    list_url=[]
    response=requests.get(url,headers=headers).text
    res=etree.HTML(response,'html')
    urls=res.xpath("//div[@class='slist']/ul/li/a/@href")

if __name__ == "__main__":
    headers={
        "cookie":"cf_clearance=oE0kos7M4azMCItcMzzPVi06B86rH9_b8djJ2NpjtyQ-1733231787-1.2.1.1-HZ9zsywWXPprtz1T691lxJHCWh0GRuiUwNzsW_S3sPjOc3.1MZ8CfHgNTMKZoPq99TNOPB8G9RN6Ljk0JQ37tLnLFklCGA126JTnz_oWuT2KxCBb22aFUGhStb2ib4sVHeJCh8YPGxf_zoyxRfyw1LIkepiySargt4Pq3koiefcTJE3TI32ElKu7ZSz1c7o69u7netFDat9fVXStrEje6s36ymNlXbblHyAvgRaOGCoe5rsnzwS4P.a6YrNq1DaLtk3GMAsdGNPxZqSiBGhVOs9WxWtVA7Zu6y9c1569tMVfQFmnVTtXHLbn..vBWlSU6HWtZgiY4vgsLQDyBk6Py_W3Ceg70R21c39ZmGT6a5EPRwvp9T7TmO7JUyBRWKCtx4go_VLrXBm2TOLnbwWjKyS590RpTph7wUWubFdz4bJHgbs0euGra4SF.8ACr6Y3_iUAoTgLGjwOYb1P6u0rrA; zkhanecookieclassrecord=%2C54%2C66%2C",
        "user-agent":fake_useragent.FakeUserAgent().random,
        "referer":"https://pic.netbian.com/4kdongman/"
    }
    base_url="https://pic.netbian.com/tupian/36399.html"
    response=requests.get(base_url,headers=headers)
    # res=etree.HTML(response,html)
    # urls=res.xpath("//div[@class='slist']/ul/li/a/@href")
    print(response.status_code)