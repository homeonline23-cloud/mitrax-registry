import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL "GOLDEN GLOW" STYLING ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Pulsing Golden Mitrax Title */
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700; }
        50% { text-shadow: 0 0 25px #FFD700, 0 0 50px #FFA500; }
        100% { text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700; }
    }
    
    .vault-header {
        text-align: center; 
        color: #FFD700; 
        font-size: 38px; 
        font-weight: bold;
        animation: goldPulse 2s infinite;
        margin-bottom: 25px;
    }
    
    /* Imperial Buttons */
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important;
        border: 2px solid #FFD700 !important;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px #FFD700 !important;
        transform: scale(1.01);
    }
    
    /* Global Mantra Box */
    .mantra-box { 
        text-align: center; color: #FFFFFF; font-size: 19px; 
        padding: 25px; background-color: #1A1A1A;
        border-radius: 15px; border: 2px solid #FFD700; margin: 15px 0px;
        line-height: 1.6;
    }

    /* High-Def Video Frame */
    .pyramid-frame {
        border: 4px solid #FFD700; 
        border-radius: 20px;
        padding: 5px; 
        background-color: #000;
        box-shadow: 0px 0px 40px rgba(255, 215, 0, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MISSION PROGRESSION LOGIC ---
if 'step' not in st.session_state: 
    st.session_state.step = 'video'

# --- PHASE 1: THE SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='mantra-box'>
    "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
    into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential 
    winning
