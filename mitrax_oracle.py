import streamlit as st
import os
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    .imperial-banner { width: 220px !important; display: block; margin: 0 auto 10px auto; padding-top: 10px; }
    .mini-board-gold { background: rgba(212, 175, 55, 0.08); border: 2px solid #D4AF37; border-radius: 10px; padding: 8px; margin: 10px auto 20px auto; max-width: 800px; }
    .matrix-cell-final { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 1px; color: #000000; height: 42px; width: 42px; }
    .red-target-final { border: 3px solid #FF0000; border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; }
    .blue-target-final { border: 3px solid #0000FF; border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; }
    .gold-pillar-final { background-color: #D4AF37; width: 10px; height: 160px; margin: 0 auto; border-radius: 5px; }
    .island-label-final { color: #D4AF37; font-weight: 900; font-size: 14px; text-transform: uppercase; margin-bottom: 5px; }
    .stTextInput > div > div > input { background-color: #FFFFFF !important; color: #000000 !important; border: 3px solid #D4AF37 !important; font-size: 24px !important; text-align: center !important; height: 60px !important; width: 120px !important; font-weight: 900 !important; }
    .bridge-final { color: #00FF00; font-size: 22px; font-weight: 900; border-bottom: 3px solid #00FF00; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANNER & BOARD ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=220)
st.markdown("<div class='mini-board-gold'><div style='display:flex; justify-content:space-around;'><p>ARUBA: 1862</p><p>BONAIRE: 2544</p><p>CURAÇAO: 7716</p><p>ST. MARTIN: 3076</p></div></div>", unsafe_allow_html=True)
st.markdown("<center><div class='bridge-final'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)

# --- 3. THE HOLE SECRET ENGINE ---
def calculate_grid_1(input_val):
    grid = [[0]*4 for _ in range(4)]
    if input_val and len(input_val) == 4:
        seed = int(input_val[0])
        # RULE: THE RABBIT LEAP (Row 1)
        grid[0][0] = seed
        grid[0][1] = (seed + 1) % 10
        grid[0][2] = (seed + 2) % 10
        grid[0][3] = (seed + 3) % 10
    return grid

# --- 4. THE DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])
red_in = st.session_state.get('v_red', "")

with cols[0]:
    st.markdown("<p class='island-label-final'>GRID 1</p>", unsafe_allow_html=True)
    g1_data = calculate_grid_1(red_in)
    for r in range(4):
        sub_cols = st.columns(4)
        for c in range(4):
            val = g1_data[r][c]
            is_target = (r == 0 and c == 0 and red_in)
            circle = "red-target-final" if is_target else ""
            html = f"<div class='matrix-cell-final' style='background-color:#D3D3D3;'>{'<div class='+circle+'>' if circle else ''}{val}{'</div>' if circle else ''}</div>"
            sub_cols[c].markdown(html, unsafe_allow_html=True)

with cols[1]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    red_in = st.text_input("", placeholder="****", max_chars=4, key="v_red", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-final'></div>", unsafe_allow_html=True)

# (Remaining grids 2, 3, 4 placeholders remain standard for now)
