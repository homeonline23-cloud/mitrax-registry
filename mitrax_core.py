import streamlit as st
from datetime import datetime

# --- 1. ENGINE CONFIGURATION ---
st.set_page_config(page_title="Mitrax Oracle Vision", layout="wide")

# --- 2. UNIVERSAL STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/impact');
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .mitrax-title { text-align: center; color: #FFD700; font-family: 'Impact', sans-serif; font-size: 50px; letter-spacing: 12px; margin-bottom: 0px; }
    .gate-frame {
        border: 3px solid #FFD700; border-radius: 20px; padding: 30px; text-align: center;
        background: rgba(255, 215, 0, 0.05); margin: 20px auto; max-width: 900px;
    }
    .video-container { border: 2px solid #FFD700; border-radius: 10px; overflow: hidden; margin-bottom: 20px; }
    .global-banner { 
        background: rgba(255, 215, 0, 0.1); border: 2px solid #FFD700; border-radius: 10px; 
        padding: 20px; text-align: center; color: #FFFFFF; font-family: 'Arial', sans-serif; 
        font-weight: bold; font-size: 18px; margin-top: 20px;
    }
    .island-header { color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; border-bottom: 2px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE LOGIC GATE ---
if 'step' not in st.session_state:
    st.session_state.step = 'gate'

# --- 4. SECTOR: THE FRONT GATE (WITH BROADCAST) ---
if st.session_state.step == 'gate':
    st.markdown("<div style='text-align: center; font-size: 60px; margin-top: 20px;'>✧🌍✧</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='gate-frame'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #FFD700; font-family: Impact; letter-spacing: 8px;'>MITRAX EMPIRE BROADCAST</h1>", unsafe_allow_html=True)
    
    # --- THE YOUTUBE SCREEN ---
    # PASTE YOUR YOUTUBE LINK BELOW!
    video_url = "https://www.youtube.com/watch?v=YOUR_updwq7Xz-cQ" 
    st.video(video_url)
    
    st.markdown("<p style='font-family: Arial; font-weight: bold;'>WATCH THE LATEST IMPERIAL BRIEFING ABOVE</p>", unsafe_allow_html=True)
    
    if st.button("🚀 ACCESS THE ORACLE VAULT"):
        st.session_state.step = 'sector3'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. SECTOR: THE ORACLE VAULT (INSIDE) ---
elif st.session_state.step == 'sector3':
    imperial_date = datetime.now().strftime("%-m/%-d/%Y")
    
    if st.button("⬅ BACK TO BROADCAST"):
        st.session_state.step = 'gate'
        st.rerun()

    st.markdown("<div class='mitrax-title'>THE MITRAX ORACLE</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:#FFD700;'>SESSION DATE: {imperial_date}</p>", unsafe_allow_html=True)

    # --- THE 4-TIER ISLAND WINNER BOARD ---
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>REGIONAL WINNER BOARD</h3>", unsafe_allow_html=True)
    i_cols = st.columns(4)
    islands = ["ARUBA", "BONAIRE", "CURAÇAO", "ST. MARTIN"]
    for i, island in enumerate(islands):
        with i_cols[i]:
            st.markdown(f"<div class='island-header'>{island}</div>", unsafe_allow_html=True)
            for row in range(1, 5):
                st.text_input(f"v_{island}_{row}", key=f"win_{island}_{row}", label_visibility="collapsed", placeholder="----")

    # --- THE WHITE BOLD ARIAL GLOBAL COMMAND BANNER ---
    st.markdown("""
        <div class='global-banner'>
            🌍 MEMBERS MAY ENTER LOCAL WINNING NUMBERS ABOVE 
            TO ANALYZE SYMMETRY WITHIN THE 6X MATRIX BELOW. 🌍
        </div>
        """, unsafe_allow_html=True)

    # THE 6X SYMMETRY MATRIX
    st.markdown("<h3 style='text-align: center; color: #FFD700; font-family:Arial;'>95% PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
    g_cols = st.columns(6)
    for i in range(6):
        with g_cols[i]:
            st.markdown(f"<div style='border: 1px solid #FFD700; padding: 10px; text-align: center; background: rgba(255,215,0,0.05); color:#FFD700; font-weight:bold;'>SECTOR {i+1}</div>", unsafe_allow_html=True)
            st.number_input(f"v_{i}", label_visibility="collapsed", key=f"v_{i}", min_value=0, max_value=9999)

    st.success("VAULT ONLINE")
    
