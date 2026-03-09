import streamlit as st

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="The Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING (GOLDEN IMPACT ARMOR) ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* THE SLOW GENTLE GLOBE PULSE */
    @keyframes slowGoldPulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 10px #FFD700); }
        50% { transform: scale(1.05); filter: drop-shadow(0 0 20px #FFD700); }
        100% { transform: scale(1); filter: drop-shadow(0 0 10px #FFD700); }
    }
    
    /* HEAVY BOLTED IMPACT HEADERS */
    .mitrax-title {
        text-align: center;
        color: #FFD700;
        font-family: 'Impact', sans-serif;
        font-size: 55px;
        font-weight: 900;
        letter-spacing: 3px;
        text-shadow: 4px 4px 0px #000000;
        margin-bottom: 0px;
    }
    
    .vault-header { text-align: center; color: #FFD700; font-size: 38px; font-weight: bold; font-family: 'Impact'; }
    
    .stButton>button { 
        background-color: #FFD700 !important; color: #000000 !important; 
        font-family: 'Impact', sans-serif !important; font-weight: 900 !important; 
        text-transform: uppercase; border-radius: 12px !important; width: 100%; 
        border: 2px solid #000000; font-size: 24px !important;
    }
    
    .pay-link {
        display: block; text-align: center; background-color: #FFD700; color: #000000 !important;
        padding: 20px; border-radius: 12px; font-family: 'Impact', sans-serif !important;
        font-weight: 900 !important; text-transform: uppercase; text-decoration: none;
        font-size: 26px; border: 3px solid #000000; margin: 15px 0;
    }
    
    .grid-box { border: 2px solid #FFD700; padding: 25px; border-radius: 15px; background-color: #1A1A1A; margin-bottom: 20px; }
    
    /* SHRUNKEN COMPASS CONTAINER */
    .symbol-container { text-align: center; margin-bottom: 10px; padding: 10px; }
    .star-base { font-size: 100px; color: #FFD700; position: relative; display: inline-block; }
    .world-center { position: absolute; top: 15%; left: 0; right: 0; font-size: 50px; animation: slowGoldPulse 6s infinite; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE SHRUNKEN UNIVERSAL COMPASS ---
st.markdown("""
    <div class='symbol-container'>
        <div class='star-base'>
            ✧
            <div class='world-center'>🌍</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'intro'

# --- PHASE 1: THE PREDICTION INTRO ---
if st.session_state.step == 'intro':
    # HEAVY BOLTED TITLE
    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:#FFD700; font-family:Impact; font-size:25px; margin-bottom:20px;'>PREDICTION PIC 4</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-bottom: 25px;'>
        <h3 style='color:#FFFFFF; font-style:italic;'>Stop gambling and start forecasting.</h3>
        <p style='font-size:20px; color:#FFFFFF;'>
            The Mitrax Oracle uses mathematical patterns to fill the Grid with winning numbers.<br>
            Get a <span style='color:#FFD700; font-weight:bold;'>95% chance of winning</span> by subscribing to the pattern analysis today.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.video("https://youtu.be/Hhj7UPfmB6U") 
    
    if st.button("PROCEED TO SUBSCRIPTION"):
        st.session_state.step = 'legal'; st.rerun()

# --- OTHER PHASES (WELCOME, SIGNUP, ETC) ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700; font-family:Impact;'>SERVICE TERMS</h1>", unsafe_allow_html=True)
    st.info("Unlock the 95% mathematical advantage using the 6x Grid system.")
    if st.button("I AGREE TO THE TERMS"):
        st.session_state.step = 'welcome'; st.rerun()

elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700; font-family:Impact;'>GET YOUR PREDICTIONS</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align:center;'>
            <h2 style='color:#FFD700; font-family:Impact;'>SUBSCRIBE FOR FULL ACCESS</h2>
            <p style='color:#FFD700; font-size:24px; font-weight:900;'>$39.95 EVERY 3 MONTHS</p>
            <a href="https://www.paypal.com/ncp/payment/ZXZXQZ7ZBYUN8" target="_blank" class="pay-link">ACTIVATE SUBSCRIPTION NOW</a>
        </div>
    """, unsafe_allow_html=True)
