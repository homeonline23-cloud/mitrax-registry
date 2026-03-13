import streamlit as st

# Force the page to use the full width of the browser
st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* Reset margins and set black background */
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }

    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 20px 0;
        background: #000;
        border-bottom: 2px solid #333;
    }

    .oracle-text {
        /* This 'clamp' makes it not too big, not too small */
        font-size: clamp(2rem, 5vw, 4rem); 
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        color: #FFD700; /* GOLD */
        text-transform: uppercase;
        letter-spacing: 5px;
        white-space: nowrap; /* Forces it to stay on one horizontal line */
        
        /* BLACK NEON LINES (Outline) */
        text-shadow: 
            -2px -2px 0 #000,  
             2px -2px 0 #000,
            -2px  2px 0 #000,
             2px  2px 0 #000,
             0 0 15px rgba(255, 215, 0, 0.5);
    }
    </style>
    
    <div class="header-container">
        <h1 class="oracle-text">MITRIX ORACLE PIC 4</h1>
    </div>
    """, unsafe_allow_html=True)
