import streamlit as st

# --- 1. CORE ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Imperial Registry", layout="wide")

# --- 2. LAYOUT CALIBRATION (CSS) ---
st.markdown("""
    <style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    .stTextInput > div > div > input {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    h2 {
        font-size: 1.5rem !important;
        margin-bottom: 0px !important;
        padding-bottom: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SANITIZED INTERFACE ---
st.title("🌌 Mitrax Registry: Sector Dashboard")

# Initializing digits in session memory
if 'd1' not in st.session_state:
    st.session_state.update({'d1': '0', 'd2': '0', 'd3': '0', 'd4': '0'})

# --- 4. THE UNIFIED HORIZONTAL GRID ---
# Using 4 equal columns for a single-line layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h2 style='color: red; text-align: center;'>7/1 (NORTH)</h2>", unsafe_allow_html=True)
    n1 = st.text_input("Data 1", value=st.session_state.d1, key="digit1", label_visibility="collapsed")

with col2:
    st.markdown("<h2 style='text-align: center; color: white;'>SECTOR 2</h2>", unsafe_allow_html=True)
    n2 = st.text_input("Data 2", value=st.session_state.d2, key="digit2", label_visibility="collapsed")

with col3:
    st.markdown("<h2 style='color: blue; text-align: center;'>8/3 (SOUTH)</h2>", unsafe_allow_html=True)
    n3 = st.text_input("Data 3", value=st.session_state.d3, key="digit3", label_visibility="collapsed")

with col4:
    st.markdown("<h2 style='text-align: center; color: white;'>SECTOR 4</h2>", unsafe_allow_html=True)
    n4 = st.text_input("Data 4", value=st.session_state.d4, key="digit4", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. ACTION CENTER ---
c_left, c_mid, c_right = st.columns([1, 2, 1])
with c_mid:
    if st.button("🚀 LOCK COORDINATES", use_container_width=True):
        st.session_state.d1 = n1
        st.session_state.d2 = n2
        st.session_state.d3 = n3
        st.session_state.d4 = n4
        st.success("Coordinates Locked into Registry.")

st.markdown("---")
st.write("SECURITY STATUS: **PRIVATE** | LAYOUT: **UNIFIED GRID**")
