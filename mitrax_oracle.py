import streamlit as st

# --- 1. IMPERIAL PAGE CONFIG (CENTERED ALIGNMENT) ---
st.set_page_config(layout="centered")

# --- 2. THE BRANDING (CENTERED) ---
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)

# --- 3. THE EXPLAINER SHIELD ---
st.markdown("""
    <div style='border: 2px solid #D4AF37; border-radius: 10px; padding: 15px; background-color: #0e1117; text-align: center; margin-bottom: 25px;'>
        <p style='color: white; font-size: 15px; margin: 0;'>
            The 4-digit Prediction Calculator for Global symmetry patterns. 
            <b>95% chance</b> of increasing your success.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE 4-ISLAND SENSORS (NAME ABOVE 3 ROWS) ---
# We use a 4-pillar layout centered on the page
colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>ARUBA</p>", unsafe_allow_html=True)
    st.success("1862")
    st.success("0801")
    st.success("9394")

with colB:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>BONAIRE</p>", unsafe_allow_html=True)
    st.success("2544")
    st.success("8732")
    st.success("7296")

with colC:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>CURAÇAO</p>", unsafe_allow_html=True)
    st.success("7716")
    st.success("5502")
    st.success("5918")

with colD:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>ST. MARTIN</p>", unsafe_allow_html=True)
    st.success("3076")
    st.success("8561")
    st.success("3465")

st.write("---")

# --- 5. THE CALIBRATION ENGINE (7/1 & 8/3 CENTERED) ---
st.markdown("<h5 style='text-align: center; color: #D4AF37;'>SYMMETRY LOCK</h5>", unsafe_allow_html=True)

# We use 3 columns here to "Push" the Red and Blue into the center
# [1, 2, 1] means the side columns are empty spacers
left_gap, center_content, right_gap = st.columns([1, 4, 1])

with center_content:
    inner_c1, inner_c2 = st.columns(2)
    inner_c1.error("7 / 1")
    inner_c2.info("8 / 3")

# --- 6. SYSTEM STATUS ---
st.write("---")
st.markdown("<p style='text-align: center; color: #555;'>System Status: Online | Balance: Stabilized</p>", unsafe_allow_html=True)
