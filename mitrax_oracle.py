import streamlit as st
import pandas as pd

# --- IMPERIAL FOUNDATION ---
st.set_page_config(page_title="MITRAX EMPIRE", layout="wide")

# --- THE 14-SOLDIER REGISTRY (2620 BALANCE) ---
data = {
    "Soldier": [f"{i+1}/1" if i < 7 else f"{i+1-7+7}/3" for i in range(14)],
    "North": [2620] * 14, "South": [2620] * 14, "East": [2620] * 14, "West": [2620] * 14
}
data["Soldier"][7] = "8/3" # Imperial Decree
df = pd.DataFrame(data)

# --- THE ORANGE SECTOR STYLING ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: orange; }}
    h1 {{ color: black; font-family: 'Courier New'; text-align: center; }}
    .stTable, table, td, th {{ font-size: 13px !important; color: black !important; }}
    th {{ background-color: #333 !important; color: white !important; }}
    </style>
    <h1>🏛️ MITRAX EMPIRE: ORANGE SECTOR</h1>
    """, unsafe_allow_html=True)

def apply_colors(row):
    if row["Soldier"] == "7/1": return ['background-color: #FF0000; color: white'] * 5
    if row["Soldier"] == "8/3": return ['background-color: #0000FF; color: white'] * 5
    return ['background-color: orange; color: black'] * 5

st.table(df.style.apply(apply_colors, axis=1))
st.markdown("<p style='text-align: right;'><b>LOCKED 🔒</b></p>", unsafe_allow_html=True)
