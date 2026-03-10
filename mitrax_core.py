import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIGURATION (LOCKED & PERMANENT) ---
st.set_page_config(page_title="MITRAX ORACLE PICK 4 PREDICTOR", layout="wide")

# --- 2. UNIVERSAL STYLING (THE GOLDEN ARMOR) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    .mitrax-header { 
        text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; 
        font-size: 50px; letter-spacing: 5px; margin-bottom: 0px; 
    }
    
    .date-stamp { text-align: center; color: #FFD700; font-family: 'Arial', sans-serif; font-size: 20px; font-weight: bold; margin-bottom: 20px; }
    
    .global-banner { 
        background: rgba(255, 215, 0, 0.15); border: 2px solid #FFD700; border-radius: 10px; 
        padding: 20px; text-align: center; color: #FFFFFF; font-family: 'Arial', sans-serif; 
        font-weight: bold; font-size: 20px; margin: 20px 0px;
    }

    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; border-bottom: 2px solid #FFD700; padding-bottom: 5px; font-family: 'Arial'; }
    .predict-label { color: #00FF00; font-weight: bold; font-size: 14px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE PERMANENT HEADER ---
st.markdown("<div style='text-align: center; font-size: 60px;'>✧🌍✧</div>", unsafe_allow_html=True)
st.markdown("<div class='mitrax-header'>MITRAX ORACLE PICK 4 PREDICTOR</div>", unsafe_allow_html=True)
st.markdown(f"<div class='date-stamp'>SESSION DATE: {datetime.now().strftime('%-m/%-d/%Y')}</div>", unsafe_allow_html=True)

# --- 4. SECTOR 1: THE IMAGE VAULT (LOCAL FILE UPLOAD) ---
st.markdown("<h3 style='color: #FFD700; text-align: center;'>IMPERIAL IMAGE BROADCAST</h3>", unsafe_allow_html=True)
img_file = st.file_uploader("Upload Strategy Chart / Image", type=["png", "jpg", "jpeg"])
if img_file:
    st.image(img_file, use_container_width=True)
else:
    st.info("Station standing by. Upload your image file to display on the main board.")

st.divider()

# --- 5. SECTOR 2: THE 5 PREDICTED PICK 4 WINNERS ---
st.markdown("<h2 style='text-align: center; color: #00FF00; font-family:Impact;'>★ 5 PREDICTED PICK 4 WINNERS ★</h2>", unsafe_allow_html=True)
p_cols = st.columns(5)
for i in range(5):
    with p_cols[i]:
        st.markdown(f"<div class='predict-label'>TARGET {i+1}</div>", unsafe_allow_html=True)
        st.text_input(f"Predict {i}", key=f"p4_pred_{i}", label_visibility="collapsed", placeholder="0000")

st.divider()

# --- 6. SECTOR 3: THE 4-TIER ISLAND BOARD ---
st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
i_cols = st.columns(4)
islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
for i, island in enumerate(islands):
    with i_cols[i]:
        st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
        for row in range(1, 5):
            st.text_input(f"{island} Rank {row}", key=f"win_{island}_{row}", label_visibility="collapsed", placeholder="----")

# --- 7. SECTOR 4: THE UNIVERSAL INSTRUCTION (WHITE BOLD ARIAL) ---
st.markdown("""
    <div class='global-banner'>
        🌍 GLOBAL ADAPTATION PROTOCOL: MEMBERS FROM OTHER NATIONS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
        TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. THE SYSTEM IS UNIVERSAL. 🌍
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR 5: THE 6X SYMMETRY MATRIX ---
st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>95% PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
g_cols = st.columns(6)
for i in range(6):
    with g_cols[i]:
        st.markdown(f"<div style='border: 1px solid #FFD700; padding: 10px; text-align: center; background: rgba(255,215,0,0.05); color:#FFD700; font-weight:bold;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
        st.text_input(f"Sec {i}", label_visibility="collapsed", key=f"sym_{i}", placeholder="----")

st.divider()
st.success("STATION STATUS: PERMANENT HULL SECURED | INDENTATION ERROR PURGED")
