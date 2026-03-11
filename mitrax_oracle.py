import streamlit as st
from datetime import datetime

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

# SEALED STYLE BLOCK
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .date-circle-red {
        border: 4px solid #FF0000;
        border-radius: 50%;
        color: #FF0000;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-circle-blue {
        border: 4px solid #0000FF;
        border-radius: 50%;
        color: #0000FF;
        font-size: 32px;
        font-weight: 900;
        width: 65px;
        height: 65px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 5px auto;
        background-color: #FFFFFF;
    }
    .date-text-header {
        color: #000000;
        background-color: #FFFFFF;
        padding: 5px 15px;
        border-radius: 5px;
        font-size: 24px;
        font-weight: 900;
        display: inline-block;
        margin-bottom: 10px;
    }
    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 12px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 10px; border: 1px solid #D4AF37; }
    .grid-light { background-color: #D3D3D3; }
    .grid-dark { background-color: #707070; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    .stSuccess { font-weight: 900; font-size: 22px; border: 2px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 5px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 22px; text-align: center; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# --- 3. DATE ANCHOR (WHITE BOX) ---
st.markdown("<div style='background-color: #FFFFFF; padding: 20px; border-radius: 15px; margin: 10px auto; max-width: 500px; border: 4px solid #D4AF37;'>", unsafe_allow_html=True)
curr_date = datetime.now().strftime("%m/%d/%Y")
st.markdown(f"<div class='date-text-header'>Date: {curr_date}</div>", unsafe_allow_html=True)

t_col1, t_col2, t_col3 = st.columns([1, 1, 1])
with t_col1:
    st.markdown("<div class='date-circle-red'>7</div>", unsafe_allow_html=True)
    st.markdown("<div class='date-circle-red'>2</div>", unsafe_allow_html=True)
with t_col3:
    st.markdown("<div class='date-circle-blue'>8</div>", unsafe_allow_html=True)
    st.markdown("<div class='date-circle-blue'>3</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("---")

# --- 4. WINNING NUMBERS RESULTS ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
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

# --- 5. THE INPUT ENGINE ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    in_left, in_right = st.columns(2)
    val_71 = in_left.text_input("", placeholder="RED IN", max_chars=4, key="v71")
    val_83 = in_right.text_input("", placeholder="BLUE IN", max_chars=4, key="v83")

st.write("---")

# --- 6. SYMMETRY MATRIX SENSORS ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>SYMMETRY MATRIX SENSORS</h4>", unsafe_allow_html=True)

def draw_radar_grid(main_val, color_class, target_type=None):
    for row in range(4):
        inner_cols = st.columns(4)
        for col in range(4):
            is_match = (row == 0 and col == 0 and main_val)
            circle_style = ""
            if is_match:
                if target_type == "red": circle_style = "red-circle"
                if target_type == "blue": circle_style = "blue-circle"
            cell_content = main_val if is_match else "0"
            if circle_style:
                display_html = f"<div class='matrix-cell {color_class}'><div class='{circle_style}'>{cell_content}</div></div>"
            else:
                display_html = f"<div class='matrix-cell {color_class}'>{cell_content}</div>"
            inner_cols[col].markdown(display_html, unsafe_allow_html=True)

g1, p1, g2, p2, g3, p3, g4 = st.columns([4, 0.5, 4, 0.5, 4, 0.5, 4])

with g1:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_radar_grid(val_71, "grid-light", "red")
with p1: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g2:
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_radar_grid(val_83, "grid-light", "blue")
with p2: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g3:
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_radar_grid("", "grid-dark")
with p3: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g4:
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_radar_grid("", "grid-dark")
