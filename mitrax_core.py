import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL BACK DOOR ---
if 'step' not in st.session_state:
    st.session_state.step = 'sector3'

# --- 2. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Oracle Global", layout="wide")

# --- 3. UNIVERSAL STYLING (THE GOLDEN HULL) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .mitrax-title { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 50px; letter-spacing: 12px; margin-bottom: 0px; }
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 22px; letter-spacing: 4px; margin-bottom: 25px; opacity: 0.9; }
    .grid-box { border: 2px solid #FFD700; border-radius: 12px; padding: 20px; text-align: center; background-color: rgba(255, 215, 0, 0.07); }
    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; margin-bottom: 10px; border-bottom: 2px solid #FFD700; padding-bottom: 5px; }
    .global-banner { 
        background: linear-gradient(90deg, rgba(255,215,0,0.1) 0%, rgba(255,215,0,0.3) 50%, rgba(255,215,0,0.1) 100%);
        border: 1px solid #FFD700; border-radius: 5px; padding: 15px; text-align: center; 
        color: #FFD700; font-family: 'Impact', sans-serif; font-size: 18px; letter-spacing: 2px; margin-top: 20px;
    }
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 26px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 26px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE ORACLE VAULT CONTENT (SECTOR 3) ---
if st.session_state.step == 'sector3':
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    st.markdown("<div style='text-align: center; font-size: 75px; margin-bottom: -10px;'>✧🌍✧</div>", unsafe_allow_html=True)
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
    st.markdown("<h3 style='text-align: center; color: #FFD700;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
    i_cols = st.columns(4)
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    for i, island in enumerate(islands):
        with i_cols[i]:
            st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
            for row in range(1, 5):
                label = f"PRIZE {row}" if row > 1 else "★ WINNER ★"
                st.text_input(label, key=f"win_{island}_{row}", placeholder="----")

    # --- THE GLOBAL COMMAND BANNER (NEW GRID) ---
    st.markdown("""
        <div class='global-banner'>
            🌍 GLOBAL ADAPTATION PROTOCOL: MEMBERS FROM OTHER NATIONS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
            TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. 🌍
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center; color: #FFD700;'>95% PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
    g_cols = st.columns(6)
    for i in range(6):
        with g_cols[i]:
            st.markdown(f"<div style='border: 1px solid #FFD700; padding: 10px; text-align: center; background: rgba(255,215,0,0.05); color:#FFD700; font-weight:bold;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"v_{i}", label_visibility="collapsed", key=f"val_{i}", min_value=0, max_value=9999)

    st.divider()
    st.success("STATION STATUS: UNIVERSAL ACCESS ENABLED | COMPASS ALIGNED")

else:
    st.error("ACCESS DENIED.")
