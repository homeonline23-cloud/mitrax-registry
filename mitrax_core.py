import streamlit as st
import pandas as pd
import os

# --- IMPERIAL FOUNDATION ---
# This configuration locks the Sector for wide-screen viewing
st.set_page_config(page_title="MITRAX EMPIRE: 2026 REGISTRY", layout="wide")

# Force the satellite to stay in the local vault, ignoring the /mount/admin/ phantom
base_path = os.path.dirname(__file__)

# --- THE 14-SOLDIER REGISTRY (2620 BALANCE) ---
# North, South, East, and West are locked to the Imperial Constant.
data = {
    "Soldier": [f"{i+1}/1" if i < 7 else f"{i+1-7+7}/3" for i in range(14)],
    "North": [2620] * 14,
    "South": [2620] * 14,
    "East": [2620] * 14,
    "West": [2620] * 14
}

# Imperial Decree: Correcting the 8/3 Naming Convention per the Head Chef
data["Soldier"][7] = "8/3" 

df = pd.DataFrame(data)

# --- THE ORANGE SECTOR STYLING (13px & Colors) ---
st.markdown(f"""
    <style>
    /* Sector Background */
    .stApp {{ background-color: orange; }}
    
    /* Imperial Header */
    h1 {{ 
        color: black; 
        font-family: 'Courier New', monospace; 
        text-align: center; 
        font-size: 32px;
        text-shadow: 2px 2px #55555533;
    }}
    
    /* 13px Sharp Precision for the Army Table */
    .stTable, table {{ 
        width: 100%;
        border-collapse: collapse;
        font-size: 13px !important; 
        font-family: 'Arial', sans-serif;
        color: black !important;
    }}
    
    /* Table Borders and Headers */
    td, th {{ 
        border: 1px solid #333 !important; 
        padding: 8px !important;
        text-align: center !important;
    }}
    
    th {{ 
        background-color: #333 !important; 
        color: white !important; 
        font-weight: bold;
    }}
    </style>
    <h1>🏛️ MITRAX EMPIRE: ORANGE SECTOR</h1>
    """, unsafe_allow_html=True)

# --- THE PILLAR HIGHLIGHTING (7/1 RED & 8/3 BLUE) ---
def apply_imperial_colors(row):
