import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V28 PILLAR RECOVERY) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V28")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE TITAN BANNER */
    .v28-banner {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 30px auto !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 25px !important;
    }

    /* THE WINNING BOARD */
    .v28-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 10px auto 50px auto !important;
        max-width: 1400px !important;
    }

    /* --- THE V28 PILLAR RECOVERY LOCK --- */
    .v28-pillar-unit {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
        justify-content: flex-start !important;
        width: 100% !important;
        margin-top: -130px !important; 
        position: relative !important;
        z-index: 9999 !important; /* MAXIMUM VISIBILITY */
        overflow: visible !important; /* PREVENTS CLIPPING */
    }

    /* THE GOLDEN PILLAR - VISIBILITY ENFORCED */
    .v28-pillar { 
        background-color: #D4AF37 !important; 
        width: 28px !important; 
        height: 320px !important; 
        margin: -5px auto 0 auto !important;
        border-radius: 14px !important;
        border: 3px solid #1A1A1A !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.9) !important;
        display: block !important;
        visibility: visible !important;
    }

    /* THE MATRIX SENSORS */
    .v28-cell { 
        font-weight: 900 !important; font-size: 24px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 10px !important; margin: 5px !important; color: #000000 !important; height: 65px !important; width: 65px !important;
        background-color: #D3D3D3 !important;
    }
    
    .v28-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 26px !important; text-transform: uppercase !important; margin-bottom: 30px !important; text-align: center !important; }

    /* THE ENTRY WINDOWS - V28 PRECISION */
    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 12px !important;
        width: 200px !important;
    }
    
    input {
        color: #000000 !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        text-align: center !important;
        height: 85px !important;
    }

    .v28-bridge { color: #00FF00 !important; font-size: 38px !important; font-weight: 900 !important; border-bottom: 8px solid #00FF00 !important; margin-bottom: 150px !important; text-align: center !important; }
    
    /* SAFETY BUFFER AT BOTTOM */
    .v28-spacer { height: 200px !important; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>MITRAX ORACLE V28</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='v28-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p style='color:#D4AF37; font-size:32px; font-weight:900;'>{name}</p><p style='color:#00FF00; font-size:52px; font-weight:900;'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='v28-bridge'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v28_grid(is_dark=False):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            rows[c].markdown(f"<div class='v28-cell' style='background-color:{bg_color}'>0</div>", unsafe_allow_html=True)

# --- THE MAIN DECK ---
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='v28-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_v28_grid(False)

with cols[1]:
    st.markdown("<div class='v28-pillar-unit'>", unsafe_allow_html=True)
    st.text_input("RED", value="", max_chars=4, key="v28_r", label_visibility="collapsed")
    st.markdown("<div class='v28-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='v28-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_v28_grid(False)

with cols[4]:
    st.markdown("<p class='v28-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_v28_grid(True)

with cols[5]:
    st.markdown("<div class='v28-pillar-unit'>", unsafe_allow_html=True)
    st.text_input("BLUE", value="", max_chars=4, key="v28_b", label_visibility="collapsed")
    st.markdown("<div class='v28-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='v28-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_v28_grid(True)

# THE DEEP SPACE BUFFER
st.markdown("<div class='v28-spacer'></div>", unsafe_allow_html=True)
