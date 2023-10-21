import requests
import time
import subprocess  # 実行するスクリプトやコマンドに応じて必要なモジュールをインポート

FASTAPI_SERVER = "http://192.168.2.151:8002"

while True:
    try:
        response = requests.get(f"{FASTAPI_SERVER}/get-command/")
        command = response.json().get('command')
        print(command)
        if command:
            # ここでRaspberry Pi上のコマンドを実行
            print("abc")
            subprocess.run([command])  # 実際のコマンド実行方法は、実行するスクリプトによって異なります
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(1)  # ポーリング間隔
