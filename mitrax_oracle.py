import streamlit as st

# --- 1. MOBILE OPTIMIZATION & LAYOUT ---
st.set_page_config(page_title="MITRAX ORACLE", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .imp-header { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; text-transform: uppercase; }
    .red-block { background-color: #FF0000; color: white; padding: 20px; text-align: center; font-family: 'Impact'; font-size: 30px; border-radius: 10px; margin: 10px 0; }
    .blue-block { background-color: #0000FF; color: white; padding: 20px; text-align: center; font-family: 'Impact'; font-size: 30px; border-radius: 10px; margin: 10px 0; }
    .grid-label { color: #FFD700; font-family: 'Impact'; font-size: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE TOP ANCHOR ---
st.markdown("<div class='imp-header' style='font-size: 50px;'>MITRAX ORACLE</div>", unsafe_allow_html=True)
if st.button("🚀 JUMP TO 6-GRID MATRIX"):
    st.markdown("<script>window.scrollTo(0, 1500);</script>", unsafe_allow_html=True) # Mobile scroll trigger

# --- 3. IMAGE BROADCAST ---
st.markdown("### 📡 STRATEGY BROADCAST")
img = st.file_uploader("Upload Chart", label_visibility="collapsed")
if img: st.image(img)

st.divider()

# --- 4. THE 5 TARGETS (VERTICAL SCROLL) ---
st.markdown("<h2 style='color:#00FF00; text-align:center;'>★ 5 TARGET WINNERS ★</h2>", unsafe_allow_html=True)
for i in range(1, 6):
    st.text_input(f"TARGET {i}", key=f"t{i}", placeholder="ENTER PICK 4")

st.divider()

# --- 5. THE COLOR PROTOCOL (7/1 & 8/3) ---
st.markdown("<div class='red-block'>SECTOR 7 / 1 : RED ACTIVE</div>", unsafe_allow_html=True)
st.markdown("<div class='blue-block'>SECTOR 8 / 3 : BLUE ACTIVE</div>", unsafe_allow_html=True)

st.divider()

# --- 6. THE 6-GRID MATRIX ---
st.markdown("<div class='imp-header' style='font-size: 35px;'>95% SYMMETRY 6-GRID</div>", unsafe_allow_html=True)
g_cols = st.columns(2) # Stacks nicely on mobile
for i in range(1, 7):
    with g_cols[i%2]:
        st.markdown(f"<div class='grid-label'>GRID SECTOR {i}</div>", unsafe_allow_html=True)
        st.text_input(f"G{i}", label_visibility="collapsed", key=f"grid{i}")

st.divider()

# --- 7. REGIONAL BOARDS (THE BOTTOM) ---
st.markdown("<div class='imp-header'>REGIONAL HISTORY</div>")
islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
for island in islands:
    st.expander(f"📂 {island} DATA STREAM").text_area(f"Input {island} numbers...")
