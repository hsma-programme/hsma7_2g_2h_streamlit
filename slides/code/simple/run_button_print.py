if st.button("Run simulation", type="primary"):
    params = Param(
        mean_patient_inter=st.session_state.mean_patient_inter,
        mean_nurse_consult_time=st.session_state.mean_nurse_consult_time,
        sd_nurse_consult_time=st.session_state.sd_nurse_consult_time,
        num_nurses=st.session_state.num_nurses,
        sim_duration=st.session_state.sim_duration,
        num_replications=st.session_state.num_replications,
        nurse_cost_per_hour=st.session_state.nurse_cost_per_hour,
    )
    trial = Trial(param=params)
    trial.run_trial()
    trial.calculate_trial_results()

    st.subheader("Scenario summary")
    st.write(f"""
    Summary of nurse queue times across **all** replications.

    * Mean: {trial.trial_mean_q_time_nurse:.2f} minutes.
    * SD: {trial.trial_sd_q_time_nurse:.2f} minutes.
    * 90th Perc: {trial.trial_perc_90_q_time_nurse:.2f} minutes.
    * Standard error: {trial.se_q_time_nurse:.2f}
    * 95% CI: ({trial.ci_lower_q_time_nurse:.2f},
    {trial.ci_upper_q_time_nurse:.2f}) minutes.
    
    Total nurse staffing cost: £{trial.total_nurse_cost:,.2f}
    """)
