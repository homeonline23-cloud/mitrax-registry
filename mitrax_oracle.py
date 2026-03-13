import streamlit as st
import datetime

# --- 1. THE IMPERIAL CHRONOMETER ---
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
today_val = f"{now.day}-1"      
tomorrow_val = f"{tomorrow.day}-3"  

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="MITRAX REGISTRY", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #050505; color: #E0E0E0; font-family: 'Courier New', monospace; }}
    .video-container {{
        position: relative; width: 100%; max-width: 900px; margin: auto;
        border: 2px solid #00D4FF; border-radius: 12px; overflow: hidden;
    }}
    .banner-overlay {{
        position: absolute; top: 12%; width: 100%; display: flex;
        justify-content: space-around; pointer-events: none; z-index: 10;
    }}
    .red-banner {{ color: #FF0000; font-size: 34px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    .blue-banner {{ color: #0000FF; font-size: 34px; font-weight: bold; text-shadow: 3px 3px 6px black; }}
    .sector-box {{
        background: rgba(255, 255, 255, 0.03); padding: 15px 5px; border-radius: 10px;
        text-align: center; border: 1px solid #222; height: 210px;
    }}
    .privacy-box {{
        background: rgba(0, 212, 255, 0.05); padding: 20px; border-radius: 12px;
        border: 1px dashed #00D4FF; margin-top: 30px; font-size: 13px;
    }}
    .international-tag {{
        color: #FFD700; font-size: 12px; font-style: italic; letter-spacing: 2px; text-align: right;
    }}
    .flag-img {{ width: 50px; margin-top: 10px; border-radius: 4px; border: 1px solid #444; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & INTERNATIONAL SIGNATURE ---
header_col, tag_col = st.columns([2, 1])
with header_col:
    st.markdown("<h2 style='color: #00D4FF; letter-spacing: 5px; margin: 0;'>🏛️ MITRAX-REGISTRY</h2>", unsafe_allow_html=True)
with tag_col:
    st.markdown("<p class='international-tag'>ALGORITHM: UNIVERSAL CAPABILITY<br>ENABLED FOR INTERNATIONAL USE</p>", unsafe_allow_html=True)

# --- 4. THE STANDBY VAULT (VIDEO) ---
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

# --- 5. THE 4-SECTOR TROPICAL SHIELD (WITH FLAGS) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='sector-box'><div style='font-size: 26px;'>🌴</div><p style='font-size: 14px; font-weight: bold; margin-bottom: 5px;'>ARUBA</p><img src='https://flagcdn.com/aw.svg' class='flag-img'></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='sector-box'><div style='font-size: 26px;'>🌴</div><p style='font-size: 14px; font-weight: bold; margin-bottom: 5px;'>BONAIRE</p><img src='https://flagcdn.com/bq.svg' class='flag-img'></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='sector-box'><div style='font-size: 26px;'>🌴</div><p style='font-size: 14px; font-weight: bold; margin-bottom: 5px;'>CURACAO</p><img src='https://flagcdn.com/cw.svg' class='flag-img'></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='sector-box'><div style='font-size: 26px;'>🌴</div><p style='font-size: 14px; font-weight: bold; margin-bottom: 5px;'>ST. MARTIN</p><img src='https://flagcdn.com/sx.svg' class='flag-img'><br><br></div>", unsafe_allow_html=True)
    st.link_button("👑 KING LOTTERY", "https://loteriasdominicanas.com/king-lottery")

# --- 6. IMPERIAL PRIVACY PACT ---
st.markdown("""
<div class='privacy-box'>
    <h4 style='color: #00D4FF; margin-top: 0;'>🔐 THE MITRAX PRIVACY PACT [ENCRYPTED]</h4>
    <p>Your data is Imperial Property. We <b>NEVER</b> sell information to third parties, advertisers, or outside agencies. 
    Your presence on this bridge is strictly between you and the Universe.</p>
    <p style='color: #FFD700;'><i><b>AUTO-DESTRUCT PROTOCOL:</b> Upon the cessation of membership, all personal logs and identifying details are automatically purged from the Registry forever. No traces remain.</i></p>
</div>
""", unsafe_allow_html=True)

# --- 7. SECURITY FOOTER ---
st.markdown("<p style='text-align: center; color: #00FF00; font-size: 10px; margin-top: 20px;'>SYSTEM STATUS: 4-SECTOR GHOST SYNC [LOCKED]</p>", unsafe_allow_html=True)
