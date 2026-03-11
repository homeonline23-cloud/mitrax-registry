import streamlit as st
import os

# --- 1. ENGINE CONFIG (V78 AIRTIGHT) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V78")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE ABSOLUTE CENTER FORCE */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN (IMAGE) */
    .stImage {
        display: flex !important;
        justify-content: center !important;
        width: 900px !important;
    }
    img {
        border: 3px solid #D4AF37;
        border-radius: 15px;
        width: 900px !important;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.3);
    }

    /* TRIPLE-STACK BOARD */
    .v78-board-container { 
        display: flex !important; 
        flex-direction: row !important; 
        justify-content: center !important;
        width: 1000px !important; 
        margin: 15px auto 40px auto !important; 
    }
    .v78-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v78-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 18px; margin-bottom: 4px; text-transform: uppercase; }
    .v78-box { background-color: #FFFFFF; border: 2px solid #000; margin: 3px 0; padding: 6px; text-align: center; border-radius: 6px; }
    .v78-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 40px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS */
    .v78-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; 
        display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
        box-shadow: 0px 0px 15px rgba(0, 255, 0, 0.2);
    }
    .v78-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 35px; height: 300px; 
        border-radius: 10px; border: 2px solid #000; 
        box-shadow: 0px 0px 25px #D4AF37; 
    }
    .red-t { border: 6px solid #FF0000; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }
    .blue-t { border: 6px solid #0000FF; border-radius: 50%; width: 55px; height: 55px; display: flex; align-items: center; justify-content: center; }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; width: 130px !important; border-radius: 10px !important; }
    input { color: #00FF00 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. THE CROWN ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

# --- 2. THE BOARD ---
st.markdown("""
<div class='v78-board-container'>
    <div class='v78-column'><div class='v78-header'>ARUBA</div><div class='v78-box'><span class='v78-num'>1862</span></div><div class='v78-box'><span class='v78-num'>0801</span></div><div class='v78-box'><span class='v78-num'>9394</span></div></div>
    <div class='v78-column'><div class='v78-header'>BONAIRE</div><div class='v78-box'><span class='v78-num'>2544</span></div><div class='v78-box'><span class='v78-num'>8732</span></div><div class='v78-box'><span class='v78-num'>7296</span>
