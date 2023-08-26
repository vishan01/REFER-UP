import streamlit as st


@st.cache_data
def choice(num):
    path = "Dataset\\r"+str(num)+".txt"
    with open(path, "r") as file:
        global ref
        ref = file.read()


def add(*x):

    tags = ["ENAME", "YNAME", "YWORK", "YPLACE", "YJOB",
            "YROLE", "YX", "YFNAME"]
    for i in range(len(tags)):
        ref.replace(tags[i], x[i])
