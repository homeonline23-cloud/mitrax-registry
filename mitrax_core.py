import streamlit as st
import pandas as pd
from datetime import datetime
from collections import Counter

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING (THE GOLDEN LABORATORY) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    .vault-header { text-align: center; color: #FFD700; font-size: 38px; font-weight: bold; animation: goldPulse 2s infinite; }
    
    .stButton>button { 
        background-color: #FFD700 !important; color: #0E1117 !important; 
        font-weight: bold !important; border-radius: 12px !important; 
        width: 100%; border: 2px solid #FFD700; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 25px #FFD700; }
    
    .pay-link {
        display: block; text-align: center; background-color: #FFD700; color: #0E1117 !important;
        padding: 15px; border-radius: 12px; font-weight: bold; text-decoration: none;
        font-size: 20px; border: 2px solid #FFD700; transition: 0.3s; margin: 10px 0;
    }
    .pay-link:hover { box-shadow: 0 0 30px #FFD700; transform: scale(1.01); }

    .grid-box { border: 2px solid #FFD700; padding: 15px; border-radius: 10px; background-color: #1A1A1A; text-align: center; }
    .brain-box { border: 2px solid #00FFFF; padding: 15px; border-radius: 10px; background-color: #000B14; text-align: center; }
    .compass-text { color: #FFD700; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER SEAL (SHIELD & PYRAMID) ---
st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 80px; filter: drop-shadow(0 0 15px #FFD700);'>🛡️</div>
        <div style='margin-top: -65px; font-size: 35px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'
if 'history' not in st.session_state: st.session_state.history = []

# --- PHASE 1: THE COUNCIL ENTRANCE ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>THE MITRAX ORACLE VISION</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='grid-box'>
        <b>The Wisdom of the Ages🌏</b><br><br>
        A 95% Probability Matrix powered by the laws of Newton, Tesla, Einstein, and the foresight of Nostradamus. 
        Identify symmetry patterns across the Universal Compass (North, South, East, West) to reveal 
        the evening's destined winning numbers.
    </div>
    """, unsafe_allow_html=True)
    
    # --- YOUR NEW SCIENTIFIC VIDEO ---
    st.video("https://youtu.be/Hhj7UPfmB6U", autoplay=True, muted=True) 
    
    if st.button("ENTER THE HALL OF WISDOM"):
        st.session_state.step = 'legal'; st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 THE ORACLE COVENANT</h1>", unsafe_allow_html=True)
    st.info("The 95% probability meter is calculated through universal symmetry. Please enter the vault with intent.")
    if st.button("I UNDERSTAND THE UNIVERSAL LAWS"):
        st.session_state.step = 'welcome'; st.rerun()

# --- PHASE 3: THE TREASURY ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME TO THE CIRCLE</h1>", unsafe_allow_html=True)
    st.markdown("<div class='grid-box'><h3>Secure the Oracle on your Home Screen</h3><p>Android: 3 Dots -> Install App | iPhone: Share -> Add to Home Screen</p></div>", unsafe_allow_html=True)
    
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
        <h2 style='color:#FFD700;'>💎 FULL SYMMETRY ACCESS</h2>
        <p style='font-size:18px;'>Unlock the 95% Probability Meter & Ghost Analysis</p>
        <p style='color:#FFD700; font-size:22px; font-weight:bold;'>Membership Renewal: $39.95 every 3 months</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <a href="https://www.paypal.com/ncp/payment/ZXZXQZ7ZBYUN8" target="_blank" class="pay-link">
            ⚜️ ACTIVATE MEMBERSHIP VIA PAYPAL
        </a>
    """, unsafe_allow_html=True)

    if st.button("PROCEED TO THE VAULT REGISTRATION"):
        st.session_state.step = 'signup'; st.rerun()

# --- PHASE 4: REGISTRATION ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>THE ORACLE VAULT 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        st.markdown("<h4 style='text-align:center;'>Visionary Registration</h4>", unsafe_allow_html=True)
        name = st.text_input("Visionary Name")
        email = st.text_input("Universal Email")
        if st.form_submit_button("ACTIVATE ORACLE VISION"):
            st.session_state.user_name = name; st.session_state.step = 'sector3'; st.rerun()

# --- PHASE 5: THE ORACLE BRAIN ---
elif st.session_state.step == 'sector3':
    st.markdown(f"<div class='vault-header'>🔱 THE ORACLE VISION ACTIVE</div>", unsafe_allow_html=True)
    
    # --- COMPASS GRID ---
    st.write("### Universal Compass Alignment")
    c1, c2, c3 = st.columns([1,2,1])
    with c2: st.markdown("<div class='grid-box'><span class='compass-text'>NORTH</span></div>", unsafe_allow_html=True)
    l, r = st.columns(2)
    with l: st.markdown("<div class='grid-box'><span class='compass-text'>WEST</span></div>", unsafe_allow_html=True)
    with r: st.markdown("<div class='grid-box'><span class='compass-text'>EAST</span></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='grid-box'><span class='compass-text'>SOUTH</span></div>", unsafe_allow_html=True)

    st.markdown("---")
    tabs = st.tabs(["🧮 Symmetry Input", "🧠 Ghost Analysis"])
    
    with tabs[0]:
        st.write("### Input Numbers for Prediction")
        cols = st.columns(4)
        n1 = cols[0].number_input("N1", 0, 9, key="n1")
        n2 = cols[1].number_input("N2", 0, 9, key="n2")
        n3 = cols[3].number_input("N3", 0, 9, key="n3")
        n4 = cols[3].number_input("N4", 0, 9, key="n4")
        if st.button("SYNC WITH THE COUNCIL"):
            pred = f"{n1}{n2}{n3}{n4}"
            st.session_state.history.append(pred)
            st.success(f"Pattern {pred} synchronized.")

    with tabs[1]:
        if st.session_state.history:
            counts = Counter(st.session_state.history)
            st.write("### 🔥 Ghost Frequencies Detected")
            for val, count in counts.most_common(3):
                st.write(f"Pattern {val} - Vision Strength: {count}x")
        else:
            st.info("The Oracle is scanning for evening frequencies...")
