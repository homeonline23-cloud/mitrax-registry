import streamlit as st

# --- 1. THE IMPERIAL BRANDING (PAYPAL MATCH) ---
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)

# --- 2. THE EXPLAINER SHIELD ---
st.markdown("""
    <div style='border: 2px solid #D4AF37; border-radius: 10px; padding: 15px; background-color: #0e1117; text-align: center; margin-bottom: 25px;'>
        <p style='color: white; font-size: 15px; margin: 0;'>
            The 4-digit Prediction Calculator for Global symmetry patterns. 
            <b>95% chance</b> of increasing your success.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 3. THE 4-ISLAND SENSORS (NAME ABOVE 3 ROWS) ---
# We create 4 columns for the 4 territories
colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>ARUBA</p>", unsafe_allow_html=True)
    st.success("1862") # Row 1
    st.success("0801") # Row 2
    st.success("9394") # Row 3

with colB:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>BONAIRE</p>", unsafe_allow_html=True)
    st.success("2544") # Row 1
    st.success("8732") # Row 2
    st.success("7296") # Row 3

with colC:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>CURAÇAO</p>", unsafe_allow_html=True)
    st.success("7716") # Row 1
    st.success("5502") # Row 2
    st.success("5918") # Row 3

with colD:
    st.markdown("<p style='text-align: center; color: #D4AF37; font-weight: bold;'>ST. MARTIN</p>", unsafe_allow_html=True)
    st.success("3076") # Row 1
    st.success("8561") # Row 2
    st.success("3465") # Row 3

st.write("---")

# --- 4. THE CALIBRATION ENGINE (RED/BLUE BLOCKS) ---
st.markdown("<h5 style='text-align: center; color: #D4AF37;'>SYMMETRY LOCK</h5>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.error("7 / 1")
with c2:
    st.info("8 / 3")

# --- 5. SYSTEM STATUS ---
st.markdown("<p style='text-align: center; color: #555;'>System Status: Online | Branch: Main</p>", unsafe_allow_html=True)
