import streamlit as st
import os

# --- 1. ENGINE CONFIG (V65 CONSOLIDATED) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V65")

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

    /* THE CROWN */
    .stImage { display: flex !important; justify-content: center !important; width: 800px !important; margin-bottom: 20px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 800px !important; }

    /* TRIPLE-STACK BOARD (HORIZONTAL) */
    .v65-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1100px !important; 
        margin: 10px auto !important; 
    }
    .v65-column { 
        border: 2px solid #4B6321; background-color: #4B6321; 
        margin: 0 5px; padding: 6px; width: 250px !important;
        display: flex; flex-direction: column; 
    }
    .v65-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 16px; margin-bottom: 4px; }
    .v65-box { background-color: #FFFFFF; border: 1px solid #000; margin: 2px 0; padding: 4px; text-align: center; }
    .v65-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 30px !important; font-weight: 900; font-style: italic; }

    /* THE CONSOLIDATED SENSOR DECK */
    .v65-sensor-deck {
        width: 1200px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: flex-start !important;
        margin-top: 40px !important;
    }

    .v65-grid-box { width: 240px; }
    .v65-unit { display: flex; flex-direction: column; align-items: center; width: 140px; }
    .v65-pillar { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 20px; height: 220px; border-radius: 10px; border: 1px solid #000; box-shadow: 0px 0px 15px #D4AF37; }
    .v65-spire { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 35px; height: 350px; border-radius: 15px; border: 2px solid #000; box-shadow: 0px 0px 25px #D4AF37; margin: 0 20px; }

    /* GRID CELLS */
    .v65-cell { background-color: #1a1a1a; border: 1px solid #00FF00; height: 50px; width: 50px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 20px; border-radius: 8px; margin: 2px; color: #00FF00; }
    .red-t { border: 3px solid #FF0000; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 3px solid #0000FF; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 3px solid #00FF00 !important; width: 120px !important; }
    input { color: #00FF00 !important; font-size: 24px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v65-board-container'>
    <div class='v65-column'><div class='v65-header'>ARUBA</div><div class='v65-box'><span class='v65-num'>1862</span></div><div class='v65-box'><span class='v65-num'>0801</span></div><div class='v65-box'><span class='v65-num'>9394</span></div></div>
    <div class='v65-column'><div class='v65-header'>BONAIRE</div><div class='v65-box'><span class='v65-num'>2544</span></div><div class='v65-box'><span class='v65-num'>8732</span></div><div class='v65-box'><span class='v65-num'>7296</span></div></div>
    <div class='v65-column'><div class='v65-header'>CURAÇAO</div><div class='v65-box'><span class='v65-num'>7716</span></div><div class='v65-box'><span class='v65-num'>5502</span></div><div class='v65-box'><span class='v65-num'>5918</span></div></div>
    <div class='v65-column'><div class='v65-header'>ST. MARTIN</div><div class='v65-box'><span class='v65-num'>3076</span></div><div class='v65-box'><span class='v65-num'>8561</span></div><div class='v65-box'><span class='v65-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS (CONSOLIDATED) ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 2px solid #00FF00; width:1000px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v65_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v65_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v65-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# SENSOR ROW
s_cols = st.columns([3, 2, 3, 1, 3, 2, 3])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v65_grid(get_v65_data(st.session_state.get('v65_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div class='v65-unit'><p style='color:red; font-weight:900; margin-bottom:5px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v65_r", label_visibility="collapsed")
    st.markdown("<div class='v65-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v65_grid(get_v65_data(st.session_state.get('v65_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div style='height:80px;'></div><div class='v65-spire'></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v65_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div class='v65-unit'><p style='color:blue; font-weight:900; margin-bottom:5px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v65_b", label_visibility="collapsed")
    st.markdown("<div class='v65-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v65_grid([[0]*4 for _ in range(4)], is_dark=True)
