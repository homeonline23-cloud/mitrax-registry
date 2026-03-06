import streamlit as st
import pandas as pd

# --- 1. IMPERIAL FOUNDATION ---
st.set_page_config(page_title="MITRAX EMPIRE", layout="wide")

# --- 2. DRAFTING THE 14-SOLDIER ARMY (THE DATA) ---
# We define 'df' here so line 11 never fails again!
data = {
    "Soldier": [f"{i+1}/1" if i < 7 else f"{i+1-7+7}/3" for i in range(14)],
    "North": [2620] * 14,
    "South": [2620] * 14,
    "East": [2620] * 14,
    "West": [2620] * 14
}
data["Soldier"][7] = "8/3" # Imperial Decree
df = pd.DataFrame(data)

# --- 3. THE COLOR RULES ---
def apply_imperial_colors(row):
    if row["Soldier"] == "7/1":
        return ['background-color: #FF0000; color: white; font-weight: bold'] * 5
    if row["Soldier"] == "8/3":
        return ['background-color: #0000FF; color: white; font-weight: bold'] * 5
    return ['background-color: orange; color: black'] * 5

# --- 4. THE ORANGE SECTOR STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: orange; }
    h1 { color: black; font-family: 'Courier New'; text-align: center; font-size: 32px; }
    .stTable, table { font-size: 13px !important; font-family: 'Arial'; color: black !important; }
    th { background-color: #333 !important; color: white !important; }
    </style>
    <h1>🏛️ MITRAX EMPIRE: ORANGE SECTOR</h1>
    """, unsafe_allow_html=True)

# --- 5. THE FINAL DEPLOYMENT ---
st.table(df.style.apply(apply_imperial_colors, axis=1))
st.markdown("<p style='text-align: right; font-weight: bold;'>VAULT STATUS: LOCKED 🔒</p>", unsafe_allow_html=True)
