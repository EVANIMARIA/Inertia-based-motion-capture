import time
import sys
for x in range(1, 10):
    print("\rtalking" + str(x),end="")
    # print(0, 1, "replying" + str(x))
    time.sleep(0.2)
