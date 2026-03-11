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
else:
    st.markdown("<h2 style='color: #00FF00;'>MITRAX ORACLE</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='mini-board-gold'>
    <div style='display:flex; justify-content:space-around; color:#D4AF37; font-weight:900;'>
        <div>ARUBA<br><span style='color:#00FF00;'>1862</span></div>
        <div>BONAIRE<br><span style='color:#00FF00;'>2544</span></div>
        <div>CURAÇAO<br><span style='color:#00FF00;'>7716</span></div>
        <div>ST. MARTIN<br><span style='color:#00FF00;'>3076</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<center><div class='bridge-final'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)

# --- 3. THE HOLE SECRET ENGINE (THE RABBIT) ---
def get_grid_data(input_val, grid_type="red"):
    grid = [[0]*4 for _ in range(4)]
    if input_val and len(input_val) == 4:
        seed = int(input_val[0])
        # ROW 1 RABBIT RULE
        grid[0][0] = seed
        grid[0][1] = (seed + 1) % 10
        grid[0][2] = (seed + 2) % 10
        grid[0][3] = (seed + 3) % 10
    return grid

# --- 4. THE FULL DECK REBUILD ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

# --- GRID 1 & RED PILLAR ---
with cols[0]:
    st.markdown("<p class='island-label-final'>GRID 1</p>", unsafe_allow_html=True)
    red_val = st.session_state.get('v_red_rabbit', "")
    g1_data = get_grid_data(red_val, "red")
    for r in range(4):
        sub_cols = st.columns(4)
        for c in range(4):
            val = g1_data[r][c]
            is_target = (r == 0 and c == 0 and red_val)
            circle = "red-target-final" if is_target else ""
            html = f"<div class='matrix-cell-final' style='background-color:#D3D3D3;'>"
            if circle: html += f"<div class='{circle}'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            sub_cols[c].markdown(html, unsafe_allow_html=True)

with cols[1]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_red_rabbit", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-final'></div>", unsafe_allow_html=True)

# --- GRID 2 & BLUE PILLAR ---
with cols[2]:
    st.markdown("<p class='island-label-final'>GRID 2</p>", unsafe_allow_html=True)
    blue_val = st.session_state.get('v_blue_rabbit', "")
    g2_data = get_grid_data(blue_val, "blue")
    for r in range(4):
        sub_cols = st.columns(4)
        for c in range(4):
            val = g2_data[r][c]
            is_target = (r == 0 and c == 0 and blue_val)
            circle = "blue-target-final" if is_target else ""
            html = f"<div class='matrix-cell-final' style='background-color:#D3D3D3;'>"
            if circle: html += f"<div class='{circle}'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            sub_cols[c].markdown(html, unsafe_allow_html=True)

# --- GRID 3 ---
with cols[4]:
    st.markdown("<p class='island-label-final'>GRID 3</p>", unsafe_allow_html=True)
    for r in range(4):
        sub_cols = st.columns(4)
        for c in range(4):
            sub_cols[c].markdown("<div class='matrix-cell-final' style='background-color:#707070;'>0</div>", unsafe_allow_html=True)

with cols[5]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_blue_rabbit", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-final'></div>", unsafe_allow_html=True)

# --- GRID 4 ---
with cols[6]:
    st.markdown("<p class='island-label-final'>GRID 4</p>", unsafe_allow_html=True)
    for r in range(4):
        sub_cols = st.columns(4)
        for c in range(4):
            sub_cols[c].markdown("<div class='matrix-cell-final' style='background-color:#707070;'>0</div>", unsafe_allow_html=True)
