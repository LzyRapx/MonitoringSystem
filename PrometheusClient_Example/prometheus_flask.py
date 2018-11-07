#coding:utf-8

import time
import random

import prometheus_client
from prometheus_client import start_http_server
from prometheus_client import Counter,Summary
import flask
from flask import Flask, request, jsonify

import os
import time
import datetime

import logging
import logging.handlers

from gevent.pywsgi import WSGIServer

import logging
import logging.handlers

app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.

@app.route("/t1")
@REQUEST_TIME.time()
def process_request():
    """A dummy function that takes some time."""
    time.sleep(1)
    return jsonify({"fuck":"prometheus"})

# 测试 prometheus 的 python接口
# 参考:https://github.com/prometheus/client_python/blob/master/README.md

if __name__ == '__main__':

    start_http_server(1111) # 这里是prometheus的监控端口，展示metrics信息
    # 启动flask
    http_server = WSGIServer(('0.0.0.0',2222),app) #服务
    http_server.serve_forever()
