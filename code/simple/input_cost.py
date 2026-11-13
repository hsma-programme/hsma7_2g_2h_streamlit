st.number_input(
    label="Cost per nurse per hour (£)",
    min_value=0.0,
    value=30.0,
    step=1.0,
    key="nurse_cost_per_hour",
    help="Nurses are costed for the full simulation duration, including time when they are not seeing patients",
)
