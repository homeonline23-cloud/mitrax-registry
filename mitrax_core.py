import streamlit as st
import datetime

# =========================================================
# 🏛️ THE MITRAX EMPIRE: FINAL GHOST SYNC (FULL-AUTO)
# =========================================================

# --- 1. THE IMPERIAL CHRONOMETER ---
# Automatically flips the banners at Midnight (Server Time)
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

today_val = f"{now.day}-1"      # The Red Pillar (Today)
tomorrow_val = f"{tomorrow.day}-3"  # The Blue Pillar (Sabbath)

# --- 2. PAGE CONFIG (THE VAULT LOOK) ---
st.set_page_config(page_title="MITRAX REGISTRY", layout="wide")

st.markdown(f"""
    <style>
    /* Imperial Dark Theme */
    .stApp {{ background-color: #050505; color: #E0E0E0; font-family: 'Courier New', monospace; }}
    
    /* The War Room Video Frame */
    .video-container {{
        position: relative; width: 100%; max-width: 900px; margin: auto;
        border: 2px solid #00D4FF; border-radius: 12px; overflow: hidden;
        box-shadow: 0px 0px 25px rgba(0, 212, 255, 0.2);
    }}
    
    /* THE DYNAMIC OVERLAY BANNERS */
    .banner-overlay {{
        position: absolute; top: 12%; width: 100%; display: flex;
        justify-content: space-around; pointer-events: none; z-index: 10;
    }}
    .red-banner {{ color: #FF0000; font-size: 34px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    .blue-banner {{ color: #0000FF; font-size: 34px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    
    /* 4-Sector Box Styling */
    .sector-box {{
        background: rgba(255, 255, 255, 0.03);
        padding: 15px 5px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #222;
        height: 160px;
        transition: 0.3s;
    }}
    .sector-box:hover {{ border-color: orange; background: rgba(255, 165, 0, 0.05); }}
    
    /* The Orange Fire Global Button */
    .stButton>button {{
        width: 100%; background-color: #00D4FF; color: black;
        font-weight: bold; border-radius: 20px; border: none;
    }}
    .stButton>button:hover {{ background-color: #FF8C00; color: white; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE COMMANDER'S HEADER & GLOBAL GATEWAY ---
header_col, button_col = st.columns([3, 1])

with header_col:
    st.markdown("<h2 style='color: #00D4FF; letter-spacing: 5px; margin: 0;'>🏛️ MITRAX-REGISTRY: GHOST SYNC</h2>", unsafe_allow_html=True)

with button_col:
    # This button takes them to the world's ingredients without exposing our names
    st.link_button("🌐 GLOBAL RESULTS", "https://www.lotterypost.com/results")

# --- 4. THE MARCHING SOLDIERS (THE HEART) ---
# Replace 'qY8S7Xv8Lp8' if you have a new YouTube ID
VIDEO_ID = "qY8S7Xv8Lp8" 
st.markdown(f"""
    <div class="video-container">
        <div class="banner-overlay">
            <div class="red-banner">{today_val} RED</div>
            <div class="blue-banner">{tomorrow_val} BLUE</div>
        </div>
        <iframe width="100%" height="480" 
            src="https://www.youtube.com/embed/{VIDEO_ID}?autoplay=1&mute=1&loop=1&playlist={VIDEO_ID}&controls=0" 
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# --- 5. THE 4-SECTOR TROPICAL SHIELD ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 26px;'>🌴 🇦🇼 🌴</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>ARUBA SECTOR</p>", unsafe_allow_html=True)
    st.caption("Utrecht Sync 19:00")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 26px;'>🌴 🇧🇶 🌴</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>BONAIRE SECTOR</p>", unsafe_allow_html=True)
    st.caption("Catochi Flow")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 26px;'>🌴 🇨🇼 🌴</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>CURACAO SECTOR</p>", unsafe_allow_html=True)
    st.caption("2620 Registry Sync")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='sector-box'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 26px;'>🌴 🇸🇽 🌴</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 14px; font-weight: bold;'>SXM SECTOR</p>", unsafe_allow_html=True)
    st.caption("Island Pick 4 Flow")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. SECURITY FOOTER ---
st.markdown("<p style='text-align: center; color: #00FF00; font-size: 10px; margin-top: 20px;'>SYSTEM STATUS: 4-SECTOR
