import streamlit as st
import os

# --- 1. THE IMPERIAL ENGINE CONFIG (V31 FIXED-AXIS) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V31")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }

    /* THE TITAN BANNER */
    .v31-banner {
        width: 1500px !important; 
        max-width: 100% !important;
        display: block;
        margin: 0 auto 30px auto !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 25px !important;
    }

    /* THE WINNING BOARD */
    .v31-board {
        background: rgba(212, 175, 55, 0.1) !important;
        border: 4px solid #D4AF37 !important;
        border-radius: 20px !important;
        padding: 30px !important;
        margin: 10px auto 50px auto !important;
        max-width: 1400px !important;
    }

    /* --- THE V31 FIXED CORRIDOR LOCK --- */
    /* This forces a narrow 200px container that CANNOT be misaligned */
    .v31-corridor {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
        width: 200px !important;
        margin: -140px auto 0 auto !important; 
        position: relative !important;
        z-index: 9999 !important;
    }

    /* THE GOLDEN PILLAR - LOCKED IN CORRIDOR */
    .v31-pillar { 
        background-color: #D4AF37 !important; 
        width: 28px !important; 
        height: 320px !important; 
        margin-top: 10px !important;
        border-radius: 14px !important;
        border: 3px solid #1A1A1A !important;
        box-shadow: 0px 0px 40px rgba(212, 175, 55, 0.9) !important;
    }

    /* THE MATRIX SENSORS */
    .v31-cell { 
        font-weight: 900 !important; font-size: 24px !important; border: 1px solid #000000 !important; 
        aspect-ratio: 1/1 !important; display: flex !important; align-items: center !important; justify-content: center !important; 
        border-radius: 10px !important; margin: 5px !important; color: #000000 !important; height: 65px !important; width: 65px !important;
        background-color: #D3D3D3 !important;
    }
    
    .red-rabbit-t { border: 6px solid #FF0000 !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    .blue-rabbit-t { border: 6px solid #0000FF !important; border-radius: 50% !important; width: 55px !important; height: 55px !important; display: flex !important; align-items: center !important; justify-content: center !important; }
    
    .v31-label { color: #D4AF37 !important; font-weight: 900 !important; font-size: 26px !important; text-transform: uppercase !important; margin-bottom: 30px !important; text-align: center !important; }

    /* FORCED CENTER FOR THE STREAMLIT INPUT WIDGET */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }

    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 6px solid #D4AF37 !important;
        border-radius: 12px !important;
        width: 180px !important; /* Slightly smaller than corridor to ensure center */
    }
    
    input {
        color: #000000 !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        text-align: center !important;
        height: 80px !important;
    }

    .v31-bridge { color: #00FF00 !important; font-size: 38px !important; font-weight: 900 !important; border-bottom: 8px solid #00FF00 !important; margin-bottom: 160px !important; text-align: center !important; }
    .v31-spacer { height: 250px !important; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITAN BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=1500) 
else:
    st.markdown("<h1 style='color:#D4AF37; text-align:center;'>MITRAX ORACLE V31</h1>", unsafe_allow_html=True)

# --- 3. THE WINNING BOARD ---
st.markdown("<div class='v31-board'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "30
