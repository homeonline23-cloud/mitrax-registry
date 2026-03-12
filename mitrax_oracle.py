import streamlit as st
import os

# --- 1. ENGINE CONFIG (V115 ATOMIC PURGE) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V115")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* THE MAIN HULL - TOTAL RESET */
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 1350px !important;
        margin: 0 auto !important;
    }

    /* THE CENTERED HEADER */
    .v115-header { text-align: center; margin-top: -60px; margin-bottom: 25px; width: 100%; }
    .v115-title { color: #D4AF37; font-size: 46px; font-weight: 900; text-shadow: 4px 4px 8px #000; }
    .v115-worldwide { color: #FFFFFF; font-size: 30px; font-weight: 700; margin-bottom: 10px; }
    .v115-mission { color: #D1D1D1; font-size: 16px; font-weight: 600; line-height: 1.5; max-width: 900px; margin: 0 auto; }

    /* WINNING BOARD */
    .v115-board-container { display: flex; justify-content: center; gap: 20px; width: 1100px; margin: 0 auto; }
    .v115-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 12px; width: 240px; border-radius: 12px; }
    .v115-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 38px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 4px 0; border-radius: 6px; }

    /* MATRIX SENSORS HEADER */
    .v115-divider { margin-top: 35px; border-bottom: 4px solid #D4AF37; width: 1250px; text-align: center; color: #D4AF37; font-weight: 900; font-size: 26px; margin-bottom: 25px; padding-bottom: 10px; }

    /* THE SENSOR ROW (TABLE LOCK WITH GAPS) */
    .v115-grid-table { border-collapse: separate; border-spacing: 6px; }
    .v115-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 68px; width: 68px; text-align: center; font-weight: 900; font-size: 34px; color: #FFFFFF; border-radius: 12px; }
    
    /* THE DOCKED MONOLITH PILLARS */
    .v115-monolith {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 170px !important;
        margin-top: 0px !important;
    }
    .v115-date-label { font-weight: 900 !important; font-size: 22px !important; margin-bottom: 8px !important; }
    .v115-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 50px !important; height: 300px !important; 
        border-radius: 0 0 15px 15px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 5px 20px rgba(212, 175, 55, 0.4) !important;
        margin-top: -5px !important;
    }

    /* THE BLACK-TEXT INPUTS */
    div[data-baseweb="input"] { 
        background-color: #FFFFFF !important; 
        border: 4px solid #D4AF37 !important; 
        width: 135px !important; 
        border-radius: 12px 12px 0 0 !important; 
    }
    input { 
        color: #000000 !important; 
        font-size: 28px !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v115-header'>
    <div class='v115-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v115-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v115-mission'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v115-board-container'>
    <div class='v115-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v115-white-num'>1862</div><div class='v115-white-num'>0801</div><div class='v115-white-num'>9394</div></div>
    <div class='v115-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v115-white-num'>2544</div><div class='v115-white-num'>8732</div><div class='v115-white-num'>7296</div></div>
    <div class='v115-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v115-white-num'>7716</div><div class='v115-white-num'>5502</div><div class='v115-white-num'>5918</div></div>
    <div class='v115-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v115-white-num'>3076</div><div class='v115-white-num'>8561</div><div class='v115-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='v115-divider'>MATRIX SENSORS</div>", unsafe_allow_html=True)

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
    
    html = "<table class='v115-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4):
            html += f"<td class='v115-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 5. THE SPACED MATRIX ROW (CORE REMOVED) ---
m_cols = st.columns([5, 3, 5, 3, 5, 3, 5])

with m_cols[0]:
    st.markdown("<div style='padding-right:15px;'><p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 1</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v115_r"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m_cols[1]:
    st.markdown("<div class='v115-monolith'><p class='v115-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R1", key="v115_r", label_visibility="collapsed")
    st.markdown("<div class='v115-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[2]:
    st.markdown("<div style='padding-left:15px; padding-right:15px;'><p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 2</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v115_b"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m_cols[3]:
    # CORE IS PHYSICALLY REMOVED FROM HERE
    st.markdown("<div class='v115-monolith' style='margin-top:43px !important;'><div class='v115-gold-shaft' style='background:#D4AF37; height:335px;'></div></div>", unsafe_allow_html=True)

with m_cols[4]:
    st.markdown("<div style='padding-left:15px; padding-right:15px;'><p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 3</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with m_cols[5]:
    st.markdown("<div class='v115-monolith'><p class='v115-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B1", key="v115_b", label_visibility="collapsed")
    st.markdown("<div class='v115-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[6]:
    st.markdown("<div style='padding-left:15px;'><p style='color:#D4AF37; text-align:center; font-weight:900; font-size:18px;'>GRID 4</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
