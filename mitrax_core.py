import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

# --- 2. TACTICAL CSS ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; max-width: 1100px; margin: auto; }
    input { text-align: center !important; font-size: 24px !important; font-weight: bold !important; border-radius: 10px !important; }
    [data-testid="column"] { width: 25% !important; flex: 1 1 25% !important; min-width: 100px !important; }
    div.stTextInput > label { font-weight: bold; color: #888; }
    .scan-box { border-radius: 8px; padding: 10px; text-align: center; border: 2px solid #444; font-family: monospace; margin-top: 5px; }
    .client-header { text-align: center; color: #FFD700; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HIDDEN MATH ENGINE ---
def get_day_root(target_date):
    d_sum = target_date.month + target_date.day
    root = int(str(d_sum)[-1])
    mirror = {0:5, 1:6, 2:7, 3:8, 4:9, 5:0, 6:1, 7:2, 8:3, 9:4}.get(root)
    return root, mirror

if 'history' not in st.session_state: st.session_state.history = []

# --- 4. CLIENT INTERFACE (FRONT OF HOUSE) ---
st.markdown("<h1 class='client-header'>🌌 Mitrax Player Registry</h1>", unsafe_allow_html=True)
st.write("Please enter your details and coordinates to play.")

# Client inputs
client_name = st.text_input("Player Name / ID", placeholder="Enter Name here...")
c1, c2, c3, c4 = st.columns(4)
with c1: v1 = st.text_input("Sector 1", value="0", key="c1")
with c2: v2 = st.text_input("Sector 2", value="0", key="c2")
with c3: v3 = st.text_input("Sector 3", value="0", key="c3")
with c4: v4 = st.text_input("Sector 4", value="0", key="c4")

if st.button("✅ SUBMIT PLAY", use_container_width=True):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.insert(0, {
        "Time": timestamp, "Player": client_name,
        "N": v1, "S2": v2, "S": v3, "S4": v4
    })
    st.success(f"Ticket Registered for {client_name}! Good luck.")

# --- 5. THE KITCHEN DOOR (CHEF ACCESS) ---
st.markdown("---")
with st.expander("🔐 STAFF ENTRANCE (Chef Only)"):
    access_code = st.text_input("Enter Security Code", type="password")
    
    if access_code == "Mitrax-Chef":
        st.info("KITCHEN OPEN: Tactical Scanners Online.")
        
        # Date Math
        today = datetime.now(); tomorrow = today + timedelta(days=1)
        r1, m1 = get_day_root(today); r2, m2 = get_day_root(tomorrow)
        
        # Scanner Row
        st.markdown(f"**🔴 TODAY: {r1}-{m1} | 🔵 NEXT: {r2}-{m2}**")
        s_cols = st.columns(4)
        inputs = [v1, v2, v3, v4]
        
        for i, sc in enumerate(s_cols):
            with sc:
                digits = [int(d) for d in str(inputs[i]) if d.isdigit()]
                bg, status = "#1A1A1A", "OFFLINE"
                if any(d in [r1, m1] for d in digits): bg, status = "#660000", f"HIT {r1}-{m1}"
                elif any(d in [r2, m2] for d in digits): bg, status = "#003366", f"HIT {r2}-{m2}"
                st.markdown(f"<div class='scan-box' style='background-color:{bg}; color:white;'><b>{status}</b></div>", unsafe_allow_html=True)
        
        # History Table
        if st.session_state.history:
            st.markdown("### 📜 Order History Log")
            st.table(pd.DataFrame(st.session_state.history))
    else:
        st.warning("Kitchen is locked. Diners only beyond this point.")
