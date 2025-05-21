import streamlit as st

st.title("Chat App")
st.subheader("Brewed with streamlit")
st.text('Welcome to your iteractive app')
st.write("choose your fav animie ")

chai = st.selectbox("your fav animie",["dragonballz","overlord","black clover"])

st.write(f"you choose{chai} nice choice")

st.success("you fav animie is cool")

