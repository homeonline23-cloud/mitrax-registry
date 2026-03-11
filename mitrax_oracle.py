import streamlit as st
import os

# --- 1. ENGINE CONFIG (V93 MOBILE SCROLL) ---
st.set_page_config(layout="centered", page_title="MITRAX MOBILE")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* MOBILE COLUMN FORCE */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN & BOARD (STACKED FOR MOBILE) */
    .mobile-board { 
        display: flex; flex-direction: column; align-items: center; 
        width: 350px; margin-bottom: 40px;
    }
    .v93-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 10px 0; padding: 15px; width: 320px;
        border-radius: 15px;
    }
    .v93-num { 
        color: #000; font-family: 'Courier New', monospace; 
        font-size: 45px; font-weight: 900; font-style: italic; text-align: center;
        background: #FFF; margin: 5px 0; border-radius: 8px;
    }

    /* THE MATRIX CELLS (MOBILE SCALE) */
    .v93-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 80px; width: 80px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 40px; border-radius: 12px; margin: 5px; color: #00FF00; 
    }
    
    /* THE MONOLITH UNIT (CENTERED STACK) */
    .v93-monolith {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; width: 350px !important;
        margin: 40px 0 !important;
    }
    .v93-label { font-weight: 900; font-size: 30px; text-align: center; margin-bottom: 10px; }
    .v93-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 60px; height: 150px; 
        border-radius: 12px; border: 3px solid #000; 
        box-shadow: 0px 0px 30px #D4AF37;
    }

    /* INPUTS - MOBILE FRIENDLY */
    div[data-baseweb="input"] { 
        background-color: #000 !important; border: 5px solid #00FF00 !important; 
        width: 200px !important; border-radius: 15px !important;
    }
    input { color: #00FF00 !important; font-size: 40px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. MOBILE SCROLL CONTENT ---

# THE CROWN
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=350)

# THE BOARD (VERTICAL SWIPE)
st.markdown("<h2 style='color:#D4AF37; text-align:center;'>WINNING BOARD</h2>", unsafe_allow_html=True)
cities = [("ARUBA", "1862", "0801", "9394"), ("BONAIRE", "2544", "8732", "7296"), 
          ("CURAÇAO", "7716", "5502", "5918"), ("ST. MARTIN", "3076", "8561", "3465")]

for city, n1, n2, n3 in cities:
    st.markdown(f"""
    <div class='v93-column'>
        <div style='color:#D4AF37; text-align:center; font-weight:900;'>{city}</div>
        <div class='v93-num'>{n1}</div>
        <div class='v93-num'>{n2}</div>
        <div class='v93-num'>{n3}</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. THE SENSOR SCROLL ---
st.markdown("<hr style='border: 3px solid #00FF00; width: 350px; margin: 50px 0;'>", unsafe_allow_html=True)

def draw_mobile_grid(input_key):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(input_key, "")
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
            style = ""
            if r == 0 and c == 0 and val:
                color = "red" if "r" in input_key else "blue"
                style = f"border:6px solid {color}; border-radius:50%; width:60px; height:60px; display:flex; align-items:center; justify-content:center;"
            cols[c].markdown(f"<div class='v93-cell'><div style='{style}'>{num}</div></div>", unsafe_allow_html=True)

# THE ROLLING STACK
st.markdown("<h2 style='color:#D4AF37;'>GRID 1</h2>", unsafe_allow_html=True)
draw_mobile_grid("v93_r")

st.markdown("<div class='v93-monolith'><p class='v93-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
st.text_input("RED SEED", key="v93_r", label_visibility="collapsed")
st.markdown("<div class='v93-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 2</h2>", unsafe_allow_html=True)
draw_mobile_grid("v93_b")

st.markdown("<div class='v93-monolith'><p class='v93-label' style='color:#D4AF37;'>CORE</p><div class='v93-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 3</h2>", unsafe_allow_html=True)
draw_mobile_grid("none")

st.markdown("<div class='v93-monolith'><p class='v93-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
st.text_input("BLUE SEED", key="v93_b", label_visibility="collapsed")
st.markdown("<div class='v93-pillar'></div></div>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#D4AF37;'>GRID 4</h2>", unsafe_allow_html=True)
draw_mobile_grid("none")
