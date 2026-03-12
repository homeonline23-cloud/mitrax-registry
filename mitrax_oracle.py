import streamlit as st
import pandas as pd

# --- 1. IMPERIAL GATEKEEPER SETUP ---
st.set_page_config(page_title="MITRAX SECURE PORTAL", layout="wide")

# Simple Gatekeeper Logic (For Client Access)
def check_password():
    def password_entered():
        if st.session_state["password"] == "mitrax2026": # THE IMPERIAL KEY
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: orange;'>🏛️ MITRAX EMPIRE LOGIN</h1>", unsafe_allow_html=True)
        st.text_input("Enter Imperial Key to view Predictions", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Access Denied. Re-enter Key", type="password", on_change=password_entered, key="password")
        st.error("❌ Invalid Key. The Utrecht Satellite has blocked your IP.")
        return False
    else:
        return True

# --- 2. THE SECURE SECTOR ---
if check_password():
    # THE GATES ARE OPEN!
    st.markdown("<h1 style='color: black; text-align: center;'>🏛️ MITRAX PREDICTION ENGINE</h1>", unsafe_allow_html=True)
    
    # --- 3. THE WINNING PREDICTION CALCULATOR ---
    st.sidebar.header("🕹️ Prediction Inputs")
    last_winning_num = st.sidebar.number_input("Enter Last Winning Number", min_value=0, max_value=9999, value=2620)
    
    # Secret Imperial Formula (Example: 2620 Balance Shift)
    prediction = (last_winning_num * 1.05) / 1 # Head Chef's secret math
    
    st.success(f"### 🎯 NEXT PREDICTED WINNING NUMBER: {int(prediction)}")

    # --- 4. THE 14-SOLDIER REGISTRY (THE BALANCE) ---
    data = {
        "Soldier": [f"{i+1}/1" if i < 7 else f"{i+1-7+7}/3" for i in range(14)],
        "North": [2620] * 14,
        "South": [2620] * 14,
        "East": [2620] * 14,
        "West": [2620] * 14
    }
    data["Soldier"][7] = "8/3"
    df = pd.DataFrame(data)

    def apply_imperial_colors(row):
        if row["Soldier"] == "7/1": return ['background-color: #FF0000; color: white; font-weight: bold'] * 5
        if row["Soldier"] == "8/3": return ['background-color: #0000FF; color: white; font-weight: bold'] * 5
        return ['background-color: orange; color: black'] * 5

    st.markdown("""
        <style>
        .stApp { background-color: orange; }
        .stTable, table { font-size: 13px !important; font-family: 'Arial'; color: black !important; }
        </style>
        """, unsafe_allow_html=True)

    st.table(df.style.apply(apply_imperial_colors, axis=1))
    
    if st.button("LOGOUT"):
        st.session_state["password_correct"] = False
        st.rerun()
