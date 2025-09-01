async def client_feedback_body():
    return """
    <section class="section">
        <!-- Top pill -->
        <a href='#' class="cta">Let’s Talk</a>

        <!-- Tagline -->
        <h2 class="tagline">
            A Modern, High-Tech Business Dashboard Displaying Real-Time Analytics, AI Chatbot, Interactions, And Automated Reports-Clean, Professional, And Futuristic.
        </h2>

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
        :root {
            --bg: #0b0b0b;
            --panel: #1111;
            --panel-2: #121212;
            --panel-3: #292828;
            --text: #ffffff;
            --muted: rgba(255, 255, 255, .6);
            --gold: #FFBB00;
            --stroke: #DFDFDF;
            --chip-bg: #FFFFFF;
            --shadow: 0 0.93vh 1.56vw rgba(0, 0, 0, .35); /* Original: 0 10px 30px */
        }

        * {
            box-sizing: border-box
        }

        .section {
            position: relative;
            min-height: 100vh;
            padding: 8.89vh 1.67vw 11.11vh; /* Original: 96px 24px 120px */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow: hidden;
            background: radial-gradient(80% 80% at 50% -10%, rgba(255, 255, 25, .06) 0%, rgba(255, 255, 255, 0) 60%), #00;
        }

        /* Top pill button (Let's Talk) */
        .cta {
            position: relative;
            margin: 0vh;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 1.93vh 1.53vw; /* Original: 10px 22px */
            background: var(--chip-bg);
            border: 0.09vw solid var(--stroke); /* Original: 1.3px */
            border-radius: 50vw; /* Original: 999px */
            color: #000;
            font: 400 1.46vw/1.3 'Poppins', system-ui, sans-serif; /* Original: 21px */
            text-transform: capitalize;
            box-shadow: var(--shadow);
            user-select: none;
            width: 13.33vw; /* Original: 12rem */
            height: 2.96vh; /* Original: 2rem */
        }

        /* Tagline gradient */
        .tagline {
            max-width: 78.89vw; /* Original: 1136px */
            text-align: center;
            margin: 11.85vh auto; /* Original: 8rem */
            font: 700 2.5vw/1.1 'Exo 2', sans-serif; /* Original: 36px */
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, .54) 7.5%, #EBF1F3 24.5%, #EBF0F3 67.4%, rgba(235, 239, 243, .54) 94.46%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Section heading gradient */
        .heading {
            margin-top: 10.37vh; /* Original: 7rem */
            text-align: center;
            font: 800 4.44vw/1.2 'Exo 2', sans-serif; /* Original: 64px */
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, .30) .22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, .72) 79.36%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .layout {
            width: min(98.4vw, 100%); /* Original: 1417px */
            display: grid;
            grid-template-columns: 22.17vw 1fr; /* Original: 420px */
            gap: 3.89vw; /* Original: 56px */
            align-items: start;
            position: relative;
            scale:0.95;
        }

        /* Left portrait card */
        .portrait {
            margin-top: 10.63vh; /* Original: 50px */
            margin-left: 2.67vw;
            width: 90%;
            height: 51.94vh; /* Original: 453px */
            border-radius: 2.08vw; /* Original: 30px */
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow);
            background:
                linear-gradient(0deg, rgba(255, 255, 255, .2), rgba(255, 255, 255, .2)),
                url("../../Resources/Images/ceo.png") center/cover no-repeat;
        }

        /* Right testimonial panel */
        .card {
            position: relative;
            height: 68.5vh; /* Original: 513px */
            border-radius: 3.47vw; /* Original: 50px */
            background: linear-gradient(to bottom, transparent 0%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.2) 100%), #1111;
        }
        
        /* Huge quote-mark watermark */
        .quote-mark {
            position: absolute;
            top: -4.63vh; /* Original: -50px */
            right: 2.08vw; /* Original: 30px */
            width: 24.44vw; /* Original: 352px */
            height: 22.68vh; /* Original: 245px */
            background: url("../../Resources/Images/comma_bg.png") no-repeat;
            background-size: contain;
            opacity: 1;
            z-index: 1;
        }

        /* Inner content */
        .card-inner {
            position: absolute;
            inset: 5.56vh 4.17vw auto 4.17vw; /* Original: 60px */
            z-index: 1;
            display: flex;
            flex-direction: column;
            gap: 1.85vh; /* Original: 20px */
        }

        .quote {
            font: 500 2.5vw/1.5 'Exo 2', sans-serif; /* Original: 36px */
            letter-spacing: -0.01em;
            color: #fff;
        }

        /* Name + title */
        .person {
            position: absolute;
            left: 4.17vw; /* Original: 60px */
            bottom: 5.56vh; /* Original: 60px */
            display: flex;
            flex-direction: column;
        }

        .person .name {
            font: 700 2.85vw/1.4 'Exo 2', sans-serif; /* Original: 41px */
            letter-spacing: -0.02em;
            margin: 0;
        }

        .person .role {
            font: 400 2.29vw/1.4 'Exo 2', sans-serif; /* Original: 33px */
            letter-spacing: -0.02em;
            color: var(--muted);
            margin: 0;
        }

        /* Divider + stars row */
        .footer-row {
            position: absolute;
            left: 4.17vw; /* Original: 60px */
            right: 4.17vw; /* Original: 60px */
            bottom: 3.33vh; /* Original: 36px */
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 1.67vw; /* Original: 24px */
        }

        .dash {
            flex: 1 1 auto;
            opacity: 1;
            background: url("data:image/svg+xml,%3Csvg width='565' height='1' viewBox='0 0 565 1' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cline y1='0.5' x2='565' y2='0.5' stroke='white' stroke-dasharray='10 10'/%3E%3C/svg%3E");
            height: 0.09vh; /* Original: 1px */
            margin-bottom: 0.12vh;
            z-index: 10;
        }

        .stars {
            display: inline-flex;
            gap: 0.28vw; /* Original: 4px */
            height: 2.22vh; /* Original: 24px */
        }

        .star {
            width: 1.67vw; /* Original: 24px */
            height: 2.22vh; /* Original: 24px */
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
                margin: 0 auto 2rem;
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
                order: 2; /* CHANGED */
                height: auto; /* Allow height to fit the content */
                border-radius: 24px;
                /* Add bottom padding to make space for absolutely positioned elements */
                padding: 2rem 1.5rem 8rem 1.5rem;
            }
            
            /* Portrait image comes FIRST */
            .portrait {
                order: 1; /* CHANGED */
                margin: 0;
                width: 100%;
                height: 350px;
                border-radius: 24px;
            }

            /* --- Styles inside the card --- */

            .quote-mark {
                top: -10px;
                right: 15px;
                width: 120px;
                height: 100px;
                opacity: 0.8;
            }
            
            .card-inner {
                position: relative; /* Change from absolute to flow normally */
                inset: auto;
            }

            .quote {
                font-size: 1.25rem;
                line-height: 1.6;
            }

            .person {
                left: 1.5rem;
                bottom: 4.5rem; /* Position above the footer row */
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
                bottom: 2rem; /* Position it firmly at the bottom */
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