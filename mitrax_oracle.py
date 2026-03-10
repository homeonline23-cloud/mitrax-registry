import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE", layout="wide")

# --- 2. THE IMPERIAL STYLING (RED/BLUE BLOCKS) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .imp-header { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; text-transform: uppercase; }
    .red-block { background-color: #FF0000; color: white; padding: 30px; text-align: center; font-family: 'Impact'; font-size: 45px; border-radius: 15px; border: 3px solid #FFD700; margin: 15px 0; }
    .blue-block { background-color: #0000FF; color: white; padding: 30px; text-align: center; font-family: 'Impact'; font-size: 45px; border-radius: 15px; border: 3px solid #FFD700; margin: 15px 0; }
    .grid-label { color: #FFD700; font-family: 'Impact'; font-size: 24px; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE COMMAND DECK ---
st.markdown("<div class='imp-header' style='font-size: 60px;'>MITRAX ORACLE</div>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #FFD700;'>SCROLL-STREAM ACTIVE: {datetime.now().strftime('%m/%d/%Y')}</p>", unsafe_allow_html=True)

# --- 4. IMPERIAL IMAGE BROADCAST ---
st.markdown("### 📡 STRATEGY BROADCAST")
img = st.file_uploader("Upload Chart", label_visibility="collapsed")
if img: st.image(img, use_container_width=True)

st.divider()

# --- 5. THE 5 TARGETS (VERTICAL MOBILE STACK) ---
st.markdown("<h2 style='color:#00FF00; text-align:center; font-family:Impact;'>★ 5 TARGET WINNERS ★</h2>", unsafe_allow_html=True)
for i in range(1, 6):
    st.text_input(f"TARGET {i}", key=f"t{i}", placeholder="ENTER PICK 4", label_visibility="collapsed")

st.divider()

# --- 6. THE FIXED COLOR PROTOCOLS ---
st.markdown("<div class='red-block'>7 / 1</div>", unsafe_allow_html=True)
st.markdown("<div class='blue-block'>8 / 3</div>", unsafe_allow_html=True)

st.divider()

# --- 7. THE 95% SYMMETRY 6-GRID MATRIX ---
st.markdown("<div class='imp-header' style='font-size: 40px;'>95% SYMMETRY 6-GRID</div>", unsafe_allow_html=True)
# Two columns for desktop, stacks to one on mobile automatically
g_cols = st.columns(2) 
for i in range(1, 7):
    with g_cols[i%2]:
        st.markdown(f"<div class='grid-label'>SECTOR GRID {i}</div>", unsafe_allow_html=True)
        st.text_input(f"GRID_{i}", label_visibility="collapsed", key=f"g{i}", placeholder="----")

st.divider()

# --- 8. REGIONAL WINNER BOARD (SCROLL BOTTOM) ---
st.markdown("<div class='imp-header' style='font-size: 35px;'>REGIONAL HISTORY</div>", unsafe_allow_html=True)
islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
for island in islands:
    with st.expander(f"📂 {island} DATA STREAM"):
        st.text_area(f"Input {island} history here...", key=f"area_{island}")

st.markdown("<p style='text-align: center; color: #444;'>END OF SCROLL - MITRAX EMPIRE</p>", unsafe_allow_html=True)
