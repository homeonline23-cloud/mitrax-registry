import streamlit as st
import os

# --- 1. ENGINE CONFIG (V49: THE TRUE ORACLE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V49")

st.markdown("""
    <style>
    /* GLOBAL DARK NEBULA */
    .stApp { 
        background-color: #000000 !important; 
        background-image: radial-gradient(circle, #001a00 0%, #000000 70%) !important;
    }

    /* THE IMPERIAL HEADER (MATCHING THE IMAGE) */
    .v49-header {
        color: #00FF00;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 50px !important;
        text-align: center;
        text-shadow: 0px 0px 15px #00FF00, 2px 2px #D4AF37;
        margin-top: 40px !important;
        margin-bottom: 5px !important;
    }
    .v49-sub-header {
        color: #00FF00;
        font-size: 40px !important;
        text-align: center;
        font-weight: 900;
        margin-bottom: 30px !important;
    }

    /* THE WINNING BOARD (EQUALIZED & CENTERED) */
    .v49-board {
        border: 2px solid #00FF00;
        background-color: rgba(0, 255, 0, 0.05);
        box-shadow: 0px 0px 20px rgba(0, 255, 0, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        width: 1000px;
        display: flex;
        justify-content: space-around;
    }
    .v45-island { text-align: center; flex: 1; border-right: 1px solid rgba(0,255,0,0.3); }
    .v45-island:last-child { border-right: none; }
    .v49-label { color: #D4AF37; font-size: 24px !important; font-weight: 900; }
    .v49-num { color: #00FF00; font-size: 48px !important; font-weight: 900; }

    /* THE PILLARS (THE GOLDEN POOLS) */
    .v49-unit { display: flex; flex-direction: column; align-items: center; margin-top: -50px; }
    .v49-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%);
        width: 25px; height: 300px; border-radius: 15px;
        box-shadow: 0px 0px 25px #D4AF37; border: 1px solid #000;
    }
    .v49-spire { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%);
        width: 45px; height: 450px; border-radius: 20px;
        box-shadow: 0px 0px 40px #D4AF37; margin-top: 80px;
    }

    /* GRID SENSORS (GLOWING) */
    .v49-cell {
        background-color: #222; border: 1px solid #00FF00; height: 60px; width: 60px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 24px; border-radius: 10px; margin: 5px; color: #00FF00;
        box-shadow: inset 0px 0px 10px rgba(0, 255, 0, 0.5);
    }
    .red-t { border: 4px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 0px 15px #FF0000; }
    .blue-t { border: 4px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 0px 15px #0000FF; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 3px solid #00FF00 !important; border-radius: 10px !important; width: 150px !important; }
    input { color: #00FF00 !important; font-size: 30px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. TITLE (MATCHING IMAGE) ---
st.markdown("<div class='v49-header'>MITRAX ORACLE PIC 4</div>", unsafe_allow_html=True)
st.markdown("<div class='v49-sub-header'>App</div>", unsafe_allow_html=True)

# --- 2. BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1000)

# --- 3. BOARD ---
st.markdown("""
<div class='v49-board'>
    <div class='v45-island'><p class='v49-label'>ARUBA</p><p class='v49-num'>1862</p></div>
    <div class='v45-island'><p class='v49-label'>BONAIRE</p><p class='v49-num'>2544</p></div>
    <div class='v45-island'><p class='v49-label'>CURAÇAO</p><p class='v49-num'>7716</p></div>
    <div class='v45-island'><p class='v49-label'>ST. MARTIN</p><p class='v49-num'>3076</p></div>
</div>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def get_v49_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v49_grid(data, is_dark=False, target=None):
    opacity = "1.0" if not is_dark else "0.3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v49-cell' style='opacity:{opacity}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- 5. MAIN DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; font-family:sans-serif; width:1000px;'>SYMMETRY MATRIX SENSORS</h2>", unsafe_allow_html=True)
m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p style='color:#00FF00; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v49_grid(get_v49_data(st.session_state.get('v49_r', "")), target="red")
with m_cols[1]:
    st.markdown("<div class='v49-unit'><p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("R", key="v49_r", label_visibility="collapsed")
    st.markdown("<div class='v49-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]:
    st.markdown("<p style='color:#00FF00; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v49_grid(get_v49_data(st.session_state.get('v49_b', "")), target="blue")
with m_cols[3]:
    st.markdown("<div class='v49-spire'></div>", unsafe_allow_html=True)
with m_cols[4]:
    st.markdown("<p style='color:#00FF00; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v49_grid([[0]*4 for _ in range(4)], is_dark=True)
with m_cols[5]:
    st.markdown("<div class='v49-unit'><p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("B", key="v49_b", label_visibility="collapsed")
    st.markdown("<div class='v49-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]:
    st.markdown("<p style='color:#00FF00; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v4_grid([[0]*4 for _ in range(4)], is_dark=True)
