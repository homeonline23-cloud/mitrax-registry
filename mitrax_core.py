import streamlit as st

# --- 1. CORE ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Imperial Registry", layout="wide")

# --- 2. SANITIZED INTERFACE ---
st.title("🌌 Mitrax Registry: Sector Dashboard")

st.sidebar.header("📡 Universal Compass Control")
st.sidebar.info("Operational Mode: Manual Coordinate Entry.")

# Initializing digits
if 'd1' not in st.session_state:
    st.session_state.update({'d1': '0', 'd2': '0', 'd3': '0', 'd4': '0'})

# --- 3. THE VISUAL GRID (North, East, South, West) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    # 7/1 Red Requirement Locked
    st.markdown("<h2 style='color: red; text-align: center;'>7/1 (NORTH)</h2>", unsafe_allow_html=True)
    n1 = st.text_input("Data Point 1", value=st.session_state.d1, key="digit1")

with col2:
    st.markdown("<h2 style='text-align: center;'>SECTOR 2 (EAST)</h2>", unsafe_allow_html=True)
    n2 = st.text_input("Data Point 2", value=st.session_state.d2, key="digit2")

with col3:
    # 8/3 Blue Requirement Locked
    st.markdown("<h2 style='color: blue; text-align: center;'>8/3 (SOUTH)</h2>", unsafe_allow_html=True)
    n3 = st.text_input("Data Point 3", value=st.session_state.d3, key="digit3")

with col4:
    st.markdown("<h2 style='text-align: center;'>SECTOR 4 (WEST)</h2>", unsafe_allow_html=True)
    n4 = st.text_input("Data Point 4", value=st.session_state.d4, key="digit4")

# --- 4. DATA LOCK ---
if st.button("🚀 LOCK COORDINATES"):
    st.session_state.d1 = n1
    st.session_state.d2 = n2
    st.session_state.d3 = n3
    st.session_state.d4 = n4
    st.success("Universal Coordinates Locked into Registry.")

st.markdown("---")
st.write("SECURITY STATUS: **PRIVATE / DE-BRANDED** | SYSTEM: **ONLINE**")
