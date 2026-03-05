import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mitrax Registry", layout="wide")
st.markdown("<h2 style='text-align: center; color: orange;'>🏛️ MITRAX EMPIRE: ORANGE SECTOR</h2>", unsafe_allow_html=True)

data = {
    "Soldier": ["1/1", "2/1", "3/1", "4/1", "5/1", "6/1", "7/1", "8/3", "9/3", "10/3", "11/3", "12/3", "13/3", "14/3"],
    "North": [2620]*14, "South": [2620]*14, "East": [2620]*14, "West": [2620]*14
}
df = pd.DataFrame(data)

def apply_styles(row):
    style = ['background-color: orange; color: black; font-weight: bold; font-size: 13px'] * 5 
    if row['Soldier'] == "7/1": return ['background-color: red; color: white; font-weight: bold; font-size: 13px'] * 5
    if row['Soldier'] == "8/3": return ['background-color: blue; color: white; font-weight: bold; font-size: 13px'] * 5
    return style

st.table(df.style.apply(apply_styles, axis=1))
