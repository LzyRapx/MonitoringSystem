#coding:utf-8
import prometheus_client
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry

# 使用Python和asyncio编写Prometheus监控

import aiohttp
import asyncio
import uvloop
import random, logging
import time

import datetime

from aiohttp import web
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

routes = web.RouteTableDef()

# metrics包含
requests_total = Counter("request_count", "Total request cout of the host") # 数值只增
random_value = Gauge("random_value", "Random value of the request") # 数值可大可小

@routes.get('/metrics')
async def metrics(request):
  requests_total.inc()   # 计数器自增
  # requests_total.inc(2)
  data = prometheus_client.generate_latest(requests_total)
  return web.Response(body = data,content_type="text/plain")  # 将计数器的值返回

@routes.get("/metrics2")
async def metrics2(request):
  random_value.set(random.randint(0, 10))  # 设置值任意值，但是一定要为 整数或者浮点数
  return web.Response(body = prometheus_client.generate_latest(random_value),
                      content_type="text/plain")  # 将值返回

@routes.get('/')
async def hello(request):
  return web.Response(text="Fuck, prometheus!!!")

# 使用labels来区分metric的特征
c = Counter('request_total','HTTP request total', ['method','clientip'])  # 添加lable的key
c.labels('get','127.0.0.1').inc() #为不同的label进行统计
c.labels('post','127.0.0.1').inc(3) #为不同的label进行统计
c.labels(method = "get", clientip = "192.168.0.1").inc()

g = Gauge('my_inprogress_requests', 'Description of gauge',['mylabelname'])
g.labels(mylabelname = 'str').set(3.6)


if __name__ == '__main__':
    logging.info("server start at : %s" % datetime.datetime.now())
    # 创建app，设置最大接收图片大小为2M
    app = web.Application(client_max_size=int(2) * 1024 ** 2)
    app.router.add_routes(routes) # 添加路由映射
    web.run_app(app,host = '0.0.0.0', port = 2222) # 启动app
    logging.info('server close: %s' % datetime.datetime.now)

