import requests
import time
import subprocess  # 実行するスクリプトやコマンドに応じて必要なモジュールをインポート

FASTAPI_SERVER = "https://everyone-l-chika.onrender.com"
FASTAPI_SERVER = "http://127.0.0.1:8000"

while True:
    try:
        response = requests.get(f"{FASTAPI_SERVER}/get-command/")
        print(response)
        command = response.json().get('status')
        print(command)
        if command:
            # ここでRaspberry Pi上のコマンドを実行
            print("abc")
            # subprocess.run([command])  # 実際のコマンド実行方法は、実行するスクリプトによって異なります
            subprocess.run(['python', 'kirakiraboshi.py'])
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(1)  # ポーリング間隔
