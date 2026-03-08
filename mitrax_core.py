import streamlit as st
from datetime import datetime

# --- 1. COMMAND CENTER ENGINE ---
st.set_page_config(page_title="Mitrax Command Center", layout="wide")

# --- 2. IMPERIAL STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { 
        background-color: #FFD700 !important; 
        color: #0E1117 !important; 
        font-weight: bold !important; 
        border-radius: 12px !important;
        border: 2px solid #FFD700 !important;
        height: 3em !important;
        width: 100% !important;
    }
    .mantra-box { 
        text-align: center; color: #FFFFFF; font-size: 18px; 
        padding: 20px; background-color: #1E1E1E;
        border-radius: 15px; border-top: 4px solid #FFD700; margin: 10px 0px;
    }
    .welcome-letter {
        background-color: #1A1A1A; padding: 25px; border-radius: 15px;
        border: 1px solid #333; line-height: 1.6; font-size: 16px;
    }
    .client-header { text-align: center; color: #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT ---
if 'step' not in st.session_state:
    st.session_state.step = 'legal'

# --- 4. PHASE 1: POP-UP TERMS & CONDITIONS ---
if st.session_state.step == 'legal':
    st.markdown("<h1 class='client-header'>📜 READ FIRST: TERMS & POLICY</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color:#1E1E1E; padding:20px; border-radius:10px; border:1px solid #FFD700; height:400px; overflow-y:scroll;'>
        <h3>Terms and Conditions & Private Policy</h3>
        <p>The Mitrax Command Center is a 4-digit Prediction Calculator used Globally. 
        By accessing the 4x Grids, you agree to the mathematical symmetry protocols... 
        Predictions provide a 95% chance of increasing your success. 
        All data entered into the Mitrax Vault is encrypted and private.</p>
        <hr>
        <p><b>Global Symmetry Protocol:</b> Standalone tactical tool. No external links required.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("I HAVE READ AND ACCEPT THE TERMS"):
        st.session_state.step = 'welcome'
        st.rerun()

# --- 5. PHASE 2: WELCOME LETTER & INSTALLATION ---
elif st.session_state.step == 'welcome':
    st.markdown("<h1 class='client-header'>✉️ WELCOME TO THE COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='welcome-letter'>
        <h3>Welcome to The Mitrax Command Center!</h3>
        <p>Dear Member,</p>
        <p>We're thrilled to have you as part of the Mitrax community! Your journey toward unlocking the powers of the 4x Grids is just the beginning, and we can't wait for you to experience everything our app has to offer.</p>
        <p><b>How to Install the Mitrax App on Your Phone:</b></p>
        <ul>
            <li><b>For Android:</b> Tap the 3 dots (⋮) in the top-right corner of your browser. Select "Install App" or "Add to Home Screen".</li>
            <li><b>For iPhone:</b> Tap the "Share" icon (square with an arrow) at the bottom of your screen. Choose "Add to Home Screen".</li>
        </ul>
        <p><i>Voila! The Mitrax Icon is now on your phone. Just tap it to wake up the 14 Soldiers anytime and begin your new experience.</i></p>
        <p>Thank you for joining the Mitrax family! If you have any questions, reach out to our support team.</p>
        <p><b>Welcome aboard!</b><br>Warm regards,<br>The Mitrax Team</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CONTINUE TO THE MITRAX VAULT"):
        st.session_state.step = 'signup'
        st.rerun()

# --- 6. PHASE 3: SIGN UP ---
elif st.session_state.step == 'signup':
    st.markdown("<h1 class='client-header'>👤 SIGN UP TO CONTINUE</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>Enter credentials to unlock the Mitrax Vault</div>", unsafe_allow_html=True)
    
    with st.form("vault_signup"):
        name = st.text_input("Member's Name")
        email = st.text_input("Imperial Email")
        if st.form_submit_button("ACTIVATE VAULT ACCESS"):
            st.success(f"Welcome to the Family, {name}! Accessing 4x Grids...")
    
    # CHEF'S SECRET ACCESS
    st.markdown("<br><br><hr>", unsafe_allow_html=True)
    with st.expander("🛠️"):
        if st.text_input("CHEF CODE", type="password") == "Mitrax-Chef":
            st.info("Vault Overridden. Grids Online.")
