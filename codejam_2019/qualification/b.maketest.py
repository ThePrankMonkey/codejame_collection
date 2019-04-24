#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import random

test_count = 30
print(test_count)
for i in range(test_count):
    size = random.randint(2,1000)
    print(size)
    path = list("S"*(size-1) + "E"*(size-1))
    random.shuffle(path)
    print("".join(path))