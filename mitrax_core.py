import streamlit as st
import pandas as pd
from datetime import datetime
from collections import Counter

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Master Computer", layout="wide")

# --- 2. IMPERIAL STYLING (GHOST ANALYSIS MODE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    @keyframes ghostGlow {
        0% { color: #00FFFF; text-shadow: 0 0 5px #00FFFF; }
        50% { color: #FFFFFF; text-shadow: 0 0 20px #00FFFF; }
        100% { color: #00FFFF; text-shadow: 0 0 5px #00FFFF; }
    }
    .vault-header { text-align: center; color: #FFD700; font-size: 38px; font-weight: bold; animation: goldPulse 2s infinite; }
    .ghost-text { text-align: center; font-size: 24px; font-weight: bold; animation: ghostGlow 1.5s infinite; }
    .stButton>button { background-color: #FFD700 !important; color: #0E1117 !important; font-weight: bold !important; border-radius: 12px !important; width: 100%; border: 2px solid #FFD700; }
    .grid-box { border: 2px solid #FFD700; padding: 15px; border-radius: 10px; background-color: #1A1A1A; text-align: center; }
    .brain-box { border: 2px solid #00FFFF; padding: 15px; border-radius: 10px; background-color: #000B14; text-align: center; }
    .compass-text { color: #FFD700; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER CREST ---
st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 80px; filter: drop-shadow(0 0 15px #FFD700);'>🛡️</div>
        <div style='margin-top: -65px; font-size: 35px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'
if 'history' not in st.session_state: st.session_state.history = []

# --- ONBOARDING FLOW ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>MITRAX MASTER COMPUTER</h1>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    if st.button("PROCEED TO MISSION BRIEFING"):
        st.session_state.step = 'legal'; st.rerun()

elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 TERMS & POLICY</h1>", unsafe_allow_html=True)
    if st.button("I ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'; st.rerun()

elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT"):
        st.session_state.step = 'signup'; st.rerun()

elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>THE MITRAX VAULT 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        name = st.text_input("Commander Name")
        email = st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE MASTER COMPUTER"):
            st.session_state.user_name = name; st.session_state.step = 'sector3'; st.rerun()

# --- SECTOR 3: GHOST ANALYSIS ENGINE ---
elif st.session_state.step == 'sector3':
    st.markdown(f"<div class='vault-header'>🔱 SECTOR 3: GHOST ANALYSIS MODE</div>", unsafe_allow_html=True)
    
    tabs = st.tabs(["🧮 Symmetry Input", "👻 Ghost Analysis Brain"])
    
    with tabs[0]:
        st.write("### Input Symmetry for Analysis")
        cols = st.columns(4)
        n1 = cols[0].number_input("N1", 0, 9, key="n1")
        n2 = cols[1].number_input("N2", 0, 9, key="n2")
        n3 = cols[2].number_input("N3", 0, 9, key="n3")
        n4 = cols[3].number_input("N4", 0, 9, key="n4")
        
        if st.button("UPLOAD TO GHOST BRAIN"):
            pred = f"{n1}{n2}{n3}{n4}"
            st.session_state.history.append(pred)
            st.success(f"Pattern {pred} synchronized with Master Computer.")

    with tabs[1]:
        st.markdown("<div class='brain-box'><span class='ghost-text'>GHOST FREQUENCY TRACKER</span></div>", unsafe_allow_html=True)
        
        if st.session_state.history:
            # GHOST ANALYSIS LOGIC
            counts = Counter(st.session_state.history)
            most_common = counts.most_common(3)
            
            st.write("### 🔥 Hot Frequencies (Top Ghosts)")
            for val, count in most_common:
                st.markdown(f"<div style='color:#00FFFF; font-size:20px;'>Pattern <b>{val}</b> detected <b>{count}</b> times in the Grid.</div>", unsafe_allow_html=True)
            
            st.markdown("---")
            st.write("### 📜 Full Brain History")
            st.write(st.session_state.history)
        else:
            st.info("Ghost Brain is currently empty. Input data to see future winnings.")

    # COMPASS REMAINS FOR ALIGNMENT
    st.markdown("---")
    c1, c2, c3 = st.columns([1,2,1])
    with c2: st.markdown("<div class='grid-box'><span class='compass-text'>NORTH, SOUTH, EAST, WEST ALIGNMENT</span></div>", unsafe_allow_html=True)
