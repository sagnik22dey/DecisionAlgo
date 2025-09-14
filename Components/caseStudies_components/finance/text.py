async def text_top_robot_section():
    return """
        <section>
            <div class="heading-container">
                <h1>
                    AI AND DATA SCIENCE IN FINANCIAL <br>SERVICES : <span>BANKING & LENDING</span>
                </h1>
            </div>
        </section>
    """
    


async def style_top_robot_section():
    return """
        <style>
            :root {
            --primary-blue: #5FC7FB;
            --primary-white: #FEFEFE;
            --primary-gray: #CCCCCC;
            --background-dark: #0A0A0A;
            --card-bg: rgba(20, 20, 20, 0.4);
            --card-border: rgba(95, 199, 251, 0.5);
        }
        
        .heading-container {
                text-align: center;
                margin-top: 5vw;
            }

            .heading-container h1 {
                font-size: 3.2rem;
                line-height: 1.2;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: -0.02em;
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

            /* --- Mobile View Modifications --- */
            @media (max-width: 768px) {
                .heading-container {
                    /* Add more vertical space and horizontal padding on mobile */
                    margin-top: 15vh;
                    margin-bottom: 10vh;
                    padding: 0 5vw;
                }

                .heading-container h1 {
                    /* Use vw for a fluid font-size that scales with the screen width */
                    font-size: 5.5vw;
                    /* Increase line-height for better readability of multi-line text */
                    line-height: 1.4;
                }
            }

        </style>
        
    """