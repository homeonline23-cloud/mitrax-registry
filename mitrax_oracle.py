import streamlit as st

# --- 1. THE IMPERIAL BRANDING (PAYPAL MATCH) ---
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)

# --- 2. THE EXPLAINER SHIELD (SO MEMBERS UNDERSTAND) ---
st.markdown("""
    <div style='border: 2px solid #D4AF37; border-radius: 10px; padding: 15px; background-color: #0e1117; text-align: center; margin-bottom: 20px;'>
        <h4 style='color: #D4AF37; margin-top: 0;'>THE 95% SYMMETRY CALCULATOR</h4>
        <p style='color: white; font-size: 15px; line-height: 1.6;'>
            The 4-digit Prediction Calculator that can be used Globally. 
            By entering the 4 chosen winning numbers into the calculator Grids, 
            you can analyze symmetry patterns to identify potential winning numbers. 
            There’s now a <b>95% chance</b> of increasing your chances of winning.
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --- 3. THE CALIBRATION ENGINE (RED/BLUE BLOCKS) ---
st.markdown("<h5 style='text-align: center; color: #D4AF37;'>7/1 & 8/3 SYMMETRY</h5>", unsafe_allow_html=True)

# This creates the side-by-side blocks for the iPhone
c1, c2 = st.columns(2)
with c1:
    st.error("7 / 1") # THE RED SUN
with c2:
    st.info("8 / 3")  # THE BLUE OCEAN

# --- 4. THE COMMAND DECK (READY FOR DATA) ---
st.write("---")
st.markdown("<p style='text-align: center; color: #D4AF37;'>System Status: Online | Branch: Main</p>", unsafe_allow_html=True)
