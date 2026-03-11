import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .matrix-cell {
        font-weight: 900 !important;
        font-size: 18px !important;
        border: 1px solid #000000 !important;
        aspect-ratio: 1 / 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        margin: 2px;
        color: #000000 !important;
    }
    
    .red-circle { border: 3px solid #FF4B4B !important; border-radius: 50% !important; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF !important; border-radius: 50% !important; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }

    .yellow-pool {
        background-color: #FFFF00 !important;
        width: 12px;
        height: 100%;
        min-height: 250px;
        margin: 0 auto;
        border-radius: 10px;
    }

    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    
    .stSuccess { font-weight: 900 !important; font-size: 22px !important; border: 2px solid #D4AF37 !important; color: #000000 !important; background-color: #D4AF37 !important; padding: 5px !important; }
    .stTextInput > div > div > input { background-color: #111111 !important; color: #D4AF37 !important; border: 2px solid #D4AF37 !important; font-size: 22px !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BRANDING & MISSION ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 15px; padding: 25px; background-color: #111111; margin: 20px auto; max-width: 900px;'>
        <p style='color: #FFFFFF; font-size: 17px; font-weight: 900; line-height: 1.6;'>
            The 4-digit Prediction Calculator that can be used Globally. <br>
            By entering the 4 chosen winning numbers into the calculator Grids. <br>
            When analyzing the symmetry patterns, you can see and identify potential 
            winning numbers in the GRID’s. <br>
            <span style='color: #D4AF37; font-size: 19px;'>There’s now a 95% chance of increasing your chances of winning.</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 3. WINNING NUMBERS RESULTS ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown
