import streamlit as st
import os

# --- 1. ENGINE CONFIG (V59 RANKED PODIUM) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V59")

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

    /* THE IMAGE (CENTER-LOCK) */
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

    /* THE RANKED BOARD (CENTERED) */
    .v59-board-wrap {
        width: 1150px !important;
        margin: 40px auto !important;
        display: flex !important;
        justify-content: center !important;
    }
    .v59-board {
        border: 4px solid #00FF00;
        background-color: rgba(0, 255, 0, 0.08);
        border-radius: 25px;
        padding: 40px;
        display: flex;
        justify-content: space-around;
        align-items: flex-end; /* ALIGN TO BOTTOM FOR PODIUM EFFECT */
        width: 100%;
        box-shadow: 0px 0px 30px rgba(0, 255, 0, 0.3);
    }
    .v59-rank-unit { text-align: center; flex: 1; padding: 10px; }
    
    /* RANKING STYLES */
    .rank-1 { color: #D4AF37; font-size: 34px !important; font-weight: 900; text-shadow: 0px 0px 10px #D4AF37; }
    .rank-2 { color: #C0C0C0; font-size: 28px !important; font-weight: 900; }
    .rank-3 { color: #CD7F32; font-size: 26px !important; font-weight: 900; }
    
    .island-name { color: #FFFFFF; font-size: 22px !important; font-weight: 700; margin: 10px 0; }
    .v59-num { color: #00FF00; font-size: 65px !important; font-weight: 900; text-shadow: 0px 0px 20px #00FF00; margin: 0; }

    /* SENSORS & PILLARS */
    .v58-unit { display: flex; flex-direction: column; align-items: center; margin-top: -60px; }
    .v58-pillar { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 25px; height: 260px; border-radius: 12px; border: 2px solid #000; box-shadow: 0px 0px 20px #D4AF37; }
    .v58-spire { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 45px; height: 400px; border-radius: 20px; border: 3px solid #000; box-shadow: 0px 0px 30px #D4AF37; }

    .v58-cell {
        background-color: #1a1a1a; border: 1px solid #00FF00; height: 60px; width: 60px;
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 24px; border-radius: 10px; margin: 4px; color: #00FF00;
    }
    .red-t { border: 5px solid #FF0000; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 5px solid #0000FF; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE (THE CROWN) ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE RANKED PODIUM BOARD ---
st.markdown("""
<div class='v59-board-wrap'>
    <div class='v59-board'>
        <div class='v59-rank-unit'>
            <p class='rank-2'>2ND PLACE</p>
            <p class='island-name'>CURAÇAO</p>
            <p class='v59-num'>7716</p>
        </div>
        <div class='v59-rank-unit'>
            <p class='rank-1'>1ST PLACE</p>
            <p class='island-name'>ARUBA</p>
            <p class='v59-num'>1862</p>
        </div>
        <div class='v59-rank-unit'>
            <p class='rank-3'>3RD PLACE</p>
            <p class='island-name'>BONAIRE</p>
            <p class='v59-num'>2544</p>
        </div>
        <div class='v59-rank-unit'>
            <p style='color:#FFF; font-size:20px; font-weight:900;'>ST. MARTIN</p>
            <p class='v59-num' style='font-size:45px !important;'>3076</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSOR DECK ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px; margin-bottom:100px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

# Engine logic remains identical to V58 to ensure stability
def get_v59_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v59_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v58-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v59_grid(get_v59_data(st.session_state.get('v59_r', "")), target="red")
with m_cols[1]:
    st.markdown("<div class='v58-unit'><p style='color:red; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("R", key="v59_r", label_visibility="collapsed")
    st.markdown("<div class='v58-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v59_grid(get_v59_data(st.session_state.get('v59_b', "")), target="blue")
with m_cols[3]:
    st.markdown("<div style='height:120px;'></div><div class='v58-spire'></div>", unsafe_allow_html=True)
with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v59_grid([[0]*4 for _ in range(4)], is_dark=True)
with m_cols[5]:
    st.markdown("<div class='v58-unit'><p style='color:blue; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("B", key="v59_b", label_visibility="collapsed")
    st.markdown("<div class='v58-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v59_grid([[0]*4 for _ in range(4)], is_dark=True)
