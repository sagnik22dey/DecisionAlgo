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
            <a href="#" class="get-started-btn">Get Started Now</a>
        </section>
    </div>
"""

async def dashboard_text_cards_style():
    return """
    <style>
        /* --- Desktop First: Base Styles --- */

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
            border-bottom: 0.15vw solid #FFFFFF; /* Replaced px with vw */
            border-radius: 0 0 150vw 150vw;
        }

        .ai-powered-section,
        .see-data-section {
            width: 90vw;
            padding: 6vh 5vw;
            text-align: center;
            border-radius: 2.5vw;
            background: linear-gradient(180deg, #2a2a2a 0%, #1e1e1e 100%);
            box-shadow: inset 0 0.2vw 0.5vw rgba(255, 255, 255, 0.05), 0 1vw 2vw rgba(0, 0, 0, 0.5);
            box-sizing: border-box;
        }

        .headline,
        .see-data-headline {
            font-size: 4.7rem;
            font-weight: 700;
            margin: 0 0 4rem 0;
            line-height: 1.2;
        }

        .headline .smart-text {
            background: linear-gradient(180deg, #E0E0E0 0%, #A0A0A0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }

        .headline .simple-text {
            color: #FFFFFF;
        }

        .headline .ai-text,
        .see-data-headline .never-before {
            color: #82C2EE;
        }
        
        .see-data-headline {
             color: #E0E0E0;
        }

        .description,
        .see-data-description {
            font-size: 1.5rem;
            font-weight: 400;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.85);
            max-width: 65vw;
            margin: 0 auto;
        }
        
        .see-data-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding: 8vh 0; /* Changed margin to padding for better layout control */
            box-sizing: border-box;
        }

        .see-data-background-card {
            position: absolute;
            width: 83vw;
            height: 42vh;
            border-top: 0.15vw solid #FFFFFF; /* Replaced px with vw */
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
            margin-top: 4rem;
            padding: 1.5rem 3rem;
            background-color: #FFFFFF;
            color: #000000;
            font-size: 1.5rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 50vw; /* Fully rounded corners */
            transition: transform 0.3s ease, background-color 0.3s ease;
            cursor: pointer;
        }

        .get-started-btn:hover {
            background-color: #EAEAEA;
            transform: scale(1.05);
        }

        /* --- Tablet View --- */
        @media (max-width: 1024px) {
            .headline,
            .see-data-headline {
                font-size: 7rem;
            }

            .description,
            .see-data-description {
                font-size: 2.5vw;
                max-width: 80vw;
            }

            .get-started-btn {
                font-size: 2.2vw;
                padding: 2vh 4vw;
            }

            .ai-powered-section,
            .see-data-section,
            .see-data-background-card {
                border-radius: 14.5vw;
            }
        }

        /* --- Mobile View (Redesigned for Elegance & Aesthetics) --- */
        @media (max-width: 767px) {
            .smart-simple-container,
            .see-data-container {
                margin-top: 5rem; /* Reduced top margin for better flow */
                padding: 2rem 0;
            }

            .ai-powered-section,
            .see-data-section {
                width: 90vw;
                padding: 4vh 3vw; /* More generous padding */
                border-radius: 5vw;
            }
            
            .decorative-line {
                width: 90vw; /* Match card width */
                height: 5vh;
            }
            
            .see-data-background-card {
                /* Subtly position it behind the main card */
                width: 80vw;
                height: 91vw;
                top: 45%;
                transform: translate(-50%, -50%) scale(1.05);
                border: 0.2vw solid rgba(255, 255, 255, 0.5); /* Make it a full, subtle border */
                background: none;
            }

            .headline,
            .see-data-headline {
                font-size: 10vw; /* Larger, more impactful text */
                margin-bottom: 4vh;
                line-height: 1.25;
            }

            .description,
            .see-data-description {
                font-size: 4.5vw;
                line-height: 1.7; /* Increased for readability */
                max-width: 100%; /* Use full width of the card */
            }

            .get-started-btn {
                font-size: 4.5vw;
                padding: 2.5vh 8vw; /* Larger tap target */
                width: 80%; /* Make button wider */
                max-width: 39.06vw; /* But not excessively so */
                box-sizing: border-box;
            }
        }
    </style>
"""