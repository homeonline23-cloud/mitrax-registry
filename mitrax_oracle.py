import streamlit as st
import os

# --- 1. ENGINE CONFIG (V103 MOBILE FUSION) ---
st.set_page_config(layout="centered", page_title="MITRAX MOBILE V103")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* V103 CENTERED TITLE WITH SHADOW */
    .v103-header-container {
        text-align: center !important;
        width: 100% !important;
        margin-top: -50px !important;
        margin-bottom: 10px !important;
    }
    .v103-main-title { 
        color: #D4AF37 !important; 
        font-size: 28px !important; 
        font-weight: 900 !important;
        text-align: center !important;
        text-shadow: 3px 3px 5px #000000, 0px 0px 10px rgba(212, 175, 55, 0.3) !important;
        width: 100% !important;
        display: block !important;
    }
    .v103-desc { 
        color: #FFFFFF !important; 
        font-size: 13px !important; 
        font-style: italic !important; 
        line-height: 1.2 !important;
        max-width: 320px;
        margin: 0 auto !important;
    }

    /* BOARD STACK */
    .v103-city-box { 
        border: 2px solid #4B6321; background-color: #4B6321; 
        margin: 4px 0; padding: 6px; width: 300px;
        border-radius: 12px;
    }
    .v103-num-row { 
        color: #000 !important; font-family: 'Courier New', monospace !important; 
        font-size: 30px !important; font-weight: 900 !important; font-style: italic !important; 
        text-align: center !important; background: #FFF !important; margin: 2px 0 !important; border-radius: 6px;
    }

    /* SENSOR CELLS */
    .v103-sensor-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
    }
    
    /* THE UNBREAKABLE PILLAR UNIT */
    .v103-monolith {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; width: 100% !important;
        margin: 25px 0 !important;
    }
    .v103-label { font-weight: 900; font-size: 22px; text-align: center; margin-bottom: 5px; width: 100%; }
    .v103-pillar-gold { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 50px; height: 130px; 
        border-radius: 0 0 10px 10px; border: 2px solid #000; 
        box-shadow: 0px 0px 20px #D4AF37;
    }

    /* INPUT LOCK - CENTERED OVER PILLAR */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 4px solid #00FF00 !important; 
        width: 150px !important; border-radius: 12px 12px 0 0 !important; margin: 0 auto !important;
    }
    input { color: #00FF00 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE PURIFIED HEADER ---
st.markdown("""
<div class='v103-header-container'>
    <div class='v103-main-title'>MITRAX ORACLE PIC 4 App. 🌏</div>
    <div class='v103-desc'>
        "The 4-digit Prediction Calculator used Globally. Symmetry patterns identify potential winning numbers in the GRID’s. 95% chance of success."
    </div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
cities = [("ARUBA", "1862", "0801", "9394"), ("BONAIRE", "2544", "8732", "7296"), 
          ("CURAÇAO", "7716", "5502", "5918"), ("ST. MARTIN", "3076", "8561", "3465")]

for city, n1, n2, n3 in cities:
    st.markdown(f"""
    <div class='v103-city-box'>
        <div style='color:#D4AF37; text-align:center; font-weight:900; font-size:14px;'>{city}</div>
        <div class='v103-num-row'>{n1}</div>
        <div class='v103-num-row'>{n2}</div>
        <div class='v103-num-row'>{n3}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. THE MATRIX STACK ---
def draw_v103_grid(key, active=True):
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
            cols[c].markdown(f"<div class='v103-sensor-cell'>{num}</div>", unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #00FF00; width: 300px; margin: 30px 0;'>", unsafe_allow_html=True)

# ROLLING DISPLAY
st.markdown("<h2 style='color:#D4AF37;'>GRID 1</h2>", unsafe_allow_html=True); draw_v103_grid("v103_r")
st.markdown("<div class='v103-monolith'><p class='v103-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
st.text_input("RED", key="v103_r", label_visibility="collapsed")
st.markdown("<div class='v103-pillar-gold'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 2</h2>", unsafe_allow_html=True); draw_v103_grid("v103_b")
st.markdown("<div class='v103-monolith'><p class='v103-label' style='color:#D4AF37;'>CORE</p><div class='v103-pillar-gold'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 3</h2>", unsafe_allow_html=True); draw_v101_grid("n", False)
st.markdown("<div class='v103-monolith'><p class='v103-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
st.text_input("BLUE", key="v103_b", label_visibility="collapsed")
st.markdown("<div class='v103-pillar-gold'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 4</h2>", unsafe_allow_html=True); draw_v101_grid("n", False)
