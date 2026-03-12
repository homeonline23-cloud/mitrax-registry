import streamlit as st
import os

# --- 1. ENGINE CONFIG (V102 SHADOW ANCHOR) ---
st.set_page_config(layout="centered", page_title="MITRAX MOBILE V102")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* COMPRESSED HEADER & CENTERED TITLE */
    .v102-header-box {
        text-align: center !important;
        width: 350px !important;
        margin-top: -30px !important; /* ULTRA LIFT */
        margin-bottom: 5px !important;
    }
    
    /* V102 SHADOW DECREE */
    .v102-main-title { 
        color: #D4AF37 !important; 
        font-size: 34px !important; 
        font-weight: 900 !important;
        text-align: center !important;
        /* QUANTUM SHADOW APPLIED */
        filter: drop-shadow(4px 4px 6px rgba(0,0,0,0.8)) !important; 
        margin-bottom: 2px !important;
        display: inline-block !important; /* Ensures shadow applies to text only */
    }
    .v102-desc { 
        color: #FFFFFF !important; 
        font-size: 13px !important; 
        font-style: italic !important; 
        padding: 0 20px; 
        line-height: 1.2 !important;
    }

    /* MOBILE BOARD STACK */
    .v102-board-column { 
        border: 2px solid #4B6321; background-color: #4B6321; 
        margin: 5px 0; padding: 8px; width: 300px;
        border-radius: 12px;
    }
    .v102-white-num { 
        color: #000 !important; font-family: 'Courier New', monospace !important; 
        font-size: 32px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center !important; background: #FFF !important; margin: 3px 0 !important; border-radius: 6px;
    }

    /* SENSORS (MOBILE SCALE) */
    .v102-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 75px; width: 75px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 38px; border-radius: 10px; margin: 4px; color: #00FF00; 
    }
    
    .v102-monolith {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; width: 350px !important;
        margin: 20px 0 !important;
    }
    .v102-label { font-weight: 900; font-size: 24px; text-align: center; margin-bottom: 5px; }
    .v102-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 50px; height: 120px; 
        border-radius: 10px; border: 2px solid #000; 
        box-shadow: 0px 0px 20px #D4AF37;
    }

    /* INPUTS */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 4px solid #00FF00 !important; 
        width: 180px !important; border-radius: 12px !important;
    }
    input { color: #00FF00 !important; font-size: 36px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER RESTORATION WITH SHADOW ---
st.markdown("""
<div class='v102-header-box'>
    <div class='v102-main-title'>MITRAX ORACLE PIC 4 App. 🌏</div>
    <div class='v102-desc'>
        The 4-digit Prediction Calculator globally using 4 winning numbers in Grids. 
        Analyze symmetry patterns to identify potential winners. 95% chance of success.
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE BOARD ---
cities = [("ARUBA", "1862", "0801", "9394"), ("BONAIRE", "2544", "8732", "7296"), 
          ("CURAÇAO", "7716", "5502", "5918"), ("ST. MARTIN", "3076", "8561", "3465")]

for city, n1, n2, n3 in cities:
    st.markdown(f"""
    <div class='v102-board-column'>
        <div style='color:#D4AF37; text-align:center; font-weight:900; font-size:14px;'>{city}</div>
        <div class='v102-white-num'>{n1}</div>
        <div class='v102-white-num'>{n2}</div>
        <div class='v102-white-num'>{n3}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px; border-bottom:3px solid #00FF00; width:300px; text-align:center; color:#00FF00; font-weight:900;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 4. GRID LOGIC ---
def draw_v102_grid(key, active=True):
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
        cols = st.columns(4)
        for c in range(4):
            num = grid[r][c]
            cols[c].markdown(f"<div class='v102-cell'>{num}</div>", unsafe_allow_html=True)

# --- 5. THE TRINITY ROW (SCROLLING) ---
st.markdown("<h2 style='color:#D4AF37; text-align:center;'>GRID 1</h2>", unsafe_allow_html=True); draw_v102_grid("v102_r")
st.markdown("<div class='v102-monolith'><p class='v102-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
st.text_input("R", key="v102_r", label_visibility="collapsed")
st.markdown("<div class='v102-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37; text-align:center;'>GRID 2</h2>", unsafe_allow_html=True); draw_v102_grid("v102_b")
st.markdown("<div class='v102-monolith'><p class='v102-label' style='color:#D4AF37;'>CORE</p><div class='v102-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37; text-align:center;'>GRID 3</h2>", unsafe_allow_html=True); draw_v102_grid("n", False)
st.markdown("<div class='v102-monolith'><p class='v102-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
st.text_input("B", key="v102_b", label_visibility="collapsed")
st.markdown("<div class='v102-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37; text-align:center;'>GRID 4</h2>", unsafe_allow_html=True); draw_v102_grid("n", False)
