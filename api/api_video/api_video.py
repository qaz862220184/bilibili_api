from fastapi import APIRouter, Query
from bilibili_api.api.dependencies import *

app_video = APIRouter()
"""
    *******
        视频基本信息
    *******
"""
@app_video.get("/video_base_info/web-interface/view", summary="获取视频详细信息(web端)")
def web_view(aid: int = Query(None, description="稿件avid"), bvid: str = Query(None, description="稿件bvid")):
    """
    note:: aid 和 bvid 必须有一个
    :param aid: 稿件avid
    :param bvid: 稿件bvid
    :return:
    """
    url = "https://api.bilibili.com/x/web-interface/view"
    params = {"aid": aid, "bvid": bvid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_video.get("/video_base_info/web-interface/view/detail", summary="获取视频超详细信息(web端)")
def web_view_detail(aid: int = Query(None, description="稿件avid"), bvid: str = Query(None, description="稿件bvid")):
    """
    note:: aid 和 bvid 必须有一个
    :param aid: 稿件avid
    :param bvid: 稿件bvid
    :return:
    """
    url = "https://api.bilibili.com/x/web-interface/view/detail"
    params = {"aid": aid, "bvid": bvid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_video.get("/video_base_info/web-interface/archive/desc", summary="获取视频简介")
def web_archive_desc(aid: int = Query(None, description="稿件avid"), bvid: str = Query(None, description="稿件bvid")):
    """
    note:: aid 和 bvid 必须有一个
    :param aid: 稿件avid
    :param bvid: 稿件bvid
    :return:
    """
    url = "https://api.bilibili.com/x/web-interface/archive/desc"
    params = {"aid": aid, "bvid": bvid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_video.get("/video_base_info/web-interface/player/pagelist", summary="查询视频分P列表 (avid/bvid转cid)")
def player_pagelist(aid: int = Query(None, description="稿件avid"), bvid: str = Query(None, description="稿件bvid")):
    """
    note:: aid 和 bvid 必须有一个
    :param aid: 稿件avid
    :param bvid: 稿件bvid
    :return:
    """
    url = "https://api.bilibili.com/x/player/pagelist"
    params = {"aid": aid, "bvid": bvid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

"""
    *******
        视频基本信息
    *******
"""
@app_video.get("/video_stat/stat", summary="视频状态数（仅avid）")
def stat(aid: int = Query(None, description="稿件avid")):
    """
    :param aid: 稿件avid
    :return:
    """
    url = "https://api.bilibili.com/archive_stat/stat"
    params = {"aid": aid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_video.get("/video_stat/web-interface/archive/stat", summary="视频状态数（bvid/avid）web端")
def web_archive_stat(aid: int = Query(None, description="稿件avid"), bvid: str = Query(None, description="稿件bvid")):
    """
    note:: aid 和 bvid 必须有一个
    :param aid: 稿件avid
    :param bvid: 稿件bvid
    :return:
    """
    url = "https://api.bilibili.com/x/web-interface/archive/stat"
    params = {"aid": aid, "bvid": bvid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}




