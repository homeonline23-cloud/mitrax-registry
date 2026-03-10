import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="centered", page_title="MITRAX ORACLE")

# FORCE BLACK BACKGROUND & SUPERSIZED BOLD NUMBERS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE GOLIATH NUMBERS (Green, Red, Blue Boxes) */
    .stSuccess, .stError, .stInfo { 
        font-weight: 900 !important; 
        font-size: 28px !important; /* SUPERSZIED TO FILL THE WINDOW */
        line-height: 1.2 !important;
        border-radius: 12px !important;
        border: 2px solid #D4AF37 !important;
        padding: 10px !important;
        color: #FFFFFF !important;
    }
    
    /* Ensuring the labels (Aruba, etc) are also thick and clear */
    .island-label {
        color: #D4AF37 !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        margin-bottom: 5px !important;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE TITLES ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #D4AF37; margin-top: 0;'>PICK 4 WORLDWIDE 🌏</h3>", unsafe_allow_html=True)

# --- 3. THE MISSION SHIELD ---
st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 15px; padding: 20px; background-color: #111111; margin-bottom: 30px;'>
        <p style='color: #FFFFFF; font-size: 18px; font-weight: 900;'>
            THE 4-DIGIT PREDICTION CALCULATOR FOR GLOBAL USE. <br>
            <span style='color: #D4AF37; font-size: 24px;'>🎯 95% CHANCE OF SUCCESS</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE 4-ISLAND PILLARS (GOLIATH NUMBERS) ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>LATEST DRAW RESULTS</h4>", unsafe_allow_html=True)

colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True)
    st.success("1862")
    st.success("0801")
    st.success("9394")
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

# --- 5. THE SYMMETRY BALANCE (CENTERED & MASSIVE) ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")
