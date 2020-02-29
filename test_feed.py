import feed
import os
import tweepy
import json
import imageTest

with open('nytimes.json') as json_file:
    json_data = json.load(json_file)


def test_getFeed():
    if not os.path.exists("keys"):
        status_json = json.loads(json_data)
        assert status_json['text'] == "The public health director of Santa Clara County, California, confirmed that the county's new coronavirus case does… https://t.co/hl8ClztVbL"
    else:
        data = feed.getFeed("realDonaldTrump", 1)
        assert len(data[0]['text']) > 0


def test_annotateImage(capsys):
    if not os.path.exists("keys"):
        assert imageTest.description == "Sport venue, Basketball, Basketball court, Tournament, Sports, Leisure centre, Competition event, Ball game, Hardwood, Floor"
    else:
        description = feed.annotateImage(imageTest.url)
        assert description == "Sport venue, Basketball, Basketball court, Tournament, Sports, Leisure centre, Competition event, Ball game, Hardwood, Floor"
