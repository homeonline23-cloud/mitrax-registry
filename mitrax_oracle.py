import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-text { color: #FFFFFF; font-size: 15px; font-weight: 900; margin-bottom: 20px; padding: 15px; border: 2px solid #D4AF37; border-radius: 10px; background-color: #111111; }

    .date-circle-red {
        border: 3px solid #FF0000; border-radius: 50%; color: #FF0000;
        font-size: 22px; font-weight: 900; width: 45px; height: 45px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 3px solid #0000FF; border-radius: 50%; color: #0000FF;
        font-size: 22px; font-weight: 900; width: 45px; height: 45px;
        display: flex; align-items: center; justify-content: center;
        margin: 8px auto; background-color: #FFFFFF;
    }
    .date-display { color: #D4AF37; font-size: 22px; font-weight: 900; margin-top: 35px; }

    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height: 45px; width: 45px;
    }
    .red-target { border: 3px solid #FF0000; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 3px solid #0000FF; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; }
    
    /* COMPRESSED HIGH-ALTITUDE PILLAR */
    .gold-pillar { background-color: #D4AF37; width: 12px; height: 210px; margin: 0 auto; border-radius: 5px; border: 1px solid #000000; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    
    .island-label { color: #D4AF37; font-weight: 900; font-size: 16px; text-transform: uppercase; margin-bottom: 5px; }

    /* MEGA INPUT BOXES - PULLED UPWARD */
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 4px solid #D4AF37 !important; font-size: 28px !important; 
        text-align: center !important; height: 70px !important; width: 150px !important;
        padding: 0px !important; font-weight: 900 !important; border-radius: 10px !important;
    }
    
    /* SKY BRIDGE TITLE */
    .symmetry-bridge { color: #D4AF37; font-size: 24px; font-weight: 900; margin-bottom: -15px; margin-top: -10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. TOP SECTION ---
st.markdown("<h1 style='color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)
st.markdown("<div class='mission-text'>The 4-digit Prediction Calculator that can be used Globally... Increases winning potential through Symmetry Matrix analysis.</div>", unsafe_allow_html=True)

# --- 3. WINNING NUMBERS BOARD ---
st.markdown("<h4 style='color: #D4AF37;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
res_cols = st.columns(4)
res_data = [("ARUBA", ["1862", "0801", "9394"]), ("BONAIRE", ["2544", "8732", "7296"]), ("CURAÇAO", ["7716", "5502", "5918"]), ("ST. MARTIN", ["3076", "8561", "3465"])]
for i, (name, nums) in enumerate(res_data):
    with res_cols[i]:
        st.markdown(f"<p class='island-label'>{name}</p>", unsafe_allow_html=True)
        for n in nums: st.success(n)

# --- 4. THE VERTICAL DATE ANCHOR ---
st.write("---")
da1, da2, da3 = st.columns([1, 2, 1])
with da1:
    st.markdown("<div class='date-circle-red'>7</div><div class='date-circle-red'>1</div>", unsafe_allow_html=True)
with da2:
    curr_date = datetime.now().strftime("%m/%d/%Y")
    st.markdown(f"<div class='date-display'>Date: {curr_date}</div>", unsafe_allow_html=True)
with da3:
    st.markdown("<div class='date-circle-blue'>8</div><div class='date-circle-blue'>3</div>", unsafe_allow_html=True)
st.write("---")

# --- 5. THE MASTER SYMMETRY DECK ---
def draw_grid(val, color, target=None):
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target" if is_m and target=="red" else "blue-target" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell {color}'><div class='{circle}'>{txt}</div></div>" if circle else f"<div class='matrix-cell {color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

# THE SKY BRIDGE TITLE (CENTERED & PULLED UP)
st.markdown("<div class='symmetry-bridge'>SYMMETRY MATRIX SENSORS</div>", unsafe_allow_html=True)

# GRID DECK (HIGH-ALTITUDE WELD)
c1, p1, c2, p2, c3, p3, c4 = st.columns([4, 1.5, 4, 0.5, 4, 1.5, 4])

with c1:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    r_val = st.session_state.get('vr_up', "")
    draw_grid(r_val, "grid-light", "red")

with p1: # RED PILLAR (Shortened and Pulled Up)
    st.write("<div style='height:20px;'></div>", unsafe_allow_html=True)
    r_val = st.text_input("", placeholder="****", max_chars=4, key="vr_up", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with c2:
