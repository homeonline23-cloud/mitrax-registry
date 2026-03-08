import streamlit as st
from datetime import datetime

# --- 1. COMMAND CENTER ENGINE ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING (BLACK & GOLD) ---
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
        line-height: 1.5;
    }
    .client-header { text-align: center; color: #FFD700; margin-bottom: 0px; }
    .welcome-card {
        background-color: #1A1A1A; padding: 25px; border-radius: 15px;
        border: 1px solid #333; line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'video'

# --- 3. PHASE 1: SOLDIER DISPLAY (WITH AUTOPLAY) ---
if st.session_state.step == 'video':
    st.markdown("<h1 class='client-header'>🛡️ THE MITRAX COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>Pick 4 Worldwide🌏</h3>", unsafe_allow_html=True)

    # THE GLOBAL MANTRA
    st.markdown("""
    <div class='mantra-box'>
    "The 4-digit Prediction Calculator that can be used Globally. By entering the 4 chosen winning numbers 
    into the calculator Grids. When analyzing the symmetry patterns, you can see and identify potential 
    winning numbers in the GRID’s. There’s now a 95% chance of increasing your chances of winning."
    </div>
    """, unsafe_allow_html=True)

    # --- THE SOLDIER VIDEO (AUTOPLAY ENABLED) ---
    # Replace the link below with your CORRECT YouTube link
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", autoplay=True, muted=True) 
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("PROCEED TO MISSION BRIEFING", use_container_width=True):
        st.session_state.step = 'legal'
        st.rerun()

# --- 4. PHASE 2: TERMS & POLICY (READ ME) ---
elif st.session_state.step == 'legal':
    st.markdown("<h1 class='client-header'>📜 READ FIRST: TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color:#1E1E1E; padding:20px; border-radius:10px; border:1px solid #FFD700; height:350px; overflow-y:scroll;'>
        <h3>Terms and Conditions & Private Policy</h3>
        <p>Analyzing symmetry patterns identifies potential winning numbers in the GRID’s. 
        There’s now a 95% chance of increasing your chances of winning. 
        All data remains independent and secured within the Mitrax Vault.</p>
        <p>By clicking accept, you acknowledge the 4x Grid symmetry protocols.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("I HAVE READ AND ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- 5. PHASE 3: THE WELCOME LETTER ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 class='client-header'>✉️ WELCOME TO THE FAMILY</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='welcome-card'>
        <h3>Welcome to The Mitrax Command Center!</h3>
        <p>Dear Member, we're thrilled to have you! Here is how to install the app:</p>
        <p><b>Android:</b> Tap 3 dots (⋮) -> "Install App".</p>
        <p><b>iPhone:</b> "Share" icon -> "Add to Home Screen".</p>
        <p><i>The Mitrax Icon is now on your phone. Wake up the 14 Soldiers anytime!</i></p>
        <p>Warm regards,<br><b>The Mitrax Team</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CONTINUE TO THE MITRAX VAULT"):
        st.session_state.step = 'signup'
        st.rerun()

# --- 6. PHASE 4: SIGN UP & VAULT ---
elif st.session_state.step == 'signup':
    st.markdown("<h1 class='client-header'>👤 SIGN UP TO CONTINUE</h1>", unsafe_allow_html=True)
    with st.form("vault_registration"):
        st.text_input("Member's Name")
        st.text_input("Active Email")
        if st.form_submit_button("ACTIVATE VAULT ACCESS"):
            st.success("Registration Sent. Welcome to the Vault.")
            
    st.markdown("<br><br><hr>", unsafe_allow_html=True)
    with st.expander("🛠️"):
        if st.text_input("CHEF CODE", type="password") == "Mitrax-Chef":
            st.info("Vault Overridden. Grids Online.")
