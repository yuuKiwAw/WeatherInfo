import uvicorn
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


@app.get("/weather")
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

if __name__ == "__main__":
    uvicorn.run(app='apiserver:app', host='localhost', port=8000, reload=True, debug=True)
