import streamlit as st
import os

# --- 1. ENGINE CONFIG (V55 THE CROWN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V55")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* FORCE EVERYTHING TO THE CENTER-AXIS */
    .block-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
        padding-top: 0rem !important; /* PIN TO TOP */
    }

    /* 1. THE IMAGE (THE CROWN - AT THE TOP) */
    .stImage {
        margin-top: 0px !important;
        margin-bottom: 20px !important;
        display: flex !important;
        justify-content: center !important;
        width: 1000px !important;
    }
    img {
        border: 4px solid #D4AF37;
        border-radius: 20px;
        width: 1000px !important;
    }

    /* 2. THE WINNING BOARD (CENTERED UNDER IMAGE) */
    .v55-board {
        border: 2px solid #00FF00;
        background-color: rgba(0, 255, 0, 0.05);
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto 60px auto !important;
        width: 1000px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        box-shadow: 0px 0px 20px rgba(0, 255, 0, 0.2);
    }
    .v55-island { text-align: center; flex: 1; }
    .v55-label { color: #D4AF37; font-size: 26px !important; font-weight: 900; text-transform: uppercase; }
    .v55-num { color: #00FF00; font-size: 52px !important; font-weight: 900; }

    /* 3. THE SENSORS */
    .v55-unit { display: flex; flex-direction: column; align-items: center; margin-top: -60px; }
    .v55-pillar { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 25px; height: 260px; border-radius: 12px; border: 2px solid #000; }
    .v55-spire { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 45px; height: 400px; border-radius: 20px; border: 3px solid #000; }

    .v55-cell {
        background-color: #1a1a1a; border: 1px solid #00FF00; height: 60px; width: 60px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 24px; border-radius: 10px; margin: 4px; color: #00FF00;
    }
    .red-t { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; width: 160px !important; }
    input { color: #00FF00 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- TOP ORBIT: THE IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- MIDDLE ORBIT: THE BOARD ---
st.markdown("""
<div class='v55-board'>
    <div class='v55-island'><p class='v55-label'>ARUBA</p><p class='v55-num'>1862</p></div>
    <div class='v55-island'><p class='v55-label'>BONAIRE</p><p class='v55-num'>2544</p></div>
    <div class='v55-island'><p class='v55-label'>CURAÇAO</p><p class='v55-num'>7716</p></div>
    <div class='v55-island'><p class='v55-label'>ST. MARTIN</p><p class='v55-num'>3076</p></div>
</div>
""", unsafe_allow_html=True)

# --- BASE ORBIT: MATRIX SENSORS ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px; margin-bottom:100px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v55_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v55_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v55-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_
