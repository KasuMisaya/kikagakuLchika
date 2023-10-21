from fastapi import FastAPI
import uvicorn

app = FastAPI()
command_to_run = None

@app.post("/run-command/")
async def run_command():
    global command_to_run
    command_to_run = "some_command"  # ここに実行したいコマンドを設定
    return {"status": "command set"}

@app.get("/get-command/")
async def get_command():
    global command_to_run
    command = command_to_run
    command_to_run = None  # コマンドをリセット
    return {"command": command}

# if __name__ == "__main__":
#     uvicorn.run("jarvis_webclient_fa:app", host="192.168.2.151", port=8002, reload=True)