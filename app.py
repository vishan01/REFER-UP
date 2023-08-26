import EDIT
import streamlit as st
import random
rnum = random.randint(1, 4)
EDIT.choice(rnum)
st.title("HELLO	:wave:, THIS IS :orange[REFERUP]")

x = []
x.append(st.text_input("Enter The Reciever Name",
         autocomplete="Hiring Team/Manager"))
x.append(st.text_input("Enter Your Name"))
x.append(st.text_input("Enter Your Current Profession"))
x.append(st.text_input("Enter Your Place of Work"))
x.append(st.text_input("Enter The Job industry"))
x.append(st.text_input("Enter The Job Role"))
x.append(st.text_input("Enter Your Years of Experience In The Role"))
x.append(x[0].split(" ")[0])

EDIT.add(x)

st.write(EDIT.ref)
