#!/usr/bin/env python3

from flask import Flask
from redis import Redis
from eureka.client import EurekaClient

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

ec = EurekaClient("redisagent1",
                  eureka_domain_name="http://localhost:8080/",
                  region="eu-west-1",
                  vip_address="http://localhost:5000/",
                  port=8080)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
