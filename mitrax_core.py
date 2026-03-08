import streamlit as st

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

# --- 2. THE ALIGNMENT SHIELD (CSS) ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; max-width: 1100px; margin: auto; }
    input { text-align: center !important; font-size: 26px !important; font-weight: bold !important; }
    [data-testid="column"] { width: 25% !important; flex: 1 1 25% !important; min-width: 120px !important; }
    div.stTextInput > label { display: none; }
    .vtrac-box { 
        background-color: #1E1E1E; 
        border-radius: 5px; 
        padding: 10px; 
        text-align: center; 
        border: 1px solid #444;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VTRAC LOGIC ---
def get_vtrac(n):
    try:
        val = int(n[-1]) # Take the last digit if multiple are entered
        mapping = {0:5, 1:6, 2:7, 3:8, 4:9, 5:0, 6:1, 7:2, 8:3, 9:4}
        return str(mapping.get(val, "?"))
    except: return "?"

# --- 4. THE INTERFACE ---
st.title("🌌 Mitrax Imperial Registry")

if 'd1' not in st.session_state:
    st.session_state.update({'d1': '0', 'd2': '0', 'd3': '0', 'd4': '0'})

# --- 5. THE UNIFIED HORIZONTAL GRID ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h3 style='color: #FF0000; text-align: center; margin-bottom:0;'>7/1 (RED)</h3>", unsafe_allow_html=True)
    n1 = st.text_input("S1", value=st.session_state.d1, key="digit1")
    st.markdown(f"<div class='vtrac-box'>VTrac: <b>{get_vtrac(n1)}</b></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='text-align: center; color: white; margin-bottom:0;'>SECTOR 2</h3>", unsafe_allow_html=True)
    n2 = st.text_input("S2", value=st.session_state.d2, key="digit2")
    st.markdown(f"<div class='vtrac-box'>VTrac: <b>{get_vtrac(n2)}</b></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<h3 style='color: #0000FF; text-align: center; margin-bottom:0;'>8/3 (BLUE)</h3>", unsafe_allow_html=True)
    n3 = st.text_input("S3", value=st.session_state.d3, key="digit3")
    st.markdown(f"<div class='vtrac-box'>VTrac: <b>{get_vtrac(n3)}</b></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<h3 style='text-align: center; color: white; margin-bottom:0;'>SECTOR 4</h3>", unsafe_allow_html=True)
    n4 = st.text_input("S4", value=st.session_state.d4, key="digit4")
    st.markdown(f"<div class='vtrac-box'>VTrac: <b>{get_vtrac(n4)}</b></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 LOCK COORDINATES", use_container_width=True):
    st.session_state.update({'d1': n1, 'd2': n2, 'd3': n3, 'd4': n4})
    st.success("Universal Coordinates & VTracs Locked.")
