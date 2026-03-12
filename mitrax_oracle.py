import streamlit as st
import os

# --- 1. ENGINE CONFIG (V112 CHROMATIC EXTRACTION) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V112")

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
    .v112-header { text-align: center; margin-top: -60px; margin-bottom: 20px; width: 100%; }
    .v112-title { color: #D4AF37; font-size: 44px; font-weight: 900; text-shadow: 4px 4px 8px #000; margin-bottom: 5px; }
    .v112-worldwide { color: #FFFFFF; font-size: 28px; font-weight: 700; margin-bottom: 10px; }
    .v112-mission { color: #D1D1D1; font-size: 15px; font-weight: 600; line-height: 1.4; max-width: 850px; margin: 0 auto; text-align: center; }

    /* WINNING BOARD */
    .v112-board-container { display: flex; justify-content: center; gap: 10px; width: 1100px; margin: 0 auto; }
    .v112-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 10px; width: 230px; border-radius: 12px; }
    .v112-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 38px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 3px 0; border-radius: 6px; }

    /* THE CENTERED DATE INPUTS */
    .v112-date-bay { display: flex; justify-content: center; gap: 120px; width: 100%; margin-top: 25px; margin-bottom: 15px; }
    .v112-date-unit { display: flex; flex-direction: column; align-items: center; width: 150px; }
    .v112-date-label { font-weight: 900; font-size: 22px; margin-bottom: 5px; }

    /* THE SENSOR ROW (TABLE LOCK) */
    .v112-main-row { display: flex; flex-direction: row; justify-content: center; align-items: flex-start; width: 1200px; gap: 10px; margin-top: 20px; }
    .v112-grid-table { border-collapse: separate; border-spacing: 4px; }
    .v112-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 65px; width: 65px; text-align: center; font-weight: 900; font-size: 34px; color: #FFFFFF; border-radius: 10px; }
    
    .v112-pillar-container { display: flex; flex-direction: column; align-items: center; margin-top: 35px; width: 50px; }
    .v112-gold-shaft { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 40px; height: 280px; border-radius: 0 0 12px 12px; border: 2px solid #000; box-shadow: 0px 0px 20px #D4AF37; }

    /* THE CLEAN WHITE INPUTS */
    div[data-baseweb="input"] { 
        background-color: #000 !important; 
        border: 3px solid #D4AF37 !important; /* Changed from green to gold */
        width: 130px !important; 
        border-radius: 10px !important; 
    }
    input { 
        color: #FFFFFF !important; /* NO MORE GREEN TEXT */
        font-size: 28px !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v112-header'>
    <div class='v112-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v112-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v112-mission'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v112-board-container'>
    <div class='v112-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v112-white-num'>1862</div><div class='v112-white-num'>0801</div><div class='v112-white-num'>9394</div></div>
    <div class='v112-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v112-white-num'>2544</div><div class='v112-white-num'>8732</div><div class='v112-white-num'>7296</div></div>
    <div class='v112-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v112-white-num'>7716</div><div class='v112-white-num'>5502</div><div class='v112-white-num'>5918</div></div>
    <div class='v112-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v112-white-num'>3076</div><div class='v112-white-num'>8561</div><div class='v112-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

# --- 4. DATE INPUT BAY ---
st.markdown("<div class='v112-date-bay'>", unsafe_allow_html=True)
col_a, col_b = st.columns([1,1])
with col_a:
    st.markdown("<div class='v112-date-unit' style='margin-left:auto;'><p class='v112-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v112_r", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div class='v112-date-unit' style='margin-right:auto;'><p class='v112-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v112_b", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 5. GRID BUILDER ---
def get_grid_html(key, active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(key, "") if active else ""
    if val:
        try:
            s = int(val[0])
            for r in range(4):
                for c in range(4): grid[r][c] = (s + r + c) % 10
        except: pass
    
    html = "<table class='v112-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4):
            html += f"<td class='v112-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 6. THE UNBREAKABLE MATRIX ---
st.markdown("<div style='margin-top:10px; border-bottom:4px solid #D4AF37; width:1100px; text-align:center; color:#D4AF37; font-weight:900; font-size:24px; margin-bottom:20px;'>MATRIX SENSORS</div>", unsafe_allow_html=True)

m_cols = st.columns([5, 1, 5, 1, 5, 1, 5])
with m_cols[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); st.markdown(get_grid_html("v112_r"), unsafe_allow_html=True)
with m_cols[1]: st.markdown("<div class='v111-pillar-container'><div class='v112-gold-shaft'></div></div>", unsafe_allow_html=True)
with m_cols[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); st.markdown(get_grid_html("v112_b"), unsafe_allow_html=True)
with m_cols[3]: st.markdown("<div class='v111-pillar-container'><div class='v112-gold-shaft' style='background:#D4AF37;'></div><p style='color:#D4AF37; font-weight:900; text-align:center;'>CORE</p></div>", unsafe_allow_html=True)
with m_cols[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
with m_cols[5]: st.markdown("<div class='v111-pillar-container'><div class='v112-gold-shaft'></div></div>", unsafe_allow_html=True)
with m_cols[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
