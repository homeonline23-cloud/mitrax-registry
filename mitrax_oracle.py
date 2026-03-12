import streamlit as st
import os

# --- 1. ENGINE CONFIG (V113 MONOLITHIC DOCKING) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V113")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 1200px !important;
        margin: 0 auto !important;
    }

    /* THE CENTERED HEADER */
    .v113-header { text-align: center; margin-top: -60px; margin-bottom: 20px; width: 100%; }
    .v113-title { color: #D4AF37; font-size: 44px; font-weight: 900; text-shadow: 4px 4px 8px #000; margin-bottom: 5px; }
    .v113-worldwide { color: #FFFFFF; font-size: 28px; font-weight: 700; margin-bottom: 10px; }
    .v113-mission { color: #D1D1D1; font-size: 15px; font-weight: 600; line-height: 1.4; max-width: 850px; margin: 0 auto; text-align: center; }

    /* WINNING BOARD */
    .v113-board-container { display: flex; justify-content: center; gap: 10px; width: 1100px; margin: 0 auto; }
    .v113-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 10px; width: 230px; border-radius: 12px; }
    .v113-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 38px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 3px 0; border-radius: 6px; }

    /* THE SENSOR ROW (TABLE LOCK) */
    .v113-grid-table { border-collapse: separate; border-spacing: 4px; }
    .v113-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 65px; width: 65px; text-align: center; font-weight: 900; font-size: 34px; color: #FFFFFF; border-radius: 10px; }
    
    /* THE DOCKED MONOLITH PILLARS */
    .v113-monolith {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 150px !important;
        margin-top: 10px !important;
    }
    .v113-date-label { font-weight: 900 !important; font-size: 20px !important; margin-bottom: 5px !important; }
    .v113-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 45px !important; height: 280px !important; 
        border-radius: 0 0 12px 12px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 0px 20px #D4AF37 !important; margin-top: -5px !important;
    }

    /* THE BLACK-TEXT INPUTS */
    div[data-baseweb="input"] { 
        background-color: #FFFFFF !important; /* White background for the box */
        border: 3px solid #D4AF37 !important; 
        width: 130px !important; 
        border-radius: 10px 10px 0 0 !important; 
    }
    input { 
        color: #000000 !important; /* FORCED BLACK TEXT */
        font-size: 28px !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v113-header'>
    <div class='v113-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v113-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v113-mission'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v113-board-container'>
    <div class='v113-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v113-white-num'>1862</div><div class='v113-white-num'>0801</div><div class='v113-white-num'>9394</div></div>
    <div class='v113-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v113-white-num'>2544</div><div class='v113-white-num'>8732</div><div class='v113-white-num'>7296</div></div>
    <div class='v113-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v113-white-num'>7716</div><div class='v113-white-num'>5502</div><div class='v113-white-num'>5918</div></div>
    <div class='v113-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v113-white-num'>3076</div><div class='v113-white-num'>8561</div><div class='v113-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:20px; border-bottom:4px solid #D4AF37; width:1100px; text-align:center; color:#D4AF37; font-weight:900; font-size:24px; margin-bottom:20px;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

# --- 4. GRID BUILDER ---
def get_grid_html(key, active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(key, "") if active else ""
    if val:
        try:
            s = int(val[0])
            for r in range(4):
                for c in range(4): grid[r][c] = (s + r + c) % 10
        except: pass
    
    html = "<table class='v113-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4):
            html += f"<td class='v113-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 5. THE MONOLITHIC MATRIX ROW ---
m_cols = st.columns([5, 2, 5, 2, 5, 2, 5])

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v113_r"), unsafe_allow_html=True)

with m_cols[1]:
    st.markdown("<div class='v113-monolith'><p class='v113-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v113_r", label_visibility="collapsed")
    st.markdown("<div class='v113-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v113_b"), unsafe_allow_html=True)

with m_cols[3]:
    st.markdown("<div class='v113-monolith' style='margin-top:40px !important;'><div class='v113-gold-shaft' style='background:#D4AF37; height:320px;'></div></div>", unsafe_allow_html=True)

with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)

with m_cols[5]:
    st.markdown("<div class='v113-monolith'><p class='v113-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v113_b", label_visibility="collapsed")
    st.markdown("<div class='v113-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
