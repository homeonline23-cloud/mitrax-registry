import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# FORCE BLACK BACKGROUND & GOLIATH BOLD NUMBERS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE INPUT WINDOW STYLING */
    .stTextInput > div > div > input {
        background-color: #111111 !important;
        color: #D4AF37 !important;
        border: 2px solid #D4AF37 !important;
        font-size: 30px !important;
        text-align: center !important;
        font-weight: 900 !important;
    }

    /* THE GOLIATH OUTPUT BOXES */
    .stSuccess, .stError, .stInfo { 
        font-weight: 900 !important; 
        font-size: 22px !important; 
        border-radius: 10px !important;
        border: 2px solid #D4AF37 !important;
        padding: 8px !important;
        color: #FFFFFF !important;
        margin-bottom: 5px !important;
    }
    
    .island-label {
        color: #D4AF37 !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        margin-bottom: 10px !important;
        margin-top: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING & MISSION (RESTORED) ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# THE FULL MISSION SHIELD
st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 15px; padding: 20px; background-color: #111111; margin: 20px auto; max-width: 800px;'>
        <p style='color: #FFFFFF; font-size: 16px; font-weight: 900; line-height: 1.6;'>
            The 4-digit Prediction Calculator that can be used Globally. <br>
            By entering the 4 chosen winning numbers into the calculator Grids. <br>
            When analyzing the symmetry patterns, you can see and identify potential 
            winning numbers in the GRID’s. <br>
            <span style='color: #D4AF37;'>There’s now a 95% chance of increasing your chances of winning.</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 3. THE WINDOW OF CHOICE ---
_, input_col, _ = st.columns([1, 1, 1])
with input_col:
    st.markdown("<h3 style='color: #FFFFFF;'>ENTER 4 NUMBERS TO START</h3>", unsafe_allow_html=True)
    member_numbers = st.text_input("", placeholder="0000", max_chars=4, key="master_input")

st.write("---")

# --- 4. THE 4 PILLARS (RESTORED TO 3 ROWS EACH) ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>LATEST DRAW RESULTS</h4>", unsafe_allow_html=True)

colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True)
    st.success(member_numbers if member_numbers else "1862") # 1st Row follows Input
    st.success("0801") # 2nd Row
    st.success("9394") # 3rd Row
with colB:
    st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True)
    st.success("2544")
    st.success("8732")
    st.success("7296")
with colC:
    st.markdown("<p class='island-label'>CURAÇAO</p>", unsafe_allow_html=True)
    st.success("7716")
    st.success("5502")
    st.success("5918")
with colD:
    st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True)
    st.success("3076")
    st.success("8561")
    st.success("3465")

st.write("---")

# --- 5. THE SYMMETRY BALANCE ---
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")
