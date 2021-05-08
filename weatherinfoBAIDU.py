import requests
import json
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup

class WEATHER_BAIDU ():
    # 获取百度天气数据
    # 导出html页面信息
    def get_bdwea_cs():
        url = 'http://weathernew.pae.baidu.com/weathernew/pc?query=%E5%B8%B8%E7%86%9F%E5%A4%A9%E6%B0%94&srcid=4982&city_name=%E8%8B%8F%E5%B7%9E&province_name=%E6%B1%9F%E8%8B%8F'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

        response = requests.get(url, headers)
        strHtml = response.text.encode('utf-8').decode('unicode_escape')

        with open('./baiduweather.html','w', encoding='utf-8') as f:
            f.write(strHtml)


    # 筛选数据
    def ex_bdcs_info():
        with open('./baiduweather.html', 'r', encoding='utf-8') as f:
            try:
                source_html = f.read()
                soup = BeautifulSoup(source_html, 'html.parser')
                data = str(soup.find("script"))  # 找到位于头部的script内容
                formatStr = data.replace('<script>window.tplData = ', '').replace(';</script>', '')
            except Exception as ex:
                print('筛选数据失败！检查获取到的信息！')
                print(ex)

        try:
            # 重新整理并筛选Json数据
            dictData = json.loads(formatStr)
            # d1 = dictData['15_day_forecast']['info'][0]    
            bdweaCS_Data_Dict = {}
            bdweaCS_Data_Json = json.loads(json.dumps(bdweaCS_Data_Dict))
            i = 0
            while i < 8:
                date = dictData['15_day_forecast']['info'][i]['date']  # 日期
                wind_direction_day = dictData['15_day_forecast']['info'][i]['wind_direction_day']  # 风向
                wind_power_day = dictData['15_day_forecast']['info'][i]['wind_power_day']  # 风量
                temperature_night = dictData['15_day_forecast']['info'][i]['temperature_night']  # 夜晚气温
                temperature_day = dictData['15_day_forecast']['info'][i]['temperature_day']  # 白天气温
                weather_day = dictData['15_day_forecast']['info'][i]['weather_day']  # 白天天气
                
                # print(date, temperature_night, temperature_day, weather_day, wind_direction_day, wind_power_day)
                temp = temperature_night + "~" + temperature_day + "℃"
                fxfs = wind_direction_day + wind_power_day
                
                bdweaCS_Data_Json[date] = {'temp': temp, 'tq': weather_day, 'fxfs': fxfs}
                i += 1
            
            finalDict = json.dumps(bdweaCS_Data_Json, ensure_ascii=False)
            with open('./baidu7daysWea.json', 'w') as f:
                f.write(finalDict)
                print('已导出json文件')
        except Exception as ex:
            print(ex)
    

    
if __name__ == '__main__':
    WEATHER_BAIDU.ex_bdcs_info()
