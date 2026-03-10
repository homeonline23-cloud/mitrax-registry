import streamlit as st

# --- 1. IMPERIAL PAGE CONFIG ---
st.set_page_config(layout="centered", page_title="MITRAX ORACLE")

# --- 2. THE BRANDING (BOLD & CENTERED FOR SUNLIGHT) ---
st.markdown("<h1 style='text-align: center; color: #D4AF37; font-weight: 900; text-transform: uppercase;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #D4AF37; font-weight: 800;'>PICK 4 WORLDWIDE 🌏</h2>", unsafe_allow_html=True)

# --- 3. THE MISSION SHIELD (HIGH CONTRAST) ---
st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 12px; padding: 20px; background-color: #000000; text-align: center; margin-bottom: 30px;'>
        <p style='color: #FFFFFF; font-size: 18px; font-weight: 900; line-height: 1.4;'>
            THE 4-DIGIT PREDICTION CALCULATOR THAT CAN BE USED GLOBALLY. <br><br>
            BY ENTERING THE 4 CHOSEN WINNING NUMBERS INTO THE CALCULATOR GRIDS, 
            YOU CAN IDENTIFY POTENTIAL WINNING NUMBERS. <br><br>
            THERE’S NOW A <span style='color: #D4AF37;'>95% CHANCE</span> OF INCREASING YOUR SUCCESS!
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE 4-ISLAND PILLARS (BOLD & CENTERED) ---
st.markdown("<h3 style='text-align: center; color: #D4AF37; font-weight: 900;'>LATEST DRAW RESULTS</h3>", unsafe_allow_html=True)

# CSS TO FORCE CENTERED BOLD TEXT IN MOBILE
st.markdown("""
    <style>
    div[data-testid="stMetricValue"] > div { text-align: center; font-weight: 900 !important; }
    .stSuccess, .stError, .stInfo { font-weight: 900 !important; text-align: center !important; font-size: 20px !important; }
    </style>
""", unsafe_allow_html=True)

colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: 900;'>ARUBA</p>", unsafe_allow_html=True)
    st.success("1862")
    st.success("0801")
    st.success("9394")
with colB:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: 900;'>BONAIRE</p>", unsafe_allow_html=True)
    st.success("2544")
    st.success("8732")
    st.success("7296")
with colC:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: 900;'>CURAÇAO</p>", unsafe_allow_html=True)
    st.success("7716")
    st.success("5502")
    st.success("5918")
with colD:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: 900;'>ST. MARTIN</p>", unsafe_allow_html=True)
    st.success("3076")
    st.success("8561")
    st.success("3465")

st.write("---")

# --- 5. THE SYMMETRY BALANCE (CENTERED & BOLD) ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")
