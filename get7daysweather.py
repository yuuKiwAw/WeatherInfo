import requests
import json
from lxml import etree


class GETWEATHER ():
    def getMainPage():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }
        url = 'http://www.weather.com.cn/weather/101190402.shtml'
        response = requests.get(url, headers)
        response.encoding = 'utf-8'
        with open('01.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

    def selectinfo():
        html = etree.parse('01.html', etree.HTMLParser())
        result = html.xpath('//script/text()')
        str_result = result[0].replace('var hour3data=', '')
        dic_result = json.loads(str_result)
        return dic_result


def main():
    # GETWEATHER.getMainPage()
    print(GETWEATHER.selectinfo())


if __name__ == '__main__':
    main()
