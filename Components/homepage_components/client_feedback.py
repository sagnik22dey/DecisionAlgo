
async def client_feedback_body():
    return """
    <section class="section">
        <!-- Top pill -->
        <div class="cta">Let’s Talk</div>

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
            --shadow: 0 10px 30px rgba(0, 0, 0, .35);
        }

        * {
            box-sizing: border-box
        }

        html,
        body {
            height: 100%
        }

        .section {
            position: relative;
            min-height: 100vh;
            padding: 96px 24px 120px;
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
            margin: -2rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 10px 22px;
            background: var(--chip-bg);
            border: 1.3px solid var(--stroke);
            border-radius: 999px;
            color: #000;
            font: 400 21px/1.3 'Poppins', system-ui, sans-serif;
            text-transform: capitalize;
            box-shadow: var(--shadow);
            user-select: none;
            width: 12rem;
            height: 2rem;
        }

        /* Tagline gradient */
        .tagline {
            max-width: 1136px;
            text-align: center;
            margin: 8rem;
            font: 700 36px/1.1 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, .54) 7.5%, #EBF1F3 24.5%, #EBF0F3 67.4%, rgba(235, 239, 243, .54) 94.46%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Section heading gradient */
        .heading {
            margin-top: 7rem;
            text-align: center;
            font: 800 64px/1.2 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, .30) .22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, .72) 79.36%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .layout {
            width: min(1417px, 100%);
            display: grid;
            grid-template-columns: 420px 1fr;
            gap: 56px;
            align-items: start;
            position: relative;
        }

        /* Left portrait card */
        .portrait {
            margin-top: 50px;
            width: 100%;
            height: 453px;
            border-radius: 30px;
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
            height: 513px;
            border-radius: 50px;
            background: linear-gradient(to bottom, transparent 0%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.2) 100%), #1111;
        }

        /* Decorative ellipses top-right (subtle, per comp) */
        
        /* Huge quote-mark watermark */
        .quote-mark {
            position: absolute;
            top: -50px;
            right: 30px;
            width: 352px;
            height: 245px;
            background: url("../../Resources/Images/comma_bg.png") no-repeat;
            background-size: contain;
            opacity: 1;
            z-index: 1;
        }

        /* Inner content */
        .card-inner {
            position: absolute;
            inset: 60px 60px auto 60px;
            z-index: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .quote {
            font: 500 36px/1.5 'Exo 2', sans-serif;
            letter-spacing: -0.01em;
            color: #fff;
        }

        /* Name + title */
        .person {
            position: absolute;
            left: 60px;
            bottom: 60px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .person .name {
            font: 700 41px/1.4 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            margin: 0;
        }

        .person .role {
            font: 400 33px/1.4 'Exo 2', sans-serif;
            letter-spacing: -0.02em;
            color: var(--muted);
            margin: 0;
        }

        /* Divider + stars row */
        .footer-row {
            position: absolute;
            left: 60px;
            right: 60px;
            bottom: 36px;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 24px;
        }

        .dash {
            flex: 1 1 auto;
            opacity: 1;
            background: url("data:image/svg+xml,%3Csvg width='565' height='1' viewBox='0 0 565 1' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cline y1='0.5' x2='565' y2='0.5' stroke='white' stroke-dasharray='10 10'/%3E%3C/svg%3E");
            height: 1px;
            z-index: 10;
         
        }

        .stars {
            display: inline-flex;
            gap: 4px;
            height: 24px;
        }

        .star {
            width: 24px;
            height: 24px;
            display: inline-block;
        }

        .star svg {
            display: block;
            width: 100%;
            height: 100%;
            fill: var(--gold)
        }

        /* Responsiveness */
        @media (max-width:1100px) {
            .layout {
                grid-template-columns: 1fr
            }

            .portrait {
                order: 2;
                height: 380px
            }

            .card {
                order: 1;
                height: auto;
                min-height: 520px
            }

            .card-inner {
                inset: 32px
            }

            .person {
                left: 32px;
                bottom: 96px
            }

            .footer-row {
                left: 32px;
                right: 32px;
                bottom: 28px
            }

            .heading {
                font-size: 48px
            }

            .tagline {
                font-size: 28px
            }
        }
    </style>
    """