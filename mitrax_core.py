import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL "GOLDEN GLOW" STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    @keyframes goldPulse {
        0% { text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700; }
        50% { text-shadow: 0 0 25px #FFD700, 0 0 50px #FFA500; }
        100% { text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700; }
    }
    
    .vault-header {
        text-align: center; 
        color: #FFD700; 
        font-size: 38px; 
        font-weight: bold;
        animation: goldPulse 2s infinite;
        margin-bottom: 25px;
    }
    
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important;
        border: 2px solid #FFD700 !important;
        width: 100%;
    }
    
    .mantra-box { 
        text-align: center; color: #FFFFFF; font-size: 19px; 
        padding: 25px; background-color: #1A1A1A;
        border-radius: 15px; border: 2px solid #FFD700; margin: 15px 0px;
    }

    .pyramid-frame {
        border: 4px solid #FFD700; 
        border-radius: 20px;
        padding: 5px; 
        background-color: #000;
        box-shadow: 0px 0px 40px rgba(255, 215, 0, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MISSION PROGRESSION LOGIC ---
if 'step' not in st.session_state: 
    st.session_state.step = 'video'

# --- PHASE 1: THE SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)
    
    st.markdown("<div class='mantra-box'>The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning.</div>", unsafe_allow_html=True)

    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    
    if st.button("PROCEED TO MISSION BRIEFING", key="btn_brief"):
        st.session_state.step = 'legal'
        st.rerun()

# --- PHASE 2: TERMS & POLICY ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 READ FIRST: TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#1E1E1E; padding:25px; border-radius:15px; border:1px solid #FFD700; height:400px; overflow-y:scroll;'><h3>The Mitrax Global Symmetry Protocol</h3><p>By entering the Mitrax Vault, you acknowledge that our 4-digit Prediction Calculator utilizes advanced symmetry grids designed for global datasets. Our analyzed patterns offer a 95% chance of increasing your success.</p></div>", unsafe_allow_html=True)
    
    if st.button("I HAVE READ AND ACCEPT THE TERMS", key="btn_accept"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- PHASE 3: THE WELCOME LETTER ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME TO THE FAMILY</h1>",
                
