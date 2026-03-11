import streamlit as st
import os

# --- 1. ENGINE CONFIG (V70 MASTER-AXIS) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V70")

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

    /* THE CROWN (IMAGE) - FORCED CENTER */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-bottom: 50px !important;
    }
    img {
        border: 6px solid #D4AF37;
        border-radius: 25px;
        width: 1100px !important; /* MASSIVE SIZE */
        box-shadow: 0px 0px 60px rgba(212, 175, 55, 0.4);
    }

    /* TRIPLE-STACK BOARD - FORCED CENTER */
    .v70-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1200px !important; 
        margin: 0 auto 80px auto !important; 
    }
    .v70-column { 
        border: 5px solid #4B6321; background-color: #4B6321; 
        margin: 0 15px; padding: 20px; width: 280px !important;
        display: flex; flex-direction: column; border-radius: 15px;
    }
    .v70-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 24px; text-transform: uppercase; }
    .v70-box { background-color: #FFFFFF; border: 3px solid #000; margin: 8px 0; padding: 12px; text-align: center; border-radius: 10px; }
    .v70-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 50px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS - FORCED CENTER */
    .v70-sensor-container {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    .v70-cell { 
        background-color: #1a1a1a; border: 4px solid #00FF00; 
        height: 100px; width: 100px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 50px; border-radius: 15px; margin: 8px; color: #00FF00; 
        box-shadow: 0px 0px 25px rgba(0, 255, 0, 0.5);
    }
    .v70-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 60px; height: 400px; 
        border-radius: 15px; border: 4px solid #000; 
        box-shadow: 0px 0px 40px #D4AF37; 
    }
    .red-t { border: 10px solid #FF0000; border-radius: 50%; width: 85px; height: 85px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 10px solid #0000FF; border-radius: 50%; width: 85px; height: 85px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 6px solid #00FF00 !important; width: 180px !important; border-radius: 15px !important; }
    input { color: #00FF00 !important; font-size: 45px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE (THE CROWN) ---
st.markdown("<div style='display: flex; justify-content: center; width: 100%;'>", unsafe_allow_html=True)
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")
st.markdown("</div>", unsafe_allow_html=True)

# --- 2. THE BOARD ---
st.markdown("""
<div class='v70-board-container'>
    <div class='v70-column'><div class='v70-header'>ARUBA</div><div class='v70-box'><span class='v70-num'>1862</span></div><div class='v70-box'><span class='v70-num'>0801</span></div><div class='v70-box'><span class='v70-num'>9394</span></div></div>
    <div class='v70-column'><div class='v70-header'>BONAIRE</div><div class='v70-box'><span class='v70-num'>2544</span></div><div class='v70-box'><span class='v70-num'>8732</span></div><div class='v70-box'><span class='v70-num'>7296</span></div></div>
    <div class='v70-column'><div class='v70-header'>CURAÇAO</div><div class='v70-box'><span class='v70-num'>7716</span></div><div class='v70-box'><span class='v70-num'>5502</span></div><div class='v70-box'><span class='v70-num'>5918</span></div></div>
    <div class='v70-column'><div class='v70-header'>ST. MARTIN</div><div class='v70-box'><span class='v70-num'>3076</span></div><div class='v70-box'><span class='v70-num'>8561</span></div><div class='v70-box'><span class='v70-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS ---
st.markdown("<h1 style='color:#00FF00; text-align:center; border-bottom: 8px solid #00FF00; width:1100px; margin-bottom:80px;'>MATRIX SENSORS</h1>", unsafe_allow_html=True)

def get_v70_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v70_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v70-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:24px;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v70_grid(get_v70_data(st.session_state.get('v70_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:red; font-weight:900; font-size:30px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v70_r", label_visibility="collapsed")
    st.markdown("<div class='v70-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:24px;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v70_grid(get_v70_data(st.session_state.get('v70_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:#D4AF37; font-weight:900; font-size:30px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:100px;'></div><div class='v70-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:24px;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v70_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:blue; font-weight:900; font-size:30px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v70_b", label_visibility="collapsed")
    st.markdown("<div class='v70-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:24px;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v70_grid([[0]*4 for _ in range(4)], is_dark=True)
