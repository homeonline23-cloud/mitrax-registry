import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL BACK DOOR ---
if 'step' not in st.session_state:
    st.session_state.step = 'sector3'

# --- 2. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Oracle Vision", layout="wide")

# --- 3. UNIVERSAL STYLING (GOLDEN FILAMENT) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .mitrax-title { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 45px; letter-spacing: 10px; margin-bottom: 0px; }
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 20px; letter-spacing: 3px; margin-bottom: 20px; }
    .grid-box { border: 2px solid #FFD700; border-radius: 10px; padding: 15px; text-align: center; background-color: rgba(255, 215, 0, 0.05); }
    .island-box { border: 1px solid #444; border-radius: 8px; padding: 10px; text-align: center; background-color: #1a1a1a; color: #FFD700; font-weight: bold; }
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 22px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 22px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE ORACLE VAULT CONTENT (SECTOR 3) ---
if st.session_state.step == 'sector3':
    # AUTOMATIC DATE
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    st.markdown("<div style='text-align: center; font-size: 60px;'>✧🌍✧</div>", unsafe_allow_html=True)
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='date-stamp'>SESSION DATE: {imperial_date}</div>", unsafe_allow_html=True)

    # THE CORE PROTOCOLS
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='grid-box'><p>PROTOCOL 7/1</p><p class='red-protocol'>RED</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='grid-box'><p>PROTOCOL 8/3</p><p class='blue-protocol'>BLUE</p></div>", unsafe_allow_html=True)

    st.divider()

    # --- THE WINNING NUMBERS BOARD (CARIBBEAN EXPANSION) ---
    st.markdown("<h3 style='text-align: center; color: #FFD700;'>ISLAND WINNER BOARD</h3>", unsafe_allow_html=True)
    i_col1, i_col2, i_col3, i_col4 = st.columns(4)
    
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    cols = [i_col1, i_col2, i_col3, i_col4]
    
    for i, island in enumerate(islands):
        with cols[i]:
            st.markdown(f"<div class='island-box'>{island}</div>", unsafe_allow_html=True)
            st.text_input("Winning Number", key=f"win_{island}", label_visibility="collapsed", placeholder="0000")

    st.divider()

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center;'>THE 6X SYMMETRY MATRIX</h3>", unsafe_allow_html=True)
    g_cols = st.columns(6)
    for i in range(6):
        with g_cols[i]:
            st.markdown(f"<div style='border: 1px solid #444; padding: 10px; text-align: center; border-radius: 5px;'>Sector {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"In {i}", label_visibility="collapsed", key=f"val_{i}")

    st.success("STATION STATUS: CARIBBEAN NODES CONNECTED | COMPASS ALIGNED")
