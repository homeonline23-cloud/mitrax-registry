import streamlit as st

# --- 1. CORE ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Imperial Registry", layout="wide")

# --- 2. THE MANUAL BRIDGE ---
# Since the 'Rabbit' is hiding, we will use manual input for now
# to ensure the Grid is ALWAYS visible.
st.title("🌌 Mitrax Registry: Sector Dashboard")

st.sidebar.header("📡 Universal Compass Control")
st.sidebar.info("Auto-Fill is currently on standby. Enter winning numbers below.")

# Initializing digits
if 'd1' not in st.session_state:
    st.session_state.update({'d1': '1', 'd2': '2', 'd3': '3', 'd4': '4'})

# --- 3. THE VISUAL GRID (North, South, East, West) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h2 style='color: red; text-align: center;'>7/1 (NORTH/RED)</h2>", unsafe_allow_html=True)
    n1 = st.text_input("Win 1", value=st.session_state.d1, key="digit1")

with col2:
    st.markdown("<h2 style='text-align: center;'>SECTOR 2 (EAST)</h2>", unsafe_allow_html=True)
    n2 = st.text_input("Win 2", value=st.session_state.d2, key="digit2")

with col3:
    st.markdown("<h2 style='color: blue; text-align: center;'>8/3 (SOUTH/BLUE)</h2>", unsafe_allow_html=True)
    n3 = st.text_input("Win 3", value=st.session_state.d3, key="digit3")

with col4:
    st.markdown("<h2 style='text-align: center;'>SECTOR 4 (WEST)</h2>", unsafe_allow_html=True)
    n4 = st.text_input("Win 4", value=st.session_state.d4, key="digit4")

# --- 4. DATA UPDATE ---
if st.button("🚀 LOCK WINNING NUMBERS"):
    st.session_state.d1 = n1
    st.session_state.d2 = n2
    st.session_state.d3 = n3
    st.session_state.d4 = n4
    st.success("Coordinates Locked into Mitrax Registry!")

st.markdown("---")
st.write("SYSTEM STATUS: **ONLINE** | GRID VISIBILITY: **FULL**")
