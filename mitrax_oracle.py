import streamlit as st
from datetime import datetime
import os

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* COMPACT BANNER - RESIZED FOR PC & MOBILE */
    .banner-container {
        max-width: 600px; /* SHRINKS THE IMAGE TO REASONABLE SIZE */
        margin: 0 auto 10px auto;
    }

    /* MINI WINNING BOARD - SAVES SPACE */
    .mini-board {
        background: rgba(212, 175, 55, 0.1);
        border: 2px solid #D4AF37;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .island-mini { color: #D4AF37; font-size: 14px; font-weight: 900; margin: 0; }
    .num-mini { color: #00FF00; font-size: 18px; font-weight: 900; margin: 0; }

    .gold-pillar { background-color: #D4AF37; width: 10px; height: 180px; margin: 0 auto; border-radius: 5px; }
    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 1px; color: #000000; height: 40px; width: 40px;
    }
    .red-target { border: 3px solid #FF0000; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 3px solid #0000FF; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 14px; text-transform: uppercase; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 3px solid #D4AF37 !important; font-size: 24px !important; 
        text-align: center !important; height: 60px !important; width: 120px !important;
        font-weight: 900 !important;
    }
    .symmetry-bridge { color: #00FF00; font-size: 22px; font-weight: 900; border-bottom: 3px solid #00FF00; padding: 0 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE COMPACT BANNER ---
st.markdown("<div class='banner-container'>", unsafe_allow_html=True)
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", use_container_width=True)
else:
    st.error("⚠️ SYSTEM ERROR: mitrax_banner.jpg not detected.")
st.markdown("</div>", unsafe_allow_html=True)

# --- 3. THE COMPACT WINNING BOARD (THE RETURN) ---
st.markdown("<div class='mini-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-mini'>{name}</p><p class='num-mini'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<center><div class='symmetry-bridge'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)

def draw_grid(val, color, target=None):
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target" if is_m and target=="red" else "blue-target" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell {color}'><div class='{circle}'>{txt}</div></div>" if circle else f"<div class='matrix-cell {color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_slim_1', ""), "grid-light", "red")

with cols[1]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_slim_1", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_slim_2', ""), "grid-light", "blue")

with cols[4]:
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")

with cols[5]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_slim_2", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
