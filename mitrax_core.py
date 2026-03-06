import datetime
import streamlit as st

# --- 1. CALCULATING THE DYNAMIC MARCHING NUMBERS ---
now = datetime.datetime.now()
today_code = f"{now.day}-1"
tomorrow_code = f"{now.day + 1}-3"

# --- 2. THE SOLDIER MARCH WITH DYNAMIC OVERLAY ---
st.markdown(f"""
    <div style="position: relative; width: 100%; max-width: 800px; margin: auto;">
        <video width="100%" autoplay loop muted style="border-radius: 15px; border: 2px solid orange; box-shadow: 0px 0px 20px rgba(255,165,0,0.5);">
            <source src="YOUR_SOLDIER_VIDEO_URL.mp4" type="video/mp4">
        </video>
        
        <div style="position: absolute; top: 15%; width: 100%; display: flex; justify-content: space-around;">
            <span style="color: #FF0000; font-family: 'Courier New'; font-weight: bold; font-size: 28px; text-shadow: 2px 2px 5px black;">
                {today_code}
            </span>
            <span style="color: #0000FF; font-family: 'Courier New'; font-weight: bold; font-size: 28px; text-shadow: 2px 2px 5px black;">
                {tomorrow_code}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
