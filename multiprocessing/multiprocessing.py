import multiprocessing

running = True

def func1():
    try:
        print("Function 1: Starting")
        while running:
            print("Function 1: running")
    except KeyboardInterrupt:
        print("Function 1: Finishing")

def func2():
    try:
        print("Function 2: Starting")
        while running:
            print("Function 2: running")
    except KeyboardInterrupt:
        print("Function 2: Finishing")

if __name__ == '__main__':
    try:
        p1 = multiprocessing.Process(target=func1)
        p1.start()
        p2 = multiprocessing.Process(target=func2)
        p2.start()
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        print("Stopping...")
