async def lets_talk_body():
    return """  

    <section class="section-1">
        <!-- Top pill -->
        <a href='#' class="cta">Let’s Talk</a>

        <!-- Tagline -->
        <h2 class="tagline">
            A Modern, High-Tech Business Dashboard Displaying Real-Time Analytics, AI Chatbot, Interactions, And Automated Reports-Clean, Professional, And Futuristic.
        </h2>
    </section>
"""

async def client_feedback_body():
    return """
    <section class="section">
     <!-- Heading -->
        <h1 class="heading">What Our Clients Say</h1>
        <div class="layout">
            <!-- Left portrait panel (Picsum image) -->
            <div class="portrait" aria-label="Client portrait from Picsum"></div>

            <!-- Testimonial card -->
            <div class="card">
                <div class="quote-mark"></div>

                <div class="card-inner">
                    <p class="quote">“DecisionAlgo’s data science expertise greatly benefited MoneyLoji by automating daily reports and developing an impressive real-time dashboard. I highly recommend their services.”</p>
                </div>

                <div class="person">
                    <p class="name">Akshay</p>
                    <p class="role">Ex CEO</p>
                </div>

                <div class="footer-row">
                    <div class="dash"></div>
                    <div class="stars" aria-label="5 star rating">
                        <span class="star" aria-hidden="true">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2.25l2.917 6.083 6.716.977-4.817 4.696 1.137 6.634L12 17.927l-5.953 3.713 1.137-6.634L2.367 9.31l6.716-.977L12 2.25z" />
                            </svg>
                        </span>
                        <span class="star" aria-hidden="true">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2.25l2.917 6.083 6.716.977-4.817 4.696 1.137 6.634L12 17.927l-5.953 3.713 1.137-6.634L2.367 9.31l6.716-.977L12 2.25z" />
                            </svg>
                        </span>
                        <span class="star" aria-hidden="true">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2.25l2.917 6.083 6.716.977-4.817 4.696 1.137 6.634L12 17.927l-5.953 3.713 1.137-6.634L2.367 9.31l6.716-.977L12 2.25z" />
                            </svg>
                        </span>
                        <span class="star" aria-hidden="true">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2.25l2.917 6.083 6.716.977-4.817 4.696 1.137 6.634L12 17.927l-5.953 3.713 1.137-6.634L2.367 9.31l6.716-.977L12 2.25z" />
                            </svg>
                        </span>
                        <span class="star" aria-hidden="true">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 2.25l2.917 6.083 6.716.977-4.817 4.696 1.137 6.634L12 17.927l-5.953 3.713 1.137-6.634L2.367 9.31l6.716-.977L12 2.25z" />
                            </svg>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """

