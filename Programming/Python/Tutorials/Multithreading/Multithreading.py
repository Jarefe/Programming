import threading, time

print("start of program")

def takeANap():
    print("napping")
    time.sleep(10)
    print("woke up")

threadObj = threading.Thread(target=takeANap())
printThread = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})

threadObj.start()
printThread.start()

print("near end of program before threads are joined")

threadObj.join()
printThread.join()

print("end of program after threads are joined")
