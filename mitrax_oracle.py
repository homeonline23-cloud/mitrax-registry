import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V41 TOTAL CENTER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V41")

st.markdown("""
    <style>
    /* GLOBAL BLACK HOLE */
    .stApp { background-color: #000000 !important; }

    /* CENTER EVERYTHING IN THE MAIN CONTAINER */
    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding-top: 2rem !important;
    }

    /* THE INDESTRUCTIBLE UNIFIED BOARD */
    .v41-board {
        border: 4px solid #D4AF37;
        background-color: rgba(212, 175, 55, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto;
        width: 1200px; /* MATCHING BANNER SCALE */
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .v41-island-unit { text-align: center; flex: 1; }
    .v41-label-text { color: #D4AF37; font-size: 28px !important; font-weight: 900; text-transform: uppercase; margin-bottom: 5px; }
    .v41-num-text { color: #00FF00; font-size: 52px !important; font-weight: 900; line-height: 1; }

    /* THE PILLAR/INPUT UNIT */
    .v41-unit {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: -60px;
    }

    /* THE PILLARS */
    .v41-gold-pool {
        background-color: #D4AF37;
        width: 25px;
        height: 250px;
        border-radius: 12px;
        border: 2px solid #000;
        box-shadow: 0px 0px 20px #D4AF37;
    }
    .v41-grand-spire {
        background-color: #D4AF37;
        width: 45px;
        height: 400px;
        border-radius: 20px;
        border: 3px solid #000;
        box-shadow: 0px 0px 30px #D4AF37;
    }

    /* THE CELLS */
    .v41-cell {
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
    
    .v41-grid-header { color: #D4AF37; font-weight: 900; font-size: 20px; text-align: center; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. CENTERED BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1200)
else:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>MITRAX EMPIRE COMMAND</h1>", unsafe_allow_html=True)

# --- 3. UNIFIED WINNING BOARD (CENTERED) ---
st.markdown("""
<div class='v41-board'>
    <div class='v41-island-unit'><p class='v41-label-text'>ARUBA</p><p class='v41-num-text'>1862</p></div>
    <div class='v41-island-unit'><p class='v41-label-text'>BONAIRE</p><p class='v41-num-text'>2544</p></div>
    <div class='v41-island-unit'><p class='v41-label-text'>CURAÇAO</p><p class='v41-num-text'>7716</p></div>
    <div class='v41-island-unit'><p class='v41-label-text'>ST. MARTIN</p><p class='v41-num-text'>3076</p></div>
</div>
""", unsafe_allow_html=True)

# --- 4. LOGIC ENGINE ---
def get_v41_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v41_grid(data, is_dark=False, target=None):
    bg = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v41-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-target'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-target'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# --- 5. THE MAIN DECK (CENTERED) ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; padding-bottom:10px; width:1200px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

# Main container for grids and pillars to keep them together in the middle
with st.container():
    m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

    with m_cols[0]:
        st.markdown("<p class='v41-grid-header'>GRID 1</p>", unsafe_allow_html=True)
        draw_v41_grid(get_v41_data(st.session_state.get('v41_r', "")), target="red")

    with m_cols[1]:
        st.markdown("<div class='v41-unit'>", unsafe_allow_html=True)
        st.markdown("<p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
        st.text_input("R", key="v41_r", label_visibility="collapsed")
        st.markdown("<div class='v41-gold-pool'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with m_cols[2]:
        st.markdown("<p class='v41-grid-header'>GRID 2</p>", unsafe_allow_html=True)
        draw_v41_grid(get_v41_data(st.session_state.get('v41_b', "")), target="blue")

    with m_cols[3]:
        st.markdown("<div style='height:100px;'></div><div class='v41-grand-spire'></div>", unsafe_allow_html=True)

    with m_cols[4]:
        st.markdown("<p class='v41-grid-header'>GRID 3</p>", unsafe_allow_html=True)
        draw_v41_grid([[0]*4 for _ in range(4)], is_dark=True)

    with m_cols[5]:
        st.markdown("<div class='v41-unit'>", unsafe_allow_html=True)
        st.markdown("<p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
        st.text_input("B", key="v41_b", label_visibility="collapsed")
        st.markdown("<div class='v41-gold-pool'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with m_cols[6]:
        st.markdown("<p class='v41-grid-header'>GRID 4</p>", unsafe_allow_html=True)
        draw_v41_grid([[0]*4 for _ in range(4)], is_dark=True)
