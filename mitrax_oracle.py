import streamlit as st
from datetime import datetime
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (FORCE NEW VERSION) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V7")

# FORCE BROWSER TO IGNORE OLD STYLES
st.markdown("""
    <style>
    /* RESET EVERYTHING */
    .stApp { background-color: #000000 !important; }
    
    /* NANO-BANNER - FORCED SMALL */
    .imperial-nano-banner {
        width: 100px !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
        padding-top: 5px;
    }

    /* MINI BOARD STABILIZER */
    .mini-board-v7 {
        background: rgba(212, 175, 55, 0.05);
        border: 1px solid #D4AF37;
        border-radius: 5px;
        padding: 4px;
        margin: 5px auto;
        max-width: 600px;
    }
    .island-v7 { color: #D4AF37; font-size: 10px; font-weight: 900; margin: 0; text-align: center; }
    .num-v7 { color: #00FF00; font-size: 14px; font-weight: 900; margin: 0; text-align: center; }

    /* HIGH-DENSITY GRID v7 */
    .matrix-cell-v7 { 
        font-weight: 900; font-size: 14px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 2px; margin: 1px; color: #000000; height: 30px; width: 30px;
        background-color: #D3D3D3;
    }
    .red-target-v7 { border: 2px solid #FF0000; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; }
    .blue-target-v7 { border: 2px solid #0000FF; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; }
    
    .gold-pillar-v7 { background-color: #D4AF37; width: 6px; height: 130px; margin: 0 auto; border-radius: 3px; }
    .island-label-v7 { color: #D4AF37; font-weight: 900; font-size: 11px; text-transform: uppercase; margin-bottom: 2px; text-align: center; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 2px solid #D4AF37 !important; font-size: 16px !important; 
        text-align: center !important; height: 35px !important; width: 70px !important;
        font-weight: 900 !important;
    }
    .bridge-v7 { color: #00FF00; font-size: 15px; font-weight: 900; border-bottom: 2px solid #00FF00; margin-bottom: 10px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE NANO-BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=100)
else:
    st.write("🌌")

# --- 3. THE SLEEK MINI BOARD ---
st.markdown("<div class='mini-board-v7'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-v7'>{name}</p><p class='num-v7'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='bridge-v7'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_grid_v7(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target-v7" if is_m and target=="red" else "blue-target-v7" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            if circle:
                html = f"<div class='matrix-cell-v7' style='background-color:{bg_color}'><div class='{circle}'>{txt}</div></div>"
            else:
                html = f"<div class='matrix-cell-v7' style='background-color:{bg_color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label-v7'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid_v7(st.session_state.get('v7_red', ""), target="red")

with cols[1]:
    st.write("<div style='height:5px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v7_red", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-v7'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label-v7'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid_v7(st.session_state.get('v7_blue', ""), target="blue")

with cols[4]:
    st.markdown("<p class='island-label-v7'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid_v7("", is_dark=True)

with cols[5]:
    st.write("<div style='height:5px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v7_blue", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-v7'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label-v7'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid_v7("", is_dark=True)
