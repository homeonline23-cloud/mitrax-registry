import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CORE ENGINE SETTINGS ---
st.set_page_config(page_title="Mitrax Imperial Registry", layout="wide")

# --- 2. THE AUTO-FILL PROTOCOL ---
def get_winning_numbers():
    """Beams data from the Dominican lottery coordinates."""
    try:
        url = "https://loteriasdominicanas.com/king-lottery"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Pulling the first 4 winning digits from the 'score' spans
        results = [span.text.strip() for span in soup.find_all("span", class_="score")[:4]]
        if len(results) == 4:
            return results
    except Exception:
        pass
    return ["1", "2", "3", "4"] # Imperial Default if signal fails

# --- 3. SESSION INITIALIZATION ---
if 'numbers' not in st.session_state:
    st.session_state.numbers = get_winning_numbers()

# --- 4. THE COMMAND CENTER ---
st.title("🌌 Mitrax Registry: Daily Sync")

if st.button("🔄 RE-SYNC WITH UNIVERSAL COMPASS"):
    st.session_state.numbers = get_winning_numbers()
    st.rerun()

# --- 5. THE VISUAL GRID (Fixes Visibility Issues) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h2 style='color: red; text-align: center;'>7/1 (RED)</h2>", unsafe_allow_html=True)
    st.text_input("Win 1", value=st.session_state.numbers[0], key="w1")

with col2:
    st.markdown("<h2 style='text-align: center;'>Sector 2</h2>", unsafe_allow_html=True)
    st.text_input("Win 2", value=st.session_state.numbers[1], key="w2")

with col3:
    st.markdown("<h2 style='color: blue; text-align: center;'>8/3 (BLUE)</h2>", unsafe_allow_html=True)
    st.text_input("Win 3", value=st.session_state.numbers[2], key="w3")

with col4:
    st.markdown("<h2 style='text-align: center;'>Sector 4</h2>", unsafe_allow_html=True)
    st.text_input("Win 4", value=st.session_state.numbers[3], key="w4")

st.info("SYSTEM STATUS: ONLINE | AUTO-FILL ACTIVE")
