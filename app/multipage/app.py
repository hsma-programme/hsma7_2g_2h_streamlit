"""Entrypoint for app. Defines navigation."""

import streamlit as st

pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
    ]
)

pg.run()