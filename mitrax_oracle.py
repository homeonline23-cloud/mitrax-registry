import streamlit as st
import os

# --- 1. ENGINE CONFIG (V69 GALACTIC-TITAN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V69")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE ABSOLUTE CENTER FORCE */
    .main .block-container {
        max-width: 95% !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }

    /* THE CROWN (TOP IMAGE - MASSIVE) */
    .stImage { display: flex !important; justify-content: center !important; width: 1200px !important; margin-bottom: 40px !important; }
    img { border: 6px solid #D4AF37; border-radius: 25px; width: 1200px !important; box-shadow: 0px 0px 50px rgba(212, 175, 55, 0.3); }

    /* TRIPLE-STACK BOARD (TITAN SCALE) */
    .v69-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1400px !important; 
        margin: 20px auto 60px auto !important; 
    }
    .v69-column { 
        border: 5px solid #4B6321; background-color: #4B6321; 
        margin: 0 12px; padding: 20px; width: 340px !important;
        display: flex; flex-direction: column; border-radius: 15px;
    }
    .v69-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 30px; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 2px; }
    .v69-box { background-color: #FFFFFF; border: 4px solid #000; margin: 6px 0; padding: 15px; text-align: center; border-radius: 10px; }
    .v69-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 65px !important; font-weight: 900; font-style: italic; }

    /* THE SENSOR DECK (TITAN CONSOLIDATED) */
    .v69-unit { display: flex; flex-direction: column; align-items: center; width: 100% !important; }
    .v69-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 70px; height: 450px; 
        border-radius: 15px; border: 4px solid #000; 
        box-shadow: 0px 0px 50px #D4AF37; 
    }

    /* TITAN GRID CELLS (GALACTIC SCALE) */
    .v69-cell { 
        background-color: #1a1a1a; border: 4px solid #00FF00; 
        height: 110px; width: 110px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 55px; border-radius: 18px; margin: 8px; color: #00FF00; 
        box-shadow: 0px 0px 25px rgba(0, 255, 0, 0.5);
    }
    .red-t { border: 10px solid #FF0000; border-radius: 50%; width: 90px; height: 90px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 10px solid #0000FF; border-radius: 50%; width: 90px; height: 90px; display: flex; align-items: center; justify-content: center; }

    /* TITAN INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 8px solid #00FF00 !important; width: 220px !important; margin-bottom: 20px !important; border-radius: 15px !important; }
    input { color: #00FF00 !important; font-size: 50px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE TITAN BOARD ---
st.markdown("""
<div class='v69-board-container'>
    <div class='v69-column'><div class='v69-header'>ARUBA</div><div class='v69-box'><span class='v69-num'>1862</span></div><div class='v69-box'><span class='v69-num'>0801</span></div><div class='v69-box'><span class='v69-num'>9394</span></div></div>
    <div class='v69-column'><div class='v69-header'>BONAIRE</div><div class='v69-box'><span class='v69-num'>2544</span></div><div class='v69-box'><span class='v69-num'>8732</span></div><div class='v69-box'><span class='v69-num'>7296</span></div></div>
    <div class='v69-column'><div class='v69-header'>CURAÇAO</div><div class='v69-box'><span class='v69-num'>7716</span></div><div class='v69-box'><span class='v69-num'>5502</span></div><div class='v69-box'><span class='v69-num'>5918</span></div></div>
    <div class='v69-column'><div class='v69-header'>ST. MARTIN</div><div class='v69-box'><span class='v69-num'>3076</span></div><div class='v69-box'><span class='v69-num'>8561</span></div><div class='v69-box'><span class='v69-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS (GALACTIC SCALE) ---
st.markdown("<h1 style='color:#00FF00; text-align:center; border-bottom: 8px solid #00FF00; width:1300px; margin-bottom:80px;'>MATRIX SENSORS</h1>", unsafe_allow_html=True)

def get_v69_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v69_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v69-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# TITAN SENSOR ROW
s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v69_grid(get_v69_data(st.session_state.get('v69_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div class='v69-unit'><p style='color:red; font-weight:900; font-size:35px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v69_r", label_visibility="collapsed")
    st.markdown("<div class='v69-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v69_grid(get_v69_data(st.session_state.get('v69_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div class='v69-unit'><p style='color:#D4AF37; font-weight:900; font-size:35px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:110px;'></div><div class='v69-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v69_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div class='v69-unit'><p style='color:blue; font-weight:900; font-size:35px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v69_b", label_visibility="collapsed")
    st.markdown("<div class='v69-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:30px;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v69_grid([[0]*4 for _ in range(4)], is_dark=True)
