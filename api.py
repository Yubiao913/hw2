import requests
import json

# 你找到的流浪動物 API 連結
url = "https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&IsTransData=1"

def fetch_animal_data():
    print("正在擷取流浪動物資料...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # 儲存成 JSON 檔案
        with open('animal_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"成功擷取 {len(data)} 筆資料並儲存為 animal_data.json")
    else:
        print(f"抓取失敗，錯誤代碼：{response.status_code}")

if __name__ == "__main__":
    fetch_animal_data()
