import base64

import streamlit as st
import requests

st.set_page_config(page_title="Apollo AI", page_icon="🌕", layout="wide")

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Simulation App")

st.markdown("---")

tab1, tab2 = st.tabs(["Control Panel", "About Project"])

with st.sidebar:
    st.header("Weather")
    wind = st.slider("Wind Speed", min_value=0.0, max_value=10.0, value=0.0, step=1.0)
    turbulence = st.slider("Turbulence", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    st.markdown("---")
    with st.expander("Additional settings"):
        st.write("Change physic")
        gravity = st.slider("Gravity", min_value=-12.0, max_value=0.0, value=-10.0, step=1.0)
with tab1:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Status")
        start_button = st.button("Start", use_container_width=True)
        stats_placeholder = st.container()

    with col2:
        if start_button:
            with st.spinner("Loading model..."):
                url = f"http://backend:8000/simulation?wind={wind}&turbulence={turbulence}&gravity={gravity}"
                try:
                    response = requests.get(url)

                    if response.status_code == 200:
                        data = response.json()
                        stats = data["stats"]
                        img = data["image"]
                        with stats_placeholder:
                            st.markdown("---")
                            st.markdown("Stats")
                            c1,c2 = st.columns(2)
                            c1.metric("Status", stats["status"])
                            c2.metric("Score", stats["score"])
                            st.metric("Steps", stats["steps"])
                            st.write("Altitude")
                            st.line_chart(stats["charts"])
                        img = base64.b64decode(img)
                        st.image(img, width=800)
                    else:
                        st.error("Error occured!")
                except requests.exceptions.ConnectionError:
                    st.error("Error occured!")
with tab2:
    st.header("Solution Architecture")
    st.write("Simple one-day project demonstrating machine learning operations (MLOps)")
    st.markdown("""
        * **AI Model:** Proximal Policy Optimization (PPO) algorithm using the Stable-Baselines3 library.
        * **Environment:** `LunarLander-v3` physics engine (Gymnasium / Box2D).
        * **Backend:** Fast, asynchronous API server built with **FastAPI**.
        * **Frontend:** Interactive web interface built with **Streamlit**.
        * **DevOps:** Fully containerized using **Docker** (multi-container architecture with Docker Compose). """)