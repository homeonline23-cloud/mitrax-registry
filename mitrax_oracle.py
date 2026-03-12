import streamlit as st
import os

# --- 1. ENGINE CONFIG (V108 STABILIZED HORIZON) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V108")

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
    .v108-header-box {
        text-align: center !important;
        width: 100% !important;
        margin-top: -60px !important;
        margin-bottom: 5px !important;
    }
    .v108-title { color: #D4AF37 !important; font-size: 40px !important; font-weight: 900 !important; text-shadow: 4px 4px 8px #000; }
    .v108-worldwide { color: #FFFFFF !important; font-size: 24px !important; font-weight: 700 !important; margin-bottom: 5px; }

    /* WINNING BOARD */
    .v108-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1100px !important; margin: 0 auto !important; 
    }
    .v108-city-card { 
        border: 3px solid #4B6321 !important; background-color: #4B6321 !important; 
        margin: 0 6px !important; padding: 10px !important; width: 230px !important;
        border-radius: 12px;
    }
    .v108-white-num { 
        color: #000 !important; font-family: 'Courier New', monospace; 
        font-size: 38px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center; background: #FFF; margin: 3px 0; border-radius: 6px;
    }

    /* THE LIFTED DATE BAY - CENTERED UNDER BOARD */
    .v108-date-bay {
        display: flex !important;
        justify-content: center !important;
        gap: 60px !important;
        margin-top: 15px !important;
        margin-bottom: 10px !important;
    }
    .v108-date-unit { display: flex; flex-direction: column; align-items: center; width: 130px; }
    .v108-date-label { font-weight: 900 !important; font-size: 18px !important; margin-bottom: 2px; }

    /* MATRIX SENSORS */
    .v108-cell { 
        background-color: #1a1a1a !important; border: 2px solid #00FF00 !important; 
        height: 65px !important; width: 65px !important; display: flex !important; 
        align-items: center !important; justify-content: center !important; 
        font-weight: 900 !important; font-size: 34px !important; color: #00FF00 !important; 
        border-radius: 10px !important; margin: 2px !important;
    }
    
    .v108-pillar-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 40px !important; height: 280px !important; 
        border-radius: 0 0 10px 10px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 0px 15px #D4AF37 !important;
        margin-top: 25px !important;
    }

    /* INPUT STYLING */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 3px solid #00FF00 !important; 
        width: 120px !important; border-radius: 8px !important;
    }
    input { color: #00FF00 !important; font-size: 24px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("""
<div class='v108-header-box'>
    <div class='v108-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v108-worldwide'>Worldwide 🌏 Advantage</div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("""
<div class='v108-board-container'>
    <div class='v108-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v108-white-num'>1862</div><div class='v108-white-num'>0801</div><div class='v108-white-num'>9394</div></div>
    <div class='v108-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v108-white-num'>2544</div><div class='v108-white-num'>8732</div><div class='v108-white-num'>7296</div></div>
    <div class='v108-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v108-white-num'>7716</div><div class='v108-white-num'>5502</div><div class='v108-white-num'>5918</div></div>
    <div class='v108-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v108-white-num'>3076</div><div class='v108-white-num'>8561</div><div class='v108-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

# --- 4. THE LIFTED DATE BAY ---
st.markdown("<div class='v108-date-bay'>", unsafe_allow_html=True)
db_c1, db_c2 = st.columns([1, 1])
with db_c1:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center; margin-left:250px;'><p class='v108-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("71", key="v108_r", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
with db_c2:
    st.markdown("<div style='display:flex; flex-direction:column; align-items:center; margin-right:250px;'><p class='v108-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("83", key="v108_b", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='margin-top:5px; border-bottom:4px solid #00FF00; width:1100px; text-align:center; color:#00FF00; font-weight:900; font-size:24px;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 5. GRID LOGIC ---
def draw_v108_grid(key, active=True):
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
            rows[c].markdown(f"<div class='v108-cell'>{num}</div>", unsafe_allow_html=True)

# --- 6. THE STABILIZED HORIZONTAL ROW ---
main_cols = st.columns([5, 2, 5, 2, 5, 2, 5])
with main_cols[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); draw_v108_grid("v108_r")
with main_cols[1]: st.markdown("<div class='v108-pillar-shaft'></div>", unsafe_allow_html=True)
with main_cols[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); draw_v108_grid("v108_b")
with main_cols[3]: st.markdown("<div class='v108-pillar-shaft' style='background:#D4AF37;'></div><p style='color:#D4AF37; font-weight:900; text-align:center;'>CORE</p>", unsafe_allow_html=True)
with main_cols[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); draw_v108_grid("n", False)
with main_cols[5]: st.markdown("<div class='v108-pillar-shaft'></div>", unsafe_allow_html=True)
with main_cols[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); draw_v108_grid("n", False)
