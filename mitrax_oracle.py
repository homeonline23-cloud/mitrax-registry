import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-text { color: #FFFFFF; font-size: 14px; font-weight: 900; margin-bottom: 20px; padding: 15px; border: 2px solid #D4AF37; border-radius: 10px; background-color: #111111; }

    .date-circle-red {
        border: 3px solid #FF0000; border-radius: 50%; color: #FF0000;
        font-size: 20px; font-weight: 900; width: 40px; height: 40px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 3px solid #0000FF; border-radius: 50%; color: #0000FF;
        font-size: 20px; font-weight: 900; width: 40px; height: 40px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-display { color: #D4AF37; font-size: 20px; font-weight: 900; margin-top: 30px; }

    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height: 42px; width: 42px;
    }
    .red-target { border: 3px solid #FF0000; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 3px solid #0000FF; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
    
    .gold-pillar { background-color: #D4AF37; width: 12px; height: 260px; margin: 0 auto; border-radius: 5px; border: 1px solid #000000; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    
    .island-label { color: #D4AF37; font-weight: 900; font-size: 14px; text-transform: uppercase; margin-bottom: 2px; }

    /* INPUTS ABOVE PILLARS */
    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 3px solid #D4AF37 !important; font-size: 24px !important; 
        text-align: center !important; height: 60px !important; width: 120px !important;
        padding: 0px !important; font-weight: 900 !important; border-radius: 8px !important;
    }
    
    /* HORIZONTAL SKY TITLE (ABOVE PILLARS) */
    .sky-title { color: #D4AF37; font-size: 22px; font-weight: 900; margin-top: -10px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. TOP SECTION ---
st.markdown("<h1 style='color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)
st.markdown("<div class='mission-text'>The 4-digit Prediction Calculator that can be used Globally... 95% chance of increasing your chances of winning.</div>", unsafe_allow_html=True)

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
def draw_grid(val, color, target=
