import streamlit as st

st.set_page_config(page_title="Test App", layout="Centered")

st.title ("Streamlist App is working")

st.write("If you can see this, your deployment is successful.")

name = st.text_inout("Enter your name:")

if name:
  st. success(f"Hello {name}, your streamli app ia live")

st.button ("click me")
