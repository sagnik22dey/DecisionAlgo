async def unleash_style():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600;700&display=swap');

        /* --- Default: Dark Mode --- */
        .unleash-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vh 5vw;
            width: 100%;
            box-sizing: border-box;
            background-color: transparent;
            transition: background-color 0.3s ease;
            --unleash-route-icon-url: url('../../Resources/Images/HomePage/route.png');
        }

        .unleash-title {
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 3.3vw;
            line-height: 1.2;
            text-align: center;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.3) 0.22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, 0.72) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8vh;
        }

        .unleash-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1.7vw;
            width: 70%;
        }

        .unleash-card {
            box-sizing: border-box;
            width: 19vw;
            height: 33vh;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 0.52vw;
            padding: 2vw 1.3vw;
            display: flex;
            flex-direction: column;
            gap: 1.5vw;
            position: relative;
            background-color: transparent;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }

        .unleash-card-header {
            display: flex;
            align-items: center;
            gap: 1.5vw;
        }

        .unleash-icon-wrapper {
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 3vw;
            height: 3vw;
            min-width: 40px;
            min-height: 40px;
            background: #0A1015;
            border: 1px solid #3A4046;
            border-radius: 0.13vw;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }

        .unleash-icon-wrapper img {
            content: var(--unleash-route-icon-url);
            width: 1.5vw;
            height: auto;
            min-width: 20px;
        }

        .unleash-card-title {
            font-family: 'Exo 2', sans-serif;
            font-weight: 600;
            font-size: 1.3vw;
            line-height: 1.2;
            text-transform: capitalize;
            color: #FFFFFF;
            transition: color 0.3s ease;
        }

        .unleash-card-description {
            font-family: 'Exo 2', sans-serif;
            font-weight: 400;
            font-size: 0.85vw;
            line-height: 1.6;
            text-transform: capitalize;
            color: #FFFFFF;
            opacity: 0.7;
            transition: color 0.3s ease;
        }

        /* --- Light Mode --- */
        @media (prefers-color-scheme: light) {
            .unleash-section {
                background-color: #FFFFFF;
                --unleash-route-icon-url: url('../../Resources/Images/HomePage/route-light.png');
            }

            .unleash-title {
                background: none;
                -webkit-background-clip: unset;
                background-clip: unset;
                -webkit-text-fill-color: unset;
                color: #111111;
            }
            
            .unleash-title .highlight {
                 color: #2196F3;
            }

            .unleash-card {
                background-color: #2196F3;
                border-color: transparent;
            }

            .unleash-card-title,
            .unleash-card-description {
                color: #FFFFFF;
            }

            .unleash-card-description {
                opacity: 0.9;
            }

            .unleash-icon-wrapper {
                background-color: #FFFFFF;
                border-color: transparent;
            }
        }
        
        /* --- Mobile View Modifications --- */
        @media (max-width: 768px) {
            .unleash-section {
                padding: 15vh 5vw;
                margin-top: -25vw;
            }

            .unleash-title {
                font-size: 9vw;
                line-height: 1.3;
                margin-bottom: 10vh;
            }

            .unleash-grid {
                width: 100%;
                flex-direction: column;
                gap: 5vh;
            }

            .unleash-card {
                width: 100%;
                height: auto;
                padding: 6vw;
                border-radius: 4vw;
                gap: 3vh;
            }

            .unleash-card-header {
                gap: 5vw;
            }

            .unleash-icon-wrapper {
                width: 13vw;
                height: 13vw;
                border-radius: 1vw;
            }

            .unleash-icon-wrapper img {
                width: 6.5vw;
            }

            .unleash-card-title {
                font-size: 5.5vw;
            }

            .unleash-card-description {
                font-size: 3.8vw;
            }
        }
    </style>
"""
async def unleash_body():
    return """
    <section class="unleash-section">
        <h1 class="unleash-title">Unleash Innovation . <span class="highlight">Transform Tomorrow</span></h1>

        <div class="unleash-grid">
            
            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2 class="unleash-card-title">AI-Driven<br>Personalization</h2>
                </header>
                <p class="unleash-card-description">
                    Leverage Our AI-Powered Solutions To Create Personalized Shopping Experiences For Your Customers.
                </p>
            </article>

            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2 class="unleash-card-title">Smart Store<br>Transformation</h2>
                </header>
                <p class="unleash-card-description">
                    Collaborate With Us To Transform Your Stores Into "Smart Stores" Using IoT And Sensor Technologies.
                </p>
            </article>
            
            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2 class="unleash-card-title">AI Chatbots For<br>Customer Support</h2>
                </header>
                <p class="unleash-card-description">
                    Integrate AI-Powered Chatbots Into Your Customer Support Systems.
                </p>
            </article>

            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2 class="unleash-card-title">AI Fraud Detection</h2>
                </header>
                <p class="unleash-card-description">
                    Protect Your Business From Fraud With AI-Driven Fraud Detection. Our Solutions Can Recognize Suspicious Transactions And Take Immediate Action
                </p>
            </article>

            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img alt="route icon">
                    </div>
                    <h2 class="unleash-card-title">AI-Powered Inventory<br>Forecasting</h2>
                </header>
                <p class="unleash-card-description">
                    Leverage Our AI-Driven Inventory Forecasting To Ensure You Have The Right Products In Stock When Customers Need Them. This Minimizes Stockouts And Enhances Customer Satisfaction.
                </p>
            </article>

        </div>
    </section>
    """