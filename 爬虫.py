import requests

def get_weather():
    url='http://127.0.0.1:8655/get/data?loc=101160701'
    r=requests.get(url)
    print(r.json())

if __name__=='__main__':
    get_weather()