import json
import streamlit as st
import requests

FASTAPI_SERVER = "http://127.0.0.1:8000"
FASTAPI_SERVER = "https://everyone-l-chika.onrender.com"
headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

st.title('KIKAGAKU Raspberry Pi Controller')

# json ファイルの読み込み
def load_json():
    with open("src/id2name.json") as f:
        return json.load(f)
    
def save_json(data):
    with open("src/id2name.json", "w") as f:
        json.dump(data, f)

dict_id2name = load_json()

# for id, name in id2name.items():
#     st.write(f"{id}: {name}")
#     if st.button('Run Command'):
#         # response = requests.post('http://everyone-l-chika.onrender.com/run-command')
#         response = requests.post('http://127.0.0.1:8000/run-command')
#         if response.ok:
#             st.success("Command was run successfully.")
#         else:
#             st.error("Failed to run the command.")

for key, value in dict_id2name.items():
    st.write(key, value)
    # 列を作成
    col1, col2 = st.columns(2)

    with col1:
        if st.button("ON", key=f"button1_{key}"):
            url = f'{FASTAPI_SERVER}/run-command'
            run_command = {
                "id":key,
                "is_run":True
            }
            response = requests.post(url, headers=headers, data=json.dumps(run_command), timeout=5)
            command = response.json().get("status")
            print(command)
            if response.ok:
                st.success("Command was run successfully.")

    with col2:
        if st.button("OFF", key=f"button2_{key}"):
            url = f'{FASTAPI_SERVER}/run-command'
            run_command = {
                "id":key,
                "is_run":False
            }
            response = requests.post(url, headers=headers, data=json.dumps(run_command), timeout=5)
            command = response.json().get("status")
            print(command)
            if response.ok:
                st.success("Command was run successfully.")

    st.write("---")

name = st.text_input("名前")

if st.button("追加"):
    if name in dict_id2name.values():
        st.error("既に登録されています。")
    else:
        max_key = max(dict_id2name.keys())
        dict_id2name[int(max(load_json().keys())) + 1] = name
        save_json(dict_id2name)
        st.write("追加されました。")