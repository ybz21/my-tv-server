import json
import os
from typing import Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException, Header
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

TOKEN = os.getenv("TOKEN", "my-tv-server")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

tvlist = []
with open("data/channels.json", "r") as file:
    tvlist = json.load(file)


@app.get("/channels")
async def get_channels():
    return tvlist


@app.post("/channels", response_model=Dict)
async def update_channels(new_tvlist: List[Dict], authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    if token != TOKEN:  # 验证令牌
        raise HTTPException(status_code=401, detail="Invalid token")

    global tvlist
    try:
        with open("data/channels.json", "w") as file:
            json.dump(new_tvlist, file, ensure_ascii=False, indent=4)
        tvlist = new_tvlist
        return {"message": "TV channels updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
