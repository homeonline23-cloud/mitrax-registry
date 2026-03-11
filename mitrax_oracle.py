import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V18 SYNCHRO-LIFT) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V18")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE TITAN BANNER */
    .st-banner-v18 {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 20px auto;
        border: 6px solid #D4AF37 !important;
        border-radius: 20px;
    }

    /* THE WINNING BOARD */
    .st-board-v18 {
        background: rgba(212, 175, 55, 0.15) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 15px;
        padding: 25px !important;
        margin: 20px auto 40px auto !important;
        max-width: 1400px !important;
    }
    .st-island-v18 { color: #D4AF37 !important; font-size: 28px !important; font-weight: 900 !important; text-align: center; }
    .st-num-v18 { color: #00FF00 !important; font-size: 45px !important; font-weight: 900 !important; text-align: center; }

    /* THE SYNCHRONIZED ELEVATION CONTAINER */
    .lift-unit {
        margin-top: -60px; /* FORCES THE ENTIRE UNIT (WINDOW + PILLAR) UP */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* THE GOLDEN PILLARS - CALIBRATED LENGTH */
    .st-pillar-v18 { 
        background-color: #D4AF37; 
        width: 22px; 
        height: 250px; /* REDUCED FROM OVER-STRETCHED 350PX */
        margin: 10px auto 0 auto;
        border-radius: 11px;
        border: 2px solid #000000;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.6);
        z-index: 99;
    }

    /* GRID CELLS */
    .st-cell-v18 { 
        font-weight: 900; font-size: 22px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 8px; margin: 4px; color: #000000; height: 60px; width: 60px;
        background-color: #D3D3D3;
    }
    .st-red-target { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .st-blue-target { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    
    .st-label-v18 { color: #D4AF37; font-weight: 900; font-size: 20px; text-transform: uppercase; margin-bottom: 20px; text-align: center; }

    /* INPUT FIELD - LIFTED */
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 4px solid #D4AF37 !important; font-size: 28px !important; 
        text-align: center !important; height: 75px !important; width: 180px !important;
        font-weight: 900 !important;
        z-index: 100;
    }
    .st-bridge-v18 { color: #00FF00; font-size: 32px; font-weight: 900; border-bottom: 6px solid #00FF00; margin-bottom: 80px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37;'>MITRAX EMPIRE</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='st-board-v18'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='st-island-v18'>{name}</p><p class='st-num-v18'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='st-bridge-v18'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v18_grid(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_start = (r == 0 and c == 0 and val)
            circle = f"st-{target}-target" if is_start and target else ""
            txt = val if is_start else "0"
            html = f"<div class='st-cell-v18' style='background-color:{bg_color}'>"
            if circle: html += f"<div class='{circle}'>{txt}</div>"
            else: html += f"{txt}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- THE MAIN DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='st-label-v18'>GRID 1</p>", unsafe_allow_html=True)
    draw_v18_grid(st.session_state.get('v18_r', ""), target="red")

with cols[1]:
    # WRAPPED IN THE LIFT-UNIT FOR SYNCHRONIZED MOVEMENT
    st.markdown("<div class='lift-unit'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v18_r", label_visibility="collapsed")
    st.markdown("<div class='st-pillar-v18'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='st-label-v18'>GRID 2</p>", unsafe_allow_html=True)
    draw_v18_grid(st.session_state.get('v18_b', ""), target="blue")

with cols[4]:
    st.markdown("<p class='st-label-v18'>GRID 3</p>", unsafe_allow_html=True)
    draw_v18_grid("", is_dark=True)

with cols[5]:
    st.markdown("<div class='lift-unit'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v18_b", label_visibility="collapsed")
    st.markdown("<div class='st-pillar-v18'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='st-label-v18'>GRID 4</p>", unsafe_allow_html=True)
    draw_v18_grid("", is_dark=True)
