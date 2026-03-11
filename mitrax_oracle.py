import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V42 CENTERED CORE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V42")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* GLOBAL CENTER LOCK */
    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 1rem !important;
    }

    /* THE UNIFIED BOARD */
    .v42-board {
        border: 4px solid #D4AF37;
        background-color: rgba(212, 175, 55, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto;
        width: 1200px;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .v42-label-text { color: #D4AF37; font-size: 28px !important; font-weight: 900; text-transform: uppercase; }
    .v42-num-text { color: #00FF00; font-size: 52px !important; font-weight: 900; }

    /* CENTERED IMAGE STYLING */
    .v42-banner-mid {
        margin: 40px auto !important;
        border: 4px solid #D4AF37;
        border-radius: 20px;
    }

    /* THE PILLAR/INPUT UNIT */
    .v42-unit {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: -60px;
    }
    .v42-gold-pool {
        background-color: #D4AF37;
        width: 25px;
        height: 250px;
        border-radius: 12px;
        border: 2px solid #000;
        box-shadow: 0px 0px 20px #D4AF37;
    }
    .v42-grand-spire {
        background-color: #D4AF37;
        width: 45px;
        height: 400px;
        border-radius: 20px;
        border: 3px solid #000;
        box-shadow: 0px 0px 30px #D4AF37;
    }

    /* THE CELLS */
    .v42-cell {
        background-color: #D3D3D3;
        border: 1px solid #000;
        height: 60px;
        width: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 22px;
        border-radius: 8px;
        margin: 4px;
        color: #000;
    }
    .red-target { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #FFF !important; border: 4px solid #D4AF37 !important; width: 160px !important; }
    input { color: #000 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    
    .v42-grid-header { color: #D4AF37; font-weight: 900; font-size: 20px; text-align: center; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 1. WINNING BOARD (NOW AT TOP) ---
st.markdown("""
<div class='v42-board'>
    <div style='text-align:center;'><p class='v42-label-text'>ARUBA</p><p class='v42-num-text'>1862</p></div>
    <div style='text-align:center;'><p class='v42-label-text'>BONAIRE</p><p class='v42-num-text'>2544</p></div>
    <div style='text-align:center;'><p class='v42-label-text'>CURAÇAO</p><p class='v42-num-text'>7716</p></div>
    <div style='text-align:center;'><p class='v42-label-text'>ST. MARTIN</p><p class='v42-num-text'>3076</p></div>
</div>
""", unsafe_allow_html=True)

# --- 2. THE IMAGE (NOW IN THE MIDDLE) ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1200)
else:
    st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)

# --- 3. THE SENSOR DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; padding-bottom:10px; width:1200px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v42_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v42_grid(data, is_dark=False, target=None):
    bg = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v42-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-target'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-target'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p class='v42-grid-header'>GRID 1</p>", unsafe_allow_html=True)
    draw_v42_grid(get_v42_data(st.session_state.get('v42_r', "")), target="red")

with m_cols[1]:
    st.markdown("<div class='v42-unit'>", unsafe_allow_html=True)
    st.markdown("<p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("R", key="v42_r", label_visibility="collapsed")
    st.markdown("<div class='v42-gold-pool'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m_cols[2]:
    st.markdown("<p class='v42-grid-header'>GRID 2</p>", unsafe_allow_html=True)
    draw_v42_grid(get_v42_data(st.session_state.get('v42_b', "")), target="blue")

with m_cols[3]:
    st.markdown("<div style='height:100px;'></div><div class='v42-grand-spire'></div>", unsafe_allow_html=True)

with m_cols[4]:
    st.markdown("<p class='v42-grid-header'>GRID 3</p>", unsafe_allow_html=True)
    draw_v42_grid([[0]*4 for _ in range(4)], is_dark=True)

with m_cols[5]:
    st.markdown("<div class='v42-unit'>", unsafe_allow_html=True)
    st.markdown("<p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("B", key="v42_b", label_visibility="collapsed")
    st.markdown("<div class='v42-gold-pool'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m_cols[6]:
    st.markdown("<p class='v42-grid-header'>GRID 4</p>", unsafe_allow_html=True)
    draw_v42_grid([[0]*4 for _ in range(4)], is_dark=True)
