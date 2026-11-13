st.slider(
    label="Simulation duration (minutes)",
    min_value=50,
    max_value=200,
    value=120,
    key="sim_duration",
)

st.slider(
    label="Number of replications",
    min_value=10,
    max_value=50,
    value=30,
    key="num_replications",
)
