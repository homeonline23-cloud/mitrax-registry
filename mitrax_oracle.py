import streamlit as st
import os

# --- 1. ENGINE CONFIG (V68 COMPACT TITAN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V68")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* GLOBAL CENTER LOCK */
    [data-testid="stVerticalBlock"] {
        align-items: center !important;
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
    }

    /* THE CROWN (TOP IMAGE) */
    .stImage { display: flex !important; justify-content: center !important; width: 1000px !important; margin-bottom: 30px !important; }
    img { border: 5px solid #D4AF37; border-radius: 20px; width: 1000px !important; }

    /* TRIPLE-STACK BOARD (HORIZONTAL & MASSIVE) */
    .v68-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1100px !important; 
        margin: 10px auto !important; 
    }
    .v68-column { 
        border: 4px solid #4B6321; background-color: #4B6321; 
        margin: 0 8px; padding: 12px; width: 260px !important;
        display: flex; flex-direction: column; 
    }
    .v68-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 22px; margin-bottom: 6px; text-transform: uppercase; }
    .v68-box { background-color: #FFFFFF; border: 3px solid #000; margin: 4px 0; padding: 8px; text-align: center; }
    .v68-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 45px !important; font-weight: 900; font-style: italic; }

    /* THE SENSOR DECK (CONSOLIDATED & CENTERED) */
    .v68-sensor-wrap {
        width: 1100px !important;
        margin: 40px auto !important;
    }

    .v68-unit { display: flex; flex-direction: column; align-items: center; width: 120px; }
    .v68-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 50px; height: 380px; 
        border-radius: 12px; border: 3px solid #000; 
        box-shadow: 0px 0px 35px #D4AF37; 
    }

    /* TITAN GRID CELLS (ULTRA RESIZED) */
    .v68-cell { 
        background-color: #1a1a1a; border: 3px solid #00FF00; 
        height: 85px; width: 85px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 38px; border-radius: 12px; margin: 5px; color: #00FF00; 
        box-shadow: 0px 0px 15px rgba(0, 255, 0, 0.4);
    }
    .red-t { border: 7px solid #FF0000; border-radius: 50%; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 7px solid #0000FF; border-radius: 50%; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; }

    /* TITAN INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 5px solid #00FF00 !important; width: 160px !important; margin-bottom: 15px !important; }
    input { color: #00FF00 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE TRIPLE-STACK BOARD ---
st.markdown("""
<div class='v68-board-container'>
    <div class='v68-column'><div class='v68-header'>ARUBA</div><div class='v68-box'><span class='v68-num'>1862</span></div><div class='v68-box'><span class='v68-num'>0801</span></div><div class='v68-box'><span class='v68-num'>9394</span></div></div>
    <div class='v68-column'><div class='v68-header'>BONAIRE</div><div class='v68-box'><span class='v68-num'>2544</span></div><div class='v68-box'><span class='v68-num'>8732</span></div><div class='v68-box'><span class='v68-num'>7296</span></div></div>
    <div class='v68-column'><div class='v68-header'>CURAÇAO</div><div class='v68-box'><span class='v68-num'>7716</span></div><div class='v68-box'><span class='v68-num'>5502</span></div><div class='v68-box'><span class='v68-num'>5918</span></div></div>
    <div class='v68-column'><div class='v68-header'>ST. MARTIN</div><div class='v68-box'><span class='v68-num'>3076</span></div><div class='v68-box'><span class='v68-num'>8561</span></div><div class='v68-box'><span class='v68-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS (TITAN CONSOLIDATED) ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 6px solid #00FF00; width:1100px; margin-bottom:50px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v68_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v68_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v68-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# COMPACT SENSOR ROW
s_cols = st.columns([4, 2, 4, 2, 4, 2, 4])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:20px;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v68_grid(get_v68_data(st.session_state.get('v68_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div class='v68-unit'><p style='color:red; font-weight:900; font-size:24px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v68_r", label_visibility="collapsed")
    st.markdown("<div class='v68-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:20px;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v68_grid(get_v68_data(st.session_state.get('v68_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div class='v68-unit'><p style='color:#D4AF37; font-weight:900; font-size:24px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:75px;'></div><div class='v68-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:20px;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v68_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div class='v68-unit'><p style='color:blue; font-weight:900; font-size:24px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v68_b", label_visibility="collapsed")
    st.markdown("<div class='v68-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:20px;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v68_grid([[0]*4 for _ in range(4)], is_dark=True)
