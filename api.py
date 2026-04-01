import requests
import json

# 流浪動物認養 API 連結
url = "https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&IsTransData=1"

def fetch_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # 儲存成 JSON 格式
        with open('animal_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("資料抓取成功並已儲存為 animal_data.json")

if __name__ == "__main__":
    fetch_data()
