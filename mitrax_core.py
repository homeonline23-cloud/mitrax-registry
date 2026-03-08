import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# --- 1. ENGINE CONFIG & DARK THEME FORCING ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

# --- 2. THE IMPERIAL STYLING (BLACK & GOLD) ---
st.markdown("""
    <style>
    /* Force Dark Background for the whole app */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .block-container { padding-top: 1rem; max-width: 1100px; margin: auto; }
    
    /* Input Box Styling */
    input { 
        text-align: center !important; 
        font-size: 24px !important; 
        font-weight: bold !important; 
        border-radius: 10px !important;
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #444 !important;
    }
    
    /* Column Alignment */
    [data-testid="column"] { width: 25% !important; flex: 1 1 25% !important; min-width: 100px !important; }
    
    /* Labels and Headers */
    label { font-weight: bold !important; color: #FFD700 !important; }
    .client-header { text-align: center; color: #FFD700; text-shadow: 2px 2px #000; }
    
    /* Scanner Boxes */
    .scan-box { 
        border-radius: 8px; padding: 10px; text-align: center; 
        border: 2px solid #444; font-family: monospace; margin-top: 5px; 
    }
    
    /* Table Styling */
    .stTable { background-color: #1E1E1E; border-radius: 10px; }
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
st.markdown("<h1 class='client-header'>🌌 MITRAX PLAYER REGISTRY</h1>", unsafe_allow_html=True)
st.write("<div style='text-align:center;'>Enter your details and coordinates to secure your play.</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Client inputs
client_name = st.text_input("PLAYER NAME / ID", placeholder="Enter Name here...")
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: v1 = st.text_input("SECTOR 1", value="0", key="c1")
with c2: v2 = st.text_input("SECTOR 2", value="0", key="c2")
with c3: v3 = st.text_input("SECTOR 3", value="0", key="c3")
with c4: v4 = st.text_input("SECTOR 4", value="0", key="c4")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✅ SUBMIT PLAY", use_container_width=True):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.insert(0, {
        "Time": timestamp, "Player": client_name,
        "N": v1, "S2": v2, "S": v3, "S4": v4
    })
    st.balloons()
    st.success(f"Ticket Registered for {client_name}! Good luck.")

# --- 5. THE KITCHEN DOOR (CHEF ACCESS) ---
st.markdown("<br><br><hr>", unsafe_allow_html=True)
with st.expander("🔐 STAFF ENTRANCE"):
    access_code = st.text_input("CHEF SECURITY CODE", type="password")
    
    if access_code == "Mitrax-Chef":
        st.info("KITCHEN ONLINE: Tactical Scanners Active.")
        
        # Date Math
        today = datetime.now(); tomorrow = today + timedelta(days=1)
        r1, m1 = get_day_root(today); r2, m2 = get_day_root(tomorrow)
        
        # Scanner Row
        st.markdown(f"### 🔴 TODAY: {r1}-{m1} | 🔵 NEXT: {r2}-{m2}")
        s_cols = st.columns(4)
        inputs = [v1, v2, v3, v4]
        
        for i, sc in enumerate(s_cols):
            with sc:
                digits = [int(d) for d in str(inputs[i]) if d.isdigit()]
                bg, status = "#1A1A1A", "OFFLINE"
                if any(d in [r1, m1] for d in digits): bg, status = "#990000", f"HIT {r1}-{m1}"
                elif any(d in [r2, m2] for d in digits): bg, status = "#003399", f"HIT {r2}-{m2}"
                st.markdown(f"<div class='scan-box' style='background-color:{bg}; color:white;'><b>{status}</b></div>", unsafe_allow_html=True)
        
        # History Table
        if st.session_state.history:
            st.markdown("### 📜 ORDER HISTORY LOG")
            st.table(pd.DataFrame(st.session_state.history))
    elif access_code != "":
        st.warning("Access Denied: Sector Locked.")
