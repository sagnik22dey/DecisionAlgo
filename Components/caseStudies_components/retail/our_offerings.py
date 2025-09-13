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

        .offerings-section-retail {
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
            gap: 5.5rem;
            width: 65rem;
            height: 43rem;
            max-width: 100%;
        }

        .offering-card {
            background-color: var(--card-bg);
            border-radius: 1rem;
            padding: 2rem;
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

        .card-header {
            margin-bottom: 4vh;
        }

        .card-title-retail {
            font-family: 'Exo 2', sans-serif;
            font-weight: 500;
            font-size: 1.5vw;
            line-height: 1.2;
            color: var(--primary-white);
            width: 70%; /* Give space for the number */
        }
        
        .card-number {
            font-family: 'Urbanist', sans-serif;
            font-weight: 400;
            font-size: 3rem;
            line-height: 1;
            color: var(--primary-blue);
            position: absolute;
            top: 2.5rem;
            right: 2.5rem;
        }

        .card-description {
            font-family: 'Urbanist', sans-serif;
            font-size: 1.5vh;
            line-height: 1.6;
            color: var(--primary-white);
        }

        /* --- Mobile View --- */
        @media (max-width: 768px) {
            .offerings-section {
                padding: 10rem 5rem;
                height: auto;
            }

            .section-title h1 {
                font-size: 8vw;
            }

            .offerings-grid {
                grid-template-columns: 1fr;
                gap: 5vh;
            }

            .offering-card {
                padding: 6vw;
                border-radius: 4vw;
            }

            .card-title-retail {
                font-size: 6vw;
            }

            .card-number {
                font-size: 10vw;
                top: 5vw;
                right: 5vw;
            }
            
            .card-header {
                margin-bottom: 5vh;
            }

            .card-description {
                font-size: 3.8vw;
            }
        }
    </style>
"""


async def our_offerings_body():
    return """
    <section class="offerings-section-retail">
        <div class="section-title">
            <h1 style="font-size: 3vw; line-height: 1.2; font-weight: 700; text-transform: uppercase; letter-spacing: -0.02em; color: var(--primary-light-gray);">NURTURE GROWTH . <span style="color: var(--primary-blue);">DELIVER VALUE</span></h1>
            <p style="font-size: 1.5vw; color: var(--primary-light-gray); margin-top: 2vh;">Lift Your Customer Journey With Versatile And Adaptable AI Innovations To Thrive In Dynamic Surroundings.</p>
        </div>

        <div class="offerings-grid">

            <!-- Card 01 -->
            <div class="offering-card">
                <div class="card-header">
                    <h2 class="card-title-retail">Product Placement Analytics</h2>
                    <span class="card-number">01.</span>
                </div>
                <p class="card-description">Our Al-driven Product Placement Analytics Suite enables retailers to strategically position products in-store, enhancing visibility, and driving customer engagement. Elevate the shopping experience and boost sales by optimizing how products are showcased</p>
            </div>

            <!-- Card 02 -->
            <div class="offering-card">
                <div class="card-header">
                    <h2 class="card-title-retail">Real-time Recommendation</h2>
                    <span class="card-number">02.</span>
                </div>
                <p class="card-description">Offer real-time product recommendations to customers while they browse or make purchases. Your solutions can use Al algorithms to suggest complementary products, enhancing upselling and cross-selling opportunities and improving customer satisfaction</p>
            </div>

            <!-- Card 03 -->
            <div class="offering-card">
                <div class="card-header">
                    <h2 class="card-title-retail">Predictive Maintenance</h2>
                    <span class="card-number">03.</span>
                </div>
                <p class="card-description">Our Al-driven Product Placement Analytics Suite enables retailers to strategically position products in-store, enhancing visibility, and driving customer engagement. Elevate the shopping experience and boost sales by optimizing how products are showcased</p>
            </div>

            <!-- Card 04 -->
            <div class="offering-card">
                <div class="card-header">
                    <h2 class="card-title-retail">Store Layout Optimization</h2>
                    <span class="card-number">04.</span>
                </div>
                <p class="card-description">Our Al-driven Product Placement Analytics Suite enables retailers to strategically position products in-store, enhancing visibility, and driving customer engagement. Elevate the shopping experience and boost sales by optimizing how products are showcased</p>
            </div>
            
        </div>
    </section>
    """
