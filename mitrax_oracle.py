import streamlit as st
import os

# --- 1. ENGINE CONFIG (V106 CENTERED AUTHORITY) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V106")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CENTERED HEADER BOX */
    .v106-header-box {
        text-align: center !important;
        width: 100% !important;
        margin-top: -60px !important;
        margin-bottom: 20px !important;
    }
    
    .v106-title { 
        color: #D4AF37 !important; 
        font-size: 44px !important; 
        font-weight: 900 !important;
        text-shadow: 4px 4px 8px #000000 !important;
        margin-bottom: 5px !important;
    }

    .v106-worldwide {
        color: #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }

    .v106-mission { 
        color: #FFFFFF !important; 
        font-size: 16px !important; 
        font-weight: 600 !important;
        line-height: 1.4 !important;
        max-width: 850px !important;
        margin: 0 auto !important;
        text-align: center !important;
    }

    /* WINNING BOARD */
    .v106-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1100px !important; margin: 0 auto !important; 
    }
    .v106-city-card { 
        border: 3px solid #4B6321 !important; background-color: #4B6321 !important; 
        margin: 0 6px !important; padding: 10px !important; width: 230px !important;
        border-radius: 12px;
    }
    .v106-white-num { 
        color: #000 !important; font-family: 'Courier New', monospace !important; 
        font-size: 38px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center !important; background: #FFF !important; margin: 3px 0 !important; border-radius: 6px;
    }

    /* SENSOR GRID CELLS */
    .v106-cell { 
        background-color: #1a1a1a !important; border: 2px solid #00FF00 !important; 
        height: 70px !important; width: 70px !important; display: flex !important; 
        align-items: center !important; justify-content: center !important; 
        font-weight: 900 !important; font-size: 36px !important; color: #00FF00 !important; 
        border-radius: 10px !important; margin: 3px !important;
    }
    
    /* PILLARS */
    .v106-monolith {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; width: 120px !important; margin-top: 30px !important;
    }
    .v106-label { font-weight: 900 !important; font-size: 18px !important; text-align: center; width: 100%; }
    .v106-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 45px !important; height: 300px !important; 
        border-radius: 0 0 12px 12px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 0px 20px #D4AF37 !important; margin-top: -5px !important;
    }

    /* INPUTS */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 3px solid #00FF00 !important; 
        width: 110px !important; border-radius: 10px 10px 0 0 !important;
    }
    input { color: #00FF00 !important; font-size: 26px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE CENTERED HEADER (V106) ---
st.markdown("""
<div class='v106-header-box'>
    <div class='v106-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v106-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v106-mission'>
        The 4-digit Prediction Calculator that can be used Globally. By entering<br>
        the 4 chosen winning numbers into the calculator Grids. When analyzing<br>
        the symmetry patterns, you can see and identify potential winning<br>
        numbers in the GRID’s. There’s now a 95% chance of increasing your<br>
        chances of winning.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("""
<div class='v106-board-container'>
    <div class='v106-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v106-white-num'>1862</div><div class='v106-white-num'>0801</div><div class='v106-white-num'>9394</div></div>
    <div class='v106-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v106-white-num'>2544</div><div class='v106-white-num'>8732</div><div class='v106-white-num'>7296</div></div>
    <div class='v106-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v106-white-num'>7716</div><div class='v106-white-num'>5502</div><div class='v106-white-num'>5918</div></div>
    <div class='v106-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v106-white-num'>3076</div><div class='v106-white-num'>8561</div><div class='v106-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px; border-bottom:4px solid #00FF00; width:1100px; text-align:center; color:#00FF00; font-weight:900; font-size:24px;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 4. GRID FUNCTION ---
def draw_v106_grid(key, active=True):
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
            rows[c].markdown(f"<div class='v106-cell'>{num}</div>", unsafe_allow_html=True)

# --- 5. THE MATRIX ROW ---
c = st.columns([5, 2, 5, 2, 5, 2, 5])
with c[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); draw_v106_grid("v106_r")
with c[1]:
    st.markdown("<div class='v106-monolith'><p class='v106-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v106_r", label_visibility="collapsed")
    st.markdown("<div class='v106-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); draw_v106_grid("v106_b")
with c[3]:
    st.markdown("<div class='v106-monolith'><p class='v106-label' style='color:#D4AF37;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:40px; width:110px; background:#111; border:3px solid #D4AF37; border-radius:10px 10px 0 0;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='v106-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); draw_v106_grid("n", False)
with c[5]:
    st.markdown("<div class='v106-monolith'><p class='v106-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v106_b", label_visibility="collapsed")
    st.markdown("<div class='v106-gold-shaft'></div></div>", unsafe_allow_html=True)
with c[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); draw_v106_grid("n", False)
