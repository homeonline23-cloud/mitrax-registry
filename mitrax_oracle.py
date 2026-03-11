import streamlit as st
import os

# --- 1. ENGINE CONFIG (V87 SEALED CORE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V87")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    .stImage { display: flex !important; justify-content: center !important; width: 900px !important; }
    img { border: 3px solid #D4AF37; border-radius: 15px; width: 900px !important; }

    .v87-board-container { 
        display: flex !important; flex-direction: row !important; justify-content: center !important;
        width: 1000px !important; margin: 10px auto 30px auto !important; 
    }
    .v87-column { 
        border: 3px solid #4B6321; background-color: #4B6321; 
        margin: 0 6px; padding: 10px; width: 230px !important;
        display: flex; flex-direction: column; border-radius: 10px;
    }
    .v87-num { color: #000; font-family: 'Courier New', Courier, monospace; font-size: 38px !important; font-weight: 900; font-style: italic; text-align: center;}

    .v87-cell { 
        background-color: #1a1a1a; border: 2px solid #00FF00; 
        height: 70px; width: 70px; display: flex; align-items: center; justify-content: center; 
        font-weight: 900; font-size: 36px; border-radius: 10px; margin: 3px; color: #00FF00; 
    }
    
    .v87-pillar-unit {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        margin-top: 35px !important;
    }
    
    .v87-label { font-weight: 900; font-size: 24px; text-align: center; width: 100%; margin-bottom: 5px !important; }
    
    .v87-pillar-graphic { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); 
        width: 50px; height: 300px; 
        border-radius: 0 0 12px 12px; border: 2px solid #000; 
        box-shadow: 0px 0px 30px #D4AF37;
        margin-top: -5px !important;
    }

    div[data-baseweb="input"] { 
        background-color: #000 !important; 
        border: 4px solid #00FF00 !important; 
        width: 140px !important; 
        border-radius: 12px 12px 0 0 !important;
        display: flex !important;
        justify-content: center !important;
    }
    input { color: #00FF00 !important; font-size: 30px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. COMPONENTS ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg")

st.markdown("""
<div class='v87-board-container'>
    <div class='v87-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v87-num'>1862</div><div class='v87-num'>0801</div><div class='v87-num'>9394</div></div></div>
    <div class='v87-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v87-num'>2544</div><div class='v87-num'>8732</div><div class='v87-num'>7296</div></div></div>
    <div class='v87-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v87-num'>7716</div><div class='v87-num'>5502</div><div class='v87-num'>5918</div></div></div>
    <div class='v87-column'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div style='background:#FFF; margin:2px; border-radius:5px;'><div class='v87-num'>3076</div><div class='v87-num'>8561</div><div class='v87-num'>3465</div></div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color:#00FF00; text-align:center; border-bottom: 5px solid #00FF00; width:1000px;'>MATRIX SENSORS</h2>", unsafe_allow_html=True)

def draw_v87_grid(input_key, is_active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(input_key, "") if is_active else ""
    if val:
        try:
            s = int(val[0])
            for c in range(4): 
                grid[0][c] = (s + c) % 10
            grid[1][0] = (grid[0][3] - 1) % 10
            for c in range(1, 4): 
                grid[1][c] = (grid[1][c-1] + 1) % 10
        except: 
            pass
    
    for r in range(
