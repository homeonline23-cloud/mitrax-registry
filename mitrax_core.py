import datetime

# --- THE DYNAMIC DATE PROTOCOL ---
today_val = datetime.datetime.now().day
tomorrow_val = today_val + 1

def apply_imperial_colors(row):
    # THE RED COMMANDER (TODAY)
    # Automatically finds the row matching today's date (e.g., 7/1)
    if row["Soldier"].startswith(f"{today_val}/"):
        return ['background-color: #FF0000; color: white; font-weight: bold; text-align: left;'] * 5
    
    # THE BLUE GENERAL (TOMORROW)
    # Automatically finds the row matching tomorrow's date (e.g., 8/3)
    if row["Soldier"].startswith(f"{tomorrow_val}/"):
        return ['background-color: #0000FF; color: white; font-weight: bold; text-align: right;'] * 5
    
    # THE ORANGE HORIZON
    return ['background-color: orange; color: black; text-align: center;'] * 5
