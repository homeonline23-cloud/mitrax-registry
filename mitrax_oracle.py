import streamlit as st
import os

# --- 1. ENGINE CONFIG (V81 VERTICAL DOCK) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V81")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* THE CROWN */
    .stImage { display: flex !important; justify-content: center !important; width: 900px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 900px !important; }

    /* TRIPLE-STACK BOARD */
    .v81-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1000px !important; margin: 10px auto 30px auto !important; 
    }
    .v81-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v81-header { color: #D4AF37; text-align: center; font-weight: 900; font-size: 18px; margin-bottom: 4px; text-transform: uppercase; }
    .v81-box { background-color: #FFFFFF; border: 2px solid #000; margin: 3px 0; padding: 6px; text-align: center; border-radius: 6px; }
    .v81-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 40px !important; font-weight: 900; font-style: italic; }

    /* MATRIX SENSORS */
    .v81-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
    }
    
    /* THE DOCKED PILLAR UNITS - FINAL ALIGNMENT */
    .v81-unit {
        display: flex; flex-direction: column; align-items: center;
        margin-top: 30px !important; /* Forces the whole block up */
    }
    .v81-label { font-weight: 900; font-size: 22px; margin-bottom: -5px !important; }
    .v81-pillar { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 40px; height: 260px; 
        border-radius: 8px; border: 2px solid #000; 
        box-shadow: 0px 0px 25px #D4AF37;
        margin-top: -10px !important; /* Docks Pillar to Input Box */
    }

    /* INPUTS */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; width: 130px !important; border-radius: 8px !important; }
    input { color: #00FF00 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. COMPONENTS ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

st.markdown("""
<div class='v81-board-container'>
    <div class='v81-column'><div class='v81-header'>ARUBA</div><div class='v81-box'><span class='v81-num'>1862</span></div><div class='v81-box'><span class='v81-num'>0801</span></div><div class='v81-box'><span class='v81-num'>9394</span></div></div>
    <div class='v81-column'><div class='v81-header'>BONAIRE</div><div class='v81-box'><span class='v81-num'>2544</span></div><div class='v81-box'><span class='v81-num'>8732</span></div><div class='v81-box'><span class='v81-num'>7296</span></div></div>
    <div class='v81-column'><div class='v81-header'>CURAÇAO</div><div class='v81-box'><span class='v81-num'>7716</span></div><div class='v81-box'><span class='v81-num'>5502</span></div><div class='v81-box'><span class='v81-num'>5918</span></div></div>
    <div class='v81-column'><div class='v81-header'>ST. MARTIN</div><div class='v81-box'><span class='v81-num'>3076</span></div><div class='v81-box'><span class='v81-num'>8561</span></div><div class='v81-box'><span class='v81-num'>3465</span></div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1000px; margin-bottom:10px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def get_v81_data(input_str):
    grid = [[0]*4 for _ in range(4)]
    if input_str and len(input_str) >= 1:
        try:
            seed = int(input_str[0])
            for c in range(4): grid[0][c] = (seed + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): grid[1][c] = (grid[1][c-1] + 1) % 10
        except: pass
    return grid

def draw_v81_grid(data, is_dark=False, target=None):
    bg = "#111" if is_dark else "#1a1a1a"
    for r in range(4):
        rows = st.columns(4)
        for c in range(4):
            val = data[r][c]
            is_target = (r == 0 and c == 0 and val != 0)
            html = f"<div class='v81-cell' style='background-color:{bg}'>"
            if is_target and target == "red": html += f"<div style='border:6px solid #FF0000; border-radius:50%; width:55px; height:55px; display:flex; align-items:center; justify-content:center;'>{val}</div>"
            elif is_target and target == "blue": html += f"<div style='border:6px solid #0000FF; border-radius:50%; width:55px; height:55px; display:flex; align-items:center; justify-content:center;'>{val}</div>"
            else: html += f"{val}"
            html += "</div>"
            rows[c].markdown(html, unsafe_allow_html=True)

s_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with s_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    draw_v81_grid(get_v81_data(st.session_state.get('v81_r', "")), target="red")
with s_cols[1]:
    st.markdown("<div class='v81-unit'><p class='v81-label' style='color:red;'>RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v81_r", label_visibility="collapsed")
    st.markdown("<div class='v81-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    draw_v81_grid(get_v81_data(st.session_state.get('v81_b', "")), target="blue")
with s_cols[3]:
    st.markdown("<div class='v81-unit'><p class='v81-label' style='color:#D4AF37;'>CORE</p>", unsafe_allow_html=True)
    st.markdown("<div style='height:48px;'></div><div class='v81-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    draw_v81_grid([[0]*4 for _ in range(4)], is_dark=True)
with s_cols[5]:
    st.markdown("<div class='v81-unit'><p class='v81-label' style='color:blue;'>BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v81_b", label_visibility="collapsed")
    st.markdown("<div class='v81-pillar'></div></div>", unsafe_allow_html=True)
with s_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    draw_v81_grid([[0]*4 for _ in range(4)], is_dark=True)
