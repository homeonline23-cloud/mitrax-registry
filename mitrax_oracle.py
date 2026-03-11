import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V32 FINAL ALIGNMENT) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V32")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE TITAN BANNER */
    .v32-banner {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 30px auto !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 25px !important;
    }

    /* THE WINNING BOARD */
    .v32-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 10px auto 50px auto !important;
        max-width: 1400px !important;
    }

    /* --- THE V32 ABSOLUTE FIXED CENTER --- */
    .v32-bridge {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
        width: 200px !important;
        margin: -140px auto 0 auto !important; 
        position: relative !important;
        z-index: 9999 !important;
    }

    /* THE GOLDEN PILLAR */
    .v32-pillar { 
        background-color: #D4AF37 !important; 
        width: 28px !important; 
        height: 320px !important; 
        margin-top: 10px !important;
        border-radius: 14px !important;
        border: 3px solid #1A1A1A !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.9) !important;
    }

    /* THE MATRIX SENSORS */
    .v32-cell { 
        font-weight: 900 !important; font-size: 24px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 10px !important; margin: 5px !important; color: #000000 !important; height: 65px !important; width: 65px !important;
        background-color: #D3D3D3 !important;
    }
    
    .red-rabbit-t { border: 6px solid #FF0000 !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    .blue-rabbit-t { border: 6px solid #0000FF !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    
    .v32-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 26px !important; text-transform: uppercase !important; margin-bottom: 30px !important; text-align: center !important; }

    /* FORCED ALIGNMENT FOR INPUT */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }

    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 12px !important;
        width: 180px !important;
    }
    
    input {
        color: #000000 !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        text-align: center !important;
        height: 80px !important;
    }

    .v32-header-bridge { color: #00FF00 !important; font-size: 38px !important; font-weight: 900 !important; border-bottom: 8px solid #00FF00 !important; margin-bottom: 160px !important; text-align: center !important; }
    .v32-spacer { height: 250px !important; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANNER & BOARD ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>MITRAX ORACLE V32</h1>", unsafe_allow_html=True)

st.markdown("<div class='v32-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p style='color:#D4AF37; font-size:32px; font-weight:900;'>{name}</p><p style='color:#00FF00; font-size:52px; font-weight:900;'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='v32-header-bridge'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 3. THE RABBIT ENGINE ---
def get_rabbit_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            grid[0][0] = seed
            grid[0][1] = (seed + 1) % 10
            grid[0][2] = (seed + 2) % 10
            grid[0][3] = (seed + 3) % 10
        except: pass
    return grid

def draw_v32_grid(data, is_dark=False, target_color=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_rabbit = (r == 0 and c == 0 and val != 0)
            target_class = f"{target_color}-rabbit-t" if is_rabbit and target_color else ""
            html = f"<div class='v32-cell' style='background-color:{bg_color}'>"
            if target_class: html += f"<div class='{target_class}'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# --- 4. THE MAIN DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='v32-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_v32_grid(get_rabbit_data(st.session_state.get('v32_r', "")), target_color="red")

with cols[1]:
    st.markdown("<div class='v32-bridge'>", unsafe_allow_html=True)
    st.text_input("RED", value="", max_chars=4, key="v32_r", label_visibility="collapsed")
    st.markdown("<div class='v32-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='v32-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_v32_grid(get_rabbit_data(st.session_state.get('v32_b', "")), target_color="blue")

with cols[4]:
    st.markdown("<p class='v32-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_v32_grid([[0]*4 for _ in range(4)], is_dark=True)

with cols[5]:
    st.markdown("<div class='v32-bridge'>", unsafe_allow_html=True)
    st.text_input("BLUE", value="", max_chars=4, key="v32_b", label_visibility="collapsed")
    st.markdown("<div class='v32-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='v32-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_v32_grid([[0]*4 for _ in range(4)], is_dark=True)

st.markdown("<div class='v32-spacer'></div>", unsafe_allow_html=True)
