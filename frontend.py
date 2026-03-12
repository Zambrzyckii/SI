import streamlit as st
import requests

st.title("Simulation App")
st.write("Trained Algorithm")

st.subheader("Weather")
wind = st.slider("Wind Speed",min_value=0,max_value=10,value=0,step=1)
turbulence = st.slider("Turbulence",min_value=0.0,max_value=1.0,value=0.0,step=0.1)
gravity = st.slider("Gravity",min_value=-12.0,max_value=0.0,value=-10.0,step = 1.0)
if st.button("start"):
    with st.spinner("Loading model..."):
        url = f"http://backend:8000/simulation?wind={wind}&turbulence={turbulence}&gravity={gravity}"
        st.info(f"Debug: {url}")
        try:
            response = requests.get(url)

            if response.status_code == 200:
                st.success("Model loaded!")
                st.image(response.content)
            else:
                st.error("Error occured!")
        except requests.exceptions.ConnectionError:
            st.error("Error occured!")