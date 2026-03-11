import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE MASTER SQUARE CELL */
    .matrix-cell {
        font-weight: 900 !important;
        font-size: 18px !important;
        border: 1px solid #000000 !important;
        aspect-ratio: 1 / 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        margin: 2px;
        color: #000000 !important;
    }
    
    /* TARGET CIRCLES */
    .red-circle { border: 3px solid #FF4B4B !important; border-radius: 50% !important; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }
    .blue-circle { border: 3px solid #0000FF !important; border-radius: 50% !important; width: 85%; height: 85%; display: flex; align-items: center; justify-content: center; }

    /* THE YELLOW POOL DIVIDER */
    .yellow-pool {
        background-color: #FFFF00 !important;
        width: 12px;
        height: 100%;
        min-height: 250px;
        margin: 0 auto;
        border-radius: 10px;
    }

    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-bottom: 5px; }
    
    /* GOLIATH DATA BOXES */
    .stSuccess { font-weight: 900 !important; font-size: 22px !important; border: 2px solid #D4AF37 !important; color: #000000 !important; background-color: #D4AF37 !important; padding: 5px !important; }
    
    /* INPUT BOXES */
    .stTextInput > div > div > input { background-color: #111111 !important; color: #D4AF37 !important; border: 2px solid #D4AF37 !important; font-size: 22px !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE BRANDING & MISSION STATEMENT (RE-WELDED) ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

# THE FULL MISSION STATEMENT BOX
st.markdown("""
    <div style='border: 3px solid #D4AF37; border-radius: 15px; padding: 25px; background-color: #111111; margin: 20px auto; max-width: 900px;'>
        <p style='color: #FFFFFF; font-size: 17px; font-weight: 900; line-height: 1.6;'>
            "The 4-digit Prediction Calculator that can be used Globally. <br>
            By entering the 4 chosen winning numbers into the calculator Grids. <br>
            When analyzing the symmetry patterns, you can see and identify potential 
            winning numbers in the GRID’s. <br>
            <span style='color: #D4AF37; font-size: 19px;'>There’s now a 95% chance of increasing your chances of winning."</span>
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 3. WINNING NUMBERS RESULTS ---
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

# --- 4. THE INPUT ENGINE (STRICT 4-DIGIT) ---
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    c_left, c_right = st.columns(2)
    c_left.error("7 / 1")
    c_right.info("8 / 3")
    in_left, in_right = st.columns(2)
    val_71 = in_left.text_input("", placeholder="----", max_chars=4, key="v71")
    val_83 = in_right.text_input("", placeholder="----", max_chars=4, key="v83")

st.write("---")

# --- 5. THE 4 GRIDS (ISOLATED BY YELLOW POOLS) ---
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
            inner_cols[col].markdown
