import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-text { color: #FFFFFF; font-size: 15px; font-weight: 900; margin-bottom: 20px; padding: 10px; border: 1px solid #D4AF37; border-radius: 10px; }

    /* SLEEK DATE CIRCLES (AS PER FIRST IMAGE) */
    .date-circle-red {
        border: 3px solid #FF0000; border-radius: 50%; color: #FF0000;
        font-size: 24px; font-weight: 900; width: 50px; height: 50px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 3px solid #0000FF; border-radius: 50%; color: #0000FF;
        font-size: 24px; font-weight: 900; width: 50px; height: 50px;
        display: flex; align-items: center; justify-content: center;
        margin: 5px auto; background-color: #FFFFFF;
    }
    .date-display { color: #D4AF37; font-size: 20px; font-weight: 900; margin-top: 20px; }

    /* GRID & MATRIX */
    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 10px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 5px; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 16px; text-transform: uppercase; }
    .stSuccess { font-weight: 900; font-size: 20px; border: 1px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 2px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. TOP SECTION ---
st.markdown("<h1 style='color: #D4AF37;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)
st.markdown("<div class='mission-text'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>", unsafe_allow_html=True)

# --- 3. WINNING NUMBERS BOARD ---
st.markdown("<h4 style='color: #D4AF37;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True); st.success("1862"); st.success("0801"); st.success("9394")
with c2: st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True); st.success("2544"); st.success("8732"); st.success("7296")
with c3: st.markdown("<p class='island-label'>CURAÇAO</p>", unsafe_allow_html=True); st.success("7716"); st.success("5502"); st.success("5918")
with c4: st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True); st.success("3076"); st.success("8561"); st.success("3465")

# --- 4. THE SLEEK DATE ANCHOR (UNDER THE BOARD) ---
st.write("---")
d_col1, d_col2, d_col3 = st.columns([1, 2, 1])
with d_col1:
    st.markdown("<div class='date-circle-red'>7</div>", unsafe_allow_html=True)
    st.markdown("<div class='date-circle-red'>2</div>", unsafe_allow_html=True)
with d_col2:
    curr_date = datetime.now().strftime("%m/%d/%Y")
    st.markdown(f"<div class='date-display'>Date: {curr_date}</div>", unsafe_allow_html=True)
with d_col3:
    st.markdown("<div class='date-circle-blue'>8</div>", unsafe_allow_html=True)
    st.markdown("<div class='date-circle-blue'>3</div>", unsafe_allow_html=True)

# --- 5. INPUTS ---
st.write("---")
_, in_center, _ = st.columns([1, 2, 1])
with in_center:
    il, ir = st.columns(2)
    val_71 = il.text_input("", placeholder="RED IN", max_chars=4, key="v71")
    val_83 = ir.text_input("", placeholder="BLUE IN", max_chars=4, key="v83")

# --- 6. GRIDS ---
def draw_radar_grid(main_val, color_class, target_type=None):
    for row in range(4):
        inner_cols = st.columns(4)
        for col in range(4):
            is_match = (row == 0 and col == 0 and main_val)
            circle_style = "red-circle" if is_match and target_type == "red" else "blue-circle" if is_match and target_type == "blue" else ""
            cell_content = main_val if is_match else "0"
            content = f"<div class='{circle_style}'>{cell_content}</div>" if circle_style else cell_content
            inner_cols[col].markdown(f"<div class='matrix-cell {color_class}'>{content}</div>", unsafe_allow_html=True)

st.markdown("<h4 style='color: #D4AF37;'>SYMMETRY MATRIX SENSORS</h4>", unsafe_allow_html=True)
g1, p1, g2, p2, g3, p3, g4 = st.columns([4, 0.5, 4, 0.5, 4, 0.5, 4])
with g1: draw_radar_grid(val_71, "grid-light", "red")
with p1: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g2: draw_radar_grid(val_83, "grid-light", "blue")
with p2: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g3: draw_radar_grid("", "grid-dark")
with p3: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g4: draw_radar_grid("", "grid-dark")
