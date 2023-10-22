from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()
command_to_run = None

@app.get("/")
def index():
    return {"Hello": "World"}

class Command(BaseModel):
    command: str

@app.post("/run-command/")
async def run_command(command: Command):
    global command_to_run
    command_to_run = command.command
    return {"message": "Command was run successfully."}
    

@app.get("/get-command/")
async def get_command():
    global command_to_run
    command = command_to_run
    command_to_run = None  # コマンドをリセット
    return {"command": command}

# if __name__ == "__main__":
#     uvicorn.run("webclient_fa:app", host="192.168.2.151", port=8002, reload=True)