async def client_feedback_style():
    return """
    
    <!-- Google Fonts (closest matches from design) -->
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;700;800&family=Poppins:wght@400;500;700&family=Urbanist:wght@400;700&display=swap" rel="stylesheet" />

    <style>
        /* Default to Light Theme */
        :root {
            /* Light Theme Variables (based on provided light image) */
            --bg: #FFFFFF;
            --body-background: linear-gradient(180deg, rgba(14,165,233,0.04) 0%, rgba(255,255,255,1) 40%), var(--bg);
            --section-background: radial-gradient(80% 80% at 50% -10%, rgba(14,165,233, .06) 0%, rgba(255, 255, 255, 0) 60%), transparent;

            --text: #05223a;
            --muted: rgba(5, 34, 58, .6);
            --gold: #FFC107;
            --stroke: #BDE5F8;
            --shadow: 0 6px 24px rgba(11, 53, 84, .06);

            --cta-bg: #29B6F6;
            --cta-text: #FFFFFF;
            
            --tagline-gradient: var(--text);
            --heading-gradient: var(--text);
            --card-bg: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(241,248,255,1) 50%, rgba(230,245,255,1) 100%);
            
            --quote-mark-image: url("../../Resources/Images/HomePage/comma_light_bg.png");
            --dash-line-image: url("data:image/svg+xml,%3Csvg width='565' height='1' viewBox='0 0 565 1' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cline y1='0.5' x2='565' y2='0.5' stroke='%2305233a' stroke-dasharray='10 10'/%3E%3C/svg%3E");
        }
        
        /* Dark Theme Override */
        @media (prefers-color-scheme: dark) {
            :root {
                /* Dark Theme Variables (based on provided dark image) */
                --bg: black;
                --body-background: var(--bg);
                --section-background: transparent;

                --text: #F9FAFB;
                --muted: rgba(249, 250, 251, .6);
                --gold: #FFC107;
                --stroke: transdparent; /* Removed stroke in dark mode to match design */
                --shadow: 0 6px 24px rgba(0, 0, 0, .25);

                --cta-bg: #FFFFFF;
                --cta-text: #1A1A1A;
                
                --tagline-gradient: var(--text); /* Fallback to solid color */
                --heading-gradient: var(--text); /* Fallback to solid color */
                --card-bg: #262626;

                /* You will need to create a dark version of this image */
                --quote-mark-image: url("../../Resources/Images/HomePage/comma_bg.png"); 
                --dash-line-image: url("data:image/svg+xml,%3Csvg width='565' height='1' viewBox='0 0 565 1' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cline y1='0.5' x2='565' y2='0.5' stroke='%239CA3AF' stroke-dasharray='10 10'/%3E%3C/svg%3E");
            }
        }

        * {
            box-sizing: border-box;
        }

        html, body {
            background: var(--body-background);
            color: var(--text);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .section {
            position: relative;
            min-height: 100vh;
            padding: 2.89vh 1.67vw 3.11vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow: hidden;
            background: var(--section-background);
        }
        .section-1 {
            position: relative;
            min-height: 30vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow: hidden;
            background: var(--section-background);
        }

        /* Top pill button (Let's Talk) */
        .cta {
            position: relative;
            margin: 0vh;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 2.93vh 2.53vw;
            background: var(--cta-bg);
            border-radius: 50vw;
            border: none; /* Removed border to match images */
            color: var(--cta-text);
            font: 500 1.46vw / 1.3 'Poppins', system-ui, sans-serif;
            text-transform: capitalize;
            box-shadow: var(--shadow);
            user-select: none;
            width: 16.33vw;
            height: 5.96vh;
            text-decoration: none;
        }

        /* Tagline text */
        .tagline {
            max-width: 78.89vw;
            text-align: center;
            margin: 11.85vh auto;
            font: 700 2.5vw/1.1 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: var(--tagline-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            color: var(--text); /* Fallback for dark mode */
        }

        /* Section heading text */
        .heading {
            margin-top: 10.37vh;
            text-align: center;
            font: 800 4.44vw/1.2 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: var(--heading-gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            color: var(--text); /* Fallback for dark mode */
        }

        .layout {
            width: min(98.4vw, 100%);
            display: grid;
            grid-template-columns: 22.17vw 1fr;
            gap: 3.89vw;
            align-items: start;
            position: relative;
            scale:0.95;
        }

        /* Left portrait card */
        .portrait {
            margin-top: 10.63vh;
            margin-left: 2.67vw;
            width: 90%;
            height: 51.94vh;
            border-radius: 2.08vw;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow);
            background:
                url("../../Resources/Images/HomePage/ceo.png") center/cover no-repeat;
        }

        /* Right testimonial panel */
        .card {
            position: relative;
            height: 68.5vh;
            border-radius: 3.47vw;
            background: var(--card-bg);
            border: 0.5vh solid var(--stroke);
            box-shadow: var(--shadow);
        }
        
        /* Huge quote-mark watermark */
        .quote-mark {
            position: absolute;
            top: -4.63vh;
            right: 2.08vw;
            width: 24.44vw;
            height: 22.68vh;
            background: var(--quote-mark-image) no-repeat;
            background-size: contain;
            opacity: 0.9;
            z-index: 1;
        }

        /* Inner content */
        .card-inner {
            position: absolute;
            inset: 5.56vh 4.17vw auto 4.17vw;
            z-index: 1;
            display: flex;
            flex-direction: column;
            gap: 1.85vh;
        }

        .quote {
            font: 500 2.5vw/1.5 'Exo 2', sans-serif;
            letter-spacing: -0.01em;
            color: var(--text);
        }

        /* Name + title */
        .person {
            position: absolute;
            left: 4.17vw;
            bottom: 5.56vh;
            display: flex;
            flex-direction: column;
        }

        .person .name {
            font: 700 2.85vw/1.4 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            margin: 0;
            color: var(--text);
        }

        .person .role {
            font: 400 2.29vw/1.4 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            color: var(--muted);
            margin: 0;
        }

        /* Divider + stars row */
        .footer-row {
            position: absolute;
            left: 4.17vw;
            right: 4.17vw;
            bottom: 3.33vh;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 1.67vw;
        }

        .dash {
            flex: 1 1 auto;
            opacity: 1;
            background: var(--dash-line-image);
            height: 0.09vh;
            margin-bottom: 0.12vh;
            z-index: 10;
        }

        .stars {
            display: inline-flex;
            gap: 0.28vw;
            height: 2.22vh;
        }

        .star {
            width: 1.67vw;
            height: 2.22vh;
            display: inline-block;
        }

        .star svg {
            display: block;
            width: 100%;
            height: 100%;
            fill: var(--gold);
        }

        /******************************************/
        /*           MOBILE STYLES                */
        /******************************************/
        @media (max-width: 768px) {
            .section {
                padding: 4rem 1rem 3rem;
                min-height: auto;
            }

            .cta {
                font-size: 0.9rem;
                padding: 0.5rem 1.25rem;
                width: auto;
                height: auto;
                margin: 0 0 2rem 0;
            }

            .tagline {
                font-size: 1.1rem;
                line-height: 1.5;
                max-width: 100%;
                margin: 0 auto 6rem;
            }

            .heading {
                font-size: 2.25rem;
                line-height: 1.2;
                margin: 0 auto 2.5rem;
            }

            .layout {
                display: flex;
                flex-direction: column;
                gap: 2rem;
                width: 100%;
            }
            
            /* Testimonial card comes SECOND on mobile */
            .card {
                order: 2;
                height: auto;
                border-radius: 24px;
                padding: 2rem 1.5rem 8rem 1.5rem;
            }
            
            /* Portrait image comes FIRST */
            .portrait {
                order: 1;
                margin: auto;
                width: 80%;
                height: 350px;
                border-radius: 24px;
            }

            /* --- Styles inside the card --- */

            .quote-mark {
                top: -10px;
                right: 15px;
                width: 120px;
                height: 100px;
                opacity: 0.9;
            }
            
            .card-inner {
                position: relative;
                inset: auto;
            }

            .quote {
                font-size: 1.25rem;
                line-height: 1.6;
            }

            .person {
                left: 1.5rem;
                bottom: 4.5rem;
            }

            .person .name {
                font-size: 1.5rem;
            }

            .person .role {
                font-size: 1rem;
                color: var(--muted);
            }

            .footer-row {
                left: 1.5rem;
                right: 1.5rem;
                bottom: 2rem;
            }
            
            .stars {
                height: 20px;
            }
            
            .star {
                width: 20px;
                height: 20px;
            }
        }
    </style>
    """