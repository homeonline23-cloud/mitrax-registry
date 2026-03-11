import streamlit as st
import os

# --- 1. ENGINE CONFIG (V72 MONOLITH SCALE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V72")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE ABSOLUTE CENTER FORCE */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN (IMAGE) */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        width: 1200px !important;
        margin-bottom: 50px !important;
    }
    img {
        border: 6px solid #D4AF37;
        border-radius: 25px;
        width: 1200px !important;
        box-shadow: 0px 0px 60px rgba(212, 175, 55, 0.5);
    }

    /* TRIPLE-STACK BOARD - MONOLITH SCALE */
    .v72-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 100% !important; 
        margin: 0 auto 100px auto !important; 
    }
    .v72-column { 
        border: 6px solid #4B6321; background-color: #4B6321; 
        margin: 0 15px; padding: 25px; width: 400px !important;
        display: flex; flex-direction: column; border-radius: 20px;
    }
    .v72-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 35px; text-transform: uppercase; margin-bottom: 10px; }
    .v72-box { background-color: #FFFFFF; border: 4px solid #000; margin: 8px 0; padding: 20px; text-align: center; border-radius: 12px; }
    .v72-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 70px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS - MONOLITH SCALE */
    .v72-sensor-deck {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }
    .v72-cell { 
        background-color: #1a1a1a; border: 5px solid #00FF00; 
        height: 125px; width: 125px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 65px; border-radius: 20px; margin: 8px; color: #00FF00; 
        box-shadow: 0px 0px 30px rgba(0, 255, 0, 0.6);
    }
    .v72-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 80px; height: 500px; 
        border-radius: 20px; border: 5px solid #000; 
        box-shadow: 0px 0px 50px #D4AF37; 
    }
    .red-t { border: 12px solid #FF0000; border-radius: 50%; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 12px solid #0000FF; border-radius: 50%; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; }

    /* TITAN INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 8px solid #00FF00 !important; width: 250px !important; border-radius: 20px !important; margin-bottom: 20px !important; }
    input { color: #00FF00 !important; font-size: 60px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v72-board-container'>
    <div class='v72-column'><div class='v72-header'>ARUBA</div><div class='v72-box'><span class='v72-num'>1862</span></div><div class='v72-box'><span class='v72-num'>0801</span></div><div class='v72-box'><span class='v72-num'>9394</span></div></div>
    <div class='v72-column'><div class='v72-header'>BONAIRE</div><div class='v72-box'><span class='v72-num'>2544</span></div><div class='v72-box'><span class='v72-num'>8732</span></div><div class='v72-box'><span class='v72-num'>7296</span></div></div>
    <div class='v72-column'><div class='v72-header'>CURAÇAO</div><div class='v72-box'><span class='v72-num'>7716</span></div><div class='v72-box'><span class='v72-num'>5502</span></div><div class='v72-box'><span class='v72-num'>5918</span></div></div>
    <div class='v72-column'><div class='v72-header'>ST. MARTIN</div><div class='v72-box'><span class='v72-num'>3076</span></div><div class='v72-box'><span class='v72-num'>8561</span></div><div class='v72-box'><span class='v72-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS ---
st.markdown("<h1 style='color:#00FF00; text-align:center; border-bottom: 10px solid #00FF00; width:1300px; margin-bottom:80px; font-size:60px;'>MATRIX SENSORS</h1>", unsafe_allow_html=True)

def get_v72_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v72_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v72-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v72_grid(get_v72_data(st.session_state.get('v72_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:red; font-weight:900; font-size:40px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v72_r", label_visibility="collapsed")
    st.markdown("<div class='v72-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v72_grid(get_v72_data(st.session_state.get('v72_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:#D4AF37; font-weight:900; font-size:40px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:115px;'></div><div class='v72-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v72_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:blue; font-weight:900; font-size:40px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v72_b", label_visibility="collapsed")
    st.markdown("<div class='v72-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v72_grid([[0]*4 for _ in range(4)], is_dark=True)
