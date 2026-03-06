import streamlit as st
import pandas as pd

# --- 1. IMPERIAL GATEKEEPER ---
st.set_page_config(page_title="MITRAX SECURE PORTAL", layout="wide")

def check_password():
    def password_entered():
        if st.session_state["password"] == "mitrax2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: orange;'>🏛️ MITRAX EMPIRE LOGIN</h1>", unsafe_allow_html=True)
        st.text_input("Enter Imperial Key", type="password", on_change=password_entered, key="password")
        return False
    return st.session_state.get("password_correct", False)

if check_password():
    # --- 2. THE ORANGE SECTOR ATMOSPHERE ---
    st.markdown("""
        <style>
        .stApp { background-color: orange; }
        .stTable, table { 
            font-size: 13px !important; 
            font-family: 'Arial'; 
            color: black !important; 
            width: 100%;
        }
        h1 { color: black; text-align: center; font-family: 'Courier New'; }
        </style>
        <h1>🏛️ MITRAX PREDICTION ENGINE</h1>
        """, unsafe_allow_html=True)

    # --- 3. DRAFTING THE 14-SOLDIER ARMY (2620 BALANCE) ---
    # HEAD CHEF: Update your North/South/East/West numbers here!
    data = {
        "Soldier": ["1/1", "2/1", "3/1", "4/1", "5/1", "6/1", "7/1", 
                    "8/3", "9/3", "10/3", "11/3", "12/3", "13/3", "14/3"],
        "North": [2620] * 14,
        "South": [2620] * 14,
        "East":  [2620] * 14,
        "West":  [2620] * 14
    }
    df = pd.DataFrame(data)

    # --- 4. THE PERMANENT COLOR LAW (RED LEFT / BLUE RIGHT) ---
    def apply_imperial_colors(row):
        # 7/1 RED - ALWAYS LEFT
        if row["Soldier"] == "7/1":
            return ['background-color: #FF0000; color: white; font-weight: bold; text-align: left;'] * 5
        # 8/3 BLUE - ALWAYS RIGHT
        if row["Soldier"] == "8/3":
            return ['background-color: #0000FF; color: white; font-weight: bold; text-align: right;'] * 5
        # THE ORANGE HORIZON
        return ['background-color: orange; color: black; text-align: center;'] * 5

    # --- 5. THE FINAL DEPLOYMENT ---
    st.table(df.style.apply(apply_imperial_colors, axis=1))
    
    if st.button("SECURE LOGOUT"):
        st.session_state["password_correct"] = False
        st.rerun()
