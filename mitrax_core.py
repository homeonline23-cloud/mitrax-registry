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
    
    /* SLOWED DOWN GOLDEN PULSE */
    @keyframes slowGoldPulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 10px #FFD700); }
        50% { transform: scale(1.03); filter: drop-shadow(0 0 20px #FFD700); }
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
    .globe-container { text-align: center; margin-bottom: 20px; }
    .globe-pulse { font-size: 80px; display: inline-block; animation: slowGoldPulse 5s infinite; }
    .compass-labels { color: #FFD700; font-family: 'Impact'; font-size: 22px; letter-spacing: 5px; line-height: 1.2; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE UNIVERSAL COMPASS SEAL ---
st.markdown("""
    <div class='globe-container'>
        <div class='compass-labels'>NORTH</div>
        <div style='display: flex; justify-content: center; align-items: center; gap: 20px;'>
            <span class='compass-labels'>WEST</span>
            <span class='globe-pulse'>🌍</span>
            <span class='compass-labels'>EAST</span>
        </div>
        <div class='compass-labels'>SOUTH</div>
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
            Get
