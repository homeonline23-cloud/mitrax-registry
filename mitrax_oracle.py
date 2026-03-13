import streamlit as st

# --- 1. IMPERIAL PAGE CONFIG ---
st.set_page_config(
    page_title="THE MITRAX ORACLE PIC 4",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE VISUAL SHIELD (STYLING) ---
st.markdown("""
    <style>
    /* Dark Imperial Theme */
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'Courier New', monospace; }
    
    /* Header & Branding */
    .oracle-title {
        color: #00D4FF; text-align: center; letter-spacing: 8px; 
        font-size: 48px; font-weight: bold; margin-bottom: 0px;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.5);
    }
    .oracle-subtitle {
        color: #FFD700; text-align: center; font-style: italic;
        font-size: 18px; margin-bottom: 30px; letter-spacing: 4px;
    }
    
    /* Description Box */
    .description-box {
        background: rgba(255, 255, 255, 0.03); border: 1px solid #333;
        padding: 20px; border-radius: 12px; margin: 20px auto;
        max-width: 800px; text-align: center; line-height: 1.6;
    }

    /* Symmetry Grid */
    .grid-container {
        display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;
        max-width: 450px; margin: 40px auto; background: #111; padding: 25px;
        border: 2px solid #00D4FF; border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(0, 212, 255, 0.2);
    }
    .grid-cell {
        aspect-ratio: 1; border: 1px solid #222; display: flex;
        align-items: center; justify-content: center; color: #444;
        font-size: 24px; border-radius: 8px; background: #080808;
        transition: 0.3s;
    }
    .grid-cell:hover { border-color: #00D4FF; color: #00D4FF; background: #001a1f; }

    /* Buttons & Inputs */
    div.stButton > button {
        width: 100%; background-color: #00D4FF !important; color: black !important;
        font-weight: bold !important; border-radius: 10px !important; border: none !important;
        height: 50px; letter-spacing: 2px;
    }
    input { background-color: #111 !important; color: white !important; border: 1px solid #333 !important; text-align: center !important; font-size: 24px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE BRANDING ---
st.markdown("<h1 class='oracle-title'>THE MITRAX ORACLE</h1>", unsafe_allow_html=True)
st.markdown("<p class='oracle-subtitle'>WORLDWIDE ADVANTAGE • PIC 4</p>", unsafe_allow_html=True)

# --- 4. THE CORE DESCRIPTION (FROM YOUR METADATA) ---
st.markdown("""
<div class='description-box'>
    "The 4-digit Prediction Calculator that can be used Globally. 
    By entering the 4 chosen winning numbers into the calculator Grids, 
    analyzing the symmetry patterns allows you to identify potential winning numbers. 
    There’s now a <b>95% chance</b> of increasing your chances of winning."
</div>
""", unsafe_allow_html=True)

# --- 5. THE INPUT VAULT ---
st.write("")
st.markdown("<p style='text-align: center; color: #888; letter-spacing: 2px;'>ENTER 4-DIGIT WINNING SEQUENCE</p>", unsafe_allow_html=True)

col_input = st.columns([1, 1, 1, 1])
with col_input[0]: d1 = st.text_input("N1", max_chars=1, key="v1", label_visibility="collapsed", placeholder="0")
with col_input[1]: d2 = st.text_input("N2", max_chars=1, key="v2", label_visibility="collapsed", placeholder="0")
with col_input[2]: d3 = st.text_input("N3", max_chars=1, key="v3", label_visibility="collapsed", placeholder="0")
with col_input[3]: d4 = st.text_input("N4", max_chars=1, key="v4", label_visibility="collapsed", placeholder="0")

st.write("")
if st.button("ANALYZE UNIVERSAL SYMMETRY"):
    st.toast("Analyzing Symmetry Grids...", icon="📡")

# --- 6. THE SYMMETRY GRID (95% PROBABILITY VISUAL) ---
# This creates the visual 4x4 grid mentioned in your mission
grid_html = "<div class='grid-container'>"
for i in range(16):
    # Mock data showing potential symmetry patterns
    val = (i * 7) % 10 
    grid_html += f"<div class='grid-cell'>{val}</div>"
grid_html += "</div>"

st.markdown(grid_html, unsafe_allow_html=True)

# --- 7. GLOBAL FOOTER ---
st.markdown("<p style='text-align: center; color: #333; font-size: 11px; margin-top: 60px;'>MITRAX EMPIRE • UNIVERSAL GHOST SYNC [ACTIVE]</p>", unsafe_allow_html=True)
