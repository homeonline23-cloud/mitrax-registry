import streamlit as st
import datetime

# --- 1. THE IMPERIAL CHRONOMETER ---
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

today_val = f"{now.day}-1"      
tomorrow_val = f"{tomorrow.day}-3"  

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="MITRAX GLOBAL REGISTRY", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; color: #E0E0E0; font-family: 'Courier New', monospace; }}
    .video-container {{
        position: relative; width: 100%; max-width: 850px; margin: auto;
        border: 3px solid #00D4FF; border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(0, 212, 255, 0.3); overflow: hidden;
    }}
    .banner-overlay {{
        position: absolute; top: 15%; width: 100%; display: flex;
        justify-content: space-around; pointer-events: none; z-index: 10;
    }}
    .red-banner {{ color: #FF0000; font-size: 36px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    .blue-banner {{ color: #0000FF; font-size: 36px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    .sector-box {{
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #333;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE COMMANDER'S HEADER ---
st.markdown("<h1 style='text-align: center; color: #00D4FF;'>🏛️ MITRAX-REGISTRY: GHOST PROTOCOL</h1>", unsafe_allow_html=True)

# --- 4. THE MARCHING SOLDIERS (THE DYNAMIC INTERFACE) ---
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

st.write("---")

# --- 5. THE TROPICAL STEALTH BRIDGE ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.header("🇳🇱")
    st.subheader("GOOD DAY FOR LUCK")
    st.write("Utrecht Signal")
    st.caption(f"Syncing Row {now.day}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.header("🥥 🇦🇼 🥥")
    st.subheader("ARUBA SECTOR")
    st.write("Wega di Number")
    st.success("Ghost Link: ACTIVE")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.header("🥥 🇸🇽 🥥")
    st.subheader("SXM SECTOR")
    st.write("Island Pick 4")
    st.info(f"Sync
