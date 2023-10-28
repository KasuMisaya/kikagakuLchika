import json
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 入力するデータ型の定義
class RunCommand(BaseModel):
    id: int
    is_run: bool

class GetCommand(BaseModel):
    id: int

def load_json():
    with open("src/status.json") as f:
        return json.load(f)

def save_json(data):
    with open("src/status.json", "w") as f:
        json.dump(data, f)

@app.get("/")
def index():
    return {"Hello": "Lchika!"}

@app.post("/run-command")
async def run_command(command: RunCommand):
    command_dict = load_json()
    command_dict[str(command.id)] = command.is_run
    print(command_dict)
    save_json(command_dict)
    return {"status": command_dict}

@app.post("/get-command/")
async def get_command(command:GetCommand):
    command_dict = load_json()
    status = command_dict.get(str(command.id), False)
    return {"status": status}

# if __name__ == "__main__":
#     uvicorn.run("webclient_fa:app", host="192.168.2.151", port=8002, reload=True)