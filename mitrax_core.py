# --- PHASE 1: THE PREDICTION INTRO (VIBRANIUM SEALED) ---
if st.session_state.step == 'intro':
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown("<div class='prediction-subtitle'>PREDICTION PIC 4</div>", unsafe_allow_html=True)
    
    # --- NO LINE BREAKS FOR THE RABBIT TO HIDE IN ---
    st.markdown("""<div style='text-align: center; margin-bottom: 25px;'><h3 style='color:#FFFFFF; font-weight: 300; font-style:italic;'>Stop gambling and start forecasting.</h3><p style='font-size:18px; color:#AAAAAA;'>The Mitrax Oracle uses mathematical patterns to fill the Grid with winning numbers.<br>Get a <span style='color:#FFD700; font-weight:bold;'>95% chance of winning</span> by subscribing today.</p></div>""", unsafe_allow_html=True)
    
    st.video("https://youtu.be/Hhj7UPfmB6U") 
    
    if st.button("PROCEED TO SUBSCRIPTION"):
        st.session_state.step = 'legal'; st.rerun()
