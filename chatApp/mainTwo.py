import streamlit as st

st.title("Make IceCream")

if st.button("make icecream"):
    st.success("your icecream is being prepared")

add_topping = st.checkbox("add toppings")

if add_topping:
    st.write("toppings added")

ice_type = st.radio("pick your scoop",["chocolate","butterscoch","magnum"])    
st.write(f"selected scoop {ice_type}")

additional_scoop = st.selectbox("choose another scoop",["mint","belgium chocolate","vanilla"])
st.write(f"selected additional scoop is {additional_scoop}")

level_of_death = st.slider("chocolate syrup level",1,5,2)

cashew=st.number_input("how many cashews",min_value=10,max_value=30,step=1)
st.write(f"cashews required {cashew}")

name= st.text_input("Enter your name")
if name:
    st.write(f"welcome {name} your ice cream is on the way!!")

dob = st.date_input("select your date of birth")    
st.write(f"your dob is {dob}")