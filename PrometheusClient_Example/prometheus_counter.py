#coding:utf-8

import prometheus_client
from prometheus_client import Counter
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

from flask import request

app = Flask(__name__)

requests_total = Counter("request_count","total request cout of the host") # only increase

@app.route("/metrics")
def request_count():
    request_count.inc()
    return Response(prometheus_client.generate_latest(requests_total),
                    mimetype = "text/plain")

def post_count():
    # do something
    requests_total.inc()
    return request(prometheus_client.generate_latest(requests_total),
                   mimtype = "text/plain")

@app.route('/')
def index():
    requests_total .inc()
    return "fuck prometheus"

if __name__ == '__main__':
   app.run(host = "0.0.0.0")
