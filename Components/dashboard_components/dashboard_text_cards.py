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

        .smart-simple-container {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 8vw;
        }

        .decorative-line {
             width: 82vw;
            /* max-width: 1500px; */
            height: 3.5vh;
            border-bottom: 1.5px solid rgba(255, 255, 255, 255);
            border-radius: 0 0 150vw 150vw;
        }

        /* --- AI Section Container --- */
        .ai-powered-section {
            width: 90vw;
            /* max-width: 1400px; */
            padding: 6vh 5vw;
            text-align: center;
            border-radius: 2.5vw;
            background: linear-gradient(180deg, #2a2a2a 0%, #1e1e1e 100%);
            box-shadow: inset 0 0.2vw 0.5vw rgba(255, 255, 255, 0.05), 0 1vw 2vw rgba(0, 0, 0, 0.5);

            /* Gradient background to mimic the lighting in the image */
            background: linear-gradient(180deg, #2a2a2a 0%, #1e1e1e 100%);

            /* Subtle shadows for depth and a top-edge highlight */
            box-shadow:
                inset 0 0.2vw 0.5vw rgba(255, 255, 255, 0.05),
                /* Inner top highlight */
                0 1vw 2vw rgba(0, 0, 0, 0.5);
            /* Outer shadow for depth */
        }

        /* --- Headline Styles --- */
        .headline {
            font-size: 4.7vw;
            /* Responsive font size */
            font-weight: 700;
            margin-top:0vh;
            margin-bottom: 4vh;
            line-height: 1.2;
        }

        /* Gradient style for "Smart." */
        .headline .smart-text {
            background: linear-gradient(180deg, #E0E0E0 0%, #A0A0A0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }

        /* Plain white style for "Simple." */
        .headline .simple-text {
            color: #FFFFFF;
        }

        /* Blue style for "AI-Powered." */
        .headline .ai-text {
            color: #82C2EE;
        }

        /* --- Paragraph Styles --- */
        .description {
            font-size: 1.5vw;
            /* Responsive font size */
            font-weight: 400;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.85);
            max-width: 65vw;
            /* Controls line length for readability */
            margin: 0 auto;
            /* Center the paragraph block */
        }
        
        .get-started-btn {
            display: inline-block;
            margin-top: 4vh;
            padding: 1.5vh 3vw;
            background-color: #FFFFFF;
            color: #000000;
            font-size: 1.5vw;
            font-weight: 600;
            text-decoration: none;
            border-radius: 50px;
            transition: background-color 0.3s ease;
            cursor: pointer;
        }

        .get-started-btn:hover {
            background-color: #EAEAEA;
        }

        .see-data-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin-top: 8vw;
            margin-bottom: 8vw;
        }

        .see-data-background-card {
            position: absolute;
            width: 83vw;
            height: 42vh;
            border-top: 1.5px solid rgba(255, 255, 255, 255);
            border-radius: 2.5vw;
            top: 9vw;
            left: 50%;
            transform: translate(-50%, -54%);
            z-index: 1;
        }

        .see-data-section {
            position: relative;
            z-index: 2;
            width: 90vw;
            padding: 6vh 5vw;
            text-align: center;
            border-radius: 2.5vw;
            background: linear-gradient(180deg, #2a2a2a 0%, #1e1e1e 100%);
            box-shadow: inset 0 0.2vw 0.5vw rgba(255, 255, 255, 0.05), 0 1vw 2vw rgba(0, 0, 0, 0.5);
        }

        .see-data-headline {
            font-size: 4.7vw;
            font-weight: 700;
            margin-top: 0vh;
            margin-bottom: 4vh;
            line-height: 1.2;
            color: #E0E0E0;
        }

        .see-data-headline .never-before {
            color: #82C2EE;
        }

        .see-data-description {
            font-size: 1.5vw;
            font-weight: 400;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.85);
            max-width: 65vw;
            margin: 0 auto 4vh auto;
        }

        /* --- Responsive Adjustments --- */
 
        /* Tablet View */
        @media (max-width: 1024px) {
            .headline, .see-data-headline {
                font-size: 7vw;
            }
 
            .description, .see-data-description {
                font-size: 2.5vw;
                max-width: 75vw;
            }

            .get-started-btn {
                font-size: 2.2vw;
                padding: 2vh 4vw;
            }

            .ai-powered-section {
                border-radius: 3.5vw;
            }
        }

        /* Mobile View */
        @media (max-width: 640px) {

            .ai-powered-section {
                width: 90vw;
                padding: 8vh 6vw;
                border-radius: 5vw;
            }

            .headline, .see-data-headline {
                font-size: 9.5vw;
                margin-bottom: 5vh;
            }
 
            .description, .see-data-description {
                font-size: 4.2vw;
                max-width: 100%;
                /* Allow full width on mobile */
            }

            .get-started-btn {
                font-size: 3.8vw;
                padding: 2vh 6vw;
            }
        }
    </style>
"""