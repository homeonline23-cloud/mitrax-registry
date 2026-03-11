import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V13 CACHE-BUSTER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V13")

# WE ARE USING TOTALLY NEW CSS CLASS NAMES TO FORCE A RE-LOAD
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE SUPER-TITAN BANNER - FORCED 1600PX */
    .st-banner-v13 {
        width: 1600px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 40px auto;
        border: 8px solid #D4AF37 !important;
        border-radius: 30px;
    }

    /* AMPLIFIED WINNING BOARD - V13 */
    .st-board-v13 {
        background: rgba(212, 175, 55, 0.2) !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 20px;
        padding: 40px !important;
        margin: 30px auto 60px auto !important;
        max-width: 1500px !important;
    }
    .st-island-v13 { color: #D4AF37 !important; font-size: 35px !important; font-weight: 900 !important; text-align: center; }
    .st-num-v13 { color: #00FF00 !important; font-size: 55px !important; font-weight: 900 !important; text-align: center; }

    /* TITAN GRID CELLS - V13 */
    .st-cell-v13 { 
        font-weight: 900; font-size: 26px; border: 2px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 10px; margin: 4px; color: #000000; height: 70px; width: 70px;
        background-color: #D3D3D3;
    }
    .st-red-v13 { border: 6px solid #FF0000; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; }
    .st-blue-v13 { border: 6px solid #0000FF; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; }
    
    .st-pillar-v13 { background-color: #D4AF37; width: 20px; height: 280px; margin: 0 auto; border-radius: 10px; }
    .st-label-v13 { color: #D4AF37; font-weight: 900; font-size: 24px; text-transform: uppercase; margin-bottom: 15px; text-align: center; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 6px solid #D4AF37 !important; font-size: 35px !important; 
        text-align: center !important; height: 90px !important; width: 220px !important;
        font-weight: 900 !important;
    }
    .st-bridge-v13 { color: #00FF00; font-size: 40px; font-weight: 900; border-bottom: 8px solid #00FF00; margin-bottom: 50px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE (FORCED RELOAD) ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1600) 
else:
    st.markdown("<h1 style='color:red;'>EMPIRE ERROR: BANNER NOT FOUND</h1>", unsafe_allow_html=True)

# --- 3. THE UPDATED WINNING BOARD ---
st.markdown("<div class='st-board-v13'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='st-island-v13'>{name}</p><p class='st-num-v13'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='st-bridge-v13'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v13_grid(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "st-red-v13" if is_m and target=="red" else "st-blue-v13" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='st-cell-v13' style='background-color:{bg_color}'>"
            if circle: html += f"<div class='{circle}'>{txt}</div>"
            else: html += f"{txt}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='st-label-v13'>GRID 1</p>", unsafe_allow_html=True)
    draw_v13_grid(st.session_state.get('v13_r', ""), target="red")

with cols[1]:
    st.write("<div style='height:30px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v13_r", label_visibility="collapsed")
    st.markdown("<div class='st-pillar-v13'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='st-label-v13'>GRID 2</p>", unsafe_allow_html=True)
    draw_v13_grid(st.session_state.get('v13_b', ""), target="blue")

with cols[4]:
    st.markdown("<p class='st-label-v13'>GRID 3</p>", unsafe_allow_html=True)
    draw_v13_grid("", is_dark=True)

with cols[5]:
    st.write("<div style='height:30px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v13_b", label_visibility="collapsed")
    st.markdown("<div class='st-pillar-v13'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='st-label-v13'>GRID 4</p>", unsafe_allow_html=True)
    draw_v13_grid("", is_dark=True)
