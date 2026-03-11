import streamlit as st
from datetime import datetime
import os

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* ULTRA-COMPACT BANNER - SHRUNK FOR TOTAL VISIBILITY */
    .banner-container {
        max-width: 320px;
        margin: 0 auto 5px auto;
        padding-top: 10px;
    }

    /* SLEEK MINI BOARD */
    .mini-board {
        background: rgba(212, 175, 55, 0.05);
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 5px;
        margin-bottom: 15px;
    }
    .island-mini { color: #D4AF37; font-size: 11px; font-weight: 900; margin: 0; line-height: 1; }
    .num-mini { color: #00FF00; font-size: 16px; font-weight: 900; margin: 0; line-height: 1.2; }

    /* REDUCED PILLAR & GRID SIZES */
    .gold-pillar { background-color: #D4AF37; width: 8px; height: 160px; margin: 0 auto; border-radius: 4px; }
    .matrix-cell { 
        font-weight: 900; font-size: 16px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 3px; margin: 1px; color: #000000; height: 35px; width: 35px;
    }
    .red-target { border: 2px solid #FF0000; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 2px solid #0000FF; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 12px; text-transform: uppercase; margin-bottom: 2px; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 2px solid #D4AF37 !important; font-size: 20px !important; 
        text-align: center !important; height: 50px !important; width: 100px !important;
        font-weight: 900 !important;
    }
    .symmetry-bridge { color: #00FF00; font-size: 18px; font-weight: 900; border-bottom: 2px solid #00FF00; padding: 0 15px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE ULTRA-COMPACT BANNER ---
st.markdown("<div class='banner-container'>", unsafe_allow_html=True)
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", use_container_width=True)
else:
    st.error("⚠️ SYSTEM ERROR")
st.markdown("</div>", unsafe_allow_html=True)

# --- 3. THE SLEEK MINI BOARD ---
st.markdown("<div class='mini-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-mini'>{name}</p><p class='num-mini'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<center><div class='symmetry-bridge'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)
st.write("") 

def draw_grid(val, color, target=None):
    # Fixed drawing logic to prevent syntax leaks
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle_class = "red-target" if is_m and target=="red" else "blue-target" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            if circle_class:
                html = f"<div class='matrix-cell {color}'><div class='{circle_class}'>{txt}</div></div>"
            else:
                html = f"<div class='matrix-cell {color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_sealed_1', ""), "grid-light", "red")

with cols[1]:
    st.write("<div style='height:10px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_sealed_1", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_sealed_2', ""), "grid-light", "blue")

with cols[4]:
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")

with cols[5]:
    st.write("<div style='height:10px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_sealed_2", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
