import queue
import threading
import video
import image
import time
import subprocess

MAX_THREADS = 4


q_images = queue.Queue(maxsize=MAX_THREADS)
q_video = queue.Queue()
done = [0, 0, 0, 0]


def thread_init():
    subprocess.call("rm ./thread0/*.mp4", cwd="media",
                    stdout=subprocess.DEVNULL, shell=True)
    subprocess.call("rm ./thread1/*.mp4", cwd="media",
                    stdout=subprocess.DEVNULL, shell=True)
    subprocess.call("rm ./thread2/*.mp4", cwd="media",
                    stdout=subprocess.DEVNULL, shell=True)
    subprocess.call("rm ./thread3/*.mp4", cwd="media",
                    stdout=subprocess.DEVNULL, shell=True)

    for i in range(MAX_THREADS):
        thread = threading.Thread(name="Thread_%s" % str(
            i), target=imageThread)
        thread.start()

    for i in range(MAX_THREADS):
        thread = threading.Thread(name="Thread_%s" % str(
            i), target=videoThread)
        thread.start()


def imageThread():
    while True:
        task = q_images.get()
        t_id = task[1]
        if task[0] != None:
            image.makeImages(task[0], "media/thread%s" % str(t_id), 500)
            break
    q_images.task_done()
    q_video.put(t_id)
    time.sleep(0.001)
    thread = threading.Thread(name="Thread_%s" % str(t_id), target=imageThread)
    thread.start()


def videoThread():
    while True:
        t_id = q_video.get()
        if t_id != None:
            video.makeVideo("media/thread%s" % str(t_id))
            break
    q_video.task_done()
    done[t_id] = 1
    time.sleep(0.001)
    thread = threading.Thread(name="Thread_%s" % str(t_id), target=videoThread)
    thread.start()



def producer(handle, t_id):
    print(t_id)
    q_images.put((handle, t_id))
