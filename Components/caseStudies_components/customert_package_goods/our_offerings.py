async def our_offerings_style():
    return """
    <style>
        :root {
            --primary-blue: #5FC7FB;
            --primary-white: #FEFEFE;
            --primary-light-gray: #EBF0F3;
            --background-dark: #0A0A0A;
            --card-bg: #1A1A1A;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }


        .offerings-section {
            width: 100vw;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vh 5vw;
        }

        .section-title {
            text-align: center;
            margin-bottom: 8vh;
        }

        .section-title h1 {
            font-size: 4rem;
            line-height: 1.2;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: -0.02em;
            color: var(--primary-light-gray);
        }

        .section-title h1 span {
            color: var(--primary-blue);
        }

        .offerings-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
            width: 90%;
            max-width: 1600px;
        }

        .offering-card {
            background-color: var(--card-bg);
            border-radius: 1.5rem;
            padding: 6vh;;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .offering-card:hover {
            transform: translateY(-1vh);
            box-shadow: 0 1vh 4vh rgba(95, 199, 251, 0.15);
        }

        .card-headers {
            margin-bottom: 4vh;
        }

        .card-titles {
            font-family: 'Exo 2', sans-serif;
            font-weight: 500;
            font-size: 2vw;
            line-height: 1.2;
            color: var(--primary-white);
            width: 70%; /* Give space for the number */
        }
        
        .card-number {
            font-family: 'Urbanist', sans-serif;
            font-weight: 400;
            font-size: 4.5rem;
            line-height: 1;
            color: var(--primary-blue);
            position: absolute;
            top: 2.5rem;
            right: 2.5rem;
        }

        .benefits-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 2vh;
        }

        .benefits-list li {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            font-family: 'Urbanist', sans-serif;
            font-size: 1.1rem;
            line-height: 1.4;
            color: var(--primary-white);
        }

        .check-icon {
            flex-shrink: 0;
            width: 1.5rem;
            height: 1.5rem;
            margin-top: 0.2rem;
        }

        /* --- Mobile View --- */
        @media (max-width: 768px) {
            .offerings-section {
                padding: 10vh 5vw;
                height: auto;
                min-height: auto; /* Override desktop min-height */
            }

            .section-title h1 {
                font-size: 8vw;
                line-height: 1.3;
            }

            .offerings-grid {
                grid-template-columns: 1fr;
                gap: 5vh;
                width: 100%; /* Use full width on mobile */
            }

            .offering-card {
                padding: 8vw 7vw;
                border-radius: 5vw;
            }

            .card-headers {
                margin-bottom: 5vh;
            }

            .card-titles {
                font-size: 6.5vw;
                width: 80%; /* Allow more space for the title on mobile */
                line-height: 1.3;
            }

            .card-number {
                font-size: 12vw;
                top: 7vw;
                right: 7vw;
                line-height: 1;
            }

            .benefits-list {
                gap: 3vh;
            }
            
            .benefits-list li {
                font-size: 4vw;
                gap: 4vw;
                line-height: 1.6;
            }

            .check-icon {
                width: 5vw;
                height: 5vw;
                margin-top: 0.5vw; /* Fine-tune vertical alignment */
            }
        }
    </style>
"""


async def our_offerings_body():
    return """

    <section class="offerings-section">
        <div class="section-title">
            <h1>Our <span>Offerings</span></h1>
        </div>

        <div class="offerings-grid">

            <!-- Card 01 -->
            <div class="offering-card">
                <div class="card-headers">
                    <h2 class="card-titles">Transforming Supply Chains using AI</h2>
                    <span class="card-number">01.</span>
                </div>
                <ul class="benefits-list">
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Enhance end-to-end supply chain efforts to optimize and streamline business operations.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Enhance customer contentment by optimizing service quality, on-time deliveries, and automating issue analysis for preemptive issue resolution.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Boost cost-effectiveness and financial performance by streamlining expenses, investigating alternative procurement possibilities, and minimizing wastage.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Achieve manufacturing brilliance by adopting a smart factory strategy and leveraging comprehensive digital data for enhancing quality and reliability.</li>
                </ul>
            </div>

            <!-- Card 02 -->
            <div class="offering-card">
                <div class="card-headers">
                    <h2 class="card-titles">Demand Optimization</h2>
                    <span class="card-number">02.</span>
                </div>
                <ul class="benefits-list">
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Realize added value through the utilization of revenue growth management (RGM) techniques, including pricing, promotions, and portfolio optimization.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Maximize digital commerce effectiveness through the pursuit of product excellence, supply chain efficiency, and precise demand prediction.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Elevate your business strategy with all-encompassing growth prediction and analytical resources, designed to inform your strategic decisions.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Unleash your innovation potential with all-in-one solutions for research and development digitization.</li>
                </ul>
            </div>

            <!-- Card 03 -->
            <div class="offering-card">
                <div class="card-headers">
                    <h2 class="card-titles">Revenue Optimization</h2>
                    <span class="card-number">03.</span>
                </div>
                <ul class="benefits-list">
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Realize your sales potential through the implementation of an all-encompassing digital business platform and a cohesive contact strategy.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Enhance sales results by employing efficient sales planning, which incorporates SKU optimization, target segmentation, and shelf performance analysis.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Enhance your in-store ambiance with advanced shelf visual analysis, asset/display suggestions, and SRM activation evaluation.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Optimize your sales capabilities by adopting a data-centric strategy employing Customer Genomics® solutions.</li>
                </ul>
            </div>

            <!-- Card 04 -->
            <div class="offering-card">
                <div class="card-headers">
                    <h2 class="card-titles">Monetary Optimization</h2>
                    <span class="card-number">04.</span>
                </div>
                <ul class="benefits-list">
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Enhance financial management and guarantee adequate cash flow by engaging in financial collaboration with instant insights and advanced data analysis.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Leverage cutting-edge technology for forward-looking strategic financial planning, budget formulation, and foresight.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Empower well-informed decision-making using sophisticated analytics, automation, and AI/ML within financial controllership.</li>
                    <li><svg class="check-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 6L9 17L4 12" stroke="#5FC7FB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>Improve financial decision-making by embracing forward-looking treasury and risk management.</li>
                </ul>
            </div>
            
        </div>
    </section>
    """