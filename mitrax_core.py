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
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 20px; letter-spacing: 4px; margin-bottom: 25px; }
    
    /* THE WHITE BOLD ARIAL BANNER */
    .global-banner { 
        background: rgba(255, 215, 0, 0.1); border: 2px solid #FFD700; border-radius: 10px; 
        padding: 20px; text-align: center; color: #FFFFFF; font-family: 'Arial', sans-serif; 
        font-weight: bold; font-size: 18px; margin-top: 20px;
    }
    
    /* PREDICTION BOARD STYLING */
    .predict-box { 
        background: linear-gradient(180deg, rgba(255,215,0,0.2) 0%, rgba(14,17,23,1) 100%);
        border: 2px solid #FFD700; border-radius: 15px; padding: 20px; text-align: center;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    }
    .predict-num { color: #00FF00; font-family: 'Impact', sans-serif; font-size: 35px; text-shadow: 0 0 10px #00FF00; }
    
    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; border-bottom: 2px solid #FFD700; font-family: 'Arial', sans-serif; }
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 26px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 26px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE ORACLE VAULT CONTENT (SECTOR 3) ---
if st.session_state.step == 'sector3':
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    st.markdown("<div style='text-align: center; font-size: 60px;'>✧🌍✧</div>", unsafe_allow_html=True)
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='date-stamp'>SESSION DATE: {imperial_date}</div>", unsafe_allow_html=True)

    # THE CORE PROTOCOLS
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div style='border:2px solid #FFD700; border-radius:10px; padding:15px; text-align:center;'>PROTOCOL 7/1<br><span class='red-protocol'>RED</span></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div style='border:2px solid #FFD700; border-radius:10px; padding:15px; text-align:center;'>PROTOCOL 8/3<br><span class='blue-protocol'>BLUE</span></div>", unsafe_allow_html=True)

    st.divider()

    # --- THE 5 PREDICTED WINNERS (THE HARVEST) ---
    st.markdown("<h2 style='text-align: center; color: #00FF00; font-family:Impact;'>★ 5 PREDICTED WINNERS ★</h2>", unsafe_allow_html=True)
    p_cols = st.columns(5)
    for i in range(5):
        with p_cols[i]:
            st.markdown(f"<div class='predict-box'><span style='color:#AAA; font-size:12px;'>TARGET {i+1}</span>", unsafe_allow_html=True)
            st.text_input("Prediction", key=f"pred_{i}", label_visibility="collapsed", placeholder="0000")
            st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # --- THE 4-TIER ISLAND WINNER BOARD ---
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
    i_cols = st.columns(4)
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    for i, island in enumerate(islands):
        with i_cols[i]:
            st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
            for row in range(1, 5):
                st.text_input(f"P{row}", key=f"win_{island}_{row}", placeholder="----", label_visibility="collapsed")

    # --- THE WHITE BOLD ARIAL GLOBAL COMMAND BANNER ---
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

    st.success("STATION STATUS: PREDICTION ENGINE ENGAGED | COMPASS NORTH")

else:
    st.error("ACCESS DENIED.")
    
