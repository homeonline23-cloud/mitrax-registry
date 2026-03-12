import streamlit as st
import os

# --- 1. ENGINE CONFIG (V117 SPACED DECK) ---
st.set_page_config(layout="wide", page_title="MITRAX ORACLE V117")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 1400px !important; /* Maximum breadth for spacing */
        margin: 0 auto !important;
    }

    /* THE HEADER */
    .v117-header { text-align: center; margin-top: -60px; margin-bottom: 40px; width: 100%; }
    .v117-title { color: #D4AF37; font-size: 44px; font-weight: 900; text-shadow: 4px 4px 8px #000; }
    .v117-worldwide { color: #FFFFFF; font-size: 28px; font-weight: 700; margin-bottom: 10px; }

    /* WINNING BOARD */
    .v117-board-container { display: flex; justify-content: center; gap: 25px; width: 1200px; margin: 0 auto; }
    .v117-city-card { border: 2px solid #2E4D23; background-color: #2E4D23; padding: 12px; width: 260px; border-radius: 12px; }
    .v117-white-num { color: #000; font-family: 'Courier New', monospace; font-size: 40px; font-weight: 900; font-style: italic; text-align: center; background: #FFF; margin: 4px 0; border-radius: 6px; }

    /* GRID TABLES */
    .v117-grid-table { border-collapse: separate; border-spacing: 8px; }
    .v117-cell { background-color: #1a1a1a; border: 2px solid #D4AF37; height: 72px; width: 72px; text-align: center; font-weight: 900; font-size: 38px; color: #FFFFFF; border-radius: 12px; }
    
    /* THE MONOLITH PILLARS - WINDOWS ON TOP */
    .v117-monolith {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        margin-top: 10px !important;
    }
    .v117-pillar-label { font-weight: 900 !important; font-size: 24px !important; margin-bottom: 8px !important; }
    .v117-gold-shaft { 
        background: linear-gradient(180deg, #D4AF37 0%, #8A6D3B 100%) !important; 
        width: 50px !important; height: 320px !important; 
        border-radius: 0 0 15px 15px !important; border: 2px solid #000 !important; 
        box-shadow: 0px 8px 25px rgba(212, 175, 55, 0.4) !important;
        margin-top: -5px !important;
    }

    /* THE BLACK-TEXT INPUTS - DOCKED ON PILLAR */
    div[data-baseweb="input"] { 
        background-color: #FFFFFF !important; 
        border: 4px solid #D4AF37 !important; 
        width: 150px !important; 
        border-radius: 12px 12px 0 0 !important; 
    }
    input { 
        color: #000000 !important; 
        font-size: 32px !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown(f"""
<div class='v117-header'>
    <div class='v117-title'>MITRAX ORACLE PIC 4 App.</div>
    <div class='v117-worldwide'>Worldwide 🌏 Advantage</div>
</div>
""", unsafe_allow_html=True)

# --- 3. BOARD ---
st.markdown("""
<div class='v117-board-container'>
    <div class='v117-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ARUBA</div><div class='v117-white-num'>1862</div><div class='v117-white-num'>0801</div><div class='v117-white-num'>9394</div></div>
    <div class='v117-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>BONAIRE</div><div class='v117-white-num'>2544</div><div class='v117-white-num'>8732</div><div class='v117-white-num'>7296</div></div>
    <div class='v117-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>CURAÇAO</div><div class='v117-white-num'>7716</div><div class='v117-white-num'>5502</div><div class='v117-white-num'>5918</div></div>
    <div class='v117-city-card'><div style='color:#D4AF37; text-align:center; font-weight:900;'>ST. MARTIN</div><div class='v117-white-num'>3076</div><div class='v117-white-num'>8561</div><div class='v117-white-num'>3465</div></div>
</div>
""", unsafe_allow_html=True)

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
    html = "<table class='v117-grid-table'>"
    for r in range(4):
        html += "<tr>"
        for c in range(4): html += f"<td class='v117-cell'>{grid[r][c]}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# --- 5. THE SPACED SENSOR ROW ---
st.markdown("<div style='margin-top:60px;'></div>", unsafe_allow_html=True)
m_cols = st.columns([5, 3, 5, 3, 5, 3, 5]) # High-ratio columns for space

with m_cols[0]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:22px; margin-bottom:15px;'>GRID 1</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v117_r"), unsafe_allow_html=True)

with m_cols[1]:
    st.markdown("<div class='v117-monolith'><p class='v117-pillar-label' style='color:red;'>7/1 RED</p>", unsafe_allow_html=True)
    st.text_input("RED", key="v117_r", label_visibility="collapsed")
    st.markdown("<div class='v117-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[2]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:22px; margin-bottom:15px;'>GRID 2</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("v117_b"), unsafe_allow_html=True)

with m_cols[3]:
    st.markdown("<div class='v117-monolith' style='margin-top:45px !important;'><div class='v117-gold-shaft' style='background:#D4AF37; height:360px;'></div></div>", unsafe_allow_html=True)

with m_cols[4]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:22px; margin-bottom:15px;'>GRID 3</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)

with m_cols[5]:
    st.markdown("<div class='v117-monolith'><p class='v117-pillar-label' style='color:blue;'>8/3 BLUE</p>", unsafe_allow_html=True)
    st.text_input("BLUE", key="v117_b", label_visibility="collapsed")
    st.markdown("<div class='v117-gold-shaft'></div></div>", unsafe_allow_html=True)

with m_cols[6]:
    st.markdown("<p style='color:#D4AF37; text-align:center; font-weight:900; font-size:22px; margin-bottom:15px;'>GRID 4</p>", unsafe_allow_html=True)
    st.markdown(get_grid_html("n", False), unsafe_allow_html=True)
