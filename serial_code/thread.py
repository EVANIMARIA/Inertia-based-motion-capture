import threading


def loop(order):
    print(str(order) + "fuck")


thread_list = []
for x in range(1, 10):
    t = threading.Thread(target=loop, args=(x))
    t.setDaemon(True)
    thread_list.append(t)
for t in thread_list:
    t.start()
for t in thread_list:
    t.jpin()
