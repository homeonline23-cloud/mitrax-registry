import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# SEALED STYLE BLOCK - FINISHED AND RE-WELDED
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-text { color: #FFFFFF; font-size: 15px; font-weight: 900; margin-bottom: 20px; padding: 15px; border: 2px solid #D4AF37; border-radius: 10px; background-color: #111111; }

    .date-circle-red {
        border: 3px solid #FF0000; border-radius: 50%; color: #FF0000;
        font-size: 22px; font-weight: 900; width: 45px; height: 45px;
        display: flex; align-items: center; justify-content: center;
        margin: 8px auto; background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 3px solid #0000FF; border-radius: 50%; color: #0000FF;
        font-size: 22px; font-weight: 900; width: 45px; height: 45px;
        display: flex; align-items: center; justify-content: center;
        margin: 8px auto; background-color: #FFFFFF;
    }
    .date-display { color: #D4AF37; font-size: 22px; font-weight: 900; margin-top: 45px; }

    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height:
