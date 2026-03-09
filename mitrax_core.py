import streamlit as st
import pandas as pd
from datetime import datetime
from collections import Counter

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING (THE GOLDEN LABORATORY) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* SLOWED DOWN GOLDEN GLOBE PULSE */
    @keyframes slowGoldPulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 10px #FFD700); }
        50% { transform: scale(1.05); filter: drop-shadow(0 0 25px #FFD700); }
        100% { transform: scale(1); filter: drop-shadow(0 0 10px #FFD700); }
    }
    
    .vault-header { text-align: center; color: #FFD700; font-size: 38px; font-weight: bold; font-family: 'Impact'; }
    
    .stButton>button { 
        background-color: #FFD700 !important; color: #000000 !important; 
        font-family: 'Impact', sans-serif !important; font-weight: 900 !important; 
        text-transform: uppercase; border-radius: 12px !important; width: 100%; 
        border: 2px solid #000000; font-size: 24px !important;
    }
    
    .pay-link {
        display: block; text-align: center; background-color: #FFD700; color: #000000 !important;
        padding: 20px; border-radius: 12px; font-family: 'Impact', sans-serif !important;
        font-weight: 900 !important; text-transform: uppercase; text-decoration: none;
        font-size: 26px; border: 3px solid #000000; margin: 15px 0;
    }
    
    .grid-box { border: 2px solid #FFD700; padding: 25px; border-radius: 15px; background-color: #1A1A1A; margin-bottom: 20px; }
    .globe-container { text-align: center; margin-bottom: 20px; position: relative; }
    .globe-pulse { font-size: 80px; display: inline-block; animation: slowGoldPulse 6s infinite; }
    
    /* CUSTOM COMPASS LABELS REMOVED PER CHEF'S COMMAND */
    .compass-labels { display: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE UNIVERSAL COMPASS SEAL (CUSTOM COMPASS DESIGN) ---
st.markdown("""
    <div class='globe-container'>
        <div style='display: flex; justify-content: center; align-items: center; position: relative;'>
            <div style='font-size: 200px; color: #FFD700; filter: drop-shadow(0 0 10px #FFD700);'>🧭</div>
            <div style='position: absolute;' class='globe-pulse'>🌍</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'intro'
if 'history' not in st.session_state: st.session_state.history = []

# --- PHASE 1: THE PREDICTION INTRO ---
if st.session_state.step == 'intro':
    st.markdown("<h1 style='text-align:center; color:#FFD700; font-family:Impact;'>THE MITRAX ORACLE PREDICTION PIC 4</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-bottom: 25px;'>
        <h3 style='color:#FFFFFF; font-style:italic;'>Stop gambling and start forecasting.</h3>
        <p style='font-size:20px; color:#FFFFFF;'>
            The Mitrax Oracle uses mathematical patterns to fill the Grid with winning numbers.<br>
            Get a <span style='color:#FFD700; font-weight:bold;'>95% chance of winning</span> by subscribing to the pattern analysis today.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.video("https://youtu.be/Hhj7UPfmB6U") 
    
    if st.button("PROCEED TO SUBSCRIPTION"):
        st.session_state.step = 'legal'; st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700; font-family:Impact;'>SERVICE TERMS</h1>", unsafe_allow_html=True)
    st.info("Unlock the 95% mathematical advantage using the 6x Grid system.")
    if st.button("I AGREE TO THE TERMS"):
        st.session_state.step = 'welcome'; st.rerun()

# --- PHASE 3: SUBSCRIPTION GATEWAY ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700; font-family:Impact;'>GET YOUR PREDICTIONS</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='grid-box'>
        <h3 style='color:#FFD700;'>HOW IT WORKS:</h3>
        <p style='font-size:18px;'>1. WE GATHER THE LAST 20 WINNING RESULTS.</p>
        <p style='font-size:18px;'>2. WE ENTER DATA INTO THE 6X GRIDS TO FIND HIDDEN CODES.</p>
        <p style='font-size:18px;'>3. YOU COPY AND PLAY THE PREDICTED NUMBERS FOR 3 DAYS.</p>
    </div>
    <div style='text-align:center;'>
        <h2 style='color:#FFD700; font-family:Impact;'>SUBSCRIBE FOR FULL ACCESS</h2>
        <p style='color:#FFD700; font-size:24px; font-weight:900;'>$39.95 EVERY 3 MONTHS</p>
        <a href="https://www.paypal.com/ncp/payment/ZXZXQZ7ZBYUN8" target="_blank" class="pay-link">ACTIVATE SUBSCRIPTION NOW</a>
    </div>
    """, unsafe_allow_html=True)

    if st.button("CONTINUE TO SIGN-UP"):
        st.session_state.step = 'signup'; st.rerun()

# --- PHASE 4: SIGN-UP ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>SIGN-UP FOR PREDICTIONS</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        name = st.text_input("NAME")
        email = st.text_input("EMAIL")
        if st.form_submit_button("ENTER THE ORACLE"):
            st.session_state.user_name = name; st.session_state.step = 'sector3'; st.rerun()

# --- PHASE 5: THE ORACLE BRAIN ---
elif st.session_state.step == 'sector3':
    st.markdown(f"<div class='vault-header'>PREDICTIONS ACTIVE</div>", unsafe_allow_html=True)
    st.write(f"Visionary {st.session_state.get('user_name', '')}, the Universal Compass is aligned.")
