import streamlit as st
import os

# --- 1. ENGINE CONFIG (V48 MASTER CLEAN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V48")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #D4AF37 !important; }

    /* ABSOLUTE CENTER LOCK */
    .block-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
        padding-top: 2rem !important;
    }

    /* CLEAN TITLE */
    .v48-title {
        color: #D4AF37; font-size: 48px !important; font-weight: 900;
        text-align: center; margin-bottom: 20px; text-shadow: 0px 0px 15px #D4AF37;
    }

    /* THE WINNING BOARD */
    .v48-board {
        border: 4px solid #D4AF37; background-color: rgba(212, 175, 55, 0.1);
        border-radius: 15px; padding: 20px; margin: 20px auto; width: 1000px;
        display: flex; justify-content: space-around; align-items: center;
    }
    .v48-island { text-align: center; flex: 1; }
    .v48-label { color: #D4AF37; font-size: 24px !important; font-weight: 900; margin: 0; }
    .v48-num { color: #00FF00; font-size: 45px !important; font-weight: 900; margin: 0; }

    /* THE TRINITY PILLARS */
    .v48-unit { display: flex; flex-direction: column; align-items: center; margin-top: -40px; }
    .v48-pillar { background-color: #D4AF37; width: 25px; height: 260px; border-radius: 12px; border: 2px solid #000; box-shadow: 0px 0px 20px #D4AF37; }
    .v48-spire { background-color: #D4AF37; width: 45px; height: 400px; border-radius: 20px; border: 3px solid #000; box-shadow: 0px 0px 30px #D4AF37; margin-top: 80px; }

    /* MATRIX CELLS */
    .v48-cell {
        background-color: #D3D3D3; border: 1px solid #000; height: 55px; width: 55px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 20px; border-radius: 8px; margin: 3px; color: #000;
    }
    .red-t { border: 4px solid #FF0000; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 4px solid #0000FF; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #FFF !important; border: 4px solid #D4AF37 !important; width: 140px !important; }
    input { color: #000 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. TITLE ---
st.markdown("<div class='v48-title'>MITRAX ORACLE PIC 4 APP</div>", unsafe_allow_html=True)

# --- 2. BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1000)

# --- 3. BOARD ---
st.markdown("""
<div class='v48-board'>
    <div class='v48-island'><p class='v48-label'>ARUBA</p><p class='v48-num'>1862</p></div>
    <div class='v48-island'><p class='v48-label'>BONAIRE</p><p class='v48-num'>2544</p></div>
    <div class='v48-island'><p class='v48-label'>CURAÇAO</p><p class='v48-num'>7716</p></div>
    <div class='v48-island'><p class='v48-label'>ST. MARTIN</p><p class='v48-num'>3076</p></div>
</div>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def get_v48_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v48_grid(data, is_dark=False, target=None):
    bg = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v48-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- 5. MAIN DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)
m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v48_grid(get_v48_data(st.session_state.get('v48_r', "")), target="red")
with m_cols[1]:
    st.markdown("<div class='v48-unit'><p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("R", key="v48_r", label_visibility="collapsed")
    st.markdown("<div class='v48-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v48_grid(get_v48_data(st.session_state.get('v48_b', "")), target="blue")
with m_cols[3]:
    st.markdown("<div class='v48-spire'></div>", unsafe_allow_html=True)
with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v48_grid([[0]*4 for _ in range(4)], is_dark=True)
with m_cols[5]:
    st.markdown("<div class='v48-unit'><p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("B", key="v48_b", label_visibility="collapsed")
    st.markdown("<div class='v48-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v48_grid([[0]*4 for _ in range(4)], is_dark=True)
