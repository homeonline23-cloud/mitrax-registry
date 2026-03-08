import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING (CLEAN & SHARP) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Pulsing Master Crest */
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    
    .vault-header { 
        text-align: center; 
        color: #FFD700; 
        font-size: 38px; 
        font-weight: bold; 
        animation: goldPulse 2s infinite; 
    }
    
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important; 
        width: 100%; 
        border: 2px solid #FFD700; 
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px #FFD700 !important;
        transform: scale(1.02);
    }
    
    .grid-box { 
        border: 2px solid #FFD700; 
        padding: 15px; 
        border-radius: 10px; 
        background-color: #1A1A1A; 
        text-align: center; 
    }
    
    .compass-text { color: #FFD700; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER CREST (SHIELD & PYRAMID) ---
# This is the ONLY place the shield appears now
st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 80px; filter: drop-shadow(0 0 15px #FFD700);'>🛡️</div>
        <div style='margin-top: -65px; font-size: 35px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- PHASE 1: SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    # SHIELD REMOVED FROM NEXT TO NAME BELOW
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; padding:20px; border:1px solid #FFD700; border-radius:15px; margin-bottom:15px; background-color: #1A1A1A;'>The 4-digit Prediction Calculator used Globally. Analyzing symmetry patterns identifies potential winning numbers. 95% Chance of Success.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    if st.button("PROCEED TO MISSION BRIEFING"):
        st.session_state.step = 'legal'
        st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.info("95% probability protocol active. Symmetry data remains secured within the Mitrax Vault.")
    if st.button("I ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- PHASE 3: WELCOME & INSTALL ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color:#1A1A1A; padding:20px; border-radius:15px; border:1px solid #333;'>
    <h3>Install the Mitrax App Icon on your phone!</h3>
    <p>Android: 3 Dots -> Install App | iPhone: Share -> Add to Home Screen</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT"):
        st.session_state.step = 'signup'
        st.rerun()

# --- PHASE 4: REGISTRATION ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>THE MITRAX VAULT 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
