import streamlit as st
import datetime

# --- 1. IMPERIAL PAGE CONFIG ---
st.set_page_config(
    page_title="MITRAX ORACLE PREDICTOR", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE STABILIZED STYLE ENGINE ---
st.markdown("""
    <style>
    /* Force white background and imperial font */
    .stApp { background-color: #FFFFFF; color: #333; font-family: 'Arial', sans-serif; }
    
    /* Title with cyan glow */
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 32px; font-weight: bold;
        text-shadow: 1px 1px 8px rgba(0, 212, 255, 0.4); margin-bottom: 5px;
        text-transform: uppercase;
    }

    /* Grey Console Box */
    .console-box {
        background-color: #8C8C8C; border-radius: 15px; padding: 20px;
        color: white; text-align: center; max-width: 900px; margin: auto;
    }

    .worldwide-tag { 
        color: #00D4FF; font-weight: bold; font-size: 20px; 
        margin-bottom: 10px; display: block;
    }

    /* Shrink the Number Input Box */
    div[data-testid="stNumberInput"] {
        width: 150px !important;
        margin: auto !important;
    }
    
    .stNumberInput input {
        background-color: #EEEEEE !important;
        color: #333 !important;
        font-size: 20px !important;
        font-weight: bold !important;
        text-align: center !important;
        border-radius: 10px !important;
    }

    /* The 16-Block Grid Styling */
    .grid-container {
        display: grid; 
        grid-template-columns: repeat(4, 1fr); 
        gap: 5px; 
        background-color: #FFFFFF; 
        padding: 10px; 
        border: 2px solid #E67E22; /* Orange border as seen in Blueprint */
        border-radius: 8px;
    }

    /* Individual small block (a-p) */
    .stTextInput input {
        height: 35px !important;
        width: 35px !important;
        font-size: 14px !important;
        text-align: center !important;
        padding: 0 !important;
        border: 1px solid #CCC !important;
        background-color: #F9F9F9 !important;
    }

    .time-box {
        background-color: #5D99A6; color: white; padding: 5px 15px;
        border-radius: 5px; font-weight: bold; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE BRANDING (MESSAGE RESTORED) ---
st.markdown("<h1 class='glow-title'>The Mitrax Oracle Pic 4 Predictor</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='console-box'>
    <span class='worldwide-tag'>Worldwide 🌏 Globally</span>
    <p style='font-style: italic; font-size: 15px; margin: 0;'>
        "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
        into the calculator Grids. When analyzing the symmetry patterns, you can find and identify 
        potential winning numbers in the GRID's. There's now a 95% chance of increasing your chances."
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. THE CHRONOMETERS ---
st.write("")
t1, spacer, t3 = st.columns([1, 2, 1])
with t1:
    st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t3:
    st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. THE SMALL ENTRY BOX ---
st.markdown("<p style='text-align: center; font-weight: bold;'>Enter Winning Number</p>", unsafe_allow_html=True)
# Main Entry linked to grid calculation
winning_input = st.number_input("MAIN", 0, 9, key="main_entry", label_visibility="collapsed")

# --- 6. THE DUAL 16-BLOCK GRID SYSTEM ---
st.write("")
grid_col1, spacer_mid, grid_col2 = st.columns([1, 0.1, 1])

# Mapping letters a-p
chars = list("abcdefghijklmnop")

# Function to auto-calculate symmetry based on main entry
def get_sym_val(idx, seed):
    if seed == 0: return ""
    return str((idx + seed) % 10)

with grid_col1:
    st.markdown("<p style='color: #00D4FF; font-weight: bold; font-size: 20px;'>Gr. 1</p>", unsafe_allow_html=True)
    # The Grid-in-a-Block
    with st.container():
        for r in range(4):
            cols = st.columns(4)
            for c in range(4):
                idx = (r * 4) + c
                char = chars[idx]
                val = get_sym_val(idx, winning_input)
                with cols[c]:
                    st.text_input(char, value=val, key=f"G1_{char}")

with grid_col2:
    st.markdown("<p style='color: #00D4FF; font-weight: bold; font-size: 20px;'>Gr. 2</p>", unsafe_allow_html=True)
    # The Grid-in-a-Block
    with st.container():
        for r in range(4):
            cols = st.columns(4)
            for c in range(4):
                idx = (r * 4) + c
                char = chars[idx]
                # Mirror logic for Grid 2
                val = get_sym_val(idx, winning_input + 3)
                with cols[c]:
                    st.text_input(char, value=val, key=f"G2_{char}")

# --- 7. FOOTER ---
st.write("---")
st.markdown("<p style='text-align: center; color: #999; font-size: 10px;'>UNIVERSAL GHOST SYNC [LOCKED]</p>", unsafe_allow_html=True)
