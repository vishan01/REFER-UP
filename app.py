import EDIT
import streamlit as st
import random
rnum = random.randint(1, 4)
EDIT.choice(rnum)
st.write(EDIT.ref)
