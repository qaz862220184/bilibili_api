
### 原项目github地址：https://github.com/SocialSisterYi/bilibili-API-collect
### 此项目为参考原项目做的简易封装


<p align="center">
    <img src="./assets/img/logo.png" width="250" height="200">
</p>
<h1 align="center">哔哩哔哩-API收集整理</h1>
<p align="center">
    <a href="https://github.com/SocialSisterYi/bilibili-API-collect/issues" style="text-decoration:none">
        <img src="https://img.shields.io/github/issues/SocialSisterYi/bilibili-API-collect.svg" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/SocialSisterYi/bilibili-API-collect/stargazers" style="text-decoration:none" >
        <img src="https://img.shields.io/github/stars/SocialSisterYi/bilibili-API-collect.svg" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/SocialSisterYi/bilibili-API-collect/network" style="text-decoration:none" >
        <img src="https://img.shields.io/github/forks/SocialSisterYi/bilibili-API-collect.svg" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/SocialSisterYi/bilibili-API-collect/actions">
        <img src="https://img.shields.io/github/actions/workflow/status/SocialSisterYi/bilibili-API-collect/vuepress-deploy.yml">
    </a>
    <a href="https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/LICENSE" style="text-decoration:none" >
        <img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg" alt="GitHub license"/>
    </a>
</p>
<h3 align="center">野生API文档</h3>
<h3 align="center">不断更新中....</h3>

本项目旨在对 B站 WEB、APP、TV 等客户端中，散落在世界各地的野生 API 进行收集整理，研究使用方法并对其进行说明，运用了黑箱法、控制变量法、代码逆向分析、拆包及反编译法、网络抓包法等研究办法

