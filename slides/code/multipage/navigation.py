import streamlit as st

# Define pages and their order
pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
    ]
)
pg.run()
