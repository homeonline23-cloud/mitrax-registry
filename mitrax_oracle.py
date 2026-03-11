import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE WHITE BOX CONTAINER */
    .date-box {
        background-color: #FFFFFF; 
        padding: 15px; 
        border-radius: 15px; 
        margin: 10px auto; 
        max-width: 550px; 
        border: 4px solid #D4AF37;
    }
    
    /* CIRCLE STYLING */
    .date-circle-red {
        border: 4px solid #FF0000;
        border-radius: 50%;
        color: #FF0000;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 4px solid #0000FF;
        border-radius: 50%;
        color: #0000FF;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-header {
        color: #000000;
        background-color: #FFFFFF;
        padding: 5px 15px;
        border-radius: 5px;
        font-size: 26px;
        font-weight: 900;
        display: block;
        margin: 0 auto 10px auto;
    }

    /* MATRIX & GRID */
    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 12px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 10px; border: 1px solid #D4AF37; }
    .grid
