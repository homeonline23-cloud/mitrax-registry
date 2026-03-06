import streamlit as st
import datetime

# =========================================================
# 🏛️ THE MITRAX EMPIRE: STEALTH MODE ENGINE
# =========================================================

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

today_val = f"{now.day}-1"      
tomorrow_val = f"{tomorrow.day}-3"  

st.set_page_config(page_title="THE MITRAX EMPIRE", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; color: #E0E0E0; font-family: 'Courier New', monospace; }}
    .video-container {{
        position: relative; width: 100%; max-width: 850px; margin: auto;
        border: 3px solid #FF8C00; border-radius: 15px;
        box-shadow: 0px 0px 30px rgba(255, 140, 0, 0.4); overflow: hidden;
    }}
    .banner-overlay {{
        position: absolute; top: 15%; width: 100%; display: flex;
        justify-content: space-around; pointer-events: none; z-index: 10;
    }}
    .red-banner {{ color: #FF0000; font-size: 34px; font-weight: bold; text-shadow: 2px 2px 5px black; }}
    .blue-banner {{ color: #0000FF; font-size: 34px; font-weight: bold; text-shadow: 2px 2px 5px black; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: orange;'>🏛️ MITRAX-REGISTRY: STEALTH</h1>", unsafe_allow_html=True)

# --- THE MARCHING SOLDIERS ---
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

# --- THE STEALTH COMPANION BRIDGE ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🇳🇱 GOOD DAY FOR LUCK")
    st.write("Utrecht Frequency")
    st.caption(f"Targeting Row {now.day}")

with col2:
    st.markdown("### 🌴 🇦🇼 🌴")
    st.write("Aruba/Curaçao Sector")
    st.success("Stealth Link: ACTIVE")

with col3:
    st.markdown("### 🌴 🇸🇽 🌴")
    st.write("St. Maarten Sector")
    st.info(f"Targeting Row {tomorrow.day}")

st.sidebar.header("⚖️ SECURITY LOCK")
st.sidebar.write("Names Encrypted.")
st.sidebar.write("Coconuts Guarding the Gates.")
