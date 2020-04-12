
import random
def randInt(min = , max = ):
    num = random.random(1.0, 101.0)
    return num

import random
print(random.random() * 100)

import random
def randInt(min = "", max = ""):
    if len(min) > 0:
        num = float(min) + 100
        return random.random() * num - float(min)
    if min == "" and max == "":
        return random.random() * 100
    if len(max) > 0:
        return random.random() * float(max) + 0
    if len(min) > 0 and len(max) > 0:
        num = float(max) - float(min)
        return random.random() * float(max) + float(min)

b = randInt()
print(b)
