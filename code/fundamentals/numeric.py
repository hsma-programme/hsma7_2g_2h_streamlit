import streamlit as st

st.slider(
    label="Pick a number", 
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

st.number_input(
    label="Pick a number",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)