import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING (THE IMPERIAL CASING) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* TITLES & DATES */
    .mitrax-title { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 60px; letter-spacing: 15px; margin-bottom: 0px; }
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 22px; letter-spacing: 5px; margin-bottom: 30px; }
    
    /* THE FRONT GATE DESIGN */
    .gate-frame {
        border: 5px double #FFD700; border-radius: 20px; padding: 50px; text-align: center;
        background: radial-gradient(circle, rgba(255,215,0,0.1) 0%, rgba(14,17,23,1) 100%);
        margin: 50px auto; max-width: 800px;
    }
    
    /* BOLD ARIAL GLOBAL BANNER */
    .global-banner { 
        background: rgba(255, 215, 0, 0.1); border: 2px solid #FFD700; border-radius: 10px; 
        padding: 25px; text-align: center; color: #FFFFFF; font-family: 'Arial', sans-serif; 
        font-weight: bold; font-size: 20px; line-height: 1.6; margin-bottom: 30px;
    }

    /* GRID BOXES */
    .grid-box { border: 2px solid #FFD700; border-radius: 12px; padding: 20px; text-align: center; background-color: rgba(255, 215, 0, 0.07); }
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 26px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 26px; }
    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; border-bottom: 2px solid #FFD700; font-family: 'Arial', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE LOGIC GATE ---
if 'step' not in st.session_state:
    st.session_state.step = 'gate'

# --- 4. SECTOR: THE FRONT GATE (LOBBY) ---
if st.session_state.step == 'gate':
    st.markdown("<div style='text-align: center; font-size: 100px; margin-top: 50px;'>✧🌍✧</div>", unsafe_allow_html=True)
    st.markdown("<div class='gate-frame'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #FFD700; font-family: Impact; letter-spacing: 10px;'>MITRAX EMPIRE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-family: Arial; font-weight: bold; font-size: 18px;'>UNIVERSAL REGISTRY & ORACLE VAULT</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 ENTER THE ORACLE VAULT"):
        st.session_state.step = 'sector3'
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #444;'>AUTHORIZED PERSONNEL ONLY - 95% PROBABILITY ACTIVE</p>", unsafe_allow_html=True)

# --- 5. SECTOR: THE ORACLE VAULT (INSIDE) ---
elif st.session_state.step == 'sector3':
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    # NAVIGATION BAR (TO GO BACK TO GATE)
    if st.button("⬅ EXIT TO LOBBY"):
        st.session_state.step = 'gate'
        st.rerun()

    st.markdown("<div style='text-align: center; font-size: 60px;'>✧🌍✧</div>", unsafe_allow_html=True)
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='date-stamp'>SESSION DATE: {imperial_date}</div>", unsafe_allow_html=True)

    # THE CORE PROTOCOLS
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='grid-box'><p style='color:#AAA;'>PROTOCOL 7/1</p><p class='red-protocol'>RED ZONE</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='grid-box'><p style='color:#AAA;'>PROTOCOL 8/3</p><p class='blue-protocol'>BLUE ZONE</p></div>", unsafe_allow_html=True)

    st.divider()

    # --- THE 4-TIER ISLAND WINNER BOARD ---
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
    i_cols = st.columns(4)
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    for i, island in enumerate(islands):
        with i_cols[i]:
            st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
            for row in range(1, 5):
                st.text_input(f"{island} P{row}", key=f"win_{island}_{row}", label_visibility="collapsed", placeholder="----")

    # --- THE WHITE BOLD ARIAL GLOBAL COMMAND BANNER ---
    st.markdown("""
        <div class='global-banner'>
            🌍 GLOBAL ADAPTATION PROTOCOL: MEMBERS FROM OTHER NATIONS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
            TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. THE SYSTEM IS UNIVERSAL. 🌍
        </div>
        """, unsafe_allow_html=True)

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>95% PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
    g_cols = st.columns(6)
    for i in range(6):
        with g_cols[i]:
            st.markdown(f"<div style='border: 1px solid #FFD700; padding: 10px; text-align: center; background: rgba(255,215,0,0.05); color:#FFD700; font-weight:bold; font-family:Arial;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"val_{i}", label_visibility="collapsed", key=f"v_{i}", min_value=0, max_value=9999)

    st.divider()
    st.success("STATION STATUS: VAULT SECURED | COMPASS ALIGNED")
