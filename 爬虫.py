import requests

def get_weather(city=None):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }
    cookie={
        'cookie': 'abc'
    }
    url=f'http://127.0.0.1:8655/get/data?loc={city}'
    r=requests.get(url,headers=headers,cookies=cookie)
    print(r.text)
if __name__=='__main__':
    get_weather()