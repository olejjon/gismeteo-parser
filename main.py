import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://www.gismeteo.ru/weather-krasnodar-5136/'


def pogoda_krd_today():
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
                      "Safari/537.36"})
    soup = bs(response.text, 'html.parser')

    data_temperature = []
    temperature = soup.find_all('span', class_='unit unit_temperature_c')
    count = 0
    for i in temperature:
        count += 1
        if count >= 7:
            data_temperature.append(i.text)

    data_precipitation_mm = []
    precipitation = soup.find_all('div', class_='row-item')
    count5 = 0
    for q in precipitation:
        count5 += 1
        if count5 in range(32, 39):
            data_precipitation_mm.append(q.contents[0].next)

    data_msk = {'temperature': data_temperature, 'precipitation_mm': data_precipitation_mm}

    with open('data_pogoda', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data_msk, ensure_ascii=False, indent=4))


pogoda_krd_today()
