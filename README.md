# video-dabadi9

## API Desicription

This API will return a .mp4 video with all the tweets from the past 24h from a specified account. If the tweet contains any type of media, it will transform the media into words using Google Vision. Each tweet is displayed for 3 seconds.

## Setup

You need to have python 3 and install the requirements, so run:

```bash
pip install -r requirements.txt.
```

You need to put your twitter keys in a file named "keys" and your google vision keys in a file named "key.json". Both files should be on the main project directory.

## Start server

```bash
python3 api.py
```

## Get video for a specific user

Make a get request to "http://127.0.0.1:5000/getvideo/%HANDLE%" where %HANDLE% is the twitter handle of the user you are looking for. The API does not perform error check to make sure that the handle exists.

Answers to assigment questions:

1. Given that the Surface Pro I am using has an i7 quadcore processor, I believe it should be able to process 4 simultaneous API calls.
2. The API can run more than one API call at the same time.
3. The processing was split into 8 threads, 4 producing images and 4 producing videos.
