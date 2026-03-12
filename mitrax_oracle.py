import streamlit as st
import os

# --- 1. ENGINE CONFIG (V110 IRON BLOCKS) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V110")

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

    /* THE TITLE BLOCK */
    .v110-header { text-align: center; margin-top: -60px; margin-bottom: 20px; }
    .v110-title { color: #D4AF37; font-size: 42px; font-weight: 900; text-shadow: 3px 3px 5px #000; }
    .v110-worldwide { color: #FFF; font-size: 26px; font-weight: 700; }
    .v110-mission { color: #FFF; font-size: 15px; font-style: italic; max-width: 900px; margin: 0 auto; line-height: 1.4; }

    /* THE WINNING BLOCK (SHRUNKEN & LOCKED) */
    .v110-board-row { display: flex; justify-content: center; gap: 10px; width: 1000px; margin: 0 auto; }
    .v110-city { background: #4B6321; border: 2px solid #4B6321; border-radius: 12px; padding: 10px; width: 220px; }
    .v110-white-num { background: #FFF; color: #000; font-family: 'Courier New', monospace; font-size: 30px; font-weight: 900; text-align: center; margin: 3px 0; border-radius: 5px; }

    /* THE DATE COCKPIT (7/1 & 8/3) */
    .v110-cockpit { display: flex; justify-content: center; gap: 100px; margin: 20px 0; width: 1000px; }
    .v110-date-label { font-size: 28px; font-weight: 900; margin-bottom: 5px; text-align: center; }

    /* THE SENSOR ROW (UNBREAKABLE) */
    .v110-sensor-row { display: flex; flex-wrap: nowrap; justify-content: center; align-items: flex-start; width: 1200px; gap: 5px; }
    .v110-grid-box { width: 260px; text-align: center; }
    .v110-cell { background: #1a1a1a; border: 2px solid #00FF00; height: 60px; width: 60px; display: inline-flex; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; color: #00FF00; border-radius: 10px; margin: 2px; }
    
    .v110-pillar-unit { width: 60px; display: flex; flex-direction: column; align-items: center; margin-top: 35px; }
    .v110-gold-pillar { background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%); width: 40px; height: 260px; border-radius: 0 0 10px 10px; border: 2px solid #000; box-shadow: 0px 0px 15px #D4AF37; }

    /* INPUT STYLING */
    div[data-baseweb="input"] { background-color: #000 !important; border: 4px solid #00FF00 !important; width: 140px !important; border-radius: 10px !important; }
    input { color: #00FF00 !important; font-size: 32px !important; text-align: center !important; font-weight: 900 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER BLOCK ---
st.markdown("""
<div class='v110-header'>
    <div class='v106-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v110-worldwide'>Worldwide 🌏 Advantage</div>
    <div class='v110-mission'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>
</div>
""", unsafe_allow_html=True)

# --- 3. WINNING BLOCK ---
st.markdown("""
<div class='v110-board-row'>
    <div class='v110-city'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v110-white-num'>1862</div><div class='v110-white-num'>0801</div><div class='v110-white-num'>9394</div></div>
    <div class='v110-city'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v110-white-num'>2544</div><div class='v110-white-num'>8732</div><div class='v110-white-num'>7296</div></div>
    <div class='v110-city'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v110-white-num'>7716</div><div class='v110-white-num'>5502</div><div class='v110-white-num'>5918</div></div>
    <div class='v110-city'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v110-white-num'>3076</div><div class='v110-white-num'>8561</div><div class='v110-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

# --- 4. DATE COCKPIT ---
st.markdown("<div style='display:flex; justify-content:center; gap:80px; width:1000px; margin:20px auto;'>", unsafe_allow_html=True)
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown("<div style='text-align:right; margin-left:350px;'><p class='v110-date-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("R", key="v110_r", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div style='text-align:left; margin-right:350px;'><p class='v110-date-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("B", key="v110_b", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #00FF00; width: 1100px;'>", unsafe_allow_html=True)

# --- 5. GRID LOGIC ---
def draw_v110_grid(key, active=True):
    grid = [[0]*4 for _ in range(4)]
    val = st.session_state.get(key, "") if active else ""
    if val:
        try:
            s = int(val[0])
            for r in range(4):
                for c in range(4): grid[r][c] = (s + r + c) % 10 # Sample logic for Row 1&2
        except: pass
    
    html = ""
    for r in range(4):
        html += "<div style='display:block;'>"
        for c in range(4):
            html += f"<div class='v110-cell'>{grid[r][c]}</div>"
        html += "</div>"
    return html

# --- 6. THE SENSOR ROW (UNBREAKABLE) ---
m_cols = st.columns([5, 1, 5, 1, 5, 1, 5])
with m_cols[0]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 1</p>", unsafe_allow_html=True); st.markdown(draw_v110_grid("v110_r"), unsafe_allow_html=True)
with m_cols[1]: st.markdown("<div class='v110-pillar-unit'><div class='v110-gold-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[2]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 2</p>", unsafe_allow_html=True); st.markdown(draw_v110_grid("v110_b"), unsafe_allow_html=True)
with m_cols[3]: st.markdown("<div class='v110-pillar-unit'><div class='v110-gold-pillar' style='background:#D4AF37;'></div><p style='color:#D4AF37; font-weight:900;'>CORE</p></div>", unsafe_allow_html=True)
with m_cols[4]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 3</p>", unsafe_allow_html=True); st.markdown(draw_v110_grid("n", False), unsafe_allow_html=True)
with m_cols[5]: st.markdown("<div class='v110-pillar-unit'><div class='v110-gold-pillar'></div></div>", unsafe_allow_html=True)
with m_cols[6]: st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900;'>GRID 4</p>", unsafe_allow_html=True); st.markdown(draw_v110_grid("n", False), unsafe_allow_html=True)
