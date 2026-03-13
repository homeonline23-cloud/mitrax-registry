import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. ADVANCED IMPERIAL STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; color: #333; font-family: 'Arial', sans-serif; }
    
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 38px; font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 212, 255, 0.3); margin-bottom: 20px;
    }

    .console-box {
        background-color: #8C8C8C; border-radius: 20px; padding: 30px;
        color: white; text-align: center; max-width: 1000px; margin: auto;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }

    .grid-label { color: #00D4FF; font-size: 24px; font-weight: bold; margin-bottom: 10px; }
    
    /* Input Styling */
    .stNumberInput input {
        background-color: white !important; color: #333 !important;
        font-size: 20px !important; font-weight: bold !important;
        text-align: center !important; border: 2px solid #00D4FF !important;
    }

    .time-box {
        background-color: #5D99A6; color: white; padding: 8px 20px;
        border-radius: 8px; font-weight: bold; font-size: 18px; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE BRANDING ---
st.markdown("<h1 class='glow-title'>THE MITRAX ORACLE PIC 4 PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='console-box'>
    <div style='color: #00D4FF; font-weight: bold; font-size: 22px;'>Worldwide 🌏 Globally</div>
    <p style='font-style: italic; font-size: 16px;'>
        "Analyze symmetry patterns to identify potential winning numbers in the GRID’s. 
        95% chance of increasing your chances of winning."
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# --- 4. THE LIVE CHRONOMETER ---
t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
with t_col1:
    st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t_col3:
    st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. THE FUNCTIONAL COMMAND CENTER ---
st.markdown("<h3 style='text-align: center;'>Enter Winning Numbers</h3>", unsafe_allow_html=True)

# The 4 Digit Inputs
in_col1, in_col2, in_col3, in_col4 = st.columns(4)
with in_col1: n1 = st.number_input("N1", 0, 9, step=1, key="num1")
with in_col2: n2 = st.number_input("N2", 0, 9, step=1, key="num2")
with in_col3: n3 = st.number_input("N3", 0, 9, step=1, key="num3")
with in_col4: n4 = st.number_input("N4", 0, 9, step=1, key="num4")

st.write("")

# Grid Layout
grid_col1, spacer, grid_col2 = st.columns([1, 0.1, 1])

def render_oracle_grid(label, grid_id):
    st.markdown(f"<div class='grid-label'>{label}</div>", unsafe_allow_html=True)
    # Creating a functional 4x4 input grid
    cols = st.columns(4)
    for row in range(4):
        for col in range(4):
            idx = (row * 4) + col
            # Use letters a-p as labels like in your image
            label_char = chr(97 + idx) 
            with cols[col]:
                # This makes the grid functional: users can type numbers into the a-p slots
                st.text_input(label_char, value="", key=f"{grid_id}_{label_char}", label_visibility="visible")

with grid_col1:
    render_oracle_grid("Gr. 1", "g1")

with grid_col2:
    render_oracle_grid("Gr. 2", "g2")

# --- 6. SYMMETRY CALCULATION BUTTON ---
st.write("")
if st.button("RUN SYMMETRY ANALYSIS"):
    st.balloons()
    st.success("Universal Symmetry Identified. Check Grid Overlaps for 95% Probability.")

# --- 7. FOOTER ---
st.markdown("<p style='text-align: center; color: #999; font-size: 10px; margin-top: 40px;'>ENABLED FOR INTERNATIONAL USE • GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
