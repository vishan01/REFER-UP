import streamlit as st

ref = ""


def choice(num):
    path = r"Dataset/r"+str(num)+".txt"
    with open(path, "r") as file:
        global ref
        ref = file.read()


def add(x):
    tags = ["ENAME", "YNAME", "YWORK", "YPLACE", "YJOB",
            "YROLE", "YX", "YFNAME"]
    global ref
    for i in range(len(tags)):
        ref = ref.replace(tags[i], x[i])
