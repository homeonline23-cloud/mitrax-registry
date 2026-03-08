import streamlit as st

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

# --- 2. THE ALIGNMENT SHIELD (CSS) ---
st.markdown("""
    <style>
    /* Force everything into a tight center container */
    .block-container {
        padding-top: 2rem;
        max-width: 800px;
    }
    /* Style the input boxes to be large and centered */
    input {
        text-align: center !important;
        font-size: 28px !important;
        font-weight: bold !important;
        border: 2px solid #4A4A4A !important;
    }
    /* Remove extra spacing */
    div.stColumn {
        padding: 0px 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE REGISTRY HEADER ---
st.title("🌌 Mitrax Imperial Registry")
st.write("Manual Coordinate Entry Mode Active | Secure & De-branded")

# Initializing digits
if 'd1' not in st.session_state:
    st.session_state.update({'d1': '0', 'd2': '0', 'd3': '0', 'd4': '0'})

st.markdown("---")

# --- 4. THE UNIFIED HORIZONTAL GRID (One Line) ---
# This creates 4 equal sectors side-by-side
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h3 style='color: red; text-align: center;'>7/1 (RED)</h3>", unsafe_allow_html=True)
    n1 = st.text_input("S1", value=st.session_state.d1, key="digit1", label_visibility="collapsed")

with col2:
    st.markdown("<h3 style='text-align: center;'>SECTOR 2</h3>", unsafe_allow_html=True)
    n2 = st.text_input("S2", value=st.session_state.d2, key="digit2", label_visibility="collapsed")

with col3:
    st.markdown("<h3 style='color: blue; text-align: center;'>8/3 (BLUE)</h3>", unsafe_allow_html=True)
    n3 = st.text_input("S3", value=st.session_state.d3, key="digit3", label_visibility="collapsed")

with col4:
    st.markdown("<h3 style='text-align: center;'>SECTOR 4</h3>", unsafe_allow_html=True)
    n4 = st.text_input("S4", value=st.session_state.d4, key="digit4", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# --- 5. THE LOCK BUTTON ---
if st.button("🚀 LOCK COORDINATES", use_container_width=True):
    st.session_state.d1 = n1
    st.session_state.d2 = n2
    st.session_state.d3 = n3
    st.session_state.d4 = n4
    st.success("Universal Coordinates Locked.")
