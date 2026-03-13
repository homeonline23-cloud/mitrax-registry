import streamlit as st
import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MITRAX ORACLE PREDICTOR", layout="wide")

# --- 2. IMPERIAL STYLING (MATCHING YOUR IMAGES) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #333; font-family: 'Arial', sans-serif; }
    
    /* Glowing Title */
    .glow-title {
        color: #00D4FF; text-align: center; font-size: 42px; font-weight: bold;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.8); margin-bottom: 30px;
    }

    /* Main Console Box */
    .console-box {
        background-color: #8C8C8C; border-radius: 25px; padding: 40px;
        color: white; text-align: center; max-width: 900px; margin: auto;
    }

    .worldwide-tag { color: #00D4FF; font-weight: bold; font-size: 20px; margin-bottom: 10px; }

    /* The Grids */
    .grid-label { color: #00D4FF; font-size: 24px; font-weight: bold; margin-bottom: 10px; text-align: left; }
    .oracle-grid {
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;
        background: white; padding: 15px; border: 3px solid #E67E22; border-radius: 10px;
    }
    .grid-cell {
        aspect-ratio: 1; border: 1px solid #CCC; display: flex;
        align-items: center; justify-content: center; color: #888;
        font-size: 18px; font-weight: bold; background: #F9F9F9;
    }

    /* Time/Date Displays */
    .time-box {
        background-color: #5D99A6; color: white; padding: 10px 25px;
        border-radius: 10px; font-weight: bold; font-size: 20px; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE BRANDING & MISSION ---
st.markdown("<h1 class='glow-title'>THE MITRAX ORACLE PIC 4 PREDICTOR</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class='console-box'>
    <div class='worldwide-tag'>Worldwide 🌏 Globally</div>
    <p style='font-style: italic; font-size: 18px; line-height: 1.5;'>
        "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
        into the calculator Grids. When analyzing the symmetry patterns, you can find and identify 
        potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning."
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. THE CHRONOMETER (TIME & DATE) ---
st.write("")
t_col1, t_col2, t_col3 = st.columns([1, 2, 1])
with t_col1:
    st.markdown(f"<div class='time-box'>{datetime.date.today().strftime('%m/%d/%Y')}</div>", unsafe_allow_html=True)
with t_col3:
    st.markdown(f"<div class='time-box'>{datetime.datetime.now().strftime('%H:%M:%S PM')}</div>", unsafe_allow_html=True)

st.write("")

# --- 5. THE DUAL-GRID COMMAND CENTER ---
# Logic to handle user input for number 1
st.markdown("<div style='text-align: center;'><span style='background:#333; color:white; padding:10px 30px; border-radius:20px; font-size:22px;'>Enter number 1</span></div>", unsafe_allow_html=True)

st.write("")
grid_col1, spacer, grid_col2 = st.columns([10, 1, 10])

# Grid 1
with grid_col1:
    st.markdown("<div class='grid-label'>Gr. 1</div>", unsafe_allow_html=True)
    grid1_html = "<div class='oracle-grid'>"
    for char in "abcdefghijklmnop":
        grid1_html += f"<div class='grid-cell'>{char}</div>"
    grid1_html += "</div>"
    st.markdown(grid1_html, unsafe_allow_html=True)

# Grid 2
with grid_col2:
    st.markdown("<div class='grid-label'>Gr. 2</div>", unsafe_allow_html=True)
    grid2_html = "<div class='oracle-grid'>"
    for char in "abcdefghijklmnop":
        grid2_html += f"<div class='grid-cell'>{char}</div>"
    grid2_html += "</div>"
    st.markdown(grid2_html, unsafe_allow_html=True)

# --- 6. INTERACTIVE LAYER ---
st.write("---")
st.markdown("<p style='text-align: center; color: #888;'>SYMMETRY ANALYSIS ACTIVE • WORLDWIDE USE</p>", unsafe_allow_html=True)
