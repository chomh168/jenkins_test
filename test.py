import time

start = time.time()
while True:

    term = time.time() - start
    if term>10:
        start = time.time()
        print(term)