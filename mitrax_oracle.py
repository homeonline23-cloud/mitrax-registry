import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. PRECISION STYLING (SQUARE GRIDS & SINGLE ENTRY) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #333; font-family: 'Arial', sans-serif; }
    
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 32px; font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 212, 255, 0.3); margin-top: 10px;
    }

    .console-box {
        background-color: #8C8C8C; border-radius: 20px; padding: 20px;
        color: white; text-align: center; max-width: 900px; margin: auto;
    }

    /* Entry Box - The Main Hook */
    .stNumberInput > div > div > input {
        background-color: #333 !important; color: #00FF00 !important;
        font-size: 28px !important; font-weight: bold !important;
        height: 70px !important; border-radius: 15px !important;
        border: 3px solid #00D4FF !important; text-align: center !important;
    }

    /* Grid Labeling */
    .grid-label { color: #00D4FF; font-size: 24px; font-weight: bold; margin-bottom: 5px; }

    /* The Secret Square Grids (a-p) */
    .stTextInput input {
        background-color: #F0F0F0 !important; color: #333 !important;
        font-size: 14px !important; font-weight: bold !important;
        text-align: center !important; border: 1px solid #CCC !important;
        height: 38px !important; width: 38px !important; margin: auto !important;
        padding: 0 !important;
    }

    .time-box {
        background-color: #5D99A6; color: white; padding: 5px 15px;
        border-radius: 5px; font-weight: bold; font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BRANDING ---
st.markdown("<h1 class='glow-title'>THE MITRAX ORACLE PIC 4 PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='console-box'>
    <div style='color: #00D4FF; font-weight: bold; font-size: 20px;'>Worldwide - Globally</div>
    <p style='font-style: italic; font-size: 14px;'>Symmetry Analysis • 95% Probability • Universal Advantage</p>
</div>
""", unsafe_allow_html=True)

# --- 4. REAL-TIME CHRONO ---
st.write("")
t1, spacer, t3 = st.columns([1, 2, 1])
with t1: st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t3: st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. THE SINGLE ENTRY VAULT (THE SECRET) ---
st.markdown("<h4 style='text-align: center; color: #333;'>Enter Winning Number</h4>", unsafe_allow_html=True)
col_entry = st.columns([1, 1, 1])
with col_entry[1]:
    winning_input = st.number_input("MAIN ENTRY", 0, 9999, key="main_entry", label_visibility="collapsed")

st.write("")

# --- 6. THE SIMULTANEOUS SYMMETRY GRIDS ---
grid_col1, spacer_mid, grid_col2 = st.columns([1, 0.2, 1])

# This logic calculates the symmetry codes based on your input
# As you type in the Main Entry, these values change spontaneously
def get_symmetry_value(char, seed):
    if seed == 0: return ""
    # Simplified Secret Logic: Spontaneous code generation based on input
    return str((ord(char) + seed) % 10)

chars = "abcdefghijklmnop"

with grid_col1:
    st.markdown("<div class='grid-label'>Gr. 1</div>", unsafe_allow_html=True)
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            idx = (r * 4) + c
            char = chars[idx]
            val = get_symmetry_value(char, winning_input)
            with cols[c]:
                st.text_input(char, value=val, key=f"G1_{char}")

with grid_col2:
    st.markdown("<div class='grid-label'>Gr. 2</div>", unsafe_allow_html=True)
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            idx = (r * 4) + c
            char = chars[idx]
            # Mirror Symmetry logic for Grid 2
            val = get_symmetry_value(char, winning_input + 7) 
            with cols[c]:
                st.text_input(char, value=val, key=f"G2_{char}")

# --- 7. FOOTER ---
st.write("---")
st.markdown("<p style='text-align: center; color: #BBB; font-size: 10px;'>MITRAX EMPIRE - UNIVERSAL GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
