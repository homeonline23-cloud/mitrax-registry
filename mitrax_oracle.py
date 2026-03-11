import streamlit as st
import os

# --- 1. ENGINE CONFIG (V85 MONOLITHIC LOCKDOWN) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V85")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN */
    .stImage { display: flex !important; justify-content: center !important; width: 900px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 900px !important; }

    /* TRIPLE-STACK BOARD */
    .v85-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1000px !important; margin: 10px auto 30px auto !important; 
    }
    .v85-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v85-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 38px !important; font-weight: 900; font-style: italic; text-align: center;}

    /* MATRIX SENSORS */
    .v85-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
    }
    
    /* THE MONOLITH PILLAR UNITS - NO SIDE DRIFT */
    .v85-unit-wrapper {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        margin-top: 35px !important;
        width: 100% !important;
    }
    .v85-label { font-weight: 900; font-size: 22px; margin-bottom: 5px !important; text-align: center; }
    
    .v85-pillar-graphic { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 45px; height: 300px; 
        border-radius: 0 0 10px 10px; border: 2px solid #000; 
        box-shadow: 0px 0px 25px #D4AF37;
        margin-top: -5px !important;
    }

    /* INPUTS - FORCED CENTER OVER PILLAR */
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

# --- 2. THE BOARD ---
st.markdown("""
<div class='v85-board-container'>
    <div class='v85-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v85-num'>1862</div><div class='v85-num'>0801</div><div class='v85-num'>9394</div></div></div>
    <div class='v85-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v85-num'>2544</div><div class='v85-num'>8732</div><div class='v85-num'>7296</div></div></div>
    <div class='v85-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v85-num'>7716</div><div class='v85-num'>5502</div><div class='v85-num'>5918</div></div></div>
    <div class='v85-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v85-num'>3076</div><div class='v85-num'>1234</div><div class='v85-num'>3465</div></div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1000px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def draw_v85_grid(input_key, is_active=True):
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
            rows[c].markdown(f"<div class='v85-cell'><div style='{style}'>{num}</div></div>", unsafe_allow_html=True)

# THE CONSOLIDATED SENSOR ROW
s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v85_grid("v85_r")
with s_cols[1]:
    st.markdown("<div class='v85-unit-wrapper'><p class='v85-label' style='color:red;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v85_r", label_visibility="collapsed")
    st.markdown("<div class='v85-pillar-graphic'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v85_grid("v85_b")
with s_cols[3]:
    st.markdown("<div class='v85-unit-wrapper'><p class='v85-label' style='color:#D4AF37;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:48px; width:130px; background:#111; border:4px solid #D4AF37; border-radius:10px 10px 0 0;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='v85-pillar-graphic'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v85_grid("none", is_active=False)
with s_cols[5]:
    st.markdown("<div class='v85-unit-wrapper'><p class='v85-label' style='color:blue;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v85_b", label_visibility="collapsed")
    st.markdown("<div class='v85-pillar-graphic'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v85_grid("none", is_active=False)
