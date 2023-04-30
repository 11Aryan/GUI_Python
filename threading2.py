from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg, 0,-1):
        print("Hello From Thread {}".format(i))

        # wait 1 sec in between each thread
        sleep(1)


if __name__ == "__main__":
    thread = Thread(target=threaded_function, args=(50,))
    thread.start()
    thread.join()
    print("thread finished...exiting")
