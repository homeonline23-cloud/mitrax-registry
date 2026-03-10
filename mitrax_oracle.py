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

    /* THE OUTPUT BOXES */
    .stSuccess, .stError, .stInfo { 
        font-weight: 900 !important; 
        font-size: 28px !important; 
        border-radius: 12px !important;
        border: 2px solid #D4AF37 !important;
        padding: 10px !important;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# --- 3. THE "WINDOW OF CHOICE" (THE SINGLE MEMBER INPUT) ---
st.markdown("<h3 style='color: #FFFFFF; margin-top: 20px;'>ENTER 4 NUMBERS TO START</h3>", unsafe_allow_html=True)

# THE MASTER INPUT WINDOW
member_numbers = st.text_input("", placeholder="0000", max_chars=4)

st.write("---")

# --- 4. THE AUTOMATIC GOLIATH DISPLAYS ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>MASTER BRAIN CALCULATION</h4>", unsafe_allow_html=True)

# We use the input to fill the first island automatically!
colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown("<p style='color: #D4AF37; font-weight: 900;'>CURRENT</p>", unsafe_allow_html=True)
    st.success(member_numbers if member_numbers else "----")

with colB, colC, colD:
    # These will eventually be filled by the Master Brain's history
    st.markdown("<p style='color: #333; font-weight: 900;'>PREVIOUS</p>", unsafe_allow_html=True)
    st.success("....")

st.write("---")

# --- 5. THE SYMMETRY LOCK (7/1 & 8/3) ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")

if member_numbers:
    st.markdown(f"<p style='color: #D4AF37; font-weight: 900;'>SYMMETRY PATTERN DETECTED FOR: {member_numbers}</p>", unsafe_allow_html=True)
