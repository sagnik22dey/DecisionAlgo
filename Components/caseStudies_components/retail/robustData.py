async def robustData_style():
    return """
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        .robust-data-section {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .robust-container {
            position: relative;
            width: 90vw;
            max-width: 1200px;
            padding: 6vh 6vw;
            border-radius: 2.8vh;
            background: linear-gradient(284.15deg, rgba(26, 26, 26, 0) 1.73%, rgba(45, 45, 45, 0.28) 33.62%, rgba(89, 89, 89, 0.36) 71.97%, rgba(128, 128, 128, 0.01) 97.84%), #101010;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 5vh;
            overflow: hidden;
        }
        .robust-ext-container {
            display: flex;
            border-bottom: 0.15vh solid white;
            border-right: 0.15vh solid white;
            border-radius: 2.8vh;
            top: 10vh;
            left: 10vh;
        }

        .robust-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 2.8vh;
            border: 1.5px solid transparent;
            background: linear-gradient(45deg, rgba(255,255,255,0.3), rgba(255,255,255,0.1), rgba(255,255,255,0.3)) border-box;
            -webkit-mask:
                linear-gradient(#fff 0 0) content-box,
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: destination-out;
            mask-composite: exclude;
        }
        
        .robust-container::after {
            content: '';
            position: absolute;
            bottom: -1.5vh;
            left: 20%;
            width: 60%;
            height: 1vh;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            filter: blur(1.5vh);
            opacity: 0.4;
            z-index: 1;
        }

        .robust-data-title {
            width: 70vw;
            max-width: 800px;
            font-weight: 600;
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            line-height: 1.2;
            text-align: center;
            letter-spacing: -0.02em;
            background: linear-gradient(90deg, #FFFFFF 0%, #E0E0E0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            margin-bottom: 2vh;
        }

        .cards-container {
            display: flex;
            justify-content: center;
            gap: 3vw;
            width: 100%;
        }

        .card {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 2.5vh 1.5vw;
            gap: 2vh;
            width: clamp(200px, 18vw, 250px);
            height: 28vh;
            background: rgba(30, 30, 30, 0.7);
            border-radius: 1.5vh;
            border: 1px solid rgba(95, 199, 251, 0.3);
            backdrop-filter: blur(8px);
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2), inset 0 0 5px rgba(95, 199, 251, 0.1);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(95, 199, 251, 0.3), inset 0 0 8px rgba(95, 199, 251, 0.2);
            border-color: rgba(95, 199, 251, 0.6);
        }

        .icon-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1vh;
            width: 5vh;
            height: 5vh;
            border: 1px solid #5FC7FB;
            border-radius: 0.8vh;
            background: rgba(95, 199, 251, 0.1);
        }

        .icon {
            width: 3vh;
            height: 3vh;
        }
        
        .icon svg {
            width: 100%;
            height: 100%;
        }

        .card-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 1vh;
            width: 100%;
        }

        .card-title {
            font-weight: 500;
            font-size: 2vh;
            line-height: 2.4vh;
            color: #FEFEFE;
        }

        .card-description {
            font-weight: 300;
            font-size: 1.4vh;
            line-height: 1.8vh;
            color: #FEFEFE;
            opacity: 0.8;
        }

        /* Responsive adjustments */
        @media (max-width: 1200px) {
            .cards-container {
                gap: 2vw;
            }
            .card {
                width: clamp(180px, 20vw, 220px);
            }
        }

        @media (max-width: 992px) {
            .robust-container {
                padding: 5vh 4vw;
            }
            .cards-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 4vh 4vw;
            }
            .card {
                width: auto;
                height: auto;
                min-height: 180px;
            }
            .title {
                font-size: clamp(2rem, 4vw, 2.5rem);
            }
        }

        @media (max-width: 768px) {
            .robust-container {
                width: 95vw;
                padding: 4vh 5vw;
            }
            .robust-data-title {
                font-size: clamp(1.8rem, 5vw, 2.2rem);
            }
            .cards-container {
                grid-template-columns: 1fr;
                gap: 3vh;
            }
            .card {
                padding: 3vh 4vw;
            }
        }
    </style>
"""


async def robustData_body():
    return """
<section class="robust-data-section">
<div class="robust-ext-container" style="margin-bottom: 10vh;">
    <div class="robust-container">
        <div class="robust-data-title">
            With Robust Data Infrastructure And A Unified Point Of Reference
        </div>
        
        <div class="cards-container" id="cardsContainer">
            <div class="card">
                <div class="icon-container">
                    <div class="icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 12H15" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M9 15H15" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M16.5 21H7.5C6.4 21 5.5 20.1 5.5 19V5C5.5 3.9 6.4 3 7.5 3H13.89C14.39 3 14.87 3.2 15.22 3.55L18.45 6.78C18.8 7.13 19 7.61 19 8.11V19C19 20.1 18.1 21 17 21H16.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
                <div class="card-content">
                    <div class="card-title">Information Frameworks</div>
                    <div class="card-description">Integrate Data Resources</div>
                </div>
            </div>
            
            <div class="card">
                <div class="icon-container">
                    <div class="icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M14 9.5C14 10.88 12.88 12 11.5 12C10.12 12 9 10.88 9 9.5C9 8.12 10.12 7 11.5 7C12.88 7 14 8.12 14 9.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M18 14.5C18 15.88 16.88 17 15.5 17C14.12 17 13 15.88 13 14.5C13 13.12 14.12 12 15.5 12C16.88 12 18 13.12 18 14.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M11.5 12C12.88 12 14 13.12 14 14.5C14 15.88 12.88 17 11.5 17C10.12 17 9 15.88 9 14.5C9 13.12 10.12 12 11.5 12Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M6 9.5C6 10.88 4.88 12 3.5 12C2.12 12 1 10.88 1 9.5C1 8.12 2.12 7 3.5 7C4.88 7 6 8.12 6 9.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
                <div class="card-content">
                    <div class="card-title">Corporate Operations</div>
                    <div class="card-description">Automate Monitoring</div>
                </div>
            </div>
            
            <div class="card">
                <div class="icon-container">
                    <div class="icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 16.17L4.83 12L3.41 13.41L9 19L21 7L19.59 5.59L9 16.17Z" fill="#5FC7FB"/>
                        </svg>
                    </div>
                </div>
                <div class="card-content">
                    <div class="card-title">Selection Frameworks</div>
                    <div class="card-description">Ignite Smart Perspectives.</div>
                </div>
            </div>
            
            <div class="card">
                <div class="icon-container">
                    <div class="icon">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M16.5 10.5C16.5 13.81 13.81 16.5 10.5 16.5C7.19 16.5 4.5 13.81 4.5 10.5C4.5 7.19 7.19 4.5 10.5 4.5C13.81 4.5 16.5 7.19 16.5 10.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M19.5 13.5C19.5 16.81 16.81 19.5 13.5 19.5C10.19 19.5 7.5 16.81 7.5 13.5C7.5 10.19 10.19 7.5 13.5 7.5C16.81 7.5 19.5 10.19 19.5 13.5Z" stroke="#5FC7FB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
                <div class="card-content">
                    <div class="card-title">Information Control</div>
                    <div class="card-description">Securely Democratize Data</div>
                </div>
            </div>
        </div>
    </div>
</div>
</section>

"""
