async def top_business_style():
    return """
    <style>
        /* --- Default: Dark Mode --- */
        :root {
            --primary-blue: #00A9FF;
            --primary-white: #FFFFFF;
            --primary-light-gray: #EBF0F3;
            --text-secondary: rgba(255, 255, 255, 0.7);
            --background-dark: #0A0A0A;
            --card-bg: #111111;
            --card-border: rgba(255, 255, 255, 0.3);
            --icon-bg: #0A1015;
            --icon-border: #3A4046;
            --top-business-route-icon-url: url('../../Resources/Images/HomePage/route.png');
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .data-science-section {
            width: 100vw;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vh 5vw;
            font-family: 'Exo 2', sans-serif;
            background-color: var(--background-dark);
            color: var(--primary-white);
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .section-heading {
            text-align: center;
            margin-bottom: 8vh;
        }

        .section-heading h1 {
            font-size: 3.5vw;
            line-height: 1.2;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: -0.02em;
            color: var(--primary-light-gray);
            transition: color 0.3s ease;
        }

        .section-heading h1 span {
            color: var(--primary-blue);
            transition: color 0.3s ease;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2vw;
            width: 90%;
            max-width: 1400px;
        }

        .benefit-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 1vw;
            padding: 2vw;
            display: flex;
            flex-direction: column;
            gap: 3vw;
            transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }

        .benefit-card:hover {
            transform: translateY(-1vh);
            border-color: var(--primary-blue);
            box-shadow: 0 1vh 3vh rgba(0, 169, 255, 0.2);
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 1.5vw;
        }

        .icon-wrapper {
            flex-shrink: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 4vw;
            height: 4vw;
            background-color: var(--icon-bg);
            border: 1px solid var(--icon-border);
            border-radius: 0.5vw;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }

        .icon-wrapper img {
            content: var(--top-business-route-icon-url);
            width: 2vw;
            height: auto;
        }

        .card-header h2 {
            font-size: 1.3vw;
            font-weight: 600;
            line-height: 1.1;
            transition: color 0.3s ease;
        }

        .card-description {
            font-size: 1vw;
            font-weight: 400;
            line-height: 1.6;
            color: var(--text-secondary);
            transition: color 0.3s ease;
        }
        
        /* --- Light Mode --- */
        @media (prefers-color-scheme: light) {
            .data-science-section {
                background-color: #FFFFFF;
                color: #111111;
            }

            .section-heading h1 {
                color: #111111;
            }

            .section-heading h1 span {
                color: #2196F3;
            }

            .benefit-card {
                background-color: #2196F3;
                border-color: transparent;
                color: #FFFFFF;
            }

            .benefit-card:hover {
                box-shadow: 0 1vh 3vh rgba(33, 150, 243, 0.3);
            }
            
            .card-header h2 {
                color: #FFFFFF;
            }

            .card-description {
                color: #FFFFFF;
                opacity: 0.9;
            }
            
            .icon-wrapper {
                background-color: #FFFFFF;
                border-color: transparent;
                --top-business-route-icon-url: url('../../Resources/Images/HomePage/route-light.png');
            }
        }

        /* --- Mobile View --- */
        @media (max-width: 768px) {
            .data-science-section {
                padding: 5vh 5vw;
                height: auto;
                min-height: auto;
            }

            .section-heading h1 {
                font-size: 5vw;
                line-height: 1.3;
            }

            .cards-grid {
                grid-template-columns: 1fr;
                width: 100%;
                gap: 4vh;
            }

            .benefit-card {
                padding: 7vw;
                border-radius: 4vw;
                gap: 4vh;
            }

            .card-header {
                gap: 5vw;
            }

            .icon-wrapper {
                width: 13vw;
                height: 13vw;
                border-radius: 2.5vw;
            }
            
            .icon-wrapper img {
                width: 6.5vw;
                height: auto;
            }

            .card-header h2 {
                font-size: 5.5vw;
                line-height: 1.2;
            }

            .card-description {
                font-size: 4vw;
                line-height: 1.6;
            }
        }
    </style>
"""

async def top_business_body():
    return """

    <section class="data-science-section">
        <div class="section-heading">
            <h1>
                Top Businesses From Diverse<br>
                <span>Consumer Goods Sectors</span> Benefit<br>
                From Data Science.
            </h1>
        </div>

        <div class="cards-grid">
            <!-- Card 1: Quality Control -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>Quality Control</h2>
                </div>
                <p class="card-description">
                    AI and Data Analytics can monitor product quality during production, helping to identify defects early in the process and reduce waste.
                </p>
            </div>

            <!-- Card 2: Demand Forecasting -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>Demand Forecasting</h2>
                </div>
                <p class="card-description">
                    Analyzing data allows for precise demand forecasts using historical sales data and market trends. AI enhances this accuracy by adapting to changing consumer behavior.
                </p>
            </div>

            <!-- Card 3: Sustainability & CSR -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>Sustainability & CSR</h2>
                </div>
                <p class="card-description">
                    Data can track the environmental impact of products and packaging. CPG companies can use AI to develop more sustainable products and reduce their carbon footprint.
                </p>
            </div>

            <!-- Card 4: Risk Management -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>Risk Management</h2>
                </div>
                <p class="card-description">
                    Data Science can assess risks associated with supply chain, compliance, and other factors, allowing CPG companies to proactively mitigate potential issues.
                </p>
            </div>

            <!-- Card 5: Supply Chain View -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>Supply Chain View</h2>
                </div>
                <p class="card-description">
                    Data Analytics and AI can provide end-to-end visibility in the supply chain, enabling better tracking of products, reducing waste, and ensuring timely deliveries.
                </p>
            </div>

            <!-- Card 6: AI-Powered Chatbots -->
            <div class="benefit-card">
                <div class="card-header">
                    <div class="icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2>AI-Powered Chatbots</h2>
                </div>
                <p class="card-description">
                    CPG companies can use AI chatbots for customer support, providing quick responses to queries and enhancing the customer experience.
                </p>
            </div>
        </div>
    </section>
"""