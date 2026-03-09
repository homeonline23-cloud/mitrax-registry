import streamlit as st
import pandas as pd
from datetime import datetime
from collections import Counter

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 2. ACCESSIBILITY STYLING (HIGH CONTRAST) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* FORCED BOLD & DARK BUTTONS FOR EYE SIGHT ACCESSIBILITY */
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #000000 !important; 
        font-weight: 900 !important; /* ULTRA BOLD */
        border-radius: 12px !important; 
        width: 100%; 
        border: 2px solid #FFD700; 
        font-size: 18px !important;
    }
    
    .pay-link {
        display: block; text-align: center; background-color: #FFD700; 
        color: #000000 !important;
        padding: 15px; border-radius: 12px; 
        font-weight: 900 !important; /* ULTRA BOLD */
        text-decoration: none;
        font-size: 20px; border: 2px solid #FFD700; margin: 10px 0;
    }

    .grid-box { border: 2px solid #FFD700; padding: 20px; border-radius: 15px; background-color: #1A1A1A; margin-bottom: 20px; }
    .highlight { color: #FFD700; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER SEAL ---
st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 80px; filter: drop-shadow(0 0 15px #FFD700);'>🛡️</div>
        <div style='margin-top: -65px; font-size: 35px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'intro'
if 'history' not in st.session_state: st.session_state.history = []

# --- PHASE 1: THE PREDICTION INTRO ---
if st.session_state.step == 'intro':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>The Mitrax Oracle Prediction Pic 4</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='grid-box'>
        <p style='font-size:18px;'><b>Stop gambling and start forecasting.</b></p>
        <p style='font-size:18px;'>The Mitrax Oracle uses mathematical patterns to fill the Grid with winning numbers. 
        Get a <span class='highlight'>95% chance of winning</span> by subscribing to the pattern analysis today.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.video("https://youtu.be/Hhj7UPfmB6U", autoplay=True, muted=True) 
    
    if st.button("PROCEED TO SUBSCRIPTION TERMS"):
        st.session_state.step = 'legal'; st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 SERVICE TERMS</h1>", unsafe_allow_html=True)
    st.info("Subscribe to unlock the 95% mathematical advantage. Patterns are identified through the 6x Grid system.")
    if st.button("I AGREE TO THE TERMS"):
        st.session_state.step = 'welcome'; st.rerun()

# --- PHASE 3: SUBSCRIPTION GATEWAY ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>GET YOUR PREDICTIONS</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='grid-box'>
        <h3>How it works:</h3>
        <p>1. We gather the last 20 winning results.</p>
        <p>2. We enter data into the 6x Grids to find hidden codes.</p>
        <p>3. You copy and play the predicted numbers for 3 days.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align:center;'>
            <h2 style='color:#FFD700;'>💎 SUBSCRIBE FOR FULL ACCESS</h2>
            <p style='color:#FFD700; font-size:22px; font-weight:bold;'>$39.95 EVERY 3 MONTHS</p>
            <a href="https://www.paypal.com/ncp/payment/ZXZXQZ7ZBYUN8" target="_blank" class="pay-link">ACTIVATE SUBSCRIPTION NOW</a>
        </div>
    """, unsafe_allow_html=True)

    if st.button("CONTINUE TO SIGN-UP"):
        st.session_state.step = 'signup'; st.rerun()

# --- PHASE 4: SIGN-UP ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>SIGN-UP FOR PREDICTIONS 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        if st.form_submit_button("ENTER THE ORACLE"):
            st.session_state.user_name = name; st.session_state.step = 'sector3'; st.rerun()

# --- PHASE 5: THE ORACLE BRAIN ---
elif st.session_state.step == 'sector3':
    st.markdown(f"<div class='vault-header'>🔱 PREDICTIONS ACTIVE</div>", unsafe_allow_html=True)
    # (Rest of calculator logic)
