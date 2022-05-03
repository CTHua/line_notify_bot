import time
import requests
import json

# 現在時間
now = time.localtime()
nowDate = time.strftime("%Y%m%d", now)

keys = []
with open("./keys.json", "r", encoding="utf-8") as keyFile:
    keys = json.load(keyFile)
print(keys)

# 讀取json
message = u""
with open(f"./data/{nowDate}.json", encoding="utf-8") as f:
    data = json.load(f)
    #message += data["公告"]+"\n"
    for block in data["blocks"]:
        for title, value in block.items():
            if int(value) != 0:
                message += f"{title} {value}\n"
        message += "\n"
    message += data["提醒"]

# 發送通知
print(message)
print("Start Broadcast:")
for name, key in keys.items():
    print(f"[{name}]")
    status = requests.get(url="https://notify-api.line.me/api/status",
                          headers={"Authorization": "Bearer " +
                                   key})
    status = status.json()
    print(f"BOT狀態: {status['message']}\n群組名稱: {status['target']}\n", end="")
    result = requests.post(url="https://notify-api.line.me/api/notify",
                           headers={"Authorization": "Bearer " +
                                    key},
                           data={"message": message})
    if(result.status_code == 200):
        print("發送成功")
    else:
        print("發送失敗")
