import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# SEALED STYLE BLOCK - TRIPLE CHECKED
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-text { color: #FFFFFF; font-size: 15px; font-weight: 900; margin-bottom: 20px; padding: 10px; border: 1px solid #D4AF37; border-radius: 10px; }

    .date-circle-red {
        border: 3px solid #FF0000; border-radius: 50%; color: #FF0000;
        font-size: 24px; font-weight: 900; width: 50px; height: 50px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 4px solid #0000FF; border-radius: 50%; color: #0000FF;
        font-size: 24px; font-weight: 900; width: 50px; height: 50px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-display { color: #D4AF37; font-size: 20px; font-weight: 900; margin-top: 20px; }

    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height: 50px;
    }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 10px; height: 260px; margin: 0 auto; border-radius: 5px; border: 1px solid #D4AF37; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    
    .island-label { color: #D4AF37; font-weight: 900; font-size: 16px; text-transform: uppercase; margin-bottom: 5px; }
    .stSuccess { font-weight: 900; font-size: 20px; border: 1px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 2px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. TOP SECTION ---
st.markdown("<h1 style='color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37;'>Pick 4 Worldwide
