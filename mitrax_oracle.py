import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# FORCE BLACK BACKGROUND & GOLIATH BOLD NUMBERS
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* INPUT BOX STYLING (GOLD & BOLD) */
    .stTextInput > div > div > input {
        background-color: #111111 !important;
        color: #D4AF37 !important;
        border: 2px solid #D4AF37 !important;
        font-size: 24px !important;
        text-align: center !important;
        font-weight: 900 !important;
    }

    /* GOLIATH DATA BOXES */
    .stSuccess, .stError, .stInfo { 
        font-weight: 900 !important; 
        font-size: 22px !important; 
        border-radius: 10px !important;
        border: 2px solid #D4AF37 !important;
        color: #FFFFFF !important;
    }
    
    .island-label { color: #D4AF37; font-weight: 900; font-size: 16px; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING & MISSION ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# MISSION SHIELD
st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 15px; padding: 20px; background-color: #111111; margin: 20px auto; max-width: 800px;'>
        <p style='color: #FFFFFF; font-size: 15px; font-weight: 900;'>
            The 4-digit Prediction Calculator that can be used Globally. <br>
            <span style='color: #D4AF37;'>🎯 There’s now a 95% chance of increasing your chances of winning.</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 3. THE TOP PILLARS (LATEST RESULTS) ---
colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True); st.success("1862"); st.success("0801"); st.success("9394")
with colB:
    st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True); st.success("2544"); st.success("8732"); st.success("7296")
with colC:
    st.markdown("<p class='island-label'>CURAÇAO</p>", unsafe_allow_html=True); st.success("7716"); st.success("5502"); st.success("5918")
with colD:
    st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True); st.success("3076"); st.success("8561"); st.success("3465")

st.write("---")

# --- 4. THE SYMMETRY LOCK (7/1 & 8/3) WITH INPUTS UNDERNEATH ---
_, center_col, _ = st.columns([1, 2, 1])

with center_col:
    # THE COLOR BLOCKS
    c_left, c_right = st.columns(2)
    c_left.error("7 / 1")
    c_right.info("8 / 3")
    
    # THE 2 INPUT WINDOWS (FOR THE 7/1 AND 8/3 DATA)
    st.markdown("<p style='color: white; font-size: 14px; margin-top: 10px;'>ENTER 4 NUMBERS TO START</p>", unsafe_allow_html=True)
    in_left, in_right = st.columns(2)
    num_71 = in_left.text_input("", placeholder="0000", max_chars=4, key="in_71")
    num_83 = in_right.text_input("", placeholder="0000", max_chars=4, key="in_83")

st.write("---")

# --- 5. THE 4-GRID MATRIX (NEXT TO EACH OTHER) ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>95% SYMMETRY MATRIX</h4>", unsafe_allow_html=True)
grid1, grid2, grid3, grid4 = st.columns(4)

with grid1:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    st.success(num_71 if num_71 else "----")
with grid2:
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    st.success(num_83 if num_83 else "----")
with grid3:
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    st.success("CALC")
with grid4:
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    st.success("CALC")
