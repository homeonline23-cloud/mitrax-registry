import streamlit as st
import os

# --- 1. ENGINE CONFIG (V50 FINAL CENTER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V50")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* GLOBAL CENTER LOCK */
    .block-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
        padding-top: 1rem !important;
    }

    /* THE IMPERIAL TITLE (MATCHING THE IMAGE) */
    .v50-header {
        color: #00FF00;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 50px !important;
        text-align: center;
        text-shadow: 0px 0px 15px #00FF00, 2px 2px #D4AF37;
        margin-top: 40px !important;
        margin-bottom: 5px !important;
    }
    .v50-sub-header {
        color: #00FF00;
        font-size: 40px !important;
        text-align: center;
        font-weight: 900;
        margin-bottom: 30px !important;
    }

    /* THE WINNING BOARD (EQUALIZED & CENTERED) */
    .v50-board-frame {
        width: 1000px !important;
        margin: 20px auto 40px auto !important;
    }
    .v50-board {
        border: 2px solid #00FF00;
        background-color: rgba(0, 255, 0, 0.05);
        box-shadow: 0px 0px 20px rgba(0, 255, 0, 0.2);
        border-radius: 15px;
        padding: 20px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 100%;
    }
    .v50-island { text-align: center; flex: 1; }
    .v50-label { color: #D4AF37; font-size: 24px !important; font-weight: 900; text-transform: uppercase; margin: 0; }
    .v50-num { color: #00FF00; font-size: 48px !important; font-weight: 900; margin: 0; }

    /* THE TRINITY PILLARS */
    .v50-unit { display: flex; flex-direction: column; align-items: center; margin-top: -60px; }
    .v50-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%);
        width: 25px; height: 260px; border-radius: 12px; border: 2px solid #000; box-shadow: 0px 0px 25px #D4AF37;
    }
    .v50-spire { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%);
        width: 45px; height: 400px; border-radius: 20px; border: 3px solid #000; box-shadow: 0px 0px 35px #D4AF37;
    }

    /* GRID SENSORS (GLOWING) */
    .v50-cell {
        background-color: #1a1a1a; border: 1px solid #00FF00; height: 60px; width: 60px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 24px; border-radius: 10px; margin: 4px; color: #00FF00;
        box-shadow: inset 0px 0px 10px rgba(0, 255, 0, 0.3);
    }
    .red-t { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 0px 15px #FF0000; }
    .blue-t { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 0px 15px #0000FF; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; border-radius: 10px !important; width: 160px !important; }
    input { color: #00FF00 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. TITLE & IMAGE ---
st.markdown("<div class='v50-header'>MITRAX ORACLE PIC 4</div>", unsafe_allow_html=True)
st.markdown("<div class='v50-sub-header'>App</div>", unsafe_allow_html=True)

if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1000)

# --- 2. BOARD (CENTERED) ---
st.markdown("""
<div class='v50-board-frame'>
    <div class='v50-board'>
        <div class='v50-island'><p class='v50-label'>ARUBA</p><p class='v50-num'>1862</p></div>
        <div class='v50-island'><p class='v50-label'>BONAIRE</p><p class='v50-num'>2544</p></div>
        <div class='v50-island'><p class='v50-label'>CURAÇAO</p><p class='v50-num'>7716</p></div>
        <div class='v50-island'><p class='v50-label'>ST. MARTIN</p><p class='v50-num'>3076</p></div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. ENGINE LOGIC ---
def get_v50_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v50_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v50-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- 4. MAIN DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px; margin-bottom:100px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)
m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v50_grid(get_v50_data(st.session_state.get('v50_r', "")), target="red")
with m_cols[1]:
    st.markdown("<div class='v50-unit'><p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("R", key="v50_r", label_visibility="collapsed")
    st.markdown("<div class='v50-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v50_grid(get_v50_data(st.session_state.get('v50_b', "")), target="blue")
with m_cols[3]:
    st.markdown("<div style='height:120px;'></div><div class='v50-spire'></div>", unsafe_allow_html=True)
with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v50_grid([[0]*4 for _ in range(4)], is_dark=True)
with m_cols[5]:
    st.markdown("<div class='v50-unit'><p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("B", key="v50_b", label_visibility="collapsed")
    st.markdown("<div class='v50-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v50_grid([[0]*4 for _ in range(4)], is_dark=True)
