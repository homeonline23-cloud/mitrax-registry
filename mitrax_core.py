import streamlit as st

# --- 1. THE IMPERIAL BACK DOOR (Skip straight to the Vault) ---
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
    
    .grid-box {
        border: 2px solid #FFD700; border-radius: 10px; padding: 15px;
        text-align: center; background-color: rgba(255, 215, 0, 0.05);
    }
    
    .red-protocol { color: #FF4B4B; font-weight: bold; font-size: 22px; }
    .blue-protocol { color: #1E90FF; font-weight: bold; font-size: 22px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE UNIVERSAL COMPASS ---
st.markdown("<div style='text-align: center; font-size: 80px; margin-top: 20px;'>✧🌍✧</div>", unsafe_allow_html=True)

# --- 5. THE ORACLE VAULT CONTENT (SECTOR 3) ---
if st.session_state.step == 'sector3':
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #AAAAAA;'>95% PROBABILITY VISION ACTIVE</h3>", unsafe_allow_html=True)
    
    st.divider()

    # THE CORE PROTOCOLS (7/1 and 8/3)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='grid-box'><p>PROTOCOL 7/1</p><p class='red-protocol'>RED</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='grid-box'><p>PROTOCOL 8/3</p><p class='blue-protocol'>BLUE</p></div>", unsafe_allow_html=True)

    st.divider()

    # THE 6X SYMMETRY GRID
    st.markdown("<h3 style='text-align: center;'>THE 6X SYMMETRY MATRIX</h3>", unsafe_allow_html=True)
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            st.markdown(f"<div style='border: 1px solid #444; padding: 10px; text-align: center; border-radius: 5px;'>Sector {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"Input {i+1}", label_visibility="collapsed", key=f"in_{i}")

    st.success("HEAD CHEF: THE UNIVERSAL COMPASS IS CALIBRATED TO NORTH.")
