import random
num = random.randint(1, 4)
path = "Dataset\\r"+str(num)+".txt"
with open(path, "r") as file:
    ref = file.read()
    print(ref)


def add(*x):
    ref = str(ref)
    tags = ["ENAME", "YNAME", "YWORK", "YPLACE", "YJOB",
            "YROLE", "YJOB", "YX", "YROLE", "YFNAME"]
    for i in tags:
        ref.replace(tags[i], x[i])
