import subprocess


def makeVideo(path):

    subprocess.call("rm *.mp4", cwd=path,
                    stdout=subprocess.DEVNULL, shell=True)

    subprocess.call("ffmpeg -framerate 0.33 -i img%d.png -c:v libx264 -r 30 -pix_fmt yuv420p video.mp4",
                    cwd=path, stdout=subprocess.DEVNULL, shell=True)

    subprocess.call("rm *.png", cwd=path,
                    stdout=subprocess.DEVNULL, shell=True)


if __name__ == "__main__":
    makeVideo("BleacherReport")
