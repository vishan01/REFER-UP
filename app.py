import EDIT
import streamlit as st
import random
import clipboard
rnum = random.randint(1, 4)
EDIT.choice(rnum)
st.title("HELLO	:wave:, THIS IS :orange[REFERUP]")

x = []
x.append(st.text_input("Enter The Reciever Name",
         autocomplete="Hiring Team/Manager"))
x.append(st.text_input("Enter Your Name"))
x.append(st.text_input("Enter Your Current Profession"))
x.append(st.text_input("Enter Your Place of Work/Education"))
x.append(st.text_input("Enter The Job industry"))
x.append(st.text_input("Enter The Job Role"))
x.append(st.text_input("Enter Your Years of Experience In The Role"))
x.append(x[1].split(" ")[0])

if st.button("Generate"):
    EDIT.add(x)
    st.write(EDIT.ref)
    if st.button("Copy to clipboard"):
        clipboard.copy(EDIT.ref)
        