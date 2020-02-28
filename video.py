import image
import tweepy
import subprocess


def makeVideo(handle):

    subprocess.call("rm *.mp4", None, stdout=subprocess.DEVNULL, shell=True)

    image.makeImages(handle, "media", 300)

    subprocess.call("ffmpeg -framerate 0.33 -i ./media/img%d.png -c:v libx264 -r 30 -pix_fmt yuv420p video.mp4",
                    None, stdout=subprocess.DEVNULL, shell=True)
    
    subprocess.call("rm ./media/*.png", None,
                    stdout=subprocess.DEVNULL, shell=True)


if __name__ == "__main__":
    makeVideo("BleacherReport")
