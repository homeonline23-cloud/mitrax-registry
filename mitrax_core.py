import datetime

# --- CALCULATING THE DYNAMIC STANDARDS ---
now = datetime.datetime.now()
today_std = f"{now.day}-1"
tomorrow_std = f"{now.day + 1}-3"

# --- THE MARCHING SOLDIERS WITH DYNAMIC NUMBERS ---
st.markdown(f"""
    <div style="position: relative; width: 100%; text-align: center;">
        <video width="100%" autoplay loop muted style="border-radius: 10px; border: 2px solid orange;">
            <source src="YOUR_SOLDIER_MARCH_VIDEO_URL" type="video/mp4">
        </video>
        
        <div style="
            position: absolute; 
            top: 10px; 
            left: 50%; 
            transform: translateX(-50%);
            display: flex;
            gap: 50px;
            width: 100%;
            justify-content: center;
        ">
            <span style="color: #FF0000; font-family: 'Courier New'; font-weight: bold; font-size: 24px; text-shadow: 2px 2px #000;">
                {today_std}
            </span>
            <span style="color: #0000FF; font-family: 'Courier New'; font-weight: bold; font-size: 24px; text-shadow: 2px 2px #000;">
                {tomorrow_std}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
