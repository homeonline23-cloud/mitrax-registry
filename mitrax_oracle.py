import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .mission-statement {
        border: 3px solid #D4AF37;
        border-radius: 15px;
        padding: 20px;
        background-color: #111111;
        margin: 10px auto;
        max-width: 900px;
        color: #FFFFFF;
        font-size: 16px;
        font-weight: 900;
    }

    .date-box {
        background-color: #FFFFFF; 
        padding: 15px; 
        border-radius: 15px; 
        margin: 10px auto; 
        max-width: 550px; 
        border: 4px solid #D4AF37;
    }
    
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

    .matrix-cell { font-weight: 900; font-size: 18px; border: 1px solid #000000; aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center; border-radius: 4px; margin: 2px; color: #000000; }
    .red-circle { border: 3px solid #FF0000; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF; border-radius: 50%; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .yellow-pool { background-color: #FFFF00; width: 12px; height: 100%; min-height: 250px; margin: 0 auto; border-radius: 10px; border: 1px solid #D4AF37; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; }
    .stSuccess { font-weight: 900; font-size: 22px; border: 2px solid #D4AF37; color: #000000; background-color: #D4AF37; padding: 5px; }
    .stTextInput > div > div > input { background-color: #111111; color: #D4AF37; border: 2px solid #D4AF37; font-size: 22px; text-align: center; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# --- 2. TOP DECK: MISSION ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class='mission-statement'>
        The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
        into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential 
        winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.
    </div>
""", unsafe_allow_html=True)

# --- 3. RESULTS BOARD ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>WINNING NUMBERS RESULTS</h4>", unsafe_allow_html=True)
colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown("<p class='island-label'>ARUBA</p>", unsafe_allow_html=True); st.success("1862"); st.success("0801"); st.success("9394")
with colB:
    st.markdown("<p class='island-label'>BONAIRE</p>", unsafe_allow_html=True); st.success("2544"); st.success("8732"); st.success("7296")
with colC:
    st.markdown("<p style='color:#D4AF37; font-weight:900;'>CURAÇAO</p>", unsafe_allow_html=True); st.success("7716"); st.success("5502"); st.success("5918")
with colD:
    st.markdown("<p class='island-label'>ST. MARTIN</p>", unsafe_allow_html=True); st.success("3076"); st.success("8561"); st.success("3465")

st.write("---")

# --- 4. THE DATE ANCHOR (NOW UNDER RESULTS) ---
curr_date = datetime.now().strftime("%m/%d/%Y")
st.markdown(f"""
    <div class='date-box'>
        <div style='color:black; font-size:24px; font-weight:900;'>Date: {curr_date}</div>
        <table style='width: 100%; border: none;'>
            <tr>
                <td style='width: 45%; text-align: center;'>
                    <div class='date-circle-red'>7</div>
                    <div class='date-circle-red'>2</div>
                </td>
                <td style='width: 10%;'></td>
                <td style='width: 45%; text-align: center;'>
                    <div class='date-circle-blue'>8</div>
                    <div class='date-circle-blue'>3</div>
                </td>
            </tr>
        </table>
    </div>
""", unsafe_allow_html=True)

# --- 5. INPUTS ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    in_left, in_right = st.columns(2)
    val_71 = in_left.text_input("", placeholder="RED IN", max_chars=4, key="v71")
    val_83 = in_right.text_input("", placeholder="BLUE IN", max_chars=4, key="v83")

st.write("---")

# --- 6. GRIDS ---
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
            display_html = f"<div class='matrix-cell {color_class}'><div class='{circle_style}'>{cell_content}</div></div>" if circle_style else f"<div class='matrix-cell {color_class}'>{cell_content}</div>"
            inner_cols[col].markdown(display_html, unsafe_allow_html=True)

g1, p1, g2, p2, g3, p3, g4 = st.columns([4, 0.5, 4, 0.5, 4, 0.5, 4])
with g1:
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    draw_radar_grid(val_71, "grid-light", "red")
with p1: st.markdown("<div class='yellow-pool'></div>", unsafe_allow_html=True)
with g2:
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    draw_radar_grid(val_83, "grid-light", "blue")
with p2: st.markdown("<div class='yellow-pool'>
                     
