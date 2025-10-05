async def smart_simple_body():
    return """
    <div class="smart-simple-container">
        <section class="ai-powered-section">
            <h1 class="headline">
                <span class="smart-text">Smart.</span>
                <span class="simple-text">Simple.</span>
                <span class="ai-text">AI-Powered.</span>
            </h1>
            <p class="description">
                Is your dashboard just for viewing data? No, it helps you act on it.</br>
                Our AI-driven insights highlight trends, predict patterns, and make decision-making effortless.
            </p>
        </section>
        <div class="decorative-line"></div>
    </div>
"""

async def see_data_body():
    return """
    <div class="see-data-container">
        <div class="see-data-background-card"></div>
        <section class="see-data-section">
            <h1 class="see-data-headline">
                See Your Data Like <span class="never-before">Never Before</span>
            </h1>
            <p class="see-data-description">
                Make faster, smarter decisions with a dashboard that works for you.
            </p>
            <a href="/contactus" class="get-started-btn">Get Started Now</a>
        </section>
    </div>
"""

async def dashboard_text_cards_style():
    return """
    <style>
        /* --- Base & Desktop Styles (Theme-Agnostic) --- */
        /* This section contains all layout, positioning, and sizing rules. */

        .smart-simple-container {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 8vh;
        }

        .decorative-line {
            width: 82vw;
            height: 3.5vh;
            border-bottom-style: solid;
            border-bottom-width: 0.15vw;
            border-radius: 0 0 150vw 150vw;
        }

        .ai-powered-section,
        .see-data-section {
            width: 90vw;
            padding: 6vh 5vw;
            text-align: center;
            border-radius: 2.5vw;
            box-sizing: border-box;
        }

        .headline,
        .see-data-headline {
            font-size: 4.7vw;
            font-weight: 700;
            margin: 0 0 4vh 0;
            line-height: 1.2;
        }

        .headline .smart-text {
            -webkit-background-clip: text;
            background-clip: text;
        }

        .description,
        .see-data-description {
            font-size: 1.5vw;
            font-weight: 400;
            line-height: 1.6;
            max-width: 65vw;
            margin: 0 auto;
        }
        
        .see-data-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding: 8vh 0;
            box-sizing: border-box;
        }

        .see-data-background-card {
            position: absolute;
            width: 83vw;
            height: 42vh;
            border-top-style: solid;
            border-top-width: 0.15vw;
            border-radius: 2.5vw;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -54%);
            z-index: 1;
        }

        .see-data-section {
            position: relative;
            z-index: 2;
        }

        .get-started-btn {
            display: inline-block;
            margin-top: 4vh;
            padding: 1.5vh 3vw;
            font-size: 1.5vw;
            font-weight: 600;
            text-decoration: none;
            border-radius: 50vw;
            transition: transform 0.3s ease, background-color 0.3s ease;
            cursor: pointer;
        }

        .get-started-btn:hover {
            transform: scale(1.05);
        }

        /* --- Theming Section --- */
        /* Contains all color and background rules for light and dark modes. */

        /* Light Theme */
        @media (prefers-color-scheme: light) {
            .decorative-line, .see-data-background-card {
                display: none; /* Hide decorative elements in light mode */
            }
            .ai-powered-section, .see-data-section {
                background-color: #2596F4;
                box-shadow: 0 0.8vw 2.5vw rgba(37, 150, 244, 0.3);
            }
            .headline, .see-data-headline, .description, .see-data-description {
                color: #FFFFFF;
            }
            .headline .smart-text, .headline .simple-text, .headline .ai-text, .see-data-headline .never-before {
                background: none; /* Remove gradient effect */
                -webkit-text-fill-color: initial; /* Reset text fill */
                color: #FFFFFF;
            }
            .description, .see-data-description {
                opacity: 0.9;
            }
            .get-started-btn {
                background-color: #FFFFFF;
                color: #4A5568;
            }
            .get-started-btn:hover {
                background-color: #F0F0F0;
            }
        }

        /* Dark Theme */
        @media (prefers-color-scheme: dark) {
            .decorative-line {
                border-bottom-color: #FFFFFF;
                display: block;
            }
             .see-data-background-card {
                border-top-color: #FFFFFF;
                display: block;
            }
            .ai-powered-section, .see-data-section {
                background: #2a2a2a;
                box-shadow: inset 0 0.2vw 0.5vw rgba(255, 255, 255, 0.05), 0 1vw 2vw rgba(0, 0, 0, 0.5);
            }
            .headline .smart-text {
                color: #FFFFFF;
            }
            .headline .simple-text {
                color: #FFFFFF;
            }
            .headline .ai-text, .see-data-headline .never-before {
                color: #82C2EE;
            }
            .see-data-headline {
                color: #E0E0E0;
            }
            .description, .see-data-description {
                color: rgba(255, 255, 255, 0.7);
            }
            .get-started-btn {
                background-color: #FFFFFF;
                color: #000000;
            }
            .get-started-btn:hover {
                background-color: #EAEAEA;
            }
        }


        /* --- Tablet View (Structural) --- */
        @media (max-width: 1024px) {
            .headline, .see-data-headline { font-size: 7vw; }
            .description, .see-data-description { font-size: 2.5vw; max-width: 80vw; }
            .get-started-btn { font-size: 2.2vw; padding: 2vh 4vw; }
            .ai-powered-section, .see-data-section, .see-data-background-card { border-radius: 6.5vw; }
        }

        /* --- Mobile View (Structural & Theming) --- */
        @media (max-width: 767px) {
            .smart-simple-container, .see-data-container { margin-top: 5vh; padding: 2vh 0; }
            .ai-powered-section, .see-data-section { width: 90vw; padding: 4vh 3vw; border-radius: 5vw; }
            .decorative-line { width: 80vw; height: 3vh; }
            .see-data-background-card {
                width: 80vw; height: 91vw; top: 45%;
                transform: translate(-50%, -50%) scale(1.05);
                background: none;
                /* Mobile border is handled in theme query below */
                border-top: none;
                border: 0.2vw solid;
            }
            .headline, .see-data-headline { font-size: 10vw; margin-bottom: 4vh; line-height: 1.25; }
            .description, .see-data-description { font-size: 4.5vw; line-height: 1.7; max-width: 100%; }
            .get-started-btn {
                font-size: 4.5vw; padding: 2.5vh 8vw; width: 80%;
                max-width: 300px; box-sizing: border-box;
            }

            /* Mobile-specific theming */
            @media (prefers-color-scheme: dark) {
                .see-data-background-card {
                    border-color: rgba(255, 255, 255, 0.5);
                }
            }
        }
    </style>
"""