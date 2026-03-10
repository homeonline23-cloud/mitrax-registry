import streamlit as st

# --- 1. IMPERIAL PAGE CONFIG ---
st.set_page_config(layout="centered", page_title="MITRAX ORACLE")

# --- 2. THE BRANDING (TOP WINDOW) ---
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #D4AF37;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# --- 3. THE UPDATED MISSION STATEMENT (CENTERED) ---
st.markdown("""
    <div style='border: 2px solid #D4AF37; border-radius: 10px; padding: 20px; background-color: #0e1117; text-align: center; margin-bottom: 30px;'>
        <p style='color: white; font-size: 16px; line-height: 1.6;'>
            The 4-digit Prediction Calculator that can be used Globally. 
            By entering the 4 chosen winning numbers into the calculator Grids. 
            When analyzing the symmetry patterns, you can see and identify potential 
            winning numbers in the GRID’s. There’s now a <b>95% chance</b> of increasing 
            your chances of winning.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE 4-ISLAND PILLARS (CENTERED) ---
st.markdown("<h4 style='text-align: center; color: #D4AF37;'>LATEST DRAW RESULTS</h4>", unsafe_allow_html=True)
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

# --- 5. THE SYMMETRY BALANCE (RED/BLUE) ---
# This pushes them to the center
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    inner_left, inner_right = st.columns(2)
    inner_left.error("7 / 1")
    inner_right.info("8 / 3")

# --- 6. SYSTEM STATUS ---
st.write("---")
st.markdown("<p style='text-align: center; color: #555;'>Status: Online | Branch: Main | Symmetry: 95%</p>", unsafe_allow_html=True)
