import tweepy
from flask import Flask, send_file
from flask_restful import Resource, Api
import feed
import video as vd

app = Flask(__name__)


@app.route('/<string:handle>')
def get(handle):
    try:
        vd.makeVideo(handle)
        return send_file("video.mp4")
    except:
        return "Error, please make sure handle is correct"


if __name__ == '__main__':
    app.run(debug=True)
