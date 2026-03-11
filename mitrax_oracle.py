import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V25 TOTAL RESET) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V25")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE TITAN BANNER - V25 RESET */
    .v25-banner {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 30px auto !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 25px !important;
    }

    /* THE WINNING BOARD - V25 */
    .v25-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 10px auto 50px auto !important;
        max-width: 1400px !important;
    }
    .v25-island { color: #D4AF37 !important; font-size: 30px !important; font-weight: 900 !important; }
    .v25-num { color: #00FF00 !important; font-size: 48px !important; font-weight: 900 !important; }

    /* --- THE V25 ABSOLUTE CENTER-LOCK --- */
    .v25-center-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        margin-top: -110px !important; /* LIFTED */
        position: relative !important;
        z-index: 999 !important;
    }

    /* THE GOLDEN PILLARS - V25 LOCK */
    .v25-pillar { 
        background-color: #D4AF37 !important; 
        width: 24px !important; 
        height: 260px !important; 
        margin: 10px auto 0 auto !important; /* FORCED AUTO MARGIN FOR CENTER */
        border-radius: 12px !important;
        border: 2px solid #000000 !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.8) !important;
    }

    /* THE MATRIX SENSORS (GRIDS) */
    .v25-cell { 
        font-weight: 900 !important; font-size: 24px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 10px !important; margin: 5px !important; color: #000000 !important; height: 65px !important; width: 65px !important;
        background-color: #D3D3D3 !important;
    }
    .v25-red-t { border: 6px solid #FF0000 !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    .v25-blue-t { border: 6px solid #0000FF !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    
    .v25-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 24px !important; text-transform: uppercase !important; margin-bottom: 25px !important; text-align: center !important; }

    /* THE ENTRY WINDOWS - V25 */
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 5px solid #D4AF37 !important; font-size: 32px !important; 
        text-align: center !important; height: 80px !important; width: 200px !important;
        font-weight: 900 !important;
        margin: 0 auto !important;
    }
    .v25-bridge { color: #00FF00 !important; font-size: 36px !important; font-weight: 900 !important; border-bottom: 8px solid #00FF00 !important; margin-bottom: 120px !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE (V25 FORCE) ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37;'>MITRAX ORACLE V25</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='v25-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='v24-island'>{name}</p><p class='v24-num'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<div class='v25-bridge'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v25_grid(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            is_start = (r == 0 and c == 0 and val != "")
            circle = f"v25-{target}-t" if is_start and target else ""
            txt = val if is_start else "0"
            html = f"<div class='v25-cell' style='background-color:{bg_color}'>"
            if circle: html += f"<div class='{circle}'>{txt}</div>"
            else: html += f"{txt}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

# --- THE V25 TITAN MAIN DECK ---
# New Ratio to force space: 3 (Grid) - 2 (Pillar) - 3 (Grid) - 1 (Gap) - 3 (Grid) - 2 (Pillar) - 3 (Grid)
cols = st.columns([3, 2, 3, 1, 3, 2, 3])

with cols[0]:
    st.markdown("<p class='v25-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_v25_grid(st.session_state.get('v25_r', ""), target="red")

with cols[1]:
    # THE V25 ABSOLUTE CENTER-LOCK
    st.markdown("<div class='v25-center-container'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v25_r", label_visibility="collapsed")
    st.markdown("<div class='v25-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='v25-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_v25_grid(st.session_state.get('v25_b', ""), target="blue")

with cols[4]:
    st.markdown("<p class='v25-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_v25_grid("", is_dark=True)

with cols[5]:
    st.markdown("<div class='v25-center-container'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v25_b", label_visibility="collapsed")
    st.markdown("<div class='v25-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='v25-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_v25_grid("", is_dark=True)
