async def text_top_robot_section():
    return """
        <section>
            <div class="heading-container">
                <h1>
                    AI AND DATA SCIENCE IN <span>TECHNOLOGY,<br> MEDIA & TELECOM</span>
                </h1>
            </div>
        </section>
    """
    

async def style_top_robot_section():
    return """
        <style>
            /* --- Default: Dark Mode --- */
            :root {
                --primary-blue: #5FC7FB;
                --primary-white: #FEFEFE;
                --primary-gray: #CCCCCC;
                --background-dark: #111111;
                --card-bg: rgba(20, 20, 20, 0.4);
                --card-border: rgba(95, 199, 251, 0.5);
            }
            
            .heading-section-wrapper {
                background-color: var(--background-dark);
            }

            .heading-container {
                text-align: center;
                margin-top: 5vw;
                padding: 5vw 0;
            }

            .heading-container h1 {
                font-family: 'Exo 2', sans-serif;
                font-style: normal;
                font-weight: 700;
                font-size: 4.16vw;
                line-height: 1.2;
                letter-spacing: -0.02em;
                text-transform: uppercase;
                background: linear-gradient(to bottom, #FFFFFF, #A9A9A9);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }

            .heading-container h1 span {
                background: none;
                -webkit-background-clip: initial;
                background-clip: initial;
                color: var(--primary-blue);
            }

            /* --- Light Mode --- */
            @media (prefers-color-scheme: light) {
                .heading-section-wrapper {
                    background-color: #FFFFFF;
                }
                
                .heading-container h1 {
                    background: none;
                    -webkit-background-clip: unset;
                    background-clip: unset;
                    color: #111111;
                }

                .heading-container h1 span {
                    color: #007AFF; 
                }
            }

            /* --- Mobile View Modifications --- */
            @media (max-width: 768px) {
                .heading-container {
                    margin-top: 8vh;
                    margin-bottom: 8vh;
                    padding: 0 5vw;
                }

                .heading-container h1 {
                    font-size: 6.5vw;
                    line-height: 1.4;
                }
            }
        </style>
    """