import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING (SLEEK GOLDEN FILAMENT) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    @keyframes slowGoldPulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; filter: drop-shadow(0 0 15px #FFD700); }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    .mitrax-title {
        text-align: center;
        color: #FFD700;
        font-family: 'Impact', sans-serif;
        font-size: 42px;
        font-weight: 400;
        letter-spacing: 8px;
        margin-bottom: 0px;
    }
    
    .prediction-subtitle {
        text-align: center;
        color: #FFD700;
        font-family: 'Impact', sans-serif;
        font-size: 18px;
        letter-spacing: 4px;
        opacity: 0.8;
        margin-bottom: 20px;
    }
    
    .stButton>button { 
        background-color: #FFD700 !important; color: #000000 !important; 
        font-family: 'Impact', sans-serif !important; 
        text-transform: uppercase; border-radius: 8px !important; width: 100%; 
        border: none; font-size: 20px !important;
    }
    
    .pay-link {
        display: block; text-align: center; background-color: #FFD700; color: #000000 !important;
        padding: 15px; border-radius: 8px; font-family: 'Impact', sans-serif !important;
        text-transform: uppercase; text-decoration: none;
        font-size: 22px; margin: 15px 0;
    }
    
    .symbol-container { text-align: center; margin-top: 20px; margin-bottom: 10px; }
    .star-base { font-size: 60px; color: #FFD700; position: relative; display: inline-block; opacity: 0.9; }
    .world-center { position: absolute; top: 12%; left: 0; right: 0; font-size: 30px; animation: slowGoldPulse 5s infinite; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE SLEEK UNIVERSAL COMPASS ---
st.markdown("""
    <div class='symbol-container'>
        <div class='star-base'>
            ✧
            <div class='world-center'>🌍</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'intro'

# --- PHASE 1: THE PREDICTION INTRO ---
if st.session_state.step == 'intro':
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE
