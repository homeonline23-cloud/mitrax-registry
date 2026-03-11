import streamlit as st
import os

# --- 1. ENGINE CONFIG (V73 GIGANTIC COMPACT) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V73")

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
    }
    img {
        border: 6px solid #D4AF37;
        border-radius: 25px;
        width: 1200px !important;
        box-shadow: 0px 0px 70px rgba(212, 175, 55, 0.6);
    }

    /* TRIPLE-STACK BOARD - GIGANTIC */
    .v73-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 100% !important; 
        margin: 40px auto 80px auto !important; 
    }
    .v73-column { 
        border: 8px solid #4B6321; background-color: #4B6321; 
        margin: 0 10px; padding: 30px; width: 420px !important;
        display: flex; flex-direction: column; border-radius: 25px;
    }
    .v73-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 40px; text-transform: uppercase; margin-bottom: 15px; }
    .v73-box { background-color: #FFFFFF; border: 5px solid #000; margin: 10px 0; padding: 25px; text-align: center; border-radius: 15px; }
    .v73-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 85px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS - GIGANTIC COMPACT */
    .v73-cell { 
        background-color: #1a1a1a; border: 6px solid #00FF00; 
        height: 150px; width: 150px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 90px; border-radius: 25px; margin: 10px; color: #00FF00; 
        box-shadow: 0px 0px 40px rgba(0, 255, 0, 0.7);
    }
    .v73-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 100px; height: 600px; 
        border-radius: 25px; border: 6px solid #000; 
        box-shadow: 0px 0px 60px #D4AF37; 
    }
    .red-t { border: 15px solid #FF0000; border-radius: 50%; width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 15px solid #0000FF; border-radius: 50%; width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; }

    /* GIGANTIC INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 10px solid #00FF00 !important; width: 300px !important; border-radius: 25px !important; margin-bottom: 30px !important; }
    input { color: #00FF00 !important; font-size: 80px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v73-board-container'>
    <div class='v73-column'><div class='v73-header'>ARUBA</div><div class='v73-box'><span class='v73-num'>1862</span></div><div class='v73-box'><span class='v73-num'>0801</span></div><div class='v73-box'><span class='v73-num'>9394</span></div></div>
    <div class='v73-column'><div class='v73-header'>BONAIRE</div><div class='v73-box'><span class='v73-num'>2544</span></div><div class='v73-box'><span class='v73-num'>8732</span></div><div class='v73-box'><span class='v73-num'>7296</span></div></div>
    <div class='v73-column'><div class='v73-header'>CURAÇAO</div><div class='v73-box'><span class='v73-num'>7716</span></div><div class='v73-box'><span class='v73-num'>5502</span></div><div class='v73-box'><span class='v73-num'>5918</span></div></div>
    <div class='v73-column'><div class='v73-header'>ST. MARTIN</div><div class='v73-box'><span class='v73-num'>3076</span></div><div class='v73-box'><span class='v73-num'>8561</span></div><div class='v73-box'><span class='v73-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE SENSORS ---
st.markdown("<h1 style='color:#00FF00; text-align:center; border-bottom: 12px solid #00FF00; width:1400px; margin-bottom:100px; font-size:80px;'>MATRIX SENSORS</h1>", unsafe_allow_html=True)

def get_v73_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v73_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v73-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div class='red-t'>{val}</div>"
            elif is_target and target == "blue": html += f"<div class='blue-t'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

s_cols = st.columns([6, 4, 6, 4, 6, 4, 6])

with s_cols[0]:
    draw_v73_grid(get_v73_data(st.session_state.get('v73_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:red; font-weight:900; font-size:50px;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v73_r", label_visibility="collapsed")
    st.markdown("<div class='v73-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    draw_v73_grid(get_v73_data(st.session_state.get('v73_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:#D4AF37; font-weight:900; font-size:50px;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:140px;'></div><div class='v73-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    draw_v73_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center;'><p style='color:blue; font-weight:900; font-size:50px;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v73_b", label_visibility="collapsed")
    st.markdown("<div class='v73-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    draw_v73_grid([[0]*4 for _ in range(4)], is_dark=True)
