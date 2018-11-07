import random
import prometheus_client
from prometheus_client import Gauge

from flask import  Response, Flask

app = Flask(__name__)

random_value = Gauge("random_value", "Ramdom value of the request")

@app.route("/metrics")
def rd_value():
    num = random.randint(0,10)
    print("num = ", num)
    random_value.set(num)

    return Response(prometheus_client.generate_latest(random_value),
                    mimetype="text/plain")
@app.route("/")
def index():
    # random_value.dec()
    return "fuck prometheus"

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
