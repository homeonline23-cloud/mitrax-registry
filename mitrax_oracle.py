import streamlit as st
import os

# --- 1. ENGINE CONFIG (V101 CACHE-BREAKER) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V101")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* FORCED HEADER LIFT */
    .v101-header-box {
        text-align: center !important;
        width: 1000px !important;
        margin-top: -60px !important; /* ULTRA LIFT */
        margin-bottom: 5px !important;
    }
    .v101-main-title { color: #D4AF37 !important; font-size: 36px !important; font-weight: 900 !important; }
    .v101-desc { color: #FFFFFF !important; font-size: 15px !important; font-style: italic !important; padding: 0 20px; }

    /* BOARD STABILITY */
    .v101-board-row { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1000px !important; margin: 0 auto !important; 
    }
    .v101-city-card { 
        border: 3px solid #4B6321 !important; background-color: #4B6321 !important; 
        margin: 0 5px !important; padding: 8px !important; width: 225px !important;
        display: flex; flex-direction: column; border-radius: 12px;
    }
    .v101-white-num { 
        color: #000 !important; font-family: 'Courier New', monospace !important; 
        font-size: 34px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center !important; background: #FFF !important; margin: 2px 0 !important; border-radius: 5px;
    }

    /* THE SENSOR HORIZON */
    .v101-sensor-container {
        margin-top: 30px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }

    .v101-matrix-cell { 
        background-color: #1a1a1a !important; border: 2px solid #00FF00 !important; 
        height: 65px !important; width: 65px !important; display: flex !important; 
        align-items: center !important; justify-content: center !important; 
        font-weight: 900 !important; font-size: 34px !important; border-radius: 10px !important; 
        margin: 2px !important; color: #00FF00 !important; 
    }
    
    /* THE FUSED PILLAR MONOLITH */
    .v101-pillar-unit {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; width: 120px !important;
        margin-top: 35px !important;
    }
    .v101-pillar-label { font-weight: 900 !important; font-size: 16px !important; margin-bottom: 2px !important; }
    .v101-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 40px !important; height: 280px !important; 
        border-radius: 0 0 10px 10px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 0px 15px #D4AF37 !important; margin-top: -5px !important;
    }

    /* INPUT LOCK */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 3px solid #00FF00 !important; 
        width: 110px !important; border-radius: 8px 8px 0 0 !important; margin: 0 auto !important;
    }
    input { color: #00FF00 !important; font-size: 24px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER RESTORATION ---
st.markdown("""
<div class='v101-header-box'>
    <div class='v101-main-title'>MITRAX ORACLE PIC 4 App. 🌏</div>
    <div class='v101-desc'>
        The 4-digit Prediction Calculator globally using 4 winning numbers in Grids. 
        Analyze symmetry patterns to identify potential winners. 95% chance of success.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v101-board-row'>
    <div class='v101-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v101-white-num'>1862</div><div class='v101-white-num'>0801</div><div class='v101-white-num'>9394</div></div>
    <div class='v101-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v101-white-num'>2544</div><div class='v101-white-num'>8732</div><div class='v101-white-num'>7296</div></div>
    <div class='v101-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v101-white-num'>7716</div><div class='v101-white-num'>5502</div><div class='v101-white-num'>5918</div></div>
    <div class='v101-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v101-white-num'>3076</div><div class='v101-white-num'>8561</div><div class='v101-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px; border-bottom:3px solid #00FF00; width:1000px; text-align:center; color:#00FF00; font-weight:900;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 4. GRID LOGIC ---
def draw_v101_grid(key, active=True):
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
            circ = f"border:4px solid {'red' if 'r' in key else 'blue'}; border-radius:50%; width:45px; height:45px; display:flex; align-items:center; justify-content:center;" if r==0 and c==0 and val else ""
            rows[c].markdown(f"<div class='v101-matrix-cell'><div style='{circ}'>{num}</div></div>", unsafe_allow_html=True)

# --- 5. THE TRINITY ROW ---
c = st.columns([5, 2, 5, 2, 5, 2, 5])
with c[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); draw_v101_grid("v101_r")
with c[1]:
    st.markdown("<div class='v101-pillar-unit'><p class='v101-pillar-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v101_r", label_visibility="collapsed")
    st.markdown("<div class='v101-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); draw_v101_grid("v101_b")
with c[3]:
    st.markdown("<div class='v101-pillar-unit'><p class='v101-pillar-label' style='color:#D4AF37;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:38px; width:110px; background:#111; border:3px solid #D4AF37; border-radius:8px 8px 0 0;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='v101-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); draw_v101_grid("n", False)
with c[5]:
    st.markdown("<div class='v101-pillar-unit'><p class='v101-pillar-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v101_b", label_visibility="collapsed")
    st.markdown("<div class='v101-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); draw_v101_grid("n", False)
