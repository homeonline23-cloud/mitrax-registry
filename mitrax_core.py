import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING (THE GOLDEN FAULT) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    .vault-header { 
        text-align: center; color: #FFD700; font-size: 38px; 
        font-weight: bold; animation: goldPulse 2s infinite; 
    }
    .stButton>button { 
        background-color: #FFD700 !important; color: #0E1117 !important; 
        font-weight: bold !important; border-radius: 12px !important; 
        width: 100%; border: 2px solid #FFD700; 
    }
    .grid-box { 
        border: 2px solid #FFD700; padding: 15px; border-radius: 10px; 
        background-color: #1A1A1A; text-align: center; 
    }
    .compass-text { color: #FFD700; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER SYMBOL (SINGLE SHIELD & PYRAMID) ---
st.markdown("""
    <div style='text-align: center;'>
        <div style='font-size: 80px; filter: drop-shadow(0 0 15px #FFD700);'>🛡️</div>
        <div style='margin-top: -65px; font-size: 35px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: 
    st.session_state.step = 'video'

# --- PHASE 1: SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<div class='grid-box'>Predictor Outcome Tool. Analyzing 4-digit Global Symmetry Patterns. 95% Chance.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    if st.button("PROCEED TO MISSION BRIEFING", key="btn_p1"):
        st.session_state.step = 'legal'
        st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.info("95% probability protocol active. Data secured within the Mitrax Vault.")
    if st.button("I ACCEPT THE TERMS", key="btn_p2"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- PHASE 3: WELCOME & INSTALL ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("<div class='grid-box'><h3>Install the Mitrax App Icon!</h3><p>Android: 3 Dots -> Install App<br>iPhone: Share -> Add to Home Screen</p></div>", unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT", key="btn_p3"):
        st.session_state.step = 'signup'
        st.rerun()

# --- PHASE 4: REGISTRATION ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>THE MITRAX VAULT 📐</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        st.markdown("<h4 style='text-align:center;'>Commander Registration</h4>", unsafe_allow_html=True)
        name = st.text_input("Commander Name")
        email = st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE PYRAMID ACCESS"):
            st.session_state.user_name = name
            st.session_state.step = 'sector2'
            st.rerun()

# --- PHASE 5: SECTOR 2 - THE CALCULATOR ---
elif st.session_state.step == 'sector2':
    st.markdown(f"<div class='vault-header'>🔱 SECTOR 2: SYMMETRY GRIDS</div>", unsafe_allow_html=True)
    st.write(f"Welcome, Commander {st.session_state.get('user_name', 'Soldier')}.")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2: st.markdown("<div class='grid-box'><span class='compass-text'>NORTH</span></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='grid-box'><span class='compass-text'>WEST</span></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='grid-box'><span class='compass-text'>EAST</span></div>", unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns([1,2,1])
    with col_s2: st.markdown("<div class='grid-box'><span class='compass-text'>SOUTH</span></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.write("### 🧮 4-Digit Symmetry Input")
    n1 = st.number_input("Winning Number 1", 0, 9, key="n1")
    n2 = st.number_input("Winning Number 2", 0, 9, key="n2")
    n3 = st.number_input("Winning Number 3", 0, 9, key="n3")
    n4 = st.number_input("Winning Number 4", 0, 9, key="n4")
    
    if st.button("CALCULATE SYMMETRY OUTCOME", key="btn_calc"):
        st.success(f"Outcome calculated for {n1}{n2}{n3}{n4}. Analyzing patterns...")
