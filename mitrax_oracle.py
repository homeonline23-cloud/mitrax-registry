import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V9 CACHE BUSTER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V9")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    /* THE GRAND ENLARGEMENT - FORCED 600PX FOR DOMINANCE */
    .imperial-banner-v9 {
        width: 600px !important; 
        display: block;
        margin: 0 auto 20px auto;
        border: 2px solid #D4AF37;
        border-radius: 15px;
    }

    .mini-board-v9 {
        background: rgba(212, 175, 55, 0.1);
        border: 2px solid #D4AF37;
        border-radius: 10px;
        padding: 15px;
        margin: 10px auto 30px auto;
        max-width: 900px;
    }
    .island-v9 { color: #D4AF37; font-size: 18px !important; font-weight: 900; text-align: center; }
    .num-v9 { color: #00FF00; font-size: 26px !important; font-weight: 900; text-align: center; }

    .matrix-cell-v9 { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 1px; color: #000000; height: 45px; width: 45px;
        background-color: #D3D3D3;
    }
    .red-target-v9 { border: 3px solid #FF0000; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; }
    .blue-target-v9 { border: 3px solid #0000FF; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; }
    
    .gold-pillar-v9 { background-color: #D4AF37; width: 10px; height: 180px; margin: 0 auto; border-radius: 5px; }
    .island-label-v9 { color: #D4AF37; font-weight: 900; font-size: 15px; text-transform: uppercase; margin-bottom: 5px; text-align: center; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 3px solid #D4AF37 !important; font-size: 24px !important; 
        text-align: center !important; height: 60px !important; width: 130px !important;
        font-weight: 900 !important;
    }
    .bridge-v9 { color: #00FF00; font-size: 24px; font-weight: 900; border-bottom: 4px solid #00FF00; margin-bottom: 25px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE IMAGE (VERSIONED TO BYPASS CACHE) ---
if os.path.exists("mitrax_banner.jpg"):
    # Using 'width' parameter inside st.image for maximum force
    st.image("mitrax_banner.jpg", width=600) 
else:
    st.write("🌌 IMAGE FILE MISSING IN REPOSITORY")

# --- 3. THE WINNING NUMBERS BOARD ---
st.markdown("<div class='mini-board-v9'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-v9'>{name}</p><p class='num-v9'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='bridge-v9'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_grid_v9(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target-v9" if is_m and target=="red" else "blue-target-v9" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            if circle:
                html = f"<div class='matrix-cell-v9' style='background-color:{bg_color}'><div class='{circle}'>{txt}</div></div>"
            else:
                html = f"<div class='matrix-cell-v9' style='background-color:{bg_color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label-v9'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid_v9(st.session_state.get('v9_red', ""), target="red")

with cols[1]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v9_red", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-v9'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label-v9'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid_v9(st.session_state.get('v9_blue', ""), target="blue")

with cols[4]:
    st.markdown("<p class='island-label-v9'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid_v9("", is_dark=True)

with cols[5]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v9_blue", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-v9'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label-v9'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid_v9("", is_dark=True)
