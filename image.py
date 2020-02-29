from PIL import Image, ImageDraw, ImageFont
import feed
import textwrap


def makeImages(handle, path, max_count):
    tweets = feed.getFeed(handle, max_count)
    failed = 0
    for i, tweet in enumerate(tweets):
        try:
            createImage(tweet['text'], tweet["image description"], handle, i - failed, path)
        except:
            failed += 1
            continue


def createImage(tweet, image, handle, counter, path):

    img = Image.new('RGB', (1400, 800), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Arial.ttf", 30)
    textWrapped = textwrap.wrap(tweet, width=80)
    displayText = ""

    for line in textWrapped:
        displayText = displayText + '\n' + line

    displayText = displayText + '\n'

    if image:
        textWrapped = textwrap.wrap(
            "Attached image description: " + image, width=80)
        for line in textWrapped:
            displayText = displayText + '\n' + line

    d.text((50, 200), displayText, fill='white', font=font)

    font = ImageFont.truetype("Arial.ttf", 35)
    handle = "@" + handle
    d.text((50, 100), handle, fill='white', font=font)

    img.save(path + '/img%d.png' % counter)
    counter += 1


if __name__ == "__main__":
    makeImages("BleacherReport", 'media', 50)
