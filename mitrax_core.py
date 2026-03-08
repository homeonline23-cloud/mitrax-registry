import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- MITRAX ENGINE CONFIG ---
st.set_page_config(page_title="Mitrax Registry", layout="wide")

def fetch_lottery():
    """Automated bridge to fetch King Lottery Evening numbers"""
    try:
        url = "https://loteriasdominicanas.com/king-lottery"
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        # Looking for the specific winning digits in the HTML
        spans = soup.find_all("span", class_="score")
        if len(spans) >= 4:
            return [s.text for s in spans[:4]]
    except:
        pass
    return ["?", "?", "?", "?"]

# --- DATA INITIALIZATION ---
if 'numbers' not in st.session_state:
    st.session_state.numbers = fetch_lottery()

# --- THE VISUAL GRID ---
st.title("🌌 Mitrax Imperial Registry: Daily Sync")

if st.button("🔄 REFRESH FROM UNIVERSAL COMPASS"):
    st.session_state.numbers = fetch_lottery()
    st.rerun()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h2 style='color: red; text-align: center;'>7/1 (RED)</h2>", unsafe_allow_html=True)
    st.text_input("Digit 1", value=st.session_state.numbers[0], key="d1")

with col2:
    st.markdown("<h2 style='text-align: center;'>Sector 2</h2>", unsafe_allow_html=True)
    st.text_input("Digit 2", value=st.session_state.numbers[1], key="d2")

with col3:
    st.markdown("<h2 style='color: blue; text-align: center;'>8/3 (BLUE)</h2>", unsafe_allow_html=True)
    st.text_input("Digit 3", value=st.session_state.numbers[2], key="d3")

with col4:
    st.markdown("<h2 style='text-align: center;'>Sector 4</h2>", unsafe_allow_html=True)
    st.text_input("Digit 4", value=st.session_state.numbers[3], key="d4")

st.success("SYSTEM STATUS: ONLINE | AUTO-FILL ACTIVE")
