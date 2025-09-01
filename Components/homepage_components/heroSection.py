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
            <h1>Is your Business drowning in Data but, Starving for Insights?</h1>
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
        /* The main container for the hero section to provide a positioning context */
        .hero-section-container {
            margin-top: 6.48vh; /* Original: 7rem */
            position: relative; 
            width: 100%;
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            padding-top: 22.22vh; /* Original: 15rem */
            padding-bottom: 29.63vh; /* Original: 20rem */
            box-sizing: border-box; 
        }

        /* Rectangle 29: Base background color layer */
        .bg-dark {
            position: absolute;
            width: 100%; 
            height: 100%; 
            left: 0;
            top: 0;
            background: #111111;
            border-radius: 3.38vw; /* Original: 65px */
        }

        /* Ellipse 4335: Top white glow effect */
        .hero-section-container::before {
            content: '';
            position: absolute;
            width: 18.23vw; /* Original: 350px */
            height: 18.23vw; /* Using vw for height to maintain aspect ratio */
            left: 50%;
            top: -9.26vh; /* Original: -100px */
            background: #FFFFFF;
            opacity: 0.2;
            filter: blur(10.42vw); /* Original: 200px */
            transform: translateX(-50%); 
            z-index: 1;
        }

        /* Rectangle 41: Gradient overlay with rounded corners */
        .gradient-overlay {
            position: absolute;
            width: 100%; 
            height: 100%; 
            left: 0;
            top: 0;
            background: linear-gradient(177.33deg, rgba(15, 15, 15, 0) 5.46%, rgba(0, 0, 0, 0.6006) 53.07%, rgba(0, 0, 0, 0.77) 93.86%);
            border-radius: 3.38vw; /* Original: 65px */
            border-bottom: solid 0.09vh; /* Original: 1px */
            border-color:#f0f0f0;
        }

        /* Rectangle 14: The grid pattern container with border */
        .grid-container {
            box-sizing: border-box;
            position: absolute;
            width: 100%; 
            height: 100%;
            left: 0;
            top: 0;
            background-image: url('../../Resources/Images/grid1.png');
            border-radius: 3.38vw; /* Original: 65px */
        }

        /* Ellipse 2: Bottom white glow effect */
        .glow-bottom {
            position: absolute;
            width: 41.67vw; /* Original: 800px */
            height: 41.67vw; /* Using vw for height to maintain aspect ratio */
            left: 50%;
            bottom: -37.04vh; /* Original: -400px */
            background: #FFFFFF;
            opacity: 0.25;
            filter: blur(13.02vw); /* Original: 250px */
            transform: translateX(-50%);
            border-radius: 50%;
        }

        .hero-content-container{
            margin-right: 31.25vw; /* Original: 600px */
        }
        
        /* Frame 2147225626: Container for all text content */
        .hero-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0;
            gap: 3.05vh; /* Original: 33px */
            position: relative; 
            max-width: 50.57vw; /* Original: 971px */
            width: 100%; 
            z-index: 10; 
        }
        

        /* Main Headline: "Is your Business..." */
        .hero-content h1 {
            font-family: 'Exo 2', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 3.75vw; /* Original: 72px */
            line-height: 4.48vw; /* Original: 86px */
            letter-spacing: -0.04em;
            color: #FFFFFF;
            text-shadow: 0 0.37vh 0.21vw rgba(0, 0, 0, 0.25); /* Original: 0px 4px 4px */
            flex: none;
            order: 0;
            align-self: stretch;
            flex-grow: 0;
            margin: 0; 
        }

        /* Paragraph: "Transform frustration..." */
        .hero-content p {
            font-family: 'Poppins', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 1.25vw; /* Original: 24px */
            line-height: 150%;
            color: #FFFFFF;
            flex: none;
            order: 1;
            align-self: stretch;
            flex-grow: 0;
            margin: 0; 
        }

        /* Frame 5: The call-to-action button */
        .cta-button {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 0.78vh 2.19vw;
            gap: 0.88vw;
            width: 12.05vw;
            height: 6.26vh;
            background: #FFFFFF;
            box-shadow: 0 0.62vh 0.35vw rgba(0, 0, 0, 0.25);
            border-radius: 5.21vw;
            flex: none;
            order: 2;
            flex-grow: 0;
            text-decoration: none;
            box-sizing: border-box;
        }

        /* Text inside the button: "Discover How" */
        .cta-button span {
            width: 6.82vw; /* Original: 131px */
            height: 3.24vh; /* Original: 35px */
            font-family: 'Jost', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 1.25vw; /* Original: 24px */
            line-height: 1.82vw; /* Original: 35px */
            display: flex;
            align-items: center;
            letter-spacing: -0.04em;
            color: #111111;
            flex: none;
            order: 0;
            flex-grow: 0;
        }

        /******************************************/
        /*           MOBILE STYLES                */
        /******************************************/
        @media (max-width: 768px) {
            .hero-section-container {
                margin-top: 3rem;
                padding: 6rem 1rem 7rem; /* Reduced padding for mobile */
            }

            .bg-dark, .gradient-overlay, .grid-container {
                border-radius: 30px; /* A fixed radius looks better on mobile */
            }

            .hero-section-container::before {
                width: 70vw; /* Make glow wider relative to screen */
                height: 70vw;
                top: -5rem;
                filter: blur(100px);
            }
            
            .glow-bottom {
                width: 100vw; /* Make glow wider */
                height: 100vw;
                bottom: -150px;
                opacity: 0.15;
                filter: blur(100px);
            }

            .hero-content-container {
                margin-right: 0; /* Remove right margin to center content */
                width: 100%;
                display: flex;
                justify-content: center;
            }

            .hero-content {
                align-items: center; /* Center-align all items */
                text-align: center;
                gap: 1.75rem; /* Adjusted gap for mobile */
                max-width: 95%; /* Allow content to use more width */
            }

            .hero-content h1 {
                font-size: 2.5rem; /* Readable font size for mobile headlines */
                line-height: 1.2;
                letter-spacing: -0.02em;
            }
            
            .hero-content p {
                font-size: 1rem; /* Readable font size for body text */
                line-height: 1.6;
                max-width: 500px; /* Prevent lines from getting too long */
            }

            .cta-button {
                width: auto; /* Let the button size itself based on content */
                height: auto;
                padding: 0.8rem 2.5rem;
                border-radius: 50px; /* A simpler radius */
            }

            .cta-button span {
                width: auto; /* Reset fixed width */
                height: auto; /* Reset fixed height */
                font-size: 1.1rem; /* Slightly larger, more tappable text */
                line-height: 1.5;
            }
        }
    </style>
    """