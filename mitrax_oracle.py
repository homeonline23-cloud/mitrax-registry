import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="centered", page_title="MITRAX ORACLE")

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
        font-size: 28px !important; 
        border-radius: 12px !important;
        border: 2px solid #D4AF37 !important;
        padding: 10px !important;
        color: #FFFFFF !important;
    }
    
    .island-label {
        color: #D4AF37 !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        margin-bottom: 5px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# --- 3. THE WINDOW OF CHOICE ---
st.markdown("<h3 style='color: #FFFFFF; margin-top: 20px;'>ENTER 4 NUMBERS TO START</h3>", unsafe_allow_html=True)
member_numbers = st.text_input("", placeholder="0000", max_chars=4, key="master_input")

st.write("---")

# --- 4. THE 4 PILLARS RESTORED (MASTER BRAIN CALCULATION) ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>MASTER BRAIN CALCULATION</h4>", unsafe_allow_html=True)

# We use 4 columns to force the islands side-by-side
colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True)
    st.success(member_numbers if member_numbers else "1862")
with colB:
    st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True)
    st.success("2544")
with colC:
    st.markdown("<p class='island-label'>CURAÇAO</p>", unsafe_allow_html=True)
    st.success("7716")
with colD:
    st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True)
    st.success("3076")

st.write("---")

# --- 5. THE SYMMETRY LOCK (CENTERED 7/1 & 8/3) ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")

# SYSTEM STATUS
st.markdown("<p style='color: #444; font-size: 10px; margin-top: 50px;'>Status: Symmetry Stabilized | 95% Engaged</p>", unsafe_allow_html=True)
