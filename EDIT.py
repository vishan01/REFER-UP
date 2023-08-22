
with open("Dataset\\r1.txt", "r") as file:
    ref = file.read()
    print(str(ref))


def add(*x):
    ref = str(ref)
    tags = ["ENAME", "YNAME", "YWORK", "YPLACE", "YJOB",
            "YROLE", "YJOB", "YX", "YROLE", "YFNAME"]
    for i in tags:
        ref.replace(tags[i], x[i])
