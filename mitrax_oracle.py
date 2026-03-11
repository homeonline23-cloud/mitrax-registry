import streamlit as st
from datetime import datetime

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE DATE ANCHOR BOXES */
    .date-circle-red {
        border: 4px solid #FF4B4B;
        border-radius: 50%;
        color: #FF4B4B;
        font-size: 30px;
        font-weight: 900;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: white;
    }
    .date-circle-blue {
        border: 4px solid #0000FF;
        border-radius: 50%;
        color: #0000FF;
        font-size: 30px;
        font-weight: 900;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: white;
    }
    .digital-calendar {
        border: 2px solid #D4AF37;
        background-color: #111111;
        color: #D4AF37;
        padding: 8px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 900;
        margin-top: 15px;
    }

    /* GRID & PILLAR STYLING */
    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF4B4B; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 12px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 10px; }
    .grid-light { background-color: #D3D3D3; }
    .grid-dark { background-color: #707070; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    .stSuccess { font-weight: 900; font-size: 22px; border: 2px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 5px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 22px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING & DATE ANCHOR (NEW TOP SECTION) ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# DATE ANCHOR MOVED HERE
t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
with t_col1: # RED DATE NUMBERS
    st.markdown("<div class='date-circle-red'>7</div>", unsafe_allow_html=True)
    st.markdown("<div class='date-circle-
