async def heroSection_body():
    return """
    <div class="hero-section-container">
        <!-- Background and Decorative Elements -->
        <div class="bg-dark"></div>
        <div class="grid-container"></div>
        <div class="gradient-overlay"></div>
        <div class="glow-bottom"></div>
        
        <!-- Foreground Content (Text and Button) -->
        <div class ="hero-content-container">
        <div class="hero-content">
            <h1>Is your Business drowning in Data but, <span class="highlight">Starving for </br> Insights?</span></h1>
            <p>Transform frustration into fortune with AI solutions that eliminate data headaches, accelerate decision-making, and drive measurable ROI.</p>
            <a href="#" class="cta-button">
                <span>Discover How</span>
            </a>
        </div>
        </div>
    </div>
"""

async def heroSection_style():
    return """    
    <style>
        /* --- THEME VARIABLES --- */
        :root {
            /* Light Theme (Default) */
            --hero-bg: #FFFFFF;
            --hero-grid-image: linear-gradient(to right, rgba(206, 222, 245, 0.7) 2px, transparent 2px), linear-gradient(to bottom, rgba(206, 222, 245, 0.7) 2px, transparent 2px);
            --hero-grid-bg-size: 3.5vw 3.5vw;
            --hero-text-primary: #111111;
            --hero-text-highlight: #2563EB; /* Blue highlight for light mode */
            --hero-button-bg: linear-gradient(105deg, #3B82F6 0%, #2563EB 100%);
            --hero-button-text: #FFFFFF;
            --hero-button-shadow: 0px 10px 20px -5px rgba(37, 99, 235, 0.4);
            --dark-mode-element-opacity: 0; /* Hides dark mode glows and overlays */
        }

        @media (prefers-color-scheme: dark) {
            :root {
                /* Dark Theme Overrides */
                --hero-bg: #111111;
                --hero-grid-image: url('../../Resources/Images/HomePage/grid1.png');
                --hero-grid-bg-size: auto;
                --hero-text-primary: #FFFFFF;
                --hero-text-highlight: var(--hero-text-primary); /* Highlight is white in dark mode */
                --hero-button-bg: #FFFFFF;
                --hero-button-text: #111111;
                --hero-button-shadow: 0 0.62vh 0.35vw rgba(0, 0, 0, 0.25);
                --dark-mode-element-opacity: 1; /* Shows dark mode glows and overlays */
            }
        }

        /* The main container for the hero section, using your exact original values */
        .hero-section-container {
            margin-top: 6.48vh;
            position: relative; 
            width: 100%;
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            padding-top: 22.22vh;
            padding-bottom: 29.63vh;
            box-sizing: border-box; 
            overflow: hidden;
        }

        /* Base background color layer */
        .bg-dark {
            position: absolute;
            width: 100%; height: 100%; 
            left: 0; top: 0;
            background: var(--hero-bg); /* Themed background */
            border-radius: 3.38vw;
        }

        /* Top white glow effect for DARK MODE ONLY */
        .hero-section-container::before {
            content: '';
            position: absolute;
            width: 18.23vw; height: 18.23vw;
            left: 50%; top: -9.26vh;
            background: #FFFFFF;
            opacity: var(--dark-mode-element-opacity); /* Controlled by theme */
            filter: blur(10.42vw);
            transform: translateX(-50%); 
            z-index: 1;
            transition: opacity 0.3s ease;
        }

        /* Gradient overlay for DARK MODE ONLY */
        .gradient-overlay {
            position: absolute;
            width: 100%; height: 100%; 
            left: 0; top: 0;
            background: linear-gradient(177.33deg, rgba(15, 15, 15, 0) 5.46%, rgba(0, 0, 0, 0.6006) 53.07%, rgba(0, 0, 0, 0.77) 93.86%);
            border-radius: 3.38vw;
            border-bottom: solid 0.09vh;
            border-color:#f0f0f0;
            opacity: var(--dark-mode-element-opacity); /* Controlled by theme */
            transition: opacity 0.3s ease;
        }

        /* The grid pattern container */
        .grid-container {
            box-sizing: border-box;
            position: absolute;
            width: 100%; height: 100%;
            left: 0; top: 0;
            background-image: var(--hero-grid-image); /* Themed grid */
            background-size: var(--hero-grid-bg-size); /* Themed grid size */
            border-radius: 3.38vw;
        }

        /* Bottom white glow effect for DARK MODE ONLY */
        .glow-bottom {
            position: absolute;
            width: 41.67vw; height: 41.67vw;
            left: 50%; bottom: -37.04vh;
            background: #FFFFFF;
            opacity: calc(0.25 * var(--dark-mode-element-opacity)); /* Controlled by theme */
            filter: blur(13.02vw);
            transform: translateX(-50%);
            border-radius: 50%;
            transition: opacity 0.3s ease;
        }

        .hero-content-container{
            margin-right: 31.25vw; /* Original value */
        }
        
        /* Container for all text content, using your exact original values */
        .hero-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0;
            gap: 3.05vh; /* Original value */
            position: relative; 
            max-width: 50.57vw; /* YOUR ORIGINAL VALUE - THIS CONTROLS TEXT WRAP */
            width: 100%; 
            z-index: 10; 
        }
        
        /* Main Headline, using your exact original values */
        .hero-content h1 {
            font-family: 'Exo 2', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 3.75vw;
            line-height: 4.48vw;
            letter-spacing: -0.04em;
            color: var(--hero-text-primary); /* Themed color */
            text-shadow: 0 0.37vh 0.21vw rgba(0, 0, 0, 0.25);
            flex: none; order: 0; align-self: stretch; flex-grow: 0;
            margin: 0; 
        }
        
        .hero-content h1 .highlight {
            color: var(--hero-text-highlight); /* Themed highlight color */
        }

        /* Paragraph, using your exact original values */
        .hero-content p {
            font-family: 'Poppins', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 1.25vw;
            line-height: 150%;
            color: var(--hero-text-primary); /* Themed color */
            flex: none; order: 1; align-self: stretch; flex-grow: 0;
            margin: 0; 
        }

        /* CTA Button, using your exact original values for layout */
        .cta-button {
            display: flex; flex-direction: row; justify-content: center; align-items: center;
            padding: 0.78vh 2.19vw;
            gap: 0.88vw;
            width: 12.05vw;
            height: 6.26vh;
            background: var(--hero-button-bg); /* Themed background */
            box-shadow: var(--hero-button-shadow); /* Themed shadow */
            border-radius: 5.21vw;
            flex: none; order: 2; flex-grow: 0;
            text-decoration: none;
            box-sizing: border-box;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .cta-button:hover {
            transform: translateY(-3px);
        }

        /* Button text, using your exact original values */
        .cta-button span {
            width: 6.82vw; height: 3.24vh;
            font-family: 'Jost', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 1.25vw;
            line-height: 1.82vw;
            display: flex;
            align-items: center;
            letter-spacing: -0.04em;
            color: var(--hero-button-text); /* Themed color */
            flex: none; order: 0; flex-grow: 0;
        }

        /******************************************/
        /*           MOBILE STYLES (Unchanged)    */
        /******************************************/
        @media (max-width: 768px) {
            .hero-section-container {
                margin-top: 3rem;
                padding: 6rem 1rem 7rem;
            }
            .bg-dark, .gradient-overlay, .grid-container {
                border-radius: 30px;
            }
            .hero-section-container::before {
                width: 70vw; height: 70vw;
                top: -5rem;
                filter: blur(100px);
            }
            .glow-bottom {
                width: 100vw; height: 100vw;
                bottom: -150px;
                opacity: calc(0.15 * var(--dark-mode-element-opacity));
                filter: blur(100px);
            }
            .hero-content-container {
                margin-right: 0;
                width: 100%;
                display: flex;
                justify-content: center;
            }
            .hero-content {
                align-items: center;
                text-align: center;
                gap: 1.75rem;
                max-width: 95%;
            }
            .hero-content h1 {
                font-size: 2.5rem;
                line-height: 1.2;
                letter-spacing: -0.02em;
            }
            .hero-content p {
                font-size: 1rem;
                line-height: 1.6;
                max-width: 500px;
            }
            .cta-button {
                width: auto;
                height: auto;
                padding: 0.8rem 2.5rem;
                border-radius: 50px;
            }
            .cta-button span {
                width: auto;
                height: auto;
                font-size: 1.1rem;
                line-height: 1.5;
            }
        }
    </style>
    """