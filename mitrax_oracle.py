import streamlit as st
from datetime import datetime
import os

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .gold-pillar { background-color: #D4AF37; width: 14px; height: 210px; margin: 0 auto; border: 2px solid #000000; border-radius: 5px; }
    .matrix-cell { 
        font-weight: 900; font-size: 20px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height: 48px; width: 48px;
    }
    .red-target { border: 4px solid #FF0000; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 4px solid #0000FF; border-radius: 50%; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 10px; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 5px solid #D4AF37 !important; font-size: 32px !important; 
        text-align: center !important; height: 75px !important; width: 140px !important;
        font-weight: 900 !important;
    }
    .symmetry-bridge { color: #00FF00; font-size: 26px; font-weight: 900; border-bottom: 4px solid #00FF00; padding: 0 30px; margin-top: 40px; }
    .grid-drop { margin-top: 140px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE LOCAL IMAGE HANDLER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", use_container_width=True)
else:
    st.error("⚠️ SYSTEM ERROR: mitrax_banner.jpg not detected.")

# --- 3. THE SYMMETRY DECK ---
# The winning numbers panel has been BANNED.
st.write("---")

def draw_grid(val, color, target=None):
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target" if is_m and target=="red" else "blue-target" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell {color}'><div class='{circle}'>{txt}</div></div>" if circle else f"<div class='matrix-cell {color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

st.markdown("<center><div class='symmetry-bridge'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_final_logic', ""), "grid-light", "red")
    st.markdown("</div>", unsafe_allow_html=True)

with cols[1]:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_final_logic", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid(st.session_state.get('v_blue_logic', ""), "grid-light", "blue")
    st.markdown("</div>", unsafe_allow_html=True)

with cols[4]:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
    st.markdown("</div>", unsafe_allow_html=True)

with cols[5]:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_blue_logic", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
    st.markdown("</div>", unsafe_allow_html=True)
