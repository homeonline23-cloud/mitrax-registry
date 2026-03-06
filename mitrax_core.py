# --- THE PILLAR HIGHLIGHTING (7/1 RED & 8/3 BLUE) ---
def apply_imperial_colors(row):
    # 4 SPACES OR 1 TAB BELOW THE 'DEF' LINE:
    if row["Soldier"] == "7/1":
        return ['background-color: #FF0000; color: white; font-weight: bold'] * 5
    if row["Soldier"] == "8/3":
        return ['background-color: #0000FF; color: white; font-weight: bold'] * 5
    return ['background-color: orange; color: black'] * 5

# Render the 14-Soldier Army with Imperial Highlighting
st.table(df.style.apply(apply_imperial_colors, axis=1))
