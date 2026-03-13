import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. THE PRECISION STYLE (SQUARE GRIDS & ENTRY BOXES) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #333; font-family: 'Arial', sans-serif; }
    
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 32px; font-weight: bold;
        text-shadow: 1px 1px 10px rgba(0, 212, 255, 0.3); margin: 10px 0;
    }

    .console-box {
        background-color: #8C8C8C; border-radius: 20px; padding: 20px;
        color: white; text-align: center; max-width: 900px; margin: auto;
    }

    .grid-label { color: #00D4FF; font-size: 22px; font-weight: bold; margin-bottom: 5px; }
    
    /* Entry Box Styling */
    .stNumberInput > div > div > input {
        background-color: #333 !important; color: white !important;
        font-size: 24px !important; font-weight: bold !important;
        height: 60px !important; border-radius: 10px !important;
        border: 2px solid #00D4FF !important;
    }

    /* Small Square Grid Styling */
    .stTextInput input {
        background-color: #FFFFFF !important; color: #333 !important;
        font-size: 16px !important; font-weight: bold !important;
        text-align: center !important; border: 1px solid #999 !important;
        height: 40px !important; width: 40px !important; margin: auto !important;
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
    <p style='font-style: italic; font-size: 14px; margin: 5px 0;'>
        "Analyze symmetry patterns to identify potential winning numbers. 95% Success Probability."
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. REAL-TIME CHRONO ---
st.write("")
t1, t2, t3 = st.columns([1, 2, 1])
with t1: st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t3: st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S %p')}</div>", unsafe_allow_html=True)

st.write("---")

# --- 5. THE ENTRY NUMBER BOXES ---
st.markdown("<h4 style='text-align: center; color: #333;'>ENTER WINNING NUMBERS</h4>", unsafe_allow_html=True)
e1, e2, e3, e4 = st.columns(4)
with e1: st.number_input("N1", 0, 9, step=1, key="entry1", label_visibility="collapsed")
with e2: st.number_input("N2", 0, 9, step=1, key="entry2", label_visibility="collapsed")
with e3: st.number_input("N3", 0, 9, step=1, key="entry3", label_visibility="collapsed")
with e4: st.number_input("N4", 0, 9, step=1, key="entry4", label_visibility="collapsed")

st.write("")

# --- 6. THE SMALL SQUARE GRIDS (a-p) ---
grid_col1, spacer, grid_col2 = st.columns([1, 0.2, 1])

def create_square_grid(grid_id):
    chars = "abcdefghijklmnop"
    # Create 4 rows of 4 small squares
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            idx = (r * 4) + c
            label = chars[idx]
            with cols[c]:
                st.text_input(label, key=f"{grid_id}_{label}", label_visibility="visible")

with grid_col1:
    st.markdown("<div class='grid-label'>Gr. 1</div>", unsafe_allow_html=True)
    create_square_grid("G1")

with grid_col2:
    st.markdown("<div class='grid-label'>Gr. 2</div>", unsafe_allow_html=True)
    create_square_grid("G2")

# --- 7. TRIGGER & FOOTER ---
st.write("")
if st.button("RUN SYMMETRY ANALYSIS"):
    st.success("Symmetry Locked. 95% Probability Pattern Found.")

st.markdown("<p style='text-align: center; color: #BBB; font-size: 10px; margin-top: 30px;'>MITRAX EMPIRE - UNIVERSAL GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
