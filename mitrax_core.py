import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL BACK DOOR ---
if 'step' not in st.session_state:
    st.session_state.step = 'sector3'

# --- 2. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Oracle Global", layout="wide")

# --- 3. UNIVERSAL STYLING (BOLD ARIAL CASING) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Imperial Headers */
    .mitrax-title { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 50px; letter-spacing: 12px; margin-bottom: 0px; }
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 22px; letter-spacing: 4px; margin-bottom: 25px; opacity: 0.9; }
    
    /* The BOLD ARIAL Global Banner */
    .global-banner { 
        background: rgba(255, 215, 0, 0.15);
        border: 2px solid #FFD700; 
        border-radius: 8px; 
        padding: 20px; 
        text-align: center; 
        color: #FFFFFF; 
        font-family: 'Arial', sans-serif; 
        font-weight: bold; 
        font-size: 20px; 
        line-height: 1.5;
        margin-top: 20px;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.2);
    }
    
    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; margin-bottom: 10px; border-bottom: 2px solid #FFD700; padding-bottom: 5px; font-family: 'Arial', sans-serif; }
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 26px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 26px; }
    .grid-box { border: 2px solid #FFD700; border-radius: 12px; padding: 20px; text-align: center; background-color: rgba(255, 215, 0, 0.07); }
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
        st.markdown("<div class='grid-box'><p style='color:#AAA; font-family:Arial;'>PROTOCOL 7/1</p><p class='red-protocol'>RED ZONE</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='grid-box'><p style='color:#AAA; font-family:Arial;'>PROTOCOL 8/3</p><p class='blue-protocol'>BLUE ZONE</p></div>", unsafe_allow_html=True)

    st.divider()

    # --- THE 4-TIER ISLAND WINNER BOARD ---
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
    i_cols = st.columns(4)
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    for i, island in enumerate(islands):
        with i_cols[i]:
            st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
            for row in range(1, 5):
                label = f"PRIZE {row}" if row > 1 else "★ WINNER ★"
                st.text_input(label, key=f"win_{island}_{row}", placeholder="----")

    # --- THE BOLD ARIAL GLOBAL COMMAND BANNER ---
    st.markdown("""
        <div class='global-banner'>
            🌍 GLOBAL ADAPTATION PROTOCOL: MEMBERS FROM OTHER NATIONS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
            TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. THE SYSTEM IS UNIVERSAL. 🌍
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>95% PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
    g_cols = st.columns(6)
    for i in range(6):
        with g_cols[i]:
            st.markdown(f"<div style='border: 1px solid #FFD700; padding: 10px; text-align: center; background: rgba(255,215,0,0.05); color:#FFD700; font-weight:bold; font-family:Arial;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"v_{i}", label_visibility="collapsed", key=f"val_{i}", min_value=0, max_value=9999)

    st.divider()
    st.success("STATION STATUS: UNIVERSAL ACCESS ENABLED | BOLD FONT ACTIVE")

else:
    st.error("ACCESS DENIED.")
