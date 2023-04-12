from fastapi import FastAPI
import uvicorn

app = FastAPI()

from bilibili_api.api import app_user,app_video

app.include_router(app_user, prefix='/bilibili/api/v/user', tags=["用户"])
app.include_router(app_video, prefix='/bilibili/api/v/video', tags=["视频"])


if __name__ == '__main__':
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=4)
    uvicorn.run("main:app", host="localhost", port=8080, reload=True, workers=4)
