import streamlit as st
import os

# --- 1. ENGINE CONFIG (V71 PERFECT PILLAR) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V71")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE ABSOLUTE CENTER FORCE */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }

    /* THE CROWN (IMAGE) - CENTERED */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        width: 1000px !important;
        margin-bottom: 40px !important;
    }
    img {
        border: 5px solid #D4AF37;
        border-radius: 20px;
        width: 1000px !important;
        box-shadow: 0px 0px 50px rgba(212, 175, 55, 0.4);
    }

    /* TRIPLE-STACK BOARD - COMPACT CENTER */
    .v71-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1100px !important; 
        margin: 0 auto 60px auto !important; 
    }
    .v71-column { 
        border: 4px solid #4B6321; background-color: #4B6321; 
        margin: 0 10px; padding: 15px; width: 250px !important;
        display: flex; flex-direction: column; border-radius: 12px;
    }
    .v71-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 20px; text-transform: uppercase; }
    .v71-box { background-color: #FFFFFF; border: 2px solid #000; margin: 5px 0; padding: 10px; text-align: center; border-radius: 8px; }
    .v71-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 42px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS - SQUEEZED CENTER */
    .v71-sensor-deck {
        width: 1100px !important; /* MATCHES BOARD WIDTH */
        display: flex !important;
        justify-content: center !important;
    }
    .v71-cell { 
        background-color: #1a1a1a; border: 3px solid #00FF00; 
        height: 85px; width: 85px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 40px; border-radius: 12px; margin: 4px; color: #00FF00; 
        box-shadow: 0px 0px 20px rgba(0, 255, 0, 0.3);
    }
    .v71-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 50px; height: 350px; 
        border-radius: 12px; border: 3px solid #000; 
        box-shadow: 0px 0px 35px #D4AF37; 
    }
    .red-t { border: 8px solid #FF0000; border-radius: 50%; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 8px solid #0000FF; border-radius: 50%; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; }

    /* TITAN INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 5px solid #00FF00 !important; width: 150px !important; border-radius: 12px !important; }
    input { color: #00FF00 !important; font-size: 38px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v71-board-container'>
    <div class='v71-column'><div class='v71-header'>ARUBA</div><div class='v71-box'><span class='v71-num'>1862</span></div><div class='v71-box'><span class='v71-num'>0801</span></div><div class='v71-box'><span class='v71-num'>9394</span></div></div>
    <div class='v71-column'><div class='v71-header'>BONAIRE</div><div class='v71-box'><span class='v71-num'>2544</span></div><div class='v71-box'><span class='v71-num'>8732</span></div><div class='v71-box'><span class='v71-num'>7296</span></div></div>
    <div class='v71-column'><div class='v71-header'>CURAÇAO</div><div class='v71-box'><span class='v71-num'>7716</span></div><div class='v71-box'><span class='v71-num'>5502</span></div><div class='v71-box'><span class='v71-num'>5918</span></div></div>
    <div class='v71-column'><div class='v71-header'>ST. MARTIN</div><div class='v71-box'><span class='v71-num'>3076</span></div><div class='v71-box'><span class='v71-num'>8561</span></div><div class='v71-box'><span class='v71-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE MATRIX ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1100px; margin-bottom:50px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v71_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v71_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v71-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# SQUEEZED SENSOR ROW
s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v71_grid(get_v71_data(st.session_state.get('v71_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:red; font-weight:900; font-size:24px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v71_r", label_visibility="collapsed")
    st.markdown("<div class='v71-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v71_grid(get_v71_data(st.session_state.get('v71_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:#D4AF37; font-weight:900; font-size:24px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:80px;'></div><div class='v71-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v71_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:blue; font-weight:900; font-size:24px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v71_b", label_visibility="collapsed")
    st.markdown("<div class='v71-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v71_grid([[0]*4 for _ in range(4)], is_dark=True)
