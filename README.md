my-tv-server是一个自定义的IPTV源订阅服务器，用户可以定义自己的IPTV源，配合my-tv（https://github.com/lizongying/my-tv） 使用

# 安装
## 本地
本地安装python>=3.9,执行下述命令即可运行

```shell
cd my-tv-server
pip3 install -r requirement.txt
cd src
uvicorn app:app  --host 0.0.0.0 --port 8080 --workers 1
```

## Docker
执行下面命令即可运行服务，访问 http://localhost:8080 or http://your-ip:80 即可。 
```shell
docker compose up -d
```

# 配置

## 电视列表
初始化的电视列表数据见 src/data/channels.json，可以修改此文件，如果服务运行起来后，可以打开 http://your-ip:8080 进行访问，修改源。

## 管理员配置
管理员可以修改电视列表，为防止其他人修改，修改接口配置了鉴权token，token配置在环境变量（名为TOKEN），可以修改docker-compose.yaml中的TOKEN环境变量，启动服务。

## my-tv客户端配置
目前my-tv 正在增加同步功能，待开发完成后，在配置页面配置。