import time

from RobloxAFK import *

time.sleep(1)  # activating
for i in range(1000):
    ra = random.randint(1, 2)
    rac = random.randint(1, 10)
    PressKey(w)
    time.sleep(ra)
    ReleaseKey(w)
    PressKey(s)
    time.sleep(ra)
    ReleaseKey(s)
    PressKey(a)
    time.sleep(1)
    ReleaseKey(a)
    PressKey(d)
    time.sleep(1)
    ReleaseKey(d)
    PressKey(SPACE)
    ReleaseKey(SPACE)


"""
while True:
    randomVal = random.randint(1,5)

    if randomVal == 1:
        PressKey(w)
        time.sleep(0.1)
        ReleaseKey(w)
    if randomVal == 2:
        PressKey(a)
        time.sleep(0.1)
        ReleaseKey(a)
    if randomVal == 3:
        PressKey(s)
        time.sleep(0.1)
        ReleaseKey(s)
    if randomVal == 4:
        PressKey(w)
        time.sleep(0.1)
        ReleaseKey(w)
    if randomVal == 5:
        PressKey(d)
        time.sleep(0.1)
        ReleaseKey(d)

        time.sleep(300)
        """
