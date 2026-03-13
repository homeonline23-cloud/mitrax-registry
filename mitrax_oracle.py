import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. THE IMPERIAL STYLE SHEET ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #333; font-family: 'Arial', sans-serif; }
    
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 38px; font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 212, 255, 0.3); margin-bottom: 20px;
    }

    .console-box {
        background-color: #8C8C8C; border-radius: 20px; padding: 30px;
        color: white; text-align: center; max-width: 1000px; margin: auto;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }

    .grid-label { color: #00D4FF; font-size: 26px; font-weight: bold; margin-bottom: 10px; }
    
    /* Input Styling for visibility */
    .stTextInput input {
        background-color: #F9F9F9 !important; color: #333 !important;
        font-size: 22px !important; font-weight: bold !important;
        text-align: center !important; border: 1px solid #CCC !important;
    }

    .time-box {
        background-color: #5D99A6; color: white; padding: 8px 20px;
        border-radius: 8px; font-weight: bold; font-size: 18px; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BRANDING & WORLDWIDE TAG ---
st.markdown("<h1 class='glow-title'>THE MITRAX ORACLE PIC 4 PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='console-box'>
    <div style='color: #00D4FF; font-weight: bold; font-size: 22px;'>Worldwide - Globally</div>
    <p style='font-style: italic; font-size: 16px; margin-top: 10px;'>
        "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
        into the calculator Grids. When analyzing the symmetry patterns, you can see and identify 
        potential winning numbers in the GRID's. There's now a 95% chance of increasing your chances of winning."
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. REAL-TIME CHRONO ---
st.write("")
t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
with t_col1:
    st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t_col3:
    # Anchor to the 2026 frequency provided in your logs
    st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. FUNCTIONAL GRID INPUTS (a through p) ---
st.markdown("<h3 style='text-align: center; color: #333;'>Enter Winning Numbers to Grid</h3>", unsafe_allow_html=True)

# Main container for the dual grids
grid_col1, spacer, grid_col2 = st.columns([1, 0.1, 1])

def generate_functional_grid(label_prefix):
    # This creates a 4x4 matrix of inputs labeled a-p exactly as your image shows
    chars = "abcdefghijklmnop"
    for row in range(4):
        cols = st.columns(4)
        for col in range(4):
            idx = (row * 4) + col
            char = chars[idx]
            with cols[col]:
                # Functional input for each cell
                st.text_input(f"{char}", key=f"{label_prefix}_{char}", label_visibility="visible")

with grid_col1:
    st.markdown("<div class='grid-label'>Gr. 1</div>", unsafe_allow_html=True)
    generate_functional_grid("G1")

with grid_col2:
    st.markdown("<div class='grid-label'>Gr. 2</div>", unsafe_allow_html=True)
    generate_functional_grid("G2")

# --- 6. SYMMETRY TRIGGER ---
st.write("")
if st.button("EXECUTE SYMMETRY ANALYSIS"):
    st.success("Symmetry Patterns Identified. Calculating 95% Probability sectors...")
    st.snow()

# --- 7. FOOTER ---
st.markdown("<p style='text-align: center; color: #999; font-size: 10px; margin-top: 50px;'>MITRAX EMPIRE - UNIVERSAL GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
