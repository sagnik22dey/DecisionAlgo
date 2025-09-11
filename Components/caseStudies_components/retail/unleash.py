
async def unleash_style():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600;700&display=swap');

        .unleash-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vh 5vw;
            width: 100%;
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
            width: 70vw;
        }

        .unleash-card {
            box-sizing: border-box;
            width: 21.3vw;
            height: 27.8vh;
            border: 0.052vw solid rgba(255, 255, 255, 0.3);
            border-radius: 0.52vw;
            padding: 3.2vh 1.3vw;
            display: flex;
            flex-direction: column;
            gap: 2.5vh;
            position: relative;
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
            width: 2.75vw;
            height: 4.9vh;
            background: #0A1015;
            border: 0.052vw solid #3A4046;
            border-radius: 0.13vw;
        }

        .unleash-icon {
            width: 1.65vw;
            height: 2.9vh;
            background: #FFFFFF;
        }

        .unleash-card-title {
            font-family: 'Exo 2', sans-serif;
            font-weight: 600;
            font-size: 1.3vw;
            line-height: 1.2;
            text-transform: capitalize;
            color: #FFFFFF;
        }

        .unleash-card-description {
            font-family: 'Exo 2', sans-serif;
            font-weight: 400;
            font-size: 0.85vw;
            line-height: 1.6;
            text-transform: capitalize;
            color: #FFFFFF;
            opacity: 0.7;
        }
    </style>
"""

async def unleash_body():
    return """
    <section class="unleash-section">
        <h1 class="unleash-title">Unleash Innovation . Transform Tomorrow</h1>

        <div class="unleash-grid">
            
            <article class="unleash-card">
                <header class="unleash-card-header">
                    <div class="unleash-icon-wrapper">
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
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
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
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
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
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
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
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
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
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