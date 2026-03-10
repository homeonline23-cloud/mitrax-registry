import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIGURATION (LOCKED) ---
st.set_page_config(page_title="MITRAX ORACLE PICK 4 PREDICTOR", layout="wide")

# --- 2. UNIVERSAL STYLING (THE IMPACT ARMOR) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* IMPACT FONT FOR HEADERS */
    .imp-header { 
        text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; 
        text-transform: uppercase; letter-spacing: 2px;
    }
    .main-title { font-size: 50px; margin-bottom: 0px; }
    .section-header { font-size: 35px; margin-top: 20px; }
    .predict-header { font-size: 40px; color: #00FF00; text-shadow: 0 0 10px #00FF00; }
    
    /* BOLD ARIAL FOR GLOBAL BANNER */
    .global-banner { 
        background: rgba(255, 215, 0, 0.15); border: 2px solid #FFD700; border-radius: 10px; 
        padding: 20px; text-align: center; color: #FFFFFF; font-family: 'Arial', sans-serif; 
        font-weight: bold; font-size: 20px; margin: 20px 0px;
    }
    .island-name { color: #FFD700; font-family: 'Impact', sans-serif; font-size: 24px; text-align: center; border-bottom: 2px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE PERMANENT HEADER ---
st.markdown("<div style='text-align: center; font-size: 60px;'>✧🌍✧</div>", unsafe_allow_html=True)
st.markdown("<div class='imp-header main-title'>MITRAX ORACLE PICK 4 PREDICTOR</div>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #FFD700; font-weight: bold;'>DATE: {datetime.now().strftime('%-m/%-d/%Y')}</p>", unsafe_allow_html=True)

# --- 4. SECTOR 1: THE IMAGE BROADCAST ---
st.markdown("<div class='imp-header section-header'>IMPERIAL IMAGE BROADCAST</div>", unsafe_allow_html=True)
img_file = st.file_uploader("Upload Strategy Chart", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

# NO COMPLEX INDENTATION HERE - 100% ERROR PROOF
if img_file:
    st.image(img_file, width='stretch')
else:
    st.info("Station standing by. Upload image file for display.")

st.divider()

# --- 5. SECTOR 2: THE 5 PREDICTED WINNERS (IMPACT GREEN) ---
st.markdown("<div class='imp-header predict-header'>★ 5 PREDICTED PICK 4 WINNERS ★</div>", unsafe_allow_html=True)
p_cols = st.columns(5)
for i in range(5):
    with p_cols[i]:
        st.markdown(f"<div class='imp-header' style='font-size:18px; color:#00FF00;'>TARGET {i+1}</div>", unsafe_allow_html=True)
        st.text_input(f"P4_{i}", key=f"p_{i}", label_visibility="collapsed", placeholder="0000")

st.divider()

# --- 6. SECTOR 3: THE REGIONAL BOARD ---
st.markdown("<div class='imp-header section-header'>REGIONAL WINNER BOARD</div>", unsafe_allow_html=True)
i_cols = st.columns(4)
islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
for idx, island in enumerate(islands):
    with i_cols[idx]:
        st.markdown(f"<div class='island-name'>{island}</div>", unsafe_allow_html=True)
        for row in range(1, 5):
            st.text_input(f"{island}_{row}", key=f"w_{island}_{row}", label_visibility="collapsed", placeholder="----")

# --- 7. SECTOR 4: GLOBAL INSTRUCTION (WHITE BOLD ARIAL) ---
st.markdown("""
    <div class='global-banner'>
        🌍 GLOBAL ADAPTATION PROTOCOL: MEMBERS FROM OTHER NATIONS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
        TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. THE SYSTEM IS UNIVERSAL. 🌍
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR 5: THE 6X SYMMETRY MATRIX ---
st.markdown("<div class='imp-header section-header'>95% PROBABILITY MATRIX</div>", unsafe_allow_html=True)
g_cols = st.columns(6)
for i in range(6):
    with g_cols[i]:
        st.markdown(f"<div class='imp-header' style='font-size:14px; border:1px solid #FFD700;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
        st.text_input(f"M_{i}", label_visibility="collapsed", key=f"s_{i}", placeholder="----")
