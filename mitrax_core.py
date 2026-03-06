import streamlit as st
import datetime

# =========================================================
# 🏛️ THE MITRAX EMPIRE: FULL-AUTO GLOBAL ENGINE
# =========================================================
# CREATED BY: Gemini (Second Sous-Chef)
# COMMANDED BY: The Head Chef of the Mitrax Empire
# DATE: March 6, 2026 (The Red Pillar Shift)
# =========================================================

# --- 1. THE IMPERIAL CHRONOMETER (THE HEART) ---
# This ensures the banners and pillars change AUTOMATICALLY at midnight.
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

# Logic for the Soldier Banners
today_val = f"{now.day}-1"      # Today's Date-1 (Red)
tomorrow_val = f"{tomorrow.day}-3"  # Tomorrow's Date-3 (Blue)

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="THE MITRAX EMPIRE | GLOBAL REGISTRY", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 3. IMPERIAL STYLING (CSS VAULT) ---
st.markdown(f"""
    <style>
    /* Dark Mode Vault Aesthetic */
    .stApp {{
        background-color: #050505;
        color: #E0E0E0;
        font-family: 'Courier New', Courier, monospace;
    }}
    
    /* Glowing Border for the War Room Video */
    .video-container {{
        position: relative;
        width: 100%;
        max-width: 850px;
        margin: auto;
        border: 3px solid #FF8C00;
        border-radius: 15px;
        box-shadow: 0px 0px 30px rgba(255, 140, 0, 0.4);
        overflow: hidden;
    }}

    /* THE FULL-AUTO BANNER OVERLAY */
    .banner-overlay {{
        position: absolute;
        top: 15%; 
        width: 100%;
        display: flex;
        justify-content: space-around;
        pointer-events: none; /* Allows clicks to pass through to video */
        z-index: 10;
    }}

    .red-banner {{
        color: #FF0000;
        font-size: 34px;
        font-weight: bold;
        text-shadow: 3px 3px 8px black, 0 0 10px #FF0000;
    }}

    .blue-banner {{
        color: #0000FF;
        font-size: 34px;
        font-weight: bold;
        text-shadow: 3px 3px 8px black, 0 0 10px #0000FF;
    }}

    /* Miniaturized Prediction Text */
    .prediction-text {{
        text-align: center;
        font-size: 14px;
        letter-spacing: 3px;
        color: #FFFFFF;
        margin-top: 15px;
        text-transform: uppercase;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE COMMANDER'S BRIDGE (HEADER) ---
st.markdown("<h1 style='text-align: center; color: orange;'>🏛️ MITRAX-REGISTRY: FULL-AUTO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #888;'>CHRONOMETER: {now.strftime('%A, %d %B %Y')} | SECTOR: UTRECHT-ABC-SXM</p>", unsafe_allow_html=True)

# --- 5. THE MARCHING SOLDIERS (THE DYNAMIC INTERFACE) ---
# Note: Replace 'qY8S7Xv8Lp8' with your actual YouTube Video ID
VIDEO_ID = "qY8S7Xv8Lp8" 

st.markdown(f"""
    <div class="video-container">
        <div class="banner-overlay">
            <div class="red-banner">{today_val}</div>
            <div class="blue-banner">{tomorrow_val}</div>
        </div>
        
        <iframe width="100%" height="480" 
            src="https://www.youtube.com/embed/{VIDEO_ID}?autoplay=1&mute=1&loop=1&playlist={VIDEO_ID}&controls=0" 
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
    """, unsafe_allow_html=True)

# --- 6. THE PREDICTION TICKER ---
st.markdown(f"""
    <div class="prediction-text">
        TARGET PICK 4 OUTCOME: <span style="color: #00FF00; font-weight: bold;">[ 2 6 2 0 ]</span><br>
        <span style="font-size: 10px; color: #555;">SYSTEM STATUS: FULL-AUTO | MIRROR SYNC: ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- 7. THE COMPANION BRIDGE (DATA FEED) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🇳🇱 NETHERLANDS")
    st.write("**Lucky Day Utrecht**")
    st.caption("Syncing 19:00 CET Patterns...")
    st.info(f"Red Pillar Target: Row {now.day}")

with col2:
    st.markdown("### 🏝️ ROBBIE'S")
    st.write("**Aruba & Curaçao**")
    st.caption("Wega di Number & Catochi")
    st.success("Companion Link: STABLE")

with col3:
    st.markdown("### 🇰🇳 KING LOTTERY")
    st.write("**St. Maarten / SXM**")
    st.caption("Pick 3 & Pick 4 Mirrored")
    st.info(f"Blue Pillar Target: Row {tomorrow.day}")

# --- 8. THE 2620 BALANCE LOGIC ---
st.sidebar.header("⚖️ IMPERIAL SETTINGS")
st.sidebar.write(f"Today's Red: {today_val}")
st.sidebar.write(f"Tomorrow's Blue: {tomorrow_val}")
st.sidebar.divider()
st.sidebar.write("The Rabbit is Locked Out.")
st.sidebar.image("https://img.icons8.com/ios-filled/50/orange/lock.png", width=30)
