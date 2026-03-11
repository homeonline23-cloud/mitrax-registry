import streamlit as st
import os

# --- 1. ENGINE CONFIG (V64 MATTER COMPRESSION) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V64")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    [data-testid="stVerticalBlock"] { align-items: center !important; display: flex !important; flex-direction: column !important; width: 100% !important; }
    
    /* THE CROWN */
    .stImage { display: flex !important; justify-content: center !important; width: 800px !important; margin-bottom: 20px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 800px !important; }

    /* THE HORIZONTAL TRIPLE-STACK BOARD */
    .v64-board-container { 
        display: flex !important; 
        flex-direction: row !important; /* FORCE SIDE-BY-SIDE */
        justify-content: center !important;
        width: 1200px !important; 
        margin: 20px auto !important; 
    }
    .v64-column { 
        border: 2px solid #4B6321; 
        background-color: #4B6321; 
        margin: 0 5px; 
        padding: 8px; 
        width: 280px !important; /* FIXED WIDTH */
        display: flex; 
        flex-direction: column; 
    }
    .v64-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    .v64-box { background-color: #FFFFFF; border: 1px solid #000; margin: 2px 0; padding: 5px; text-align: center; }
    .v64-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 32px !important; font-weight: 900; font-style: italic; }

    /* RESTORED SENSORS & PILLARS */
    .v64-unit { display: flex; flex-direction: column; align-items: center; margin-top: -40px; }
    .v64-pillar { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 22px; height: 240px; border-radius: 10px; border: 2px solid #000; box-shadow: 0px 0px 15px #D4AF37; }
    .v64-spire { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 40px; height: 380px; border-radius: 15px; border: 2px solid #000; box-shadow: 0px 0px 25px #D4AF37; }

    .v64-cell { background-color: #1a1a1a; border: 1px solid #00FF00; height: 55px; width: 55px; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 22px; border-radius: 8px; margin: 3px; color: #00FF00; }
    .red-t { border: 4px solid #FF0000; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 4px solid #0000FF; border-radius: 50%; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 3px solid #00FF00 !important; width: 130px !important; }
    input { color: #00FF00 !important; font-size: 26px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. TRIPLE-STACK BOARD (HORIZONTAL FORCE) ---
st.markdown("""
<div class='v64-board-container'>
    <div class='v64-column'><div class='v64-header'>ARUBA</div><div class='v64-box'><span class='v64-num'>1862</span></div><div class='v64-box'><span class='v64-num'>0801</span></div><div class='v64-box'><span class='v64-num'>9394</span></div></div>
    <div class='v64-column'><div class='v64-header'>BONAIRE</div><div class='v64-box'><span class='v64-num'>2544</span></div><div class='v64-box'><span class='v64-num'>8732</span></div><div class='v64-box'><span class='v64-num'>7296</span></div></div>
    <div class='v64-column'><div class='v64-header'>CURAÇAO</div><div class='v64-box'><span class='v64-num'>7716</span></div><div class='v64-box'><span class='v64-num'>5502</span></div><div class='v64-box'><span class='v64-num'>5918</span></div></div>
    <div class='v64-column'><div class='v64-header'>ST. MARTIN</div><div class='v64-box'><span class='v64-num'>3076</span></div><div class='v64-box'><span class='v64-num'>8561</span></div><div class='v64-box'><span class='v64-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. MATRIX SENSORS ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 4px solid #00FF00; width:1000px; margin-bottom:80px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v64_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v64_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v64-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

m_cols = st.columns([4, 2, 4, 1, 4, 2, 4])
with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v64_grid(get_v64_data(st.session_state.get('v64_r', "")), target="red")
with m_cols[1]:
    st.markdown("<div class='v64-unit'><p style='color:red; font-weight:900;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v64_r", label_visibility="collapsed")
    st.markdown("<div class='v64-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v64_grid(get_v64_data(st.session_state.get('v64_b', "")), target="blue")
with m_cols[3]:
    st.markdown("<div style='height:100px;'></div><div class='v64-spire'></div>", unsafe_allow_html=True)
with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v64_grid([[0]*4 for _ in range(4)], is_dark=True)
with m_cols[5]:
    st.markdown("<div class='v64-unit'><p style='color:blue; font-weight:900;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v64_b", label_visibility="collapsed")
    st.markdown("<div class='v64-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v64_grid([[0]*4 for _ in range(4)], is_dark=True)
