#!/usr/bin/env python3

from flask import Flask
from redis import Redis
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

eureka_client.init(eureka_server="http://localhost:8080/eureka/v2",
                   app_name="redisagent1",
                   instance_port=5000,
                   regions='us-west-1')

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
