import streamlit as st
import time
from datetime import datetime, timedelta

# --- 1. COMMAND CENTER ENGINE ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING (BLACK & GOLD) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { background-color: #FFD700 !important; color: #0E1117 !important; font-weight: bold !important; border-radius: 10px !important; }
    .legal-box { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 1px solid #FFD700; height: 300px; overflow-y: scroll; font-size: 14px; }
    .client-header { text-align: center; color: #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE TRACKING ---
if 'step' not in st.session_state: st.session_state.step = 'video'

# --- 4. PHASE 1: VIDEO INTRODUCTION (SOLDIERS DISPLAY) ---
if st.session_state.step == 'video':
    st.markdown("<h1 class='client-header'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    # Placeholder for your soldier display video
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with your actual Soldiers Display URL
    
    st.write("Initializing Imperial Systems...")
    time.sleep(2) # Simulated 20-second threshold progress
    if st.button("PROCEED TO MISSION BRIEFING"):
        st.session_state.step = 'legal'
        st.rerun()

# --- 5. PHASE 2: TERMS & PRIVATE POLICY ---
elif st.session_state.step == 'legal':
    st.markdown("<h2 class='client-header'>📜 READ FIRST: TERMS & POLICY</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='legal-box'>
    <b>TERMS AND CONDITIONS:</b><br>
    The Mitrax Command Center is a 4-digit Prediction Calculator intended for global use...
    By using this symmetry pattern analyzer, you acknowledge that predictions are based on 
    mathematical symmetry. We provide a 95% probability increase based on global data...
    <br><br><b>PRIVACY POLICY:</b><br>
    Your tactical data and coordinate entries remain encrypted within the Mitrax Empire...
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("I ACCEPT THE IMPERIAL TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- 6. PHASE 3: WELCOME & INSTALLATION ---
elif st.session_state.step == 'welcome':
    st.markdown("<h2 class='client-header'>✉️ WELCOME, COMMANDER</h2>", unsafe_allow_html=True)
    st.write("""
    ### Installation Instructions:
    1. **On Mobile:** Click the browser menu (three dots) and select 'Add to Home Screen'.
    2. **On Desktop:** Click the 'Install' icon in the URL bar.
    3. **Registry:** Secure your login to access the worldwide symmetry grids.
    """)
    if st.button("CONTINUE TO SIGN-UP"):
        st.session_state.step = 'signup'
        st.rerun()

# --- 7. PHASE 4: SIGN-UP & ACCESS ---
elif st.session_state.step == 'signup':
    st.markdown("<h2 class='client-header'>👤 SIGN UP TO CONTINUE</h2>", unsafe_allow_html=True)
    with st.form("signup_form"):
        st.text_input("Imperial ID / Email")
        st.text_input("Access Code Request", type="password")
        if st.form_submit_button("ACTIVATE COMMANDER ACCESS"):
            st.success("Registration Sent. Accessing Global Symmetry Grids...")
            # Here we would link back to your main Calculator code
