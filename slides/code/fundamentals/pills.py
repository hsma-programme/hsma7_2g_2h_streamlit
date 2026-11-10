import streamlit as st

st.segmented_control(
    label="Choose an option",
    options=["A", "B", "C"],
    default="A",
)

st.radio(
    label="Choose an option",
    options=["A", "B", "C"],
    index=0,
)