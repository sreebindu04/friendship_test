import streamlit as st
import random
st.title("❤️friendship calculator")
n1=st.text_input("your name")
n2=st.text_input("friend's name")
if st.button("Check %"):
    s=random.randint(90, 100)
    st.success(f"❤️friendship score: {s}%")
    st.balloons()