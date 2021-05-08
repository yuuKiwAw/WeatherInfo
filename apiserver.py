import uvicorn
import json
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get7daysweather import GETWEATHER

app = FastAPI()

# api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def welcome():
    return {"Welcome to fastAPI by python. No BUG No CRASH. Have a good day."}


# 获取天气信息(中国天气网)
@app.get("/days7weather")
async def weather():
    try:
        weather_json = GETWEATHER.selectinfo()
        # print(weather_json)
        print('获取天气api成功')
        return weather_json
    except IOError as ex:
        print('获取天气api失败')
        print(ex)
        return {'failed'}


@app.get("/days7wea-baidu")
async def weatherbd():    
    try:
        with open('./baidu7daysWea.json', 'r') as f:
            str = f.read()
        weather_json_baidu = json.loads(str)
        print("获取百度天气信息" + time.asctime(time.localtime(time.time())))
        return weather_json_baidu        
    except Exception as ex:
        print('获取百度天气api失败')
        print(ex)
        return {'failed'}
    
if __name__ == "__main__":
    uvicorn.run(app='apiserver:app', host='localhost', port=8000, reload=True, debug=True)
