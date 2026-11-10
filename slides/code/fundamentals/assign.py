import streamlit as st

chosen_value = st.slider(
    label="Pick a number", 
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

st.write(f"Chosen number: {chosen_value}")