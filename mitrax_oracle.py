import streamlit as st
import os

# --- 1. ENGINE CONFIG (V116 DIRECT DOCK) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V116")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 1300px !important;
        margin: 0 auto !important;
    }

    /* THE HEADER */
    .v116-header { text-align: center; margin-top: -60px; margin-bottom: 20px; width: 100%; }
    .v116-title { color: #D4AF37; font-size: 44px; font-weight: 900; text-shadow: 4px 4px 8px #000; }
    .v116-worldwide { color: #FFFFFF; font-size: 28px; font-weight: 700; margin-bottom: 10px; }

    /* WINNING BOARD */
    .v116-board-container { display: flex; justify-content: center; gap: 15px; width: 1100px; margin: 0 auto; }
    .v116-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 10px; width: 240px; border-radius: 12px; }
    .v116-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 38px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 3px 0; border-radius: 6px; }

    /* DIRECT DOCKED DATES */
    .v116-dock-row { display: flex; justify-content: center; gap: 300px; width: 1100px; margin: 15px auto; }
    .v116-date-unit { display: flex; flex-direction: column; align-items: center; width: 160px; }
    .v116-date-label { font-weight: 900; font-size: 22px; margin-bottom: 5px; }

    /* SENSORS */
    .v116-divider { margin-top: 20px; border-bottom: 4px solid #D4AF37; width: 1200px; text-align: center; color: #D4AF37; font-weight: 900; font-size: 24px; margin-bottom: 20px; padding-bottom: 10px; }
    .v116-grid-table { border-collapse: separate; border-spacing: 5px; }
    .v116-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 68px; width: 68px; text-align: center; font-weight: 900; font-size: 34px; color: #FFFFFF; border-radius: 10px; }
    
    .v116-gold-shaft { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 45px; height: 300px; border-radius: 0 0 15px 15px; border: 2px solid #000; box-shadow: 0px 5px 20px rgba(212, 175, 55, 0.4); margin-top: 40px; }

    /* BLACK-TEXT INPUTS */
    div[data-baseweb="input"] { background-color: #FFFFFF !important; border: 4px solid #D4AF37 !important; width: 140px !important; border-radius: 10px !important; }
    input { color: #000000 !important; font-size: 28px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v116-header'>
    <div class='v116-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v116-worldwide'>Worldwide 🌏 Advantage</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v116-board-container'>
    <div class='v116-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v116-white-num'>1862</div><div class='v116-white-num'>0801</div><div class='v116-white-num'>9394</div></div>
    <div class='v116-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v116-white-num'>2544</div><div class='v116-white-num'>8732</div><div class='v116-white-num'>7296</div></div>
    <div class='v116-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v116-white-num'>7716</div><div class='v116-white-num'>5502</div><div class='v116-white-num'>5918</div></div>
    <div class='v116-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v116-white-num'>3076</div><div class='v116-white-num'>8561</div><div class='v116-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

# --- 4. DIRECT DOCKED DATES ---
st.markdown("<div class='v116-dock-row'>", unsafe_allow_html=True)
col_left, col_right = st.columns([1,1])
with col_left:
    st.markdown("<div class='v116-date-unit' style='margin-left:220px;'><p class='v116-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R-Date", key="v116_r", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
with col_right:
    st.markdown("<div class='v116-date-unit' style='margin-right:220px;'><p class='v116-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B-Date", key="v116_b", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='v116-divider'>MATRIX SENSORS</div>", unsafe_allow_html=True)

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
    html = "<table class='v116-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4): html += f"<td class='v116-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 6. THE SENSOR ROW ---
m_cols = st.columns([5, 1, 5, 1, 5, 1, 5])
with m_cols[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); st.markdown(get_grid_html("v116_r"), unsafe_allow_html=True)
with m_cols[1]: st.markdown("<div class='v116-gold-shaft'></div>", unsafe_allow_html=True)
with m_cols[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); st.markdown(get_grid_html("v116_b"), unsafe_allow_html=True)
with m_cols[3]: st.markdown("<div class='v116-gold-shaft' style='background:#D4AF37;'></div>", unsafe_allow_html=True)
with m_cols[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
with m_cols[5]: st.markdown("<div class='v116-gold-shaft'></div>", unsafe_allow_html=True)
with m_cols[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