本文档探讨的对象是主站业务接口，[官方开放平台](https://openhome.bilibili.com/doc) 和 [直播开放平台](https://open-live.bilibili.com/document/) 均不属于本项目范畴，请移步

B站 API 采用 C/S 结构，大多数接口为 REST API 和 gRPC，少部分接口为 WebSocket；REST API 接口请求数据大多为 url query 表单或 JSON，返回数据大多为 JSON 或 Protobuf，强制使用 https 协议

📖阅读地址：[GithubPages](https://socialsisteryi.github.io/bilibili-API-collect/)

小小的 Demo：~~av583785685~~ [视频失效原因](https://shakaianee.top/archives/56/) ([Youtube备链](https://www.youtube.com/watch?v=nfF91Z6fqGk))

::: warning ⚠️声明

1. 本项目遵守 CC-BY-NC 4.0 协议，禁止一切商业使用，如需转载请注明作者 ID
2. **请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！**
3. 利用本项目提供的接口、文档等造成不良影响及后果与本人无关
4. 由于本项目的特殊性，可能随时停止开发或删档
5. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容

:::


## 🍴目录

计划整理分类 & 目录：(文档已完结请选中 checkbox) 

- [ ] [API 签名](docs/other/API_sign.md)
- [ ] [公共错误码](docs/other/errcode.md)
- [ ] [图片格式化](docs/other/picture.md)
- [ ] [bvid 说明](docs/other/bvid_desc.md)
- [ ] [gRPC API 接口定义](grpc_api)
- [ ] [登录](docs/login)
  - [ ] [登录操作 (人机认证)](docs/login/login_action)
    - [ ] [短信登录](docs/login/login_action/SMS.md)
    - [ ] [密码登录](docs/login/login_action/password.md)
    - [ ] [二维码登录](docs/login/login_action/QR.md)
    - [ ] SNS 登录 (QQ & 微信 & 微博)
  - [ ] [登录基本信息](docs/login/login_info.md)
  - [ ] [个人中心](docs/login/member_center.md)
  - [ ] [注销登录](docs/login/exit.md)
  - [ ] [登录记录](docs/login/login_notice.md)
- [ ] [消息中心](docs/message)
  - [ ] [通知类消息](docs/message/msg.md)
  - [ ] [私信](docs/message/private_msg.md)
  - [ ] 设置
- [ ] [用户](docs/user)
  - [x] [基本信息](docs/user/info.md)
  - [x] [状态数](docs/user/status_number.md)
  - [x] [关系](docs/user/relation.md)
  - [ ] [个人空间](docs/user/space.md)
  - [x] [检查昵称是否可注册](docs/user/check_nickname.md)
  - [ ] [用户注册](docs/user/register.md)
- [ ] [大会员](docs/vip)
  - [ ] [大会员基本信息](docs/vip/info.md)
  - [ ] [大会员中心](docs/vip/center.md)
  - [ ] [大会员签到](docs/vip/clockin.md)
  - [ ] [大会员操作](docs/vip/action.md)
- [ ] [视频](docs/video)
  - [ ] [视频分区一览 (分区代码)](docs/video/video_zone.md)
  - [x] [基本信息](docs/video/info.md)
  - [x] [状态数](docs/video/status_number.md)
  - [ ] [快照](docs/video/snapshot.md)
  - [ ] [点赞 & 投币 & 收藏 & 分享](docs/video/action.md)
  - [ ] [TAG](docs/video/tags.md)
  - [ ] [视频推荐](docs/video/recommend.md)
  - [ ] [播放&下载地址 (视频流)](docs/video/videostream_url.md)
  - [ ] [互动视频](docs/video/interact_video.md)
  - [ ] [高能进度条](docs/video/pbp.md)
  - [ ] [信息上报 (心跳及记录历史)](docs/video/report.md)
  - [ ] [视频属性数据](docs/video/attribute_data.md)
  - [ ] [视频在线人数](docs/video/online.md)
- [ ] [剧集 (番剧、影视)](docs/bangumi)
  - [ ] [基本信息](docs/bangumi/info.md)
  - [ ] [播放&下载地址（视频流）](docs/bangumi/videostream_url.md)
  - [ ] [时间轴](docs/bangumi/timeline.md)
  - [ ] 状态数
  - [ ] 操作
- [ ] [视频弹幕](docs/danmaku)
  - [ ] [protobuf 实时弹幕](docs/danmaku/danmaku_proto.md)
  - [ ] [protobuf 弹幕元数据（BAS 弹幕 / 互动弹幕）](docs/danmaku/danmaku_view_proto.md)
  - [ ] [xml 实时弹幕](docs/danmaku/danmaku_xml.md)
  - [ ] [历史弹幕](docs/danmaku/history.md)
  - [ ] [快照](docs/danmaku/snapshot.md)
  - [ ] [弹幕操作](docs/danmaku/action.md)
  - [ ] 高级弹幕
  - [ ] 屏蔽管理
  - [ ] 智能防挡弹幕
  - [ ] [弹幕个人配置修改](docs/danmaku/config.md)
  - [ ] [名词解释](docs/danmaku/buzzword.md)
- [ ] [视频笔记](docs/note)
  - [ ] [笔记列表](docs/note/list.md)
  - [ ] [笔记详细信息](docs/note/info.md)
  - [ ] [笔记操作](docs/note/action.md)
- [ ] [专栏](docs/article)
  - [ ] 分区
  - [ ] [基本信息](docs/article/info.md)
  - [ ] [点赞 & 投币 & 收藏 & 分享](docs/article/action.md)
  - [ ] [文集基本信息](docs/article/articles.md)
  - [ ] [获取用户专栏文章列表](docs/article/list.md)
- [ ] [音频](docs/audio)
  - [ ] [歌曲基本信息](docs/audio/info.md)
  - [ ] [歌单 & 音频收藏夹详细信息](docs/audio/music_list.md)
  - [ ] [状态数](docs/audio/status_number.md)
  - [ ] [投币 & 收藏](docs/audio/action.md)
  - [ ] [播放 & 下载地址（音频流）](docs/audio/musicstream_url.md)
  - [ ] 音频榜单
- [ ] [排行榜 & 最新视频](docs/video_ranking)
  - [ ] [排行榜](docs/video_ranking/ranking.md)
  - [ ] [热门视频](docs/video_ranking/popular.md)
  - [ ] [最新视频](docs/video_ranking/dynamic.md)
  - [ ] [入站必刷视频](docs/video_ranking/precious_videos.md)
- [ ] [搜索](docs/search)
  - [ ] [搜索请求](docs/search/search_request.md)
  - [ ] [搜索结果](docs/search/search_response.md)
  - [ ] [默认搜索 & 热搜](docs/search/hot.md)
  - [ ] [搜索建议](docs/search/suggest.md)
- [ ] [小黑屋](docs/blackroom)
  - [ ] 基本信息
  - [ ] [封禁公示](docs/blackroom/banlist.md)
  - [ ] [风纪委员及众裁案件相关](docs/blackroom/jury)
    - [ ] [风纪委员基本信息](docs/blackroom/jury/base_info.md)
    - [ ] [众裁案件基本信息](docs/blackroom/jury/judgement_info.md)
    - [ ] [裁决操作](docs/blackroom/jury/action.md)
- [ ] [评论区](docs/comment)
  - [ ] [评论区明细](docs/comment/list.md)
  - [ ] [操作](docs/comment/action.md)
- [ ] [表情](docs/emoji)
  - [ ] [表情及表情包信息](docs/emoji/list.md)
  - [ ] [操作](docs/emoji/action.md)
- [ ] [创作中心](docs/creativecenter)
  - [ ] [统计与数据](docs/creativecenter/statistics&data.md)
  - [ ] 列表查询相关
  - [ ] [电磁力数据](docs/creativecenter/railgun.md)
- [ ] [实时广播（通讯协议）](docs/broadcast)
  - [ ] [视频内广播](docs/broadcast/video_room.md)
- [ ] [充电](docs/electric)
  - [ ] [包月充电操作](docs/electric/monthly.md)
  - [ ] [自定义充电（B币方式）](docs/electric/Bcoin.md)
  - [ ] [自定义充电（微信 & 支付宝方式）](docs/electric/WeChat&Alipay.md)
  - [ ] [充电留言](docs/electric/charge_msg.md)
  - [ ] [充电列表](docs/electric/charge_list.md)
- [ ] [动态](docs/dynamic)
  - [ ] [动态基本信息](docs/dynamic/basicInfo.md)
  - [ ] [发送 & 转载动态](docs/dynamic/publish.md)
  - [ ] [根据关键字搜索用户（at 别人时的填充列表）](docs/dynamic/atlist.md)
  - [ ] [操作](docs/dynamic/action.md)
  - [ ] 动态列表
    - [ ] [特定话题动态列表](docs/dynamic/tag_dynamics.md)
  - [ ] [动态内容](docs/dynamic/get_dynamic_detail.md)
- [ ] [相簿](docs/album)
  - [ ] [基本信息](docs/album/info.md)
  - [ ] [相簿列表](docs/album/list.md)
  - [ ] [推荐作者](docs/album/recommend_author.md)
  - [ ] [活动列表](docs/album/activity_list.md)
  - [ ] [操作](docs/album/action.md)
  - [ ] 投稿
- [ ] [历史记录 & 稍后再看](docs/history&toview)
  - [ ] [历史记录](docs/history&toview/history.md)
  - [ ] [稍后再看](docs/history&toview/toview.md)
- [ ] [收藏夹](docs/fav)
  - [ ] [基本信息](docs/fav/info.md)
  - [ ] [收藏夹内容](docs/fav/list.md)
  - [ ] [收藏夹操作](docs/fav/action.md)
- [ ] [课程](docs/cheese)
  - [ ] [课程基本信息](docs/cheese/info.md)
  - [ ] 已购课程
  - [ ] 分区推荐列表
  - [ ] 操作
  - [ ] [播放 & 下载地址（视频流）](docs/cheese/videostream_url.md)
- [ ] [直播](docs/live)
  - [ ] [直播间基本信息](docs/live/info.md)
  - [ ] [直播分区](docs/live/live_area.md)
  - [ ] [直播间管理](docs/live/manage.md)
  - [ ] 直播间操作
  - [ ] [直播视频流](docs/live/live_stream.md)
  - [ ] [直播信息流](docs/live/message_stream.md)
  - [ ] [直播红包](docs/live/redpocket.md)
  - [ ] [直播间用户实用 API](docs/live/user.md)
- [ ] [转正答题](docs/newbie_exam)
  - [ ] [查询信息](docs/newbie_exam/info.md)
  - [ ] [拉取题目](docs/newbie_exam/fetch.md)
  - [ ] [操作](docs/newbie_exam/action.md)
- [ ] B币钱包
  - [ ] 基本信息
  - [ ] B币充值
  - [ ] 贝壳相关
- [ ] [哔哩哔哩漫画](docs/manga)
  - [ ] [用户信息](docs/manga/user.md)
  - [ ] [签到](docs/manga/ClockIn.md)
  - [ ] [积分商城](docs/manga/point_shop.md)
  - [ ] [漫画操作](docs/manga/Comic.md)
  - [ ] [漫画赛季](docs/manga/Season.md)
  - [ ] [漫读券/已购相关](docs/manga/User.md)
  - [ ] [下载](docs/manga/Download.md)
  - [ ] [data.index解析](docs/manga/index_file.md)
- [ ] 哔哩哔哩游戏
- [ ] [终端网络查询](docs/clientinfo)
  - [ ] [基于ip的地理位置查询](docs/clientinfo/ip.md)
  - [ ] [终端信息查询](docs/clientinfo/client_info.md)
- [ ] [其他](docs/other)
  - [ ] [获取当前时间戳](docs/other/time_stamp.md)
- [ ] [web端组件](docs/web_widget)
  - [ ] [分区当日投稿数](docs/web_widget/zone_upload.md)
  - [ ] [404 页漫画收集](docs/web_widget/404_manga.md)
- [ ] [APP端组件](docs/APP_widget)
  - [ ] [开屏图片 + 恰饭珍贵录像](docs/APP_widget/splash.md)
- [ ] [个性装扮](docs/garb)
  - [ ] [APP 主题](docs/garb/skin.md)
  - [ ] [主题色](docs/garb/color.md)



## 🔗相关项目推荐

### 库及文档

- [jingyuexing/bilibiliAPI](https://github.com/jingyuexing/bilibiliAPI)
- [fython/BilibiliAPIDocs](https://github.com/fython/BilibiliAPIDocs)
- [czp3009/bilibili-api](https://github.com/czp3009/bilibili-api)
- [Vespa314/bilibili-api](https://github.com/Vespa314/bilibili-api)
- [wnstar/bili-utils](https://github.com/wnstar/bili-utils)
- [lovelyyoshino/Bilibili-Live-API](https://github.com/lovelyyoshino/Bilibili-Live-API)
- [flaribbit/bilibili-manga-spider](https://github.com/flaribbit/bilibili-manga-spider)
- [simon300000/bili-api](https://github.com/simon300000/bili-api)
- [iyear/biligo](https://github.com/iyear/biligo) Bilibili API SDK in Golang
- [bilibili-openplatform/demo](https://github.com/bilibili-openplatform/demo): 哔哩哔哩开放平台示例代码库
- [ddiu8081/blive-message-listener](https://github.com/ddiu8081/blive-message-listener): Bilibili-live danmu listener with type. Bilibili 直播间弹幕监听库，支持类型输出。
- [Nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api): 哔哩哔哩常用API调用。支持视频、番剧、用户、频道、音频等功能。工具齐全。
- [CuteReimu/bilibili](https://github.com/CuteReimu/bilibili): 哔哩哔哩API的Go版本SDK

### 成品

- [NullPointerException/AnimePipe](https://codeberg.org/NullPointerException/AnimePipe): 功能完善的Android流媒体综合客户端，支持Bilibili, Youtube, NicoNico
- [3Shain/BiliChat](https://github.com/3Shain/BiliChat) : 基于h5的B站直播弹幕姬
- [AncientLysine/BiliLocal](https://github.com/AncientLysine/BiliLocal):本地弹幕播放器
- [zyzsdy/biliroku](https://github.com/zyzsdy/biliroku):bilibili 生放送（直播）录制
- [otakustay/danmaku-to-ass](https://github.com/otakustay/danmaku-to-ass):A站B站弹幕转字幕文件
- [bilibili-helper/bilibili-helper-o](https://github.com/bilibili-helper/bilibili-helper-o):哔哩哔哩 (bilibili.com) 辅助工具，可以下载视频，查询弹幕发送人以及一些十分实用的直播区功能。
- [apachecn/BiliDriveEx](https://github.com/apachecn/BiliDriveEx):基于B站相簿上传的文件分块索引存储器
- [apachecn/CDNDrive](https://github.com/apachecn/CDNDrive):基于B站相簿上传的文件分块索引存储器
- [Hsury/BiliDrive](https://github.com/Hsury/BiliDrive):基于B站相簿上传的文件分块索引存储器
- [Tsuk1ko/bilibili-live-chat](https://github.com/Tsuk1ko/bilibili-live-chat):无后端的仿 YouTube Live Chat 风格的简易 Bilibili 弹幕姬
- [ironmanic/crawler_target_users_good](https://github.com/ironmanic/crawler_target_users_good):搜索bilibili特定视频，为评论 点赞，关注，私信，一体化服务
- [dd-center/DDatElectron](https://github.com/dd-center/DDatElectron):DD@Home 分布式项目, 桌面客户端
- [dd-center/vtbs.moe](https://github.com/dd-center/vtbs.moe):B站VTB数据中心
- [JunzhouLiu/BILIBILI-HELPER](https://github.com/JunzhouLiu/BILIBILI-HELPER):利用Linux Crontab定时任务,云函数，Docker等方式实现B站，哔哩哔哩（Bilibili）每日自动投币，签到，银瓜子兑换硬币，领取大会员福利，大会员月底给自己充电等。每天轻松获取65经验值。
- [the1812/Bilibili-Evolved](https://github.com/the1812/Bilibili-Evolved):强大的哔哩哔哩增强脚本: 下载视频, 音乐, 封面, 弹幕 / 简化直播间, 评论区, 首页 / 自定义顶栏, 删除广告, 夜间模式 / 触屏设备支持
- [xlzy520/bili-short-url](https://github.com/xlzy520/bili-short-url): 哔哩哔哩短链生成器
- [zjkwdy/bili_app_splash](https://github.com/zjkwdy/bili_app_splash): B站壁纸娘和开屏图自动下载，每天使用Actions自动同步
- [Jannchie/BiliOB](https://github.com/Jannchie/BiliOB): BiliOB观测者是一个观测B站UP主及视频数据变化，并予以分析的Web应用程序
- [biliob233/biliob233.github.io](https://github.com/biliob233/biliob233.github.io): ~~无可奉告~~
- [biliup/biliup](https://github.com/biliup/biliup): 全自动录播、投稿工具，也支持twitch、ytb频道搬运。提供分p上传b站接口，腾讯云内网免流+大幅提速
- [ddiu8081/bilicli](https://github.com/ddiu8081/bilicli): Bilibili-live danmu dashboard in your terminal. 
- [MotooriKashin/Bilibili-Old](https://github.com/MotooriKashin/Bilibili-Old): 恢复旧版Bilibili页面，为了那些念旧的人。
- [SocialSisterYi/bcut-asr](https://github.com/SocialSisterYi/bcut-asr): 使用必剪API的语音字幕识别
- [CzJam/Bili_Realtime_Data](https://github.com/CzJam/Bili_Realtime_Data): Bilibili粉丝与视频实时数据统计

### 其他

- [kuresaru/geetest-validator](https://github.com/kuresaru/geetest-validator):geetest调试器

- [uw-labs/bloomrpc](https://github.com/uw-labs/bloomrpc): GUI Client for GRPC Services

- [grpc/grpc](https://github.com/grpc/grpc): The C based gRPC (C++, Python, Ruby, Objective-C, PHP, C#) 

 - [quicktype](https://github.com/quicktype/quicktype) quicktype generates strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries, making it a breeze to work with JSON type-safely in many programming languages.一键生成多种语言的json反序列化所需类,以便于快速反序列化, 有网页版