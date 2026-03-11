import streamlit as st
import os

# --- 1. ENGINE CONFIG (V60 TRIPLE-STACK) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V60")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* GLOBAL CENTER FORCE */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
    }

    /* THE IMAGE (TOP CROWN) */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        margin: 0 auto !important;
        width: 1000px !important;
    }
    img {
        border: 4px solid #D4AF37;
        border-radius: 20px;
        width: 1000px !important;
    }

    /* THE TRIPLE-STACK BOARD */
    .v60-board-container {
        width: 1200px !important;
        margin: 40px auto !important;
        display: flex !important;
        justify-content: center !important;
    }
    .v60-column {
        border: 3px solid #4B6321; /* DARK IMPERIAL GREEN */
        background-color: #4B6321;
        margin: 0 5px;
        padding: 5px;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .v60-header-cell {
        color: #D4AF37;
        text-align: center;
        font-weight: 900;
        font-size: 22px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .v60-number-box {
        background-color: #FFFFFF;
        border: 2px solid #000000;
        margin: 3px 0;
        padding: 5px;
        text-align: center;
    }
    .v60-num-text {
        color: #000000;
        font-family: 'Courier New', Courier, monospace;
        font-size: 42px !important;
        font-weight: 900;
        font-style: italic;
    }

    /* SENSOR STYLES (KEEPING STABILITY) */
    .v58-cell {
        background-color: #1a1a1a; border: 1px solid #00FF00; height: 60px; width: 60px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 24px; border-radius: 10px; margin: 4px; color: #00FF00;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE TRIPLE-STACK BOARD (MATCHING YOUR IMAGE) ---
st.markdown("""
<div class='v60-board-container'>
    <div class='v60-column'>
        <div class='v60-header-cell'>ARUBA</div>
        <div class='v60-number-box'><span class='v60-num-text'>1862</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>0801</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>9394</span></div>
    </div>
    <div class='v60-column'>
        <div class='v60-header-cell'>BONAIRE</div>
        <div class='v60-number-box'><span class='v60-num-text'>2544</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>8732</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>7296</span></div>
    </div>
    <div class='v60-column'>
        <div class='v60-header-cell'>CURAÇAO</div>
        <div class='v60-number-box'><span class='v60-num-text'>7716</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>5502</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>5918</span></div>
    </div>
    <div class='v60-column'>
        <div class='v60-header-cell'>ST. MARTIN</div>
        <div class='v60-number-box'><span class='v60-num-text'>3076</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>8561</span></div>
        <div class='v60-number-box'><span class='v60-num-text'>3465</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSOR DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px; margin-bottom:100px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

# Grid logic preserved for Row 1 & 2
def get_v60_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v60_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v58-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div style='border:4px solid red; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center;'>{val}</div>"
            elif is_target and target == "blue": html += f"<div style='border:4px solid blue; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center;'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])
with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v60_grid(get_v60_data(st.session_state.get('v60_r', "")), target="red")
with m_cols[1]:
    st.text_input("R", key="v60_r", label_visibility="collapsed")
with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v60_grid(get_v60_data(st.session_state.get('v60_b', "")), target="blue")
# ... (Continuing the columns for Grid 3/4)
