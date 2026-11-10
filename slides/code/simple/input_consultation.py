st.number_input(
    label="Mean nurse consultation length (minutes)",
    min_value=3.0,
    max_value=9.0,
    value=6.0,
    key="mean_nurse_consult_time",
)

st.number_input(
    label="Standard deviation of nurse consultation length (minutes)",
    min_value=0.0,
    value=1.0,
    key="sd_nurse_consult_time",
)