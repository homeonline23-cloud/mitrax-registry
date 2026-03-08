import streamlit as st
import pandas as pd
from datetime import datetime
from collections import Counter

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Master Computer", layout="wide")

# --- 2. IMPERIAL STYLING (ALERTS & TREASURY) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    
    @keyframes alertRed {
        0% { background-color: #1A0000; border: 2px solid #FF0000; box-shadow: 0 0 5px #FF0000; }
        50% { background-color: #4D0000; border: 2px solid #FF4444; box-shadow: 0 0 25px #FF0000; }
        100% { background-color: #1A0000; border: 2px solid #FF0000; box-shadow: 0 0 5px #FF0000; }
    }

    .vault-header { text-align: center; color: #FFD700; font-size: 38px; font-weight: bold; animation: goldPulse 2s infinite; }
    
    .stButton>button { 
        background-color: #FFD700 !important; color: #0E1117 !important; 
        font-weight: bold !important; border-radius: 12px !important; 
        width: 100%; border: 2px solid #FFD700; transition: 0.3s;
    }
    
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px #FFD700; }

    .imperial-alert {
        padding: 20px; border-radius: 15px; text-align: center;
        animation: alertRed 1.5s infinite; color: #FFFFFF; font-weight: bold; font-size: 22px;
        margin: 20px 0;
    }

    .grid-box { border: 2px solid #FFD700; padding: 15px; border-radius: 10px; background-color: #1A1A1A; text-align: center; }
    .brain-box { border: 2px solid #00FFFF; padding: 15px; border-radius: 10px; background-color: #000B14; text-align: center; }
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
    
    # --- TREASURY MODULE (PAYMENT GATEWAY) ---
    st.markdown("<div class='grid-box'><h3>💎 UPGRADE TO FULL IMPERIAL ACCESS</h3><p>Unlock 24/7 Ghost Analysis & Prediction History</p></div>", unsafe_allow_html=True)
    if st.button("⚜️ ACTIVATE GOLDEN MEMBERSHIP (PAYPAL)"):
        # Placeholder link until tomorrow's update
        st.warning("TREASURY LINK INITIALIZING... PAYPAL GATEWAY OPENING TOMORROW.")
        # When you have the link, we replace the line below:
        # st.markdown("[Click here to pay](https://www.paypal.com/...)")

    if st.button("CONTINUE TO VAULT REGISTRATION"):
        st.session_state.step = 'signup'; st.rerun()

elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>THE MITRAX VAULT 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        name = st.text_input("Commander Name")
        email = st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE MASTER COMPUTER"):
            st.session_state.user_name = name; st.session_state.step = 'sector3'; st.rerun()

# --- SECTOR 3: GHOST ANALYSIS & IMPERIAL ALERT ---
elif st.session_state.step == 'sector3':
    st.markdown(f"<div class='vault-header'>🔱 SECTOR 3: MASTER COMPUTER</div>", unsafe_allow_html=True)
    
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
            st.success(f"Pattern {pred} synchronized.")

    with tabs[1]:
        if st.session_state.history:
            counts = Counter(st.session_state.history)
            most_common = counts.most_common(1)
            
            # --- THE IMPERIAL ALERT ---
            if most_common[0][1] >= 2:
                st.markdown(f"""
                <div class='imperial-alert'>
                    🚨 IMPERIAL ALERT: 100% SYMMETRY MATCH DETECTED! 🚨<br>
                    PATTERN {most_common[0][0]} IS MANIFESTING IN THE GRID!
                </div>
                """, unsafe_allow_html=True)

            st.write("### 🔥 Ghost Frequencies")
            for val, count in counts.most_common(3):
                st.write(f"Pattern {val} - Strength: {count}x")
        else:
            st.info("Ghost Brain scanning for evening frequencies...")
