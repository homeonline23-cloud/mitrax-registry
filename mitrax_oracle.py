<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MITRIX ORACLE PIC 4</title>
    <style>
        /* The "Oracle" Aesthetic */
        body {
            background-color: #000000; /* Pure Black Background */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        .oracle-header {
            text-align: center;
            padding: 40px;
        }

        .oracle-title {
            /* FONT SIZE LARGE */
            font-size: 120px; 
            font-family: 'Arial Black', Gadget, sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 15px;
            margin: 0;

            /* COLOR GOLD */
            color: #FFD700; 

            /* BLACK NEON LINES (The "Outline" effect) */
            /* We use multiple black shadows to create a thick "line" around the gold */
            text-shadow: 
                -4px -4px 0 #000,  
                 4px -4px 0 #000,
                -4px  4px 0 #000,
                 4px  4px 0 #000,
                 0 0 20px rgba(255, 215, 0, 0.6), /* Inner Glow */
                 0 0 40px rgba(255, 215, 0, 0.4); /* Outer Glow */
        }

        /* Optional: Add a subtle pulse to the gold */
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        .oracle-title {
            animation: pulse 3s infinite ease-in-out;
        }
    </style>
</head>
<body>

    <div class="oracle-header">
        <h1 class="oracle-title">MITRIX ORACLE PIC 4</h1>
    </div>

</body>
</html>
