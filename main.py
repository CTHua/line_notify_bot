import time
import requests
import json

# 現在時間
now = time.localtime()
nowDate = time.strftime("%Y%m%d", now)

keys = []
with open("./keys.json", "r") as keyFile:
    keys = json.load(keyFile)
print(keys)

# 讀取json
message = u""
with open(f"./data/{nowDate}.json", encoding="utf-8") as f:
    data = json.load(f)
    message += data["公告"]+"\n"
    for title, value in data["total"].items():
        message += f"{title} {value}\n"
    message += "\n"
    for title, value in data["data"].items():
        if value != 0:
            message += f"{title} {value}\n"
    message += "\n"
    message += data["提醒"]+"\n"

# 發送通知
print(message)
for name, key in keys.items():
    status = requests.get(url="https://notify-api.line.me/api/status",
                          headers={"Authorization": "Bearer " +
                                   key})
    print(name, status.json())
    result = requests.post(url="https://notify-api.line.me/api/notify",
                           headers={"Authorization": "Bearer " +
                                    key},
                           data={"message": message})
    print(name, result.json())
