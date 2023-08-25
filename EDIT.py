def choice(num):
    path = "Dataset\\r"+str(num)+".txt"
    with open(path, "r") as file:
        global ref
        ref = file.read()


def add(*x):
    ref = str(ref)
    tags = ["ENAME", "YNAME", "YWORK", "YPLACE", "YJOB",
            "YROLE", "YJOB", "YX", "YROLE", "YFNAME"]
    for i in tags:
        ref.replace(tags[i], x[i])
