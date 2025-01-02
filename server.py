import sys

from flask import Flask, request, render_template
import requests
import json
app=Flask(__name__)

@app.route('/')
def index():
    # city =101160901
    # data=get_weather(city)
    location='天津'
    temp='1'
    desc='小雨'
    # with open('./templates/index.html','r',encoding='utf-8') as f:
    #     content=f.read()
    # return render_template('index.html',location=data['name'],temp=data['temp'],desc=data['desc'])
    return render_template('index.html',location=location,temp=temp,desc=desc)
    # return content

@app.route('/get/data')
def weather_data():
    loc=request.args.get('loc')
    ua=request.headers.get('User-Agent')
    cookie=request.cookies.get('cookie')
    weather='NO DATA'
    if 'python' in ua:
        msg='检测到自动化程序'
    elif not cookie or cookie != 'abc':
        msg='cookie错误'
    else:
        msg='请求正常'
        weather=get_weather(loc)
    # msg = '请求正常'
    # weather=get_weather(loc)
    weather_info={'msg':msg,'data':weather}
    return json.dumps(weather_info)
def get_weather(city_code):
    url=f'http://t.weather.itboy.net/api/weather/city/{city_code}'
    r=requests.get(url)
    data=json.loads(r.text)
    name=data['cityInfo']['city']
    temp=data['data']['wendu']
    desc=data['data']['ganmao']
    weather={'name':name,'temp':temp,'desc':desc}
    return weather
if __name__ == '__main__':
    app.run('127.0.0.1', 8655)
    # print(get_weather('101010100'))