import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL "GOLDEN GLOW" STYLING ---
st.markdown("""
    <style>
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
    
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important;
        border: 2px solid #FFD700 !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 15px #FFD700 !important;
        transform: scale(1.02);
    }
    
    .pyramid-frame {
        border: 4px solid #FFD700; 
        border-radius: 20px;
        padding: 5px; 
        background-color: #000;
        box-shadow: 0px 0px 40px rgba(255, 215, 0, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- 3. FLOW CONTROL ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)
    
    # Soldier Display Video (Autoplay)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    
    if st.button("PROCEED TO MISSION BRIEFING", use_container_width=True):
        st.session_state.step = 'legal'
        st.rerun()

elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 READ FIRST</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#1E1E1E; padding:20px; border-radius:10px; border:1px solid #FFD700; height:350px; overflow-y:scroll;'><h3>Terms and Conditions & Private Policy</h3><p>95% probability based on internal symmetry detection...</p></div>", unsafe_allow_html=True)
    if st.button("I ACCEPT THE TERMS", use_container_width=True):
        st.session_state.step = 'welcome'
        st.rerun()

elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#1A1A1A; padding:20px; border-radius:15px; border:1px solid #333;'><h3>Welcome to The Mitrax Command Center!</h3><p>Wake up the 14 Soldiers anytime!</p></div>", unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT", use_container_width=True):
