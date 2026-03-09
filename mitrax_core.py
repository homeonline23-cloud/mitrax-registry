import streamlit as st  # <--- THE MASTER KEY!

# --- THE IMPERIAL BACK DOOR LEVER ---
if 'step' not in st.session_state: 
    st.session_state.step = 'sector3'
