import tweepy
from google.cloud import vision
import io
from PIL import Image
from datetime import datetime
import urllib.request
import os
import configparser


def getFeed(handle, count):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
    config = configparser.ConfigParser()
    config.read("keys")
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
                               config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(),
                          config.get('auth', 'access_secret').strip())
    api = tweepy.API(auth)

    feed = []

    public_tweets = api.user_timeline(id=handle, count=count)
    public_tweets.reverse()

    for tweet in public_tweets:
        entry = {}
        today = datetime.today().date()
        if today == tweet.created_at.date():
            entry.update({"text": tweet.text})
            entry.update({"image description": None})
            if 'media' in tweet.entities:
                for media in tweet.entities["media"]:
                    entry.update(
                        {"image description": annotateImage(media["media_url"])})

            feed.append(entry)
    return feed


def annotateImage(URL):
    client = vision.ImageAnnotatorClient()

    with urllib.request.urlopen(URL) as url:
        f = io.BytesIO(url.read())

    content_jpeg = Image.open(f)

    imgByteArr = io.BytesIO()
    content_jpeg.save(imgByteArr, format=content_jpeg.format)
    content = imgByteArr.getvalue()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    summary = ""

    for label in labels:
        summary += label.description
        summary += ", "

    summary = summary[: -2]

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return summary


if __name__ == "__main__":
    print(getFeed("BleacherReport", 50))
