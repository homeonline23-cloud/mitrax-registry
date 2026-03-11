import streamlit as st

# --- 1. THE MIDNIGHT SYSTEM CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    /* THE 16 SMALL BOXES (4x4 MATRIX CELLS) */
    .matrix-cell {
        background-color: #D4AF37 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        border: 1px solid #000000 !important;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
    }
    
    .island-label { color: #FFFFFF; font-weight: 900; font-size: 18px; text-transform: uppercase; margin-top: 15px; margin-bottom: 5px; }
    
    /* INPUT BOXES */
    .stTextInput > div > div > input {
        background-color: #222222 !important;
        color: #D4AF37 !important;
        border: 2px solid #FFFFFF !important;
        font-size: 22px !important;
        text-align: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. BRANDING & INPUTS ---
st.markdown("<h1 style='color: #D4AF37; margin-bottom: 0;'>MITRAX ORACLE Pic 4 App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #D4AF37; margin-top: 0;'>Pick 4 Worldwide🌏</h2>", unsafe_allow_html=True)

_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    c_left, c_right = st.columns(2)
    c_left.error("7 / 1")
    c_right.info("8 / 3")
    in_left, in_right = st.columns(2)
    val_71 = in_left.text_input("", placeholder="----", key="v71")
    val_83 = in_right.text_input("", placeholder="----", key="v83")

st.write("---")

# --- 3. THE 4 GRIDS (EACH WITH 16 SMALL BOXES) ---
st.markdown("<h4 style='color: #D4AF37; font-weight: 900;'>16-CELL SYMMETRY MATRIX</h4>", unsafe_allow_html=True)
g1, g2, g3, g4 = st.columns(4)

def draw_16_grid(label, main_val):
    st.markdown(f"<p class='island-label'>{label}</p>", unsafe_allow_html=True)
    # This creates the 4x4 internal structure
    for row in range(4):
        cols = st.columns(4)
        for col in range(4):
            # If it's the first cell, show the input, else show a placeholder
            cell_text = main_val if (row == 0 and col == 0 and main_val) else "0"
            cols[col].markdown(f"<div class='matrix-cell'>{cell_text}</div>", unsafe_allow_html=True)

with g1:
    draw_16_grid("GRID 1", val_71)
with g2:
    draw_16_grid("GRID 2", val_83)
with g3:
    draw_16_grid("GRID 3", "")
with g4:
    draw_16_grid("GRID 4", "")
