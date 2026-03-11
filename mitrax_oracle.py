# --- 2. THE CALIBRATED BANNER ---
if os.path.exists("mitrax_banner.jpg"):
    st.image("mitrax_banner.jpg", width=220)
else:
    st.markdown("<h2 style='color: #00FF00;'>MITRAX ORACLE</h2>", unsafe_allow_html=True)

# --- 3. THE STABILIZED WINNING BOARD ---
st.markdown("<div class='mini-board-gold'>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
islands = [("ARUBA", "1862"), ("BONAIRE", "2544"), ("CURAÇAO", "7716"), ("ST. MARTIN", "3076")]
for i, (name, num) in enumerate(islands):
    with [c1, c2, c3, c4][i]:
        st.markdown(f"<p class='island-text'>{name}</p><p class='num-text'>{num}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. THE SYMMETRY DECK ---
st.markdown("<center><div class='bridge-final'>SYMMETRY MATRIX SENSORS</div></center>", unsafe_allow_html=True)

def draw_grid_final(val, is_dark=False, target=None):
    bg_color = "#707070" if is_dark else "#D3D3D3"
    for r in range(4):
        cols = st.columns(4)
        for c in range(4):
            is_m = (r == 0 and c == 0 and val)
            circle = "red-target-final" if is_m and target=="red" else "blue-target-final" if is_m and target=="blue" else ""
            txt = val if is_m else "0"
            html = f"<div class='matrix-cell-final' style='background-color:{bg_color}'>"
            if circle: html += f"<div class='{circle}'>{txt}</div>"
            else: html += f"{txt}"
            html += "</div>"
            cols[c].markdown(html, unsafe_allow_html=True)

cols = st.columns([4, 2, 4, 1, 4, 2, 4])

with cols[0]:
    st.markdown("<p class='island-label-final'>GRID 1</p>", unsafe_allow_html=True)
    draw_grid_final(st.session_state.get('v_final_red', ""), target="red")

with cols[1]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_final_red", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-final'></div>", unsafe_allow_html=True)

with cols[2]:
    st.markdown("<p class='island-label-final'>GRID 2</p>", unsafe_allow_html=True)
    draw_grid_final(st.session_state.get('v_final_blue', ""), target="blue")

with cols[4]:
    st.markdown("<p class='island-label-final'>GRID 3</p>", unsafe_allow_html=True)
    draw_grid_final("", is_dark=True)

with cols[5]:
    st.write("<div style='height:15px;'></div>", unsafe_allow_html=True)
    st.text_input("", placeholder="****", max_chars=4, key="v_final_blue", label_visibility="collapsed")
    st.markdown("<div class='gold-pillar-final'></div>", unsafe_allow_html=True)

with cols[6]:
    st.markdown("<p class='island-label-final'>GRID 4</p>", unsafe_allow_html=True)
    draw_grid_final("", is_dark=True)
