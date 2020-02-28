import time

start = time.time()
while True:

    term = time.time() - start
    if term>13:
        start = time.time()
        print(term)