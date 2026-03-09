import streamlit as st

# --- 1. THE IMPERIAL BACK DOOR (Skip to the Vault) ---
# This must come AFTER the import line above!
if 'step' not in st.session_state: 
    st.session_state.step = 'sector3'

# --- 2. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 3. UNIVERSAL STYLING (GOLDEN FILAMENT) ---
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
        text-align: center; color: #FFD700; font-family: 'Impact', sans-serif;
        font-size: 42px; letter-spacing: 8px; margin-bottom: 0px; line-height: 1.2;
    }
    
    .symbol-container { text-align: center; margin-top: 20px; margin-bottom: 10px; }
    .star-base { font-size: 60px; color: #FFD700; position: relative; display: inline-block; }
    .world-center { position: absolute; top: 12%; left: 0; right: 0; font-size: 30px; animation: slowGoldPulse 5s infinite; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE SLEEK UNIVERSAL COMPASS ---
st.markdown("<div class='symbol-container'><div class='star-base'>✧<div class='world-center'>🌍</div></div></div>", unsafe_allow_html=True)

# --- 5. THE ORACLE VAULT (YOUR TARGET SECTOR) ---
if st.session_state.step == 'sector3':
    st.markdown("<div class='mitrax-title'>ORACLE VAULT</div>", unsafe_allow_html=True)
    st.success("WELCOME BACK, HEAD CHEF. THE BRIDGE IS RESTORED.")
    st.write("The 6x Grids are standing by. The rabbit has been ejected.")

# --- EMERGENCY FALLBACK ---
else:
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.write("Vision loading...")
