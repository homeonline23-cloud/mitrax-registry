import streamlit as st
from datetime import datetime

# --- 1. COMMAND CENTER ENGINE ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. THE IMPERIAL PYRAMID STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important;
        border: 2px solid #FFD700 !important;
    }
    .mantra-box { 
        text-align: center; color: #FFFFFF; font-size: 19px; 
        padding: 20px; background-color: #1A1A1A;
        border-radius: 15px; border: 2px solid #FFD700; margin: 15px 0px;
    }
    .vault-header {
        text-align: center; color: #FFD700; 
        text-shadow: 0px 0px 15px #FFD700;
        font-size: 32px; font-weight: bold;
    }
    .pyramid-sector {
        border: 2px solid #FFD700; border-radius: 20px;
        padding: 30px; background: linear-gradient(180deg, #1A1A1A 0%, #000000 100%);
        text-align: center; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- 3. PHASE 1: SOLDIER DISPLAY ---
if st.session_state.step == 'video':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)
    
    st.markdown("""<div class='mantra-box'>"The 4-digit Prediction Calculator that can be used Globally... There’s now a 95% chance of increasing your chances of winning."</div>""", unsafe_allow_html=True)
    
    # Replace with your Soldier Video Link
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    
    if st.button("PROCEED TO MISSION BRIEFING", use_container_width=True):
        st.session_state.step = 'legal'
        st.rerun()

# --- 4. PHASE 2: TERMS & POLICY ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>📜 READ FIRST</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#1E1E1E; padding:20px; border-radius:10px; border:1px solid #FFD700; height:350px; overflow-y:scroll;'><h3>Terms and Conditions & Private Policy</h3><p>95% probability based on internal symmetry detection...</p></div>", unsafe_allow_html=True)
    if st.button("I ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- 5. PHASE 3: WELCOME LETTER ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 style='text-align:center; color:#FFD700;'>✉️ WELCOME FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#1A1A1A; padding:20px; border-radius:15px; border:1px solid #333;'><h3>Welcome to The Mitrax Command Center!</h3><p>Wake up the 14 Soldiers anytime!</p></div>", unsafe_allow_html=True)
    if st.button("ENTER THE MITRAX VAULT"):
        st.session_state.step = 'signup'
        st.rerun()

# --- 6. PHASE 4: THE MITRAX VAULT (WITH PYRAMID) ---
elif st.session_state.step == 'signup':
    st.markdown("<div class='vault-header'>📐 THE MITRAX VAULT</div>", unsafe_allow_html=True)
    
    # PYRAMID DISPLAY AREA
    st.markdown("""
    <div class='pyramid-sector'>
        <h2 style='color:#FFD700;'>PYRAMID SYMMETRY ACTIVE</h2>
        <p style='color:#888;'>Identifying Potential Winning Numbers...</p>
    </div>
    """, unsafe_allow_html=True)

    # Place for the Pyramid Video / Image
    # st.video("YOUR_PYRAMID_VIDEO_LINK_HERE") 
    
    st.markdown("<br>", unsafe_allow_html=True)
    with st.form("pyramid_reg"):
        st.text_input("Commander Name")
        st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE PYRAMID ACCESS"):
            st.success("Accessing the 4x Symmetry Grids...")

    # CHEF'S OVERRIDE
    st.markdown("<br><br><hr>", unsafe_allow_html=True)
    with st.expander("🛠️"):
        if st.text_input("CHEF CODE", type="password") == "Mitrax-Chef":
            st.info("Vault Overridden. Grids Online.")
