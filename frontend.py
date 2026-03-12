import streamlit as st
import requests

st.title("Simulation App")
st.write("Trained Algorithm")

if st.button("start"):
    with st.spinner("Loading model..."):
        try:
            response = requests.get("http://127.0.0.1:8000/simulation")

            if response.status_code == 200:
                st.success("Model loaded!")
                st.image(response.content)
            else:
                st.error("Error occured!")
        except requests.exceptions.ConnectionError:
            st.error("Error occured!")