import streamlit as st

st.title("chocolate taste poll")

col1,col2=st.columns(2)

with col1:
    st.header("nestle")
    #st.image(url,width=100)
    vote1 = st.button("vote nestle")
with col2:    
    st.header("galaxy")
    vote2 = st.button("vote galaxy")

if vote1:
    st.success("thanks for voting nestle")
elif vote2:
    st. success("thanks for voting galaxy")   

name= st.sidebar.text_input("enter your name")    
choco = st.sidebar.selectbox("choose your chocolate",["galaxy","lindt"])

st.write(f"{name} your fav is {choco}")

with st.expander("Show chai making instructions"):
    st.write("""
    1. select finest coco beans
    2. roast the beans     
    3. grid them             
""")
    
st.markdown('### chocolate is life')    