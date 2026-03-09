import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL BACK DOOR (Sector 3 Entry) ---
if 'step' not in st.session_state:
    st.session_state.step = 'sector3'

# --- 2. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 3. UNIVERSAL STYLING (THE GOLDEN CASING) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    .mitrax-title {
        text-align: center; color: #FFD700; font-family: 'Impact', sans-serif;
        font-size: 45px; letter-spacing: 10px; margin-bottom: 0px;
    }
    
    .date-stamp {
        text-align: center; color: #FFD700; font-family: 'Impact', sans-serif;
        font-size: 22px; letter-spacing: 3px; margin-top: 5px; opacity: 0.9;
    }

    .grid-box {
        border: 2px solid #FFD700; border-radius: 10px; padding: 20px;
        text-align: center; background-color: rgba(255, 215, 0, 0.05);
    }
    
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 24px; text-shadow: 0 0 10px #FF4B4B; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 24px; text-shadow: 0 0 10px #1E90FF; }
    
    /* Center the globe */
    .compass-container { text-align: center; font-size: 70px; margin-top: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE ORACLE VAULT CONTENT (SECTOR 3) ---
if st.session_state.step == 'sector3':
    # AUTOMATIC CELESTIAL DATE
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    # Header Display
    st.markdown("<div class='compass-container'>✧🌍✧</div>", unsafe_allow_html=True)
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='date-stamp'>SESSION DATE: {imperial_date}</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #AAAAAA; font-weight: 300;'>95% PROBABILITY VISION ACTIVE</h3>", unsafe_allow_html=True)
    
    st.divider()

    # THE CORE PROTOCOLS (UNBREAKABLE COLOR ASSIGNMENTS)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='grid-box'><p style='margin-bottom:5px;'>PROTOCOL 7/1</p><p class='red-protocol'>RED</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='grid-box'><p style='margin-bottom:5px;'>PROTOCOL 8/3</p><p class='blue-protocol'>BLUE</p></div>", unsafe_allow_html=True)

    st.divider()

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center; color: #FFD700;'>6X SYMMETRY MATRIX</h3>", unsafe_allow_html=True)
    
    # Building the 6 columns for members to view/input
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            st.markdown(f"<div style='border: 1px solid #444; padding: 10px; text-align: center; border-radius: 5px; background: #1a1a1a;'>Sector {i+1}</div>", unsafe_allow_html=True)
            # Standard input for number data
            st.number_input(f"Value {i+1}", label_visibility="collapsed", key=f"v_{i}", min_value=0, max_value=100)

    st.divider()
    st.success("STATION STATUS: ONLINE | COMPASS ALIGNED NORTH | NO ERRORS DETECTED")

# --- FALLBACK PROTECTION ---
else:
    st.warning("PLEASE RE-ENTER THROUGH THE IMPERIAL GATEWAY.")
