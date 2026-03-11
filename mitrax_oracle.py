import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V16 ALIGNED TITAN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V16")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE TITAN BANNER */
    .st-banner-v16 {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 20px auto;
        border: 6px solid #D4AF37 !important;
        border-radius: 20px;
    }

    /* THE WINNING BOARD */
    .st-board-v16 {
        background: rgba(212, 175, 55, 0.15) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 15px;
        padding: 25px !important;
        margin: 20px auto 40px auto !important;
        max-width: 1400px !important;
    }
    .st-island-v16 { color: #D4AF37 !important; font-size: 28px !important; font-weight: 900 !important; text-align: center; }
    .st-num-v16 { color: #00FF00 !important; font-size: 45px !important; font-weight: 900 !important; text-align: center; }

    /* THE GOLDEN PILLARS (FIXED VERTICAL SINKING) */
    .st-pillar-v16 { 
        background-color: #D4AF37; 
        width: 18px; 
        height: 290px; /* FORCED VERTICAL HEIGHT */
        margin: 0 auto; 
        border-radius: 9px;
        border: 2px solid #000000;
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.4);
    }

    /* GRID CELLS */
    .st-cell-v16 { 
        font-weight: 900; font-size: 22px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 8px; margin: 4px; color: #000000; height: 60px; width: 60px;
        background-color: #D3D3D3;
    }
    .st-red-target { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .st-blue-target { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    
    .st-label-v16 { color: #D4AF37; font-weight: 900; font-size: 20px; text-transform: uppercase; margin-bottom: 20px; text-align: center; }

    /* INPUT FIELD CALIBRATION */
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 4px solid #D4AF37 !important; font-size: 28px !important; 
        text-align: center !important; height: 75px !important; width: 180px !important;
        font-weight: 900 !important;
    }
    .st-bridge-v16 { color: #00FF00; font-size: 32px; font-weight: 900; border-bottom: 6px solid #00FF00; margin-bottom: 60px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37;'>MITRAX EMPIRE</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='st-board-v16'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='st-island-v16'>{name}</p><p class='st-num-v16'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='st-bridge-v16'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_titan_grid(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_start = (r == 0 and c == 0 and val)
            circle = f"st-{target}-target" if is_start and target else ""
            txt = val if is_start else "0"
            html = f"<div class='st-cell-v16' style='background-color:{bg_color}'>"
            if circle: html += f"<div class='{circle}'>{txt}</div>"
            else: html += f"{txt}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- THE MAIN DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='st-label-v16'>GRID 1</p>", unsafe_allow_html=True)
    draw_titan_grid(st.session_state.get('v16_r', ""), target="red")

with cols[1]:
    st.write("<div style='height:30px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v16_r", label_visibility="collapsed")
    # THE RE-RAISED PILLAR
    st.markdown("<div class='st-pillar-v16'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='st-label-v16'>GRID 2</p>", unsafe_allow_html=True)
    draw_titan_grid(st.session_state.get('v16_b', ""), target="blue")

with cols[4]:
    st.markdown("<p class='st-label-v16'>GRID 3</p>", unsafe_allow_html=True)
    draw_titan_grid("", is_dark=True)

with cols[5]:
    st.write("<div style='height:30px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v16_b", label_visibility="collapsed")
    # THE RE-RAISED PILLAR
    st.markdown("<div class='st-pillar-v16'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='st-label-v16'>GRID 4</p>", unsafe_allow_html=True)
    draw_titan_grid("", is_dark=True)
