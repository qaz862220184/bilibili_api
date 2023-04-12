from fastapi import APIRouter, Query
from bilibili_api.api.dependencies import *

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

@app_user.get('/user_stat/upload_count', summary='相簿投稿数')
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
@app_user.get('/user_relation/followers', summary="查询用户粉丝明细")
def followers(access_key: str = Query(None, description='App登陆Token'), vmid: int = Query(description='目标用户mid'),
              ps: int = Query(50,description='每页数量'), pn: int = Query(1, description='页码')):
    """
    note:: 登录可看自己前1000名，其他用户可查看前250名（网页端请求时ps为20，所以直接查看只能看到前100名）
    :param access_key: App登陆Token
    :param vmid: 目标用户mid
    :param ps: 每页数量
    :param pn: 页码
    :return:
    """
    url = "https://api.bilibili.com/x/relation/followers"
    params = {"access_key": access_key, "vmid": vmid, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/followings', summary="查询用户关注明细")
def followings(access_key: str = Query(None, description='App登陆Token'), vmid: int = Query(description='目标用户mid'),
               ps: int = Query(50, description='每页数量'), pn: int = Query(1, description='页码'),
               order_type: str = Query(None, description='排序方式')):
    """
    :param access_key: App登陆Token
    :param vmid: 目标用户mid
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1,其他用户仅可查看前5页
    :param order_type: 排序方式 -> 按照关注顺序排列：留空, 按照最常访问排列：attention
    :return:
    """
    url = "https://api.bilibili.com/x/relation/followings"
    params = {"access_key": access_key, "vmid": vmid, "ps": ps, "pn": pn, "order_type": order_type}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/followings_2', summary="查询用户关注明细2")
def followings_two(vmid: int = Query(description='目标用户mid'),
               ps: int = Query(50, description='每页数量'), pn: int = Query(1, description='页码')):
    """
    note::仅可查看前5页，可以获取已设置可见性隐私的关注列表
    :param vmid: 目标用户mid
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1,其他用户仅可查看前5页
    :return:
    """
    url = "https://app.biliapi.net/x/v2/relation/followings"
    params = {"vmid": vmid, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/followings_3', summary="查询用户关注明细3")
def followings_three(vmid: int = Query(description='目标用户mid'),
               ps: int = Query(20, description='每页数量'), pn: int = Query(1, description='页码')):
    """
    note::可获取用户所有关注列表，对于设置了可见性隐私的用户会返回空列表
    :param vmid: 目标用户mid
    :param ps: 每页数量 -> 默认为20
    :param pn: 页码 -> 默认为1,其他用户仅可查看前5页
    :return:
    """
    url = "https://line3-h5-mobile-api.biligame.com/game/center/h5/user/relationship/following_list"
    params = {"vmid": vmid, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/search', summary="搜索关注明细")
def search(access_key: str = Query(None, description='App登陆Token'), vmid: int = Query(description='目标用户mid'),
           name: str = Query(description='搜索关键词'),
               ps: int = Query(50, description='每页数量'), pn: int = Query(1, description='页码')):
    """
    note::搜索我的关注列表中关键词 name
    :param access_key: APP登录Token
    :param vmid: 目标用户mid
    :param name: 搜索关键词
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1
    :return:
    """
    url = "https://api.bilibili.com/x/relation/followings/search"
    params = {"access_key": access_key, "vmid": vmid, "name": name, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/same_followings', summary="查询共同关注明细")
def same_followings(access_key: str = Query(None, description='App登陆Token'), vmid: int = Query(description='目标用户mid'),
               ps: int = Query(50, description='每页数量'), pn: int = Query(1, description='页码')):
    """
    :param access_key: APP登录Token
    :param vmid: 目标用户mid
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1
    :return:
    """
    url = "https://api.bilibili.com/x/relation/same/followings"
    params = {"access_key": access_key, "vmid": vmid, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/whispers', summary="查询悄悄关注明细")
def whispers(access_key: str = Query(None, description='App登陆Token'),
               ps: int = Query(50, description='每页数量'), pn: int = Query(1, description='页码')):
    """
    :param access_key: APP登录Token
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1
    :return:
    """
    url = "https://api.bilibili.com/x/relation/whispers"
    params = {"access_key": access_key, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/friends', summary="查询互相关注明细")
def friends(access_key: str = Query(None, description='App登陆Token')):
    """
    :param access_key: APP登录Token
    :return:
    """
    url = "https://api.bilibili.com/x/relation/friends"
    params = {"access_key": access_key}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/blacks', summary="查询黑名单明细")
def blacks(access_key: str = Query(None, description='App登陆Token'), ps: int = Query(50, description='每页数量'),
           pn: int = Query(1, description='页码')):
    """
    :param access_key: APP登录Token
    :param ps: 每页数量 -> 默认为50
    :param pn: 页码 -> 默认为1
    :return:
    """
    url = "https://api.bilibili.com/x/relation/blacks"
    params = {"access_key": access_key, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/modify', summary="操作用户关系")
def blacks(access_key: str = Query(None, description='App登陆Token'), fid: int = Query(description='目标用户mid'),
           act: int = Query(description='操作代码'), re_src: int = Query(description="关注来源代码"),
           csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param fid: 目标用户mid
    :param act: 操作代码 -> 1=>关注, 2=>取关, 3=>悄悄关注, 4=>取消悄悄关注, 5=>拉黑, 6=>取消拉黑, 7=>踢出粉丝
    :param re_src: 关注来源代码 -> 11=>空间, 14=>视频, 115=>文章, 222=>活动页面
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/modify"
    params = {"access_key": access_key, "fid": fid, "act": act, "re_src": re_src, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/batch_modify', summary="批量操作用户关系")
def batch_modify(access_key: str = Query(None, description='App登陆Token'), fid: str = Query(description='目标用户mid'),
           act: int = Query(description='操作代码'), re_src: int = Query(description="关注来源代码"),
           csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    note::批量关注mid=1,2,3,4,5的用户
    :param access_key: APP登录Token
    :param fid: 目标用户mid -> 每个之间用,间隔
    :param act: 操作代码 -> 1=>关注, 5=>拉黑
    :param re_src: 关注来源代码 -> 11=>空间, 14=>视频, 115=>文章, 222=>活动页面
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/batch/modify"
    params = {"access_key": access_key, "fid": fid, "act": act, "re_src": re_src, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/relation', summary="查询用户与自己关系_仅查关注")
def relation(access_key: str = Query(None, description='App登陆Token'), fid: str = Query(description='目标用户mid')):
    """
    :param access_key: APP登录Token
    :param fid: 目标用户mid
    :return:
    """
    url = "https://api.bilibili.com/x/relation"
    params = {"access_key": access_key, "fid": fid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/acc_relation', summary="查询用户与自己关系_互相")
def acc_relation(access_key: str = Query(None, description='App登陆Token'), mid: str = Query(description='目标用户mid')):
    """
    :param access_key: APP登录Token
    :param mid: 目标用户mid
    :return:
    """
    url = "https://api.bilibili.com/x/space/acc/relation"
    params = {"access_key": access_key, "mid": mid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/relations', summary="查询用户与自己关系_互相")
def relations(access_key: str = Query(None, description='App登陆Token'), fids: str = Query(description='目标用户mid')):
    """
    note::批量查询mid=1,2,3,4,5的关系
    :param access_key: APP登录Token
    :param fids: 目标用户mid -> 每个之间用,间隔
    :return:
    """
    url = "https://api.bilibili.com/x/relation/relations"
    params = {"access_key": access_key, "fids": fids}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

"""
    *******
        关注分组相关
    *******
"""

@app_user.get('/user_relation/tags', summary="查询关注分组列表")
def tags(access_key: str = Query(None, description='App登陆Token')):
    """
    :param access_key: APP登录Token
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tags"
    params = {"access_key": access_key}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag', summary="查询关注分组明细")
def tag(access_key: str = Query(None, description='App登陆Token'), tagid: int = Query(description="分组id"),
        order_type: str = Query(None, description="排序方式"), ps: int = Query(50, description='每页数量'),
        pn: int = Query(1, description='页码')):
    """
    :param access_key: APP登录Token
    :param tagid: 分组id -> -10=>特别关注, 0=>默认分组
    :param order_type: 排序方式 -> 按照关注顺序排列：留空, 按照最常访问排列：attention
    :param ps: 每页数量 -> 默认50
    :param pn: 页码 -> 默认1
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag"
    params = {"access_key": access_key, "tagid": tagid, "order_type": order_type, "ps": ps, "pn": pn}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag_user', summary="查询目标用户所在的分组")
def tag_user(access_key: str = Query(None, description='App登陆Token'), fid: int = Query(description="目标用户mid")):
    """
    :param access_key: APP登录Token
    :param fid: 目标用户mid
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag/user"
    params = {"access_key": access_key, "fid": fid}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag_special', summary="查询所有特别关注的mid")
def tag_special(access_key: str = Query(None, description='App登陆Token')):
    """
    :param access_key: APP登录Token
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag/special"
    params = {"access_key": access_key}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag_create', summary="创建分组")
def tag_create(access_key: str = Query(None, description='App登陆Token'), tag: str = Query(description="分组名"),
               csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param tag: 分组名 -> 最长16字符
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag/create"
    params = {"access_key": access_key, "tag": tag, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag_update', summary="重命名分组")
def tag_update(access_key: str = Query(None, description='App登陆Token'), tagid: int = Query(description="分组id"),
               name: str = Query(description="新名称"), csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param tagid: 分组名 -> 分组id
    :param name: 分组名 -> 最长16字符
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag/update"
    params = {"access_key": access_key, "tagid": tagid, "name": name, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tag_delete', summary="删除分组")
def tag_delete(access_key: str = Query(None, description='App登陆Token'), tagid: int = Query(description="分组id"),
               csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param tagid: 分组id
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tag/del"
    params = {"access_key": access_key, "tagid": tagid, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tags_add_user', summary="修改分组成员")
def tags_add_user(access_key: str = Query(None, description='App登陆Token'), tagids: str = Query(description="分组id"),
               fids: str = Query(description="目标用户mid"), csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param fids: 目标用户mid -> 每个之间用,间隔
    :param tagid: 分组id -> 每个之间用,间隔
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tags/addUsers"
    params = {"access_key": access_key, "tagids": tagids, "fids": fids, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tags_copy_users', summary="复制关注到分组")
def tags_copy_users(access_key: str = Query(None, description='App登陆Token'), tagids: str = Query(description="分组id"),
               fids: str = Query(description="目标用户mid"), csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param fids: 待复制的用户mid -> 每个之间用,间隔
    :param tagid: 分组id -> 每个之间用,间隔
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tags/copyUsers"
    params = {"access_key": access_key, "tagids": tagids, "fids": fids, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

@app_user.get('/user_relation/tags_move_users', summary="移动关注到分组")
def tags_move_users(access_key: str = Query(None, description='App登陆Token'), beforeTagids: str = Query(description="原分组id"),
                    afterTagids: str = Query(description="新分组id"),
               fids: str = Query(description="目标用户mid"), csrf: str = Query(None, description="CSRF Token(位于cookie)")):
    """
    :param access_key: APP登录Token
    :param beforeTagids: 原分组id -> 每个之间用,间隔
    :param afterTagids: 新分组id -> 每个之间用,间隔
    :param fids: 待复制的用户mid -> 每个之间用,间隔
    :param csrf: CSRF Token(位于cookie) -> Cookie方式必要
    :return:
    """
    url = "https://api.bilibili.com/x/relation/tags/moveUsers"
    params = {"access_key": access_key, "beforeTagids": beforeTagids, "afterTagids": afterTagids, "fids": fids, "csrf": csrf}
    try:
        response = requests.post(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}

"""
    *******
        检查昵称是否可注册
    *******
"""

@app_user.get('/generic/check/nickname', summary='检查昵称')
def check_nickname(nickName: str = Query(description="目标昵称")):
    """
        :param nickName: 目标昵称 -> 最长为16字符
        :return:
    """
    url = "https://passport.bilibili.com/web/generic/check/nickname"
    params = {"nickName": nickName}
    try:
        response = requests.get(url=url, params=params, headers=header)
        data = response.json()
        return {"code": 1, "message": "请求成功", "data": data}
    except:
        return {"code": -1, "message": "请求失败", "data": {}}
