async def ready_body():
    return """     
    <main class="viewport-container">
        <!-- Background Elements -->
        <div class="ellipse ellipse-1"></div>
        <div class="ellipse ellipse-2"></div>

        <!-- Left Side: Text -->
        <div class="text-container">
            <div class="text-content">
                <h1 class="main-heading">Ready to Make Data Work for You?</h1>
                <p class="sub-heading">Say goodbye to guesswork.</p>
                <p class="description">Let’s turn your business into a data-driven powerhouse!</p>
            </div>
        </div>

        <!-- Right Side: Images -->
        <div class="image-container">
            <div class="image-box image-box-short">
                <img src="../../Resources/Images/HomePage/Tripple_1.png" alt="Futuristic data dashboard">
            </div>
            <div class="image-box image-box-long">
                 <img src="../../Resources/Images/HomePage/Tripple_2.png" alt="Robotic hand interacting with a digital interface">
            </div>
            <div class="image-box image-box-short">
                 <img src="../../Resources/Images/HomePage/Tripple_3.png" alt="Woman in a modern, futuristic setting">
            </div>
        </div>

        <!-- Buttons (Moved here to be a sibling for layout control) -->
        <div class="buttons-container">
            <a href="#" class="button primary-button">Get a Free Consultation</a>
            <a href="#" class="button secondary-button">Try Our Solutions</a>
        </div>
    </main>
"""
async def ready_style():
    return """ 
    <!-- Google Fonts Import -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&family=Outfit:wght@600&display=swap" rel="stylesheet">
    
    <style>
        /* ============================================================= */
        /* THEME VARIABLES                                               */
        /* ============================================================= */
        :root {
            /* Light Theme (Default) */
            --section-bg: #FFFFFF;
            --ellipse-opacity: 0;
            --text-primary: #111827;
            --text-secondary: #4B5563;
            --btn-primary-bg: #2563EB;
            --btn-primary-text: #FFFFFF;
            --btn-secondary-text: #2563EB;
            --btn-secondary-border: #2563EB;
            --image-border-color: #E5E7EB;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                /* Dark Theme Overrides */
                --section-bg: #141414;
                --ellipse-opacity: 1;
                --text-primary: #FFFFFF;
                --text-secondary: #FFFFFF;
                --btn-primary-bg: #FFFFFF;
                --btn-primary-text: #000000;
                --btn-secondary-text: #FFFFFF;
                --btn-secondary-border: #FFFFFF;
                --image-border-color: #616161;
            }
        }

        /* ============================================================= */
        /* ORIGINAL LAYOUT (UNCHANGED SIZES & SPACING)                   */
        /* ============================================================= */
        .viewport-container {
            position: relative;
            width: 100vw;
            min-height: 100vh;
            display: grid;
            grid-template-columns: 46vw auto;
            grid-template-areas:
                "text   images"
                "buttons images";
            align-items: center;
            justify-content: center;
            gap: 5.18vh 5vw;
            padding: 5vh 5vw;
            overflow: hidden;
            box-sizing: border-box;
            background-color: var(--section-bg); /* Themed */
        }

        /* Ellipses: Your layout, themed opacity */
        .ellipse {
            position: absolute;
            filter: blur(10.42vw);
            z-index: -1;
            opacity: var(--ellipse-opacity); /* Themed */
            transition: opacity 0.3s ease;
        }
        .ellipse-1 {
            width: 10.53vw; height: 30.46vh; left: 5vw; top: 20vh;          
            background: rgba(255, 255, 255, 0.48);
        }
        .ellipse-2 {
            width: 10.53vw; height: 30.46vh; right: 5vw; top: 15vh;
            background: rgba(255, 255, 255, 0.49);
            transform: matrix(0.45, 0.89, 0.89, -0.45, 0, 0);
        }

        /* Text: Your layout, themed colors */
        .text-container {
            grid-area: text; display: flex; flex-direction: column;
            align-items: flex-start; align-self: end;
        }
        .text-content {
            display: flex; flex-direction: column;
            align-items: flex-start; gap: 2.03vh; width: 100%;
        }
        .main-heading {
            width: 100%; font-family: 'Exo 2', sans-serif; font-weight: 700;
            font-size: 3.33vw; line-height: 1.2; margin: 0;
            color: var(--text-primary); /* Themed */
        }
        .sub-heading {
            width: 100%; font-family: 'Exo 2', sans-serif; font-weight: 700;
            font-size: 1.9vw; line-height: 1.2; margin: 0;
            color: var(--text-primary); /* Themed */
        }
        .description {
            width: 100%; font-family: 'Exo 2', sans-serif; font-weight: 400;
            font-size: 1.52vw; line-height: 1.5; margin: 0;
            color: var(--text-secondary); /* Themed */
        }

        /* Buttons: Your layout, themed colors */
        .buttons-container {
            grid-area: buttons; display: flex; flex-direction: row;
            align-items: center; gap: 1.14vw; flex-wrap: wrap; align-self: start;
        }
        .button {
            display: flex; justify-content: center; align-items: center;
            text-decoration: none; font-family: 'Outfit', sans-serif;
            font-weight: 600; font-size: 1.15vw; height: 6.02vh;
            box-sizing: border-box; border-radius: 9.52vw;
            white-space: nowrap; padding-left: 2.28vw; padding-right: 2.28vw;
            transition: transform 0.2s ease, opacity 0.2s ease;
        }
        .button:hover { transform: scale(1.03); opacity: 0.9; }
        .primary-button {
            background: var(--btn-primary-bg);
            color: var(--btn-primary-text);
        }
        .secondary-button {
            border: 0.1vw solid var(--btn-secondary-border);
            color: var(--btn-secondary-text);
            background: transparent;
        }

        /* Images: Your layout, themed border */
        .image-container {
            grid-area: images; display: flex; flex-direction: column;
            align-items: flex-start; gap: 1.36vh; width: 16.32vw;
            filter: drop-shadow(0 0.37vh 0.21vw rgba(0, 0, 0, 0.25));
        }
        .image-box {
            box-sizing: border-box; width: 100%;
            border: 0.1vw solid var(--image-border-color); /* Themed */
            border-radius: 1.64vw; overflow: hidden;
        }
        .image-box-short { height: 13.59vh; }
        .image-box-long { height: 26.4vh; }
        .image-container img {
            width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%);
        }

        /******************************************/
        /*           MOBILE STYLES                */
        /******************************************/
        @media (max-width: 768px) {
            .viewport-container {
                display: flex; flex-direction: column;
                padding: 4rem 1.5rem; justify-content: flex-start;
                gap: 3rem; min-height: auto;
            }
            .ellipse-1 { width: 60vw; height: 60vw; top: 5vh; left: -20vw; filter: blur(100px); }
            .ellipse-2 { width: 60vw; height: 60vw; top: 50vh; right: -20vw; filter: blur(100px); transform: none; }
            .text-container { width: 100%; align-items: center; text-align: center; }
            .text-content { align-items: center; gap: 1rem; }
            .main-heading { font-size: 2.5rem; line-height: 1.2; }
            .sub-heading { font-size: 1.25rem; line-height: 1.3; }
            .description { font-size: 1rem; line-height: 1.6; }
            .buttons-container { flex-direction: column; width: 100%; max-width: 400px; gap: 1rem; margin : auto; }
            .button { width: 100%; font-size: 1rem; height: auto; padding: 0.9rem 1.5rem; border-radius: 50px; }
            .secondary-button { border-width: 2px; }
            .image-container { flex-direction: row; width: 100%; gap: 0.75rem; justify-content: center; }
            .image-box { border-radius: 16px; border-width: 2px; }
            .image-box-short { width: 30%; height: 150px; }
            .image-box-long { width: 40%; height: 200px; transform: translateY(-25px); }
        }
    </style>
    """