import streamlit as st
import os

# --- 1. ENGINE CONFIG (V114 SPATIAL DECOMPRESSION) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V114")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE MAIN HULL - WIDENED FOR BREATHING ROOM */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 1350px !important;
        margin: 0 auto !important;
    }

    /* THE CENTERED HEADER */
    .v114-header { text-align: center; margin-top: -50px; margin-bottom: 30px; width: 100%; }
    .v114-title { color: #D4AF37; font-size: 46px; font-weight: 900; text-shadow: 4px 4px 8px #000; margin-bottom: 10px; }
    .v114-worldwide { color: #FFFFFF; font-size: 30px; font-weight: 700; margin-bottom: 15px; }
    .v114-mission { color: #D1D1D1; font-size: 16px; font-weight: 600; line-height: 1.6; max-width: 950px; margin: 0 auto; text-align: center; }

    /* WINNING BOARD - GAPPED */
    .v114-board-container { display: flex; justify-content: center; gap: 20px; width: 1200px; margin: 0 auto; }
    .v114-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 15px; width: 250px; border-radius: 12px; }
    .v114-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 40px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 5px 0; border-radius: 8px; }

    /* MATRIX SENSORS HEADER */
    .v114-sensor-divider { margin-top: 40px; border-bottom: 4px solid #D4AF37; width: 1250px; text-align: center; color: #D4AF37; font-weight: 900; font-size: 26px; margin-bottom: 30px; padding-bottom: 10px; }

    /* THE SENSOR ROW (TABLE LOCK WITH GUTTERS) */
    .v114-grid-table { border-collapse: separate; border-spacing: 6px; }
    .v114-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 70px; width: 70px; text-align: center; font-weight: 900; font-size: 36px; color: #FFFFFF; border-radius: 12px; }
    
    /* THE DOCKED MONOLITH PILLARS - SPACED */
    .v114-monolith {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 180px !important; /* Wider to create gutters */
        margin-top: 5px !important;
    }
    .v114-date-label { font-weight: 900 !important; font-size: 22px !important; margin-bottom: 12px !important; letter-spacing: 1px; }
    .v114-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 50px !important; height: 300px !important; 
        border-radius: 0 0 15px 15px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 10px 25px rgba(212, 175, 55, 0.4) !important; margin-top: -5px !important;
    }

    /* THE BLACK-TEXT INPUTS - REFINED */
    div[data-baseweb="input"] { 
        background-color: #FFFFFF !important; 
        border: 4px solid #D4AF37 !important; 
        width: 140px !important; 
        border-radius: 12px 12px 0 0 !important; 
    }
    input { 
        color: #000000 !important; 
        font-size: 30px !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v114-header'>
    <div class='v114-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v114-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v114-mission'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v114-board-container'>
    <div class='v114-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v114-white-num'>1862</div><div class='v114-white-num'>0801</div><div class='v114-white-num'>9394</div></div>
    <div class='v114-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v114-white-num'>2544</div><div class='v114-white-num'>8732</div><div class='v114-white-num'>7296</div></div>
    <div class='v114-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v114-white-num'>7716</div><div class='v114-white-num'>5502</div><div class='v114-white-num'>5918</div></div>
    <div class='v114-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v114-white-num'>3076</div><div class='v114-white-num'>8561</div><div class='v114-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='v114-sensor-divider'>MATRIX SENSORS</div>", unsafe_allow_html=True)

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
    
    html = "<table class='v114-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4):
            html += f"<td class='v114-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 5. THE SPACED MATRIX ROW ---
m_cols = st.columns([5, 3, 5, 3, 5, 3, 5]) # Adjusted ratios for more gutter space

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 1</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v114_r"), unsafe_allow_html=True)

with m_cols[1]:
    st.markdown("<div class='v114-monolith'><p class='v114-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R1", key="v114_r", label_visibility="collapsed")
    st.markdown("<div class='v114-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 2</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v114_b"), unsafe_allow_html=True)

with m_cols[3]:
    st.markdown("<div class='v114-monolith' style='margin-top:55px !important;'><div class='v114-gold-shaft' style='background:#D4AF37; height:335px;'></div><p style='color:#D4AF37; font-weight:900; margin-top:5px;'>CORE</p></div>", unsafe_allow_html=True)

with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 3</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)

with m_cols[5]:
    st.markdown("<div class='v114-monolith'><p class='v114-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B1", key="v114_b", label_visibility="collapsed")
    st.markdown("<div class='v114-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 4</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
