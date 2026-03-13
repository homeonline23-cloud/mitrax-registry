import streamlit as st

# This line tells Python to ignore the CSS and just send it to the web browser
st.markdown("""
    <style>
    /* THE GOLD NEON CSS */
    .oracle-title {
        font-size: 80px; 
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        color: #FFD700;
        text-transform: uppercase;
        text-align: center;
        
        /* BLACK NEON LINES */
        text-shadow: 
            -3px -3px 0 #000,  
             3px -3px 0 #000,
            -3px  3px 0 #000,
             3px  3px 0 #000,
             0 0 20px #FFD700;
        
        padding: 50px;
        background-color: #000;
    }
    
    body {
        background-color: #000;
    }
    </style>

    <div class="oracle-title">
        MITRIX ORACLE PIC 4
    </div>
    """, unsafe_allow_html=True)
