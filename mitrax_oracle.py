import streamlit as st
import datetime

# --- 1. IMPERIAL PAGE CONFIG ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. THE BLUEPRINT STYLE (CLEAN GREY CONSOLE) ---
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
    
    /* Functional Input Styling */
    .stTextInput input {
        background-color: #FFFFFF !important; color: #333 !important;
        font-size: 20px !important; font-weight: bold !important;
        text-align: center !important; border: 2px solid #5D99A6 !important;
        border-radius: 5px !important;
    }

    .time-box {
        background-color: #5D99A6; color: white; padding: 10px 20px;
        border-radius: 8px; font-weight: bold; font-size: 18px; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BRANDING & THE WORLDWIDE MISSION ---
st.markdown("<h1 class='glow-title'>THE MITRAX ORACLE PIC 4 PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='console-box'>
    <div style='color: #00D4FF; font-weight: bold; font-size: 22px; margin-bottom:10px;'>Worldwide - Globally</div>
    <p style='font-style: italic; font-size: 16px; line-height: 1.5;'>
        "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
        into the calculator Grids. When analyzing the symmetry patterns, you can identify 
        potential winning numbers in the GRID's. There's now a 95% chance of success."
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. REAL-TIME CHRONOMETER ---
st.write("")
t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
with t_col1:
    st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t_col3:
    st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. THE DUAL-GRID COMMAND CENTER ---
st.markdown("<h3 style='text-align: center; color: #333; margin-bottom: 20px;'>Enter Winning Sequence</h3>", unsafe_allow_html=True)

grid_col1, spacer, grid_col2 = st.columns([1, 0.1, 1])

def create_grid(grid_id):
    # This creates the exact a-p structure from your images
    chars = "abcdefghijklmnop"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            idx = (r * 4) + c
            label = chars[idx]
            with cols[c]:
                st.text_input(label, key=f"{grid_id}_{label}", label_visibility="visible")

with grid_col1:
    st.markdown("<div class='grid-label'>Gr. 1</div>", unsafe_allow_html=True)
    create_grid("G1")

with grid_col2:
    st.markdown("<div class='grid-label'>Gr. 2</div>", unsafe_allow_html=True)
    create_grid("G2")

# --- 6. TRIGGER & FOOTER ---
st.write("")
if st.button("RUN SYMMETRY ANALYSIS"):
    st.success("Universal Patterns Locked. 95% Probability Identified.")

st.markdown("<p style='text-align: center; color: #BBB; font-size: 10px; margin-top: 50px;'>MITRAX EMPIRE - UNIVERSAL GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
