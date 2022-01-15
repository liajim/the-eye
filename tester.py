import threading
import time
from datetime import datetime

import requests

payload = {
    "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
    "category": "page interaction",
    "name": "cta click",
    "data": {
        "host": "www.consumeraffairs.com",
        "path": "/",
        "element": "chat bubble"
    },
    "timestamp": "2021-01-01 09:15:27.243860"
}

response = requests.post("http://localhost:8000/api-token-auth/",
                         data={"username": "your_user", "password": "your_password"})
token = response.json()["token"]

threads = []


def request_task(url, json, headers):
    requests.post(url, json=json, headers=headers)


def fire_and_forget(url, json, headers):
    thread = threading.Thread(target=request_task, args=(url, json, headers))
    thread.start()
    threads.append(thread)


print(datetime.now())
for _ in range(2):
    for index in range(50):
        print(index)
        fire_and_forget("http://localhost:8000/api/event/", json=payload,
                        headers={"Authorization": "Token " + token})
    time.sleep(0.3)
print("done!")
print(datetime.now())
print("waiting 10 seconds!")
time.sleep(10)
print("all finished!")
