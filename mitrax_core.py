import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING (THE GOLDEN FAULT & CREST) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Pulsing Golden Mitrax Title & Crest */
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
        50% { text-shadow: 0 0 30px #FFD700; filter: drop-shadow(0 0 20px #FFD700); }
        100% { text-shadow: 0 0 10px #FFD700; filter: drop-shadow(0 0 5px #FFD700); }
    }
    
    .imperial-crest {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100px;
        animation: goldPulse 3s infinite;
    }

    .vault-header { 
        text-align: center; 
        color: #FFD700; 
        font-size: 38px; 
        font-weight: bold; 
        animation: goldPulse 2s infinite; 
    }
    
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important; 
        width: 100%; 
        border: 2px solid #FFD700; 
    }
    
    .grid-box { 
        border: 2px solid #FFD700; 
        padding: 15px; 
        border-radius: 10px; 
        background-color: #1A1A1A; 
        text-align: center; 
    }
    
    .compass-text { color: #FFD700; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE IMPERIAL SYMBOL INJECTOR ---
# This replaces the placeholder with the Golden Compass & Pyramid Symbol
st.markdown("""
    <div style='text-align: center;'>
        <span style='font-size: 80px; filter: drop-shadow(0 0 10px #FFD700);'>🧭</span>
        <div style='margin-top: -40px; font-size: 40px;'>📐</div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- PHASE 1: SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; padding:20px; border:1px solid #FFD700; border-radius:15px; margin-bottom:15px;'>The 4-digit Prediction Calculator used Globally. Analyzing symmetry patterns identifies potential winning numbers. 95% Chance of Success.</div>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    if st.button("PROCEED TO MISSION BRIEFING"):
        st.session_state.step = 'legal'
        st.rerun()

# --- PHASE 2: TERMS ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.info("95% probability protocol active. Symmetry data remains secured within the Mitrax Vault.")
    if st.button("I ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- PHASE 3: WELCOME & INSTALL ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color:#1A1A1A; padding:20px; border-radius:15px; border:1px solid #333;'>
    <h3>Install the Mitrax App Icon on your phone!</h3>
    <p>Android: 3 Dots -> Install App | iPhone: Share -> Add to Home Screen</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT"):
        st.session_state.step = 'signup'
        st.rerun()

# --- PHASE 4: REGISTRATION ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>📐 THE MITRAX VAULT</div>", unsafe_allow_html=True)
    with st.form("vault_reg"):
        name = st.text_input("Commander Name")
        email = st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE PYRAMID ACCESS"):
            st.session_state.user_name = name
            st.session_state.step = 'sector2'
            st.rerun()

# --- PHASE 5: SECTOR 2 - THE CALCULATOR ---
elif st.session_state.step == 'sector2':
    st.markdown(f"<div class='vault-header'>🔱 SECTOR 2: SYMMETRY GRIDS</div>", unsafe_allow_html=True)
    st.write(f"Welcome, Commander {st.session_state.get('user_name', 'Soldier')}. Compass alignment complete.")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<div class='grid-box'><span class='compass-text'>NORTH</span><br>--- SYMMETRY CORE ---</div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='grid-box'><span class='compass-text'>WEST</span></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='grid-box'><span class='compass-text'>EAST</span></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='grid-box'><span class='compass-text'>SOUTH</span></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.write("### 🧮 4-Digit Input")
    n1 = st.number_input("Winning Number 1", 0, 9)
    n2 = st.number_input("Winning Number 2", 0, 9)
    n3 = st.number_input("Winning Number 3", 0, 9)
    n4 = st.number_input("Winning Number 4", 0, 9)
    
    if st.button("CALCULATE SYMMETRY OUTCOME"):
        st.success(f"Outcome calculated for {n1}{n2}{n3}{n4}. Analyzing patterns...")
