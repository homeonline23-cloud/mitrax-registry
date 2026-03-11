import streamlit as st
import os

# --- 1. ENGINE CONFIG (V92 CENTRAL ANCHOR) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V92")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN & BOARD */
    .stImage { display: flex !important; justify-content: center !important; width: 900px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 900px !important; }

    .v92-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1000px !important; margin: 0 auto !important; 
    }
    .v92-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v92-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 38px !important; font-weight: 900; font-style: italic; text-align: center;}

    /* THE SENSOR DECK - TOTAL CENTER LOCK */
    .v92-sensor-deck {
        margin-top: 150px !important;
        width: 1100px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }

    .v92-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
    }
    
    /* THE MONOLITH UNIT - FORCED CENTER */
    .v92-monolith {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 140px !important;
        margin-top: 35px !important;
    }
    
    .v92-label { font-weight: 900; font-size: 20px; text-align: center; margin-bottom: 5px !important; width: 100%; }
    
    .v92-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 45px; height: 280px; 
        border-radius: 0 0 12px 12px; border: 2px solid #000; 
        box-shadow: 0px 0px 25px #D4AF37;
        margin-top: -5px !important;
    }

    /* INPUTS - NO DRIFT */
    div[data-baseweb="input"] { 
        background-color: #000 !important; 
        border: 4px solid #00FF00 !important; 
        width: 130px !important; 
        border-radius: 10px 10px 0 0 !important;
        margin: 0 auto !important;
    }
    input { color: #00FF00 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. CROWN & BOARD ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

st.markdown("""
<div class='v92-board-container'>
    <div class='v92-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v92-num'>1862</div><div class='v92-num'>0801</div><div class='v92-num'>9394</div></div></div>
    <div class='v92-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v92-num'>2544</div><div class='v92-num'>8732</div><div class='v92-num'>7296</div></div></div>
    <div class='v92-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v92-num'>7716</div><div class='v92-num'>5502</div><div class='v92-num'>5918</div></div></div>
    <div class='v92-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v92-num'>3076</div><div class='v92-num'>8561</div><div class='v92-num'>3465</div></div></div>
</div>
""", unsafe_allow_html=True)

# --- 3. SENSOR DECK ---
st.markdown("<div class='v92-sensor-deck'><h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1000px; margin-bottom:20px;'>MATRIX SENSORS</h2></div>", unsafe_allow_html=True)

def draw_v92_grid(input_key, is_active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(input_key, "") if is_active else ""
    if val:
        try:
            s = int(val[0])
            for c in range(4): grid[0][c] = (s + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            num = grid[r][c]
            style = ""
            if r == 0 and c == 0 and val:
                color = "red" if "r" in input_key else "blue"
                style = f"border:6px solid {color}; border-radius:50%; width:55px; height:55px; display:flex; align-items:center; justify-content:center;"
            rows[c].markdown(f"<div class='v92-cell'><div style='{style}'>{num}</div></div>", unsafe_allow_html=True)

# THE TRINITY LOCK COLUMN SYSTEM
s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v92_grid("v92_r")
with s_cols[1]:
    st.markdown("<div class='v92-monolith'><p class='v92-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v92_r", label_visibility="collapsed")
    st.markdown("<div class='v92-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v92_grid("v92_b")
with s_cols[3]:
    st.markdown("<div class='v92-monolith'><p class='v92-label' style='color:#D4AF37;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:46px; width:130px; background:#111; border:4px solid #D4AF37; border-radius:10px 10px 0 0;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='v92-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v92_grid("none", is_active=False)
with s_cols[5]:
    st.markdown("<div class='v92-monolith'><p class='v92-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v92_b", label_visibility="collapsed")
    st.markdown("<div class='v92-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v92_grid("none", is_active=False)
