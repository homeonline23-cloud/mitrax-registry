import streamlit as st
import os

# --- 1. ENGINE CONFIG (V77 SEALED) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V77")

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
        width: 900px !important;
    }
    img {
        border: 3px solid #D4AF37;
        border-radius: 15px;
        width: 900px !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.3);
    }

    /* TRIPLE-STACK BOARD */
    .v77-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1000px !important; 
        margin: 15px auto 40px auto !important; 
    }
    .v77-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v77-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 18px; margin-bottom: 4px; text-transform: uppercase; }
    .v77-box { background-color: #FFFFFF; border: 2px solid #000; margin: 3px 0; padding: 6px; text-align: center; border-radius: 6px; }
    .v77-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 40px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS */
    .v77-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
        box-shadow: 0px 0px 15px rgba(0, 255, 0, 0.2);
    }
    .v77-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 35px; height: 300px; 
        border-radius: 10px; border: 2px solid #000; 
        box-shadow: 0px 0px 25px #D4AF37; 
    }
    .red-t { border: 6px solid #FF0000; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 6px solid #0000FF; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; width: 130px !important; border-radius: 10px !important; }
    input { color: #00FF00 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v77-board-container'>
    <div class='v77-column'><div class='v77-header'>ARUBA</div><div class='v77-box'><span class='v77-num'>1862</span></div><div class='v77-box'><span class='v77-num'>0801</span></div><div class='v77-box'><span class='v77-num'>9394</span></div></div>
    <div class='v77-column'><div class='v77-header'>BONAIRE</div><div class='v77-box'><span class='v77-num'>2544</span></div><div class='v77-box'><span class='v77-num'>8732</span></div><div class='v77-box'><span class='v77-num'>7296</span></div></div>
    <div class='v77-column'><div class='v77-header'>CURAÇAO</div><div class='v77-box'><span class='v77-num'>7716</span></div><div class='v77-box'><span class='v77-num'>5502</span></div><div class='v77-box'><span class='v77-num'>5918</span></div></div>
    <div class='v77-column'><div class='v77-header'>ST. MARTIN</div><div class='v77-box'><span class='v77-num'>3076</span></div><div class='v77-box'><span class='v77-num'>8561</span></div><div class='v77-box'><span class='v77-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS ---
st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1000px; margin-bottom:50px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v77_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v77_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v77-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    draw_v77_grid(get_v77_data(st.session_state.get('v77_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:red; font-weight:900; font-size:22px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v
