import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V26 ATOMIC ALIGNMENT) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V26")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE TITAN BANNER */
    .v26-banner {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 30px auto !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 25px !important;
    }

    /* THE WINNING BOARD */
    .v26-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 10px auto 50px auto !important;
        max-width: 1400px !important;
    }

    /* --- THE V26 ATOMIC CENTER LOCK --- */
    /* This forces the container to IGNORE internal alignment and stay DEAD CENTER */
    .v26-center-lock {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        width: 100% !important;
        margin: -120px auto 0 auto !important; 
        position: relative !important;
        z-index: 999 !important;
    }

    /* THE GOLDEN PILLARS - TOTAL RE-CENTERING */
    .v26-pillar { 
        background-color: #D4AF37 !important; 
        width: 24px !important; 
        height: 280px !important; 
        margin: 10px auto 0 auto !important; /* FORCED AUTO MARGIN */
        border-radius: 12px !important;
        border: 2px solid #000000 !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.8) !important;
        display: block !important;
    }

    /* THE MATRIX SENSORS */
    .v26-cell { 
        font-weight: 900 !important; font-size: 24px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 10px !important; margin: 5px !important; color: #000000 !important; height: 65px !important; width: 65px !important;
        background-color: #D3D3D3 !important;
    }
    
    .v26-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 24px !important; text-transform: uppercase !important; margin-bottom: 25px !important; text-align: center !important; }

    /* THE ENTRY WINDOWS - FORCED CENTER */
    .stTextInput {
        width: 200px !important;
        margin: 0 auto !important;
    }
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 5px solid #D4AF37 !important; font-size: 32px !important; 
        text-align: center !important; height: 80px !important; width: 200px !important;
        font-weight: 900 !important;
    }
    .v26-bridge { color: #00FF00 !important; font-size: 36px !important; font-weight: 900 !important; border-bottom: 8px solid #00FF00 !important; margin-bottom: 140px !important; text-align: center !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN IMAGE ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>MITRAX ORACLE V26</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='v26-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p style='color:#D4AF37; font-size:30px; font-weight:900;'>{name}</p><p style='color:#00FF00; font-size:48px; font-weight:900;'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='v26-bridge'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

def draw_v26_grid(is_dark=False):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            rows[c].markdown(f"<div class='v26-cell' style='background-color:{bg_color}'>0</div>", unsafe_allow_html=True)

# --- THE MAIN DECK ---
# Using 7 columns to separate the units
cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='v26-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_v26_grid(False)

with cols[1]:
    # THE ATOMIC CENTER LOCK
    st.markdown("<div class='v26-center-lock'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v26_r", label_visibility="collapsed")
    st.markdown("<div class='v26-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='v26-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_v26_grid(False)

with cols[4]:
    st.markdown("<p class='v26-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_v26_grid(True)

with cols[5]:
    st.markdown("<div class='v26-center-lock'>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v26_b", label_visibility="collapsed")
    st.markdown("<div class='v26-pillar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='v26-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_v26_grid(True)
