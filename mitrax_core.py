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
    .mantra-text { 
        text-align: center; 
        color: #CCCCCC; 
        font-style: italic; 
        font-size: 18px; 
        padding: 10px 20px; 
        border-left: 3px solid #FFD700; 
        border-right: 3px solid #FFD700;
        margin-bottom: 30px;
    }
    .client-header { text-align: center; color: #FFD700; margin-bottom: 5px; }
    .legal-box { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 1px solid #FFD700; height: 300px; overflow-y: scroll; }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- 3. MISSION FLOW ---
if st.session_state.step == 'video':
    # MAIN TITLES
    st.markdown("<h1 class='client-header'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)
    
    # THE GLOBAL MANTRA
    st.markdown("""
    <div class='mantra-text'>
    "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
    into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential 
    winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning."
    </div>
    """, unsafe_allow_html=True)
    
    # Soldiers Display Placeholder
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
    
    if st.button("PROCEED TO MISSION BRIEFING", use_container_width=True):
        st.session_state.step = 'legal'
        st.rerun()

elif st.session_state.step == 'legal':
    st.markdown("<h2 class='client-header'>📜 TERMS & PRIVATE POLICY</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='legal-box'>
    <b>THE MITRAX COMMAND CENTER - GLOBAL PROTOCOL</b><br><br>
    The 4-digit Prediction Calculator that can be used Globally... 
    Analyzing symmetry patterns identifies potential winning numbers in the GRID’s. 
    There’s now a 95% chance of increasing your chances of winning...
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("I ACCEPT THE IMPERIAL TERMS", use_container_width=True):
        st.session_state.step = 'welcome'
        st.rerun()

elif st.session_state.step == 'welcome':
    st.markdown("<h2 class='client-header'>✉️ WELCOME LETTER & INSTALLATION</h2>", unsafe_allow_html=True)
    st.info("Mobile: Tap 'Add to Home Screen' | Desktop: Click Install in URL bar.")
    if st.button("GO TO SIGN-UP", use_container_width=True):
        st.session_state.step = 'signup'
        st.rerun()

elif st.session_state.step == 'signup':
    st.markdown("<h2 class='client-header'>👤 COMMANDER SIGN-UP</h2>", unsafe_allow_html=True)
    with st.form("reg"):
        st.text_input("Player Name")
        st.text_input("Imperial Email")
        if st.form_submit_button("REGISTER FOR ACCESS"):
            st.success("Data Sent to Command. Awaiting Authorization.")
            
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    with st.expander("🛠️ COMMANDER OVERRIDE"):
        if st.text_input("CHEF CODE", type="password") == "Mitrax-Chef":
            st.info("Accessing Symmetry Grids...")
