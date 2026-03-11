import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V11 TITAN CACHE-BUSTER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE TITAN")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE TITAN BANNER - FORCED 1600PX (4X BIGGER) */
    .titan-banner-v11 {
        width: 1600px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 40px auto;
        border: 6px solid #D4AF37;
        border-radius: 25px;
    }

    /* AMPLIFIED WINNING BOARD */
    .titan-board-v11 {
        background: rgba(212, 175, 55, 0.2);
        border: 4px solid #D4AF37;
        border-radius: 20px;
        padding: 30px;
        margin: 20px auto 50px auto;
        max-width: 1400px;
    }
    .island-titan { color: #D4AF37; font-size: 28px !important; font-weight: 900; text-align: center; text-transform: uppercase; }
    .num-titan { color: #00FF00; font-size: 40px !important; font-weight: 900; text-align: center; }

    /* TITAN-STRENGTH GRID */
    .matrix-cell-titan { 
        font-weight: 900; font-size: 24px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 8px; margin: 3px; color: #000000; height: 65px; width: 65px;
        background-color: #D3D3D3;
    }
    .red-target-titan { border: 5px solid #FF0000; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }
    .blue-target-titan { border: 5px solid #0000FF; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }
    
    .gold-pillar-titan { background-color: #D4AF37; width: 16px; height: 250px; margin: 0 auto; border-radius: 8px; }
    .island-label-titan { color: #D4AF37; font-weight: 900; font-size: 22px; text-transform: uppercase; margin-bottom: 12px; text-align: center; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 5px solid #D4AF37 !important; font-size: 32px !important; 
        text-align: center !important; height: 85px !important; width: 200px !important;
        font-weight: 900 !important;
    }
    .bridge-titan { color: #00FF00; font-size: 36px; font-weight: 900; border-bottom: 6px solid #00FF00; margin-bottom: 40px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE (FORCED EXPANSION) ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1600) 
else:
    st.write("🌌 TITAN MOTHERSHIP NOT DETECTED")

# --- 3. THE AMPLIFIED WINNING BOARD ---
st.markdown("<div class='titan-board-v11'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-titan'>{name}</p><p class='num-titan'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='bridge-titan'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_grid_titan(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target-titan" if is_m and target=="red" else "blue-target-titan" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell-titan' style='background-color:{bg_color}'>"
            if circle:
                html += f"<div class='{circle}'>{txt}</div>"
            else:
                html += f"{txt}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label-titan'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid_titan(st.session_state.get('v11_red', ""), target="red")

with cols[1]:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v11_red", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-titan'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label-titan'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid_titan(st.session_state.get('v11_blue', ""), target="blue")

with cols[4]:
    st.markdown("<p class='island-label-titan'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid_titan("", is_dark=True)

with cols[5]:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v11_blue", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-titan'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label-titan'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid_titan("", is_dark=True)
