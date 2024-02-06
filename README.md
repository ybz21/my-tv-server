# 我的电视服务器
my-tv-server是一个自定义的IPTV源订阅服务器，用户通过服务器订阅视频源，配合my-tv（ https://github.com/lizongying/my-tv ） 使用。

# 安装
## 本地
本地安装python>=3.9，执行下述命令即可运行。

```shell
cd my-tv-server
pip3 install -r requirement.txt
cd src
uvicorn app:app  --host 0.0.0.0 --port 8080 --workers 1
```

## Docker
执行下面命令即可运行服务，访问 http://localhost:8080 or http://your-ip:80 即可访问。 
```shell
docker compose up -d
```

# 配置

## 电视列表
初始化的电视列表数据见 src/data/channels.json，可以修改此文件，如果服务运行起来后，可以打开 http://your-ip:8080 进行访问，修改源。
本repo使用的文件： https://github.com/lizongying/my-tv/blob/4fb27ba502ff29da165cbd281b86fd5e1d370837/app/src/main/res/raw/channels.json 

其电视列表格式如下：
```JSON
[
    {
        "id": 0,
        "videoIndex": 0,
        "channel": "channel",
        "logo": "xxxx",
        "pid": "xxx",
        "sid": "xxx",
        "programId": "xxxx",
        "needToken": false,
        "mustToken": false,
        "title": "xx卫视",
        "videoUrl": [
            "xxx.m3u8"
        ]
    }
]
```
每个字段含义：

* id: 源的唯一标识符。
* videoIndex: 视频索引，用于标识不同的视频。
* channel: 频道类别。
* logo: 频道的标识或标志的 URL。
* pid: 频道的节目 ID。
* sid: 频道的服务 ID。
* programId: 节目的 ID。
* needToken: 指示是否需要令牌（token）进行访问，true/false。
* mustToken: 指示是否必须使用令牌进行访问，true/false。
* title: 节目或频道的标题。
* videoUrl: 视频的 URL，可能是一个或多个 URL 组成的列表。必须是m3u8格式。

## 管理员配置
管理员可以修改电视列表，为防止其他人修改，修改接口配置了鉴权token，token配置在环境变量（名为TOKEN），可以修改docker-compose.yaml中的TOKEN环境变量，启动服务。

## my-tv客户端配置
目前my-tv 正在增加同步功能，待开发完成后，在配置页面配置订阅 http://your-ip:8080/channels 。