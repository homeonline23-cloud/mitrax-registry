import datetime

# --- 1. THE IMPERIAL CHRONOMETER LOGIC ---
now = datetime.datetime.now()
day_num = now.day
month_name = now.strftime("%B").upper()
year_val = now.year

# --- 2. DISPLAYING THE DIGITAL CALENDAR ---
st.sidebar.markdown(f"""
    <div style="
        background-color: #222; 
        border: 2px solid orange; 
        border-radius: 10px; 
        padding: 10px; 
        text-align: center;
        box-shadow: 0px 0px 15px orange;
    ">
        <h3 style="color: orange; margin: 0; font-family: 'Courier New'; font-size: 14px;">IMPERIAL DATE</h3>
        <h1 style="color: white; margin: 0; font-family: 'Arial'; font-size: 48px;">{day_num}</h1>
        <h3 style="color: orange; margin: 0; font-family: 'Courier New'; font-size: 18px;">{month_name}</h3>
        <p style="color: #666; margin: 0; font-size: 12px;">QUADRANT {year_val}</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC PILLAR LOGIC (THE SHIFT) ---
# Today's Row becomes Red, Tomorrow's Row becomes Blue
today_row = f"{day_num}/1"
tomorrow_row = f"{day_num + 1}/3"
