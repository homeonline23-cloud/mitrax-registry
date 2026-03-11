import streamlit as st
from datetime import datetime

# --- 1. THE IMPERIAL ENGINE CONFIG ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, h4, p, div { text-align: center !important; font-family: 'Arial Black', Gadget, sans-serif; }
    
    .gold-pillar { background-color: #D4AF37; width: 14px; height: 210px; margin: 0 auto; border-radius: 5px; border: 2px solid #000000; }
    .matrix-cell { 
        font-weight: 900; font-size: 18px; border: 1px solid #000000; 
        aspect-ratio: 1/1; display: flex; align-items: center; justify-content: center; 
        border-radius: 4px; margin: 2px; color: #000000; height: 45px; width: 45px;
    }
    .red-target { border: 3px solid #FF0000; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; }
    .blue-target { border: 3px solid #0000FF; border-radius: 50%; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; }
    
    .grid-light { background-color: #D3D3D3 !important; }
    .grid-dark { background-color: #707070 !important; }
    .island-label { color: #D4AF37; font-weight: 900; font-size: 16px; text-transform: uppercase; margin-bottom: 5px; }

    .stTextInput > div > div > input { 
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 4px solid #D4AF37 !important; font-size: 28px !important; 
        text-align: center !important; height: 70px !important; width: 140px !important;
        padding: 0px !important; font-weight: 900 !important; border-radius: 10px !important;
    }
    .symmetry-bridge { color: #D4AF37; font-size: 26px; font-weight: 900; margin-bottom: 20px; border-bottom: 3px solid #D4AF37; display: inline-block; padding: 0 20px; }
    .grid-drop { margin-top: 145px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE MITRAX IMPERIAL STRATEGY CHART (BANNER) ---
# Direct Link Restore - The Imperial Crown
st.image("https://files.oaiusercontent.com/file-92csyc92csyc92cs", use_container_width=True, caption="MITRAX STRATEGY CHART")

# --- 3. WINNING NUMBERS BOARD ---
st.write("---")
res_cols = st.columns(4)
res_data = [("ARUBA", ["1862", "0801"]), ("BONAIRE", ["2544", "8732"]), ("CURAÇAO", ["7716", "5502"]), ("ST. MARTIN", ["3076", "8561"])]
for i, (name, nums) in enumerate(res_data):
    with res_cols[i]:
        st.markdown(f"<p class='island-label'>{name}</p>", unsafe_allow_html=True)
        for n in nums: st.success(n)

# --- 4. THE MASTER SYMMETRY DECK ---
st.write("---")
def draw_grid(val, color, target=None):
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target" if is_m and target=="red" else "blue-target" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell {color}'><div class='{circle}'>{txt}</div></div>" if circle else f"<div class='matrix-cell {color}'>{txt}</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

st.markdown("<center><div class='symmetry-bridge'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)

c1, p1, c2, mid, c3, p3, c4 = st.columns([4, 2, 4, 1, 4, 2, 4])

with c1:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 1</p>", unsafe_allow_html=True)
    r_val = st.session_state.get('vr_restore', "")
    draw_grid(r_val, "grid-light", "red")
    st.markdown("</div>", unsafe_allow_html=True)

with p1:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    r_val = st.text_input("", placeholder="****", max_chars=4, key="vr_restore", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 2</p>", unsafe_allow_html=True)
    b_val = st.session_state.get('vb_restore', "")
    draw_grid(b_val, "grid-light", "blue")
    st.markdown("</div>", unsafe_allow_html=True)

with mid:
    st.write("") 

with c3:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
    st.markdown("</div>", unsafe_allow_html=True)

with p3:
    st.write("<div style='height:25px;'></div>", unsafe_allow_html=True)
    b_val = st.text_input("", placeholder="****", max_chars=4, key="vb_restore", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar'></div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='grid-drop'>", unsafe_allow_html=True)
    st.markdown("<p class='island-label'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid("", "grid-dark")
    st.markdown("</div>", unsafe_allow_html=True)
