import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V39 SOUTHERN LEAP) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V39")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE WINNING BOARD */
    .v39-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 20px !important;
        margin: 10px auto 30px auto !important;
        max-width: 1400px !important;
    }

    /* THE PILLAR UNIT */
    .v39-unit {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
        width: 100% !important;
        margin-top: -80px !important; 
        position: relative !important;
        z-index: 9999 !important;
    }

    /* THE GOLDEN POOLS */
    .v39-pillar { 
        background-color: #D4AF37 !important; 
        width: 25px !important; 
        height: 250px !important; 
        margin-top: 10px !important;
        border-radius: 12px !important;
        border: 3px solid #1A1A1A !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.8) !important;
    }

    /* THE GRAND CENTRAL SPIRE */
    .v39-grand-spire {
        background-color: #D4AF37 !important;
        width: 40px !important;
        height: 400px !important;
        border-radius: 20px !important;
        border: 4px solid #1A1A1A !important;
        box-shadow: 0px 0px 50px rgba(212, 175, 55, 1.0) !important;
        margin: 0 auto !important;
    }

    /* THE MATRIX SENSORS */
    .v39-cell { 
        font-weight: 900 !important; font-size: 22px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 8px !important; margin: 4px !important; color: #000000 !important; height: 58px !important; width: 58px !important;
        background-color: #D3D3D3 !important;
    }
    
    /* SPECIAL COLOR TARGETS */
    .red-t { border: 5px solid #FF0000 !important; border-radius: 50% !important; width: 50px !important; height: 50px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    .blue-t { border: 5px solid #0000FF !important; border-radius: 50% !important; width: 50px !important; height: 50px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    
    .v39-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 20px !important; text-transform: uppercase !important; margin-bottom: 15px !important; text-align: center !important; }

    /* INPUTS */
    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 5px solid #D4AF37 !important;
        border-radius: 10px !important;
        width: 160px !important;
        margin: 5px auto !important;
    }
    input { color: #000000 !important; font-size: 32px !important; font-weight: 900 !important; text-align: center !important; height: 65px !important; }

    .v39-bridge-text { color: #00FF00 !important; font-size: 32px !important; font-weight: 900 !important; border-bottom: 6px solid #00FF00 !important; margin-bottom: 60px !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE RABBIT ENGINE (V39: TWO-ROW DATA) ---
def get_matrix_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            # ROW 1 (NORTH)
            seed = int(input_str[0])
            grid[0][0] = seed
            grid[0][1] = (grid[0][0] + 1) % 10
            grid[0][2] = (grid[0][1] + 1) % 10
            grid[0][3] = (grid[0][2] + 1) % 10
            
            # ROW 2 (SOUTH LEAP - THE HOLE SECRET)
            grid[1][0] = (grid[0][3] - 1) % 10
            grid[1][1] = (grid[1][0] + 1) % 10
            grid[1][2] = (grid[1][1] + 1) % 10
            grid[1][3] = (grid[1][2] + 1) % 10
        except: pass
    return grid

# --- 3. WINNING BOARD ---
st.markdown("<div class='v39-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p style='color:#D4AF37; font-size:24px; font-weight:900; text-align:center;'>{name}</p><p style='color:#00FF00; font-size:42px; font-weight:900; text-align:center;'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='v39-bridge-text'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v39_grid(data, is_dark=False, target_color=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            # SPECIAL COLOR ASSIGNMENTS: 7/1 RED, 8/3 BLUE
            is_red_target = (r == 0 and c == 0 and target_color == "red")
            is_blue_target = (r == 0 and c == 0 and target_color == "blue")
            
            html = f"<div class='v39-cell' style='background-color:{bg_color}'>"
            if is_red_target: html += f"<div class='red-t'>{val}</div>"
            elif is_blue_target: html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# --- 4. THE MAIN DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='v39-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_v39_grid(get_matrix_data(st.session_state.get('v39_r', "")), target_color="red")

with cols[1]:
    st.markdown("<div class='v39-unit'>", unsafe_allow_html=True)
    st.markdown("<p style='color:#FF0000; font-weight:900;'>RED 7/1</p>", unsafe_allow_html=True)
    st.text_input("RED", key="v39_r", label_visibility="collapsed")
    st.markdown("<div class='v39-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='v39-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_v39_grid(get_matrix_data(st.session_state.get('v39_b', "")), target_color="blue")

with cols[3]:
    st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='v39-grand-spire'></div>", unsafe_allow_html=True)

with cols[4]:
    st.markdown("<p class='v39-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_v39_grid([[0]*4 for _ in range(4)], is_dark=True)

with cols[5]:
    st.markdown("<div class='v39-unit'>", unsafe_allow_html=True)
    st.markdown("<p style='color:#0000FF; font-weight:900;'>BLUE 8/3</p>", unsafe_allow_html=True)
    st.text_input("BLUE", key="v39_b", label_visibility="collapsed")
    st.markdown("<div class='v39-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='v39-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_v39_grid([[0]*4 for _ in range(4)], is_dark=True)
