import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# SEALED STYLE BLOCK - TRIPLE CHECKED
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .date-box {
        background-color: #FFFFFF; 
        padding: 15px; 
        border-radius: 15px; 
        margin: 10px auto; 
        max-width: 550px; 
        border: 4px solid #D4AF37;
    }
    
    .date-circle-red {
        border: 4px solid #FF0000;
        border-radius: 50%;
        color: #FF0000;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 4px solid #0000FF;
        border-radius: 50%;
        color: #0000FF;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-header {
        color: #000000;
        background-color: #FFFFFF;
        padding: 5px 15px;
        border-radius: 5px;
        font-size: 26px;
        font-weight: 900;
        display: block;
        margin: 0 auto 10px auto;
    }

    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 12px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 10px; border: 1px solid #D4AF37; }
    .grid-light { background-color: #D3D3D3; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    .stSuccess { font-weight: 900; font-size: 22px; border: 2px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 5px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 22px; text-align: center; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BRANDING ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# --- 3. THE DATE ANCHOR (TRIPLE-QUOTE FIXED) ---
curr_date = datetime.now().strftime("%m/%d/%Y")
st.markdown(f"""
    <div class='date-box'>
        <div class='date-header'>Date: {curr_date}</div>
        <table style='width: 100%; border: none;'>
            <tr>
                <td style='width: 45%; text-align: center;'>
                    <div class='date-circle-red'>7</div>
                    <div class='date-circle-red'>2</div>
                </td>
                <td style='width: 10%;'></td>
                <td style='width: 45%; text-align: center;'>
                    <div class='date-circle-blue'>8</div>
                    <div class='date-circle-blue'>3</div>
                </td>
            </tr>
        </table>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --- 4. RESULTS ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True); st.success("1862"); st.success("0801"); st.success("9394")
with colB:
    st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True); st.success("2544"); st.success("8732"); st.success("7296")
with colC:
    st.markdown("<p class='island-label'>CURAÇAO</p>", unsafe_allow_html=True); st.success("7716"); st.success("5502"); st.success("5918")
with colD:
    st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True); st.success("3076"); st.success("8561"); st.success("3465")

st.write("---")

# --- 5. INPUTS ---
_, center_col, _ = st.columns([1, 2, 1])
with
