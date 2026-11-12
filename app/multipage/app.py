"""Entrypoint for app. Defines navigation."""

import streamlit as st

st.write("Entrypoint:", __file__)
st.write("Streamlit version:", st.__version__)

pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
    ]
)

st.write("Selected page:", pg.title)
st.write("Selected URL path:", pg.url_path)

pg.run()