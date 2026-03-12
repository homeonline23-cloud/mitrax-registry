import streamlit as st
import os

# --- 1. ENGINE CONFIG (V109 BALANCED SCALE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V109")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* CENTERED HEADER */
    .v109-header-box {
        text-align: center !important;
        width: 1000px !important;
        margin-top: -65px !important;
    }
    .v109-title { color: #D4AF37 !important; font-size: 38px !important; font-weight: 900 !important; text-shadow: 4px 4px 8px #000; }
    .v109-worldwide { color: #FFFFFF !important; font-size: 22px !important; font-weight: 700 !important; margin-bottom: 5px; }

    /* SHRUNKEN WINNING BOARD */
    .v109-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 900px !important; margin: 0 auto !important; 
    }
    .v109-city-card { 
        border: 2px solid #4B6321 !important; background-color: #4B6321 !important; 
        margin: 0 4px !important; padding: 6px !important; width: 200px !important;
        border-radius: 10px;
    }
    .v109-white-num { 
        color: #000 !important; font-family: 'Courier New', monospace; 
        font-size: 28px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center; background: #FFF; margin: 2px 0; border-radius: 4px;
    }

    /* ENLARGED DATE INPUTS (THE LIFTED BAY) */
    .v109-date-bay {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 1000px !important;
        margin-top: 25px !important;
        margin-bottom: 20px !important;
    }
    .v109-date-unit { display: flex; flex-direction: column; align-items: center; width: 220px !important; }
    .v109-date-label { font-weight: 900 !important; font-size: 32px !important; margin-bottom: 8px !important; }

    /* MATRIX SENSORS */
    .v109-cell { 
        background-color: #1a1a1a !important; border: 2px solid #00FF00 !important; 
        height: 65px !important; width: 65px !important; display: flex !important; 
        align-items: center !important; justify-content: center !important; 
        font-weight: 900 !important; font-size: 34px !important; color: #00FF00 !important; 
        border-radius: 10px !important; margin: 2px !important;
    }
    
    .v109-pillar-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 40px !important; height: 280px !important; 
        border-radius: 0 0 10px 10px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 0px 15px #D4AF37 !important;
        margin-top: 25px !important;
    }

    /* LARGE INPUT BOXES */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 5px solid #00FF00 !important; 
        width: 180px !important; border-radius: 12px !important;
    }
    input { color: #00FF00 !important; font-size: 40px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("""
<div class='v109-header-box'>
    <div class='v109-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v109-worldwide'>Worldwide 🌏 Advantage</div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD (SHRUNKEN) ---
st.markdown("""
<div class='v109-board-container'>
    <div class='v109-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v109-white-num'>1862</div><div class='v109-white-num'>0801</div><div class='v109-white-num'>9394</div></div>
    <div class='v109-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v109-white-num'>2544</div><div class='v109-white-num'>8732</div><div class='v109-white-num'>7296</div></div>
    <div class='v109-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v109-white-num'>7716</div><div class='v109-white-num'>5502</div><div class='v109-white-num'>5918</div></div>
    <div class='v109-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v109-white-num'>3076</div><div class='v109-white-num'>8561</div><div class='v109-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

# --- 4. THE LARGE DATE BAY ---
db_c1, db_c2, db_c3 = st.columns([2, 1, 2])
with db_c1:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:flex-end; padding-right:50px;'><p class='v109-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("71", key="v109_r", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
with db_c3:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:flex-start; padding-left:50px;'><p class='v109-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("83", key="v109_b", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='margin-top:10px; border-bottom:4px solid #00FF00; width:1100px; text-align:center; color:#00FF00; font-weight:900; font-size:24px;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 5. GRID LOGIC ---
def draw_v109_grid(key, active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(key, "") if active else ""
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
            rows[c].markdown(f"<div class='v109-cell'>{num}</div>", unsafe_allow_html=True)

# --- 6. THE STABILIZED HORIZONTAL ROW ---
main_cols = st.columns([5, 2, 5, 2, 5, 2, 5])
with main_cols[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); draw_v109_grid("v109_r")
with main_cols[1]: st.markdown("<div class='v109-pillar-shaft'></div>", unsafe_allow_html=True)
with main_cols[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); draw_v109_grid("v109_b")
with main_cols[3]: st.markdown("<div class='v109-pillar-shaft' style='background:#D4AF37;'></div><p style='color:#D4AF37; font-weight:900; text-align:center;'>CORE</p>", unsafe_allow_html=True)
with main_cols[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); draw_v109_grid("n", False)
with main_cols[5]: st.markdown("<div class='v109-pillar-shaft'></div>", unsafe_allow_html=True)
with main_cols[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); draw_v109_grid("n", False)
