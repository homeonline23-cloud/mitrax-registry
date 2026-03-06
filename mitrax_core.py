# --- THE MARCHING SOLDIERS VIDEO OVERLAY ---
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID") # The Soldiers Marching

# --- THE "SMALLER" PREDICTED OUTCOME TEXT ---
st.markdown("""
    <div style="
        text-align: center; 
        padding-top: 5px;
    ">
        <p style="
            color: white; 
            font-size: 14px;  /* SHRINKING THE SIZE HERE */
            font-family: 'Courier New', monospace; 
            letter-spacing: 2px;
            margin-bottom: 0px;
        ">
            TARGET PICK 4 OUTCOME: <span style="color: orange; font-weight: bold;">[ 2 6 2 0 ]</span>
        </p>
        <p style="color: #666; font-size: 10px;">SYSTEM STATUS: MIRROR SYNCED</p>
    </div>
    """, unsafe_allow_html=True)
