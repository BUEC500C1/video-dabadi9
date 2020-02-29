from flask import Flask, send_file
from flask_restful import Resource, Api
import threads

calls = -1

app = Flask(__name__)


@app.route('/getvideo/<string:handle>')
def get(handle):
    global calls
    calls += 1

    t_id = calls % threads.MAX_THREADS
    threads.producer(handle, t_id)

    if calls == 0:
        threads.thread_init()
    while True:
        if (threads.done[t_id] == 1):
            threads.done[t_id] = 0
            return send_file("media\\thread%s\\video.mp4" % str(t_id))


if __name__ == '__main__':
    app.run(debug=True)
