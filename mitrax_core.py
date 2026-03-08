import streamlit as st
from datetime import datetime, timedelta

# --- 1. ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

# --- 2. TACTICAL CSS ---
st.markdown("""
    <style>
    .block-container { padding-top: 1rem; max-width: 1100px; margin: auto; }
    input { text-align: center !important; font-size: 28px !important; font-weight: bold !important; border-radius: 12px !important; }
    [data-testid="column"] { width: 25% !important; flex: 1 1 25% !important; min-width: 120px !important; }
    div.stTextInput > label { display: none; }
    .scan-box { 
        border-radius: 8px; padding: 12px; text-align: center; 
        border: 2px solid #444; font-family: 'Courier New', monospace; font-size: 18px;
        margin-top: 5px;
    }
    .date-banner {
        background-color: #111; padding: 15px; text-align: center; 
        border-radius: 15px; border: 1px solid #333; margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. AUTO-MATH ENGINE ---
def get_day_root(target_date):
    # Chef's Rule: Month + Day, take last digit
    d_sum = target_date.month + target_date.day
    root = int(str(d_sum)[-1])
    mirror = {0:5, 1:6, 2:7, 3:8, 4:9, 5:0, 6:1, 7:2, 8:3, 9:4}.get(root)
    return root, mirror

# --- 4. SCANNER DATA ---
today = datetime.now()
tomorrow = today + timedelta(days=1)
r1, m1 = get_day_root(today)      # Red Frequency (Today)
r2, m2 = get_day_root(tomorrow)   # Blue Frequency (Tomorrow)

# --- 5. INTERFACE ---
st.title("🌌 Mitrax Imperial Registry: Autopilot Mode")

st.markdown(f"""
<div class='date-banner'>
    <span style='color:#FF3131; font-weight:bold; font-size:22px;'>🔴 CURRENT: {r1}-{m1}</span>
    <span style='color:white; margin: 0 20px;'> | </span>
    <span style='color:#00D2FF; font-weight:bold; font-size:22px;'>🔵 INCOMING: {r2}-{m2}</span>
</div>
""", unsafe_allow_html=True)

if 'd1' not in st.session_state:
    st.session_state.update({'d1': '0', 'd2': '0', 'd3': '0', 'd4': '0'})

# --- 6. UNIFIED SECTOR GRID ---
cols = st.columns(4)
sector_configs = [
    {"label": "7/1 (NORTH)", "color": "#FF3131", "key": "d1"},
    {"label": "SECTOR 2", "color": "white", "key": "d2"},
    {"label": "8/3 (SOUTH)", "color": "#00D2FF", "key": "d3"},
    {"label": "SECTOR 4", "color": "white", "key": "d4"}
]

for i, col in enumerate(cols):
    with col:
        conf = sector_configs[i]
        st.markdown(f"<h3 style='color:{conf['color']}; text-align:center; margin-bottom:0;'>{conf['label']}</h3>", unsafe_allow_html=True)
        val = st.text_input(f"In{i}", value=st.session_state[conf['key']], key=f"input_{conf['key']}")
        
        # Scanner Logic
        digits = [int(d) for d in str(val) if d.isdigit()]
        bg, txt, status = "#1A1A1A", "#444", "OFFLINE"
        
        # Check Priority: Today (Red) then Tomorrow (Blue)
        if any(d in [r1, m1] for d in digits):
            bg, txt, status = "#440000", "white", f"MATCH: {r1}-{m1}"
        elif any(d in [r2, m2] for d in digits):
            bg, txt, status = "#002244", "white", f"MATCH: {r2}-{m2}"
            
        st.markdown(f"<div class='scan-box' style='background-color:{bg}; color:{txt};'><b>{status}</b></div>", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.write("🛰️ **AUTOPILOT STATUS:** SCANNING SECTORS FOR MIRROR FREQUENCIES...")
