from fastapi import APIRouter, Query
from dependencies import *

app_user = APIRouter()
"""
    *******
        用户基本信息
    *******
"""
@app_user.get('/user_info/space_info', summary="用户空间详细信息") # tags=["用户基本信息"]
async def space_info(mid: int = Query(description='用户ID')):
    url = "https://api.bilibili.com/x/space/acc/info"
    params = {"mid": mid}
    # 添加cookie可查看自己的信息
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_info/cart_info', summary="用户名片信息") # tags=["用户基本信息"]
async def cart_info(mid: int = Query(description='用户ID'), photo: bool = Query(None, description='是否请求用户主页头图')):
    url = "https://api.bilibili.com/x/web-interface/card"
    params = {"mid": mid, "photo": photo}
    # 添加cookie可查看自己的信息
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_info/space_myinfo', summary="登录用户空间详细信息") # tags=["用户基本信息"]
async def space_myinfo(sessdata: str = Query(description='登录信息')):
    url = "https://api.bilibili.com/x/space/myinfo"
    new_header = header.update({"SESSDATA": sessdata})
    # 添加cookie可查看自己的信息
    try:
        response = requests.get(url=url, headers=new_header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_info/carts_info', summary="多用户详细信息") # tags=["用户基本信息"]
async def carts_info(mid: str = Query(description='用户ID,用,分隔')):
    url = "https://api.vc.bilibili.com/account/v1/user/cards"
    params = {"uids": mid}
    # 添加cookie可查看自己的信息
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

"""
    *******
        用户状态数
    *******
"""
@app_user.get('/user_stat/relation_stat', summary="关系状态数")
async def relation_stat(access_key: str = Query(None, description="app登录token,app方式必要"), vmid: int = Query(description="目标用户mid")):
    url = "https://api.bilibili.com/x/relation/stat"
    params = {"access_key": access_key, "vmid": vmid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}
########### 这个接口有问题，后面再看一下url是否正常
@app_user.get('/user_stat/space_upstat', summary = "UP主状态数", include_in_schema = False)
async def space_upstat(access_key: str = Query(None, description="app登录token,app方式必要"), mid: int = Query(description="目标用户mid")):
    url = "https://api.bilibili.com/x/space/upstat"
    params = {"access_key": access_key, "mid": mid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('user_stat/upload_count', summary='相簿投稿数')
async def upload_count(uid: int = Query(description="目标用户mid")):
    url = "https://api.vc.bilibili.com/link_draw/v1/doc/upload_count"
    params = {"uid": uid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

"""
    *******
        用户关系相关
    *******
"""

