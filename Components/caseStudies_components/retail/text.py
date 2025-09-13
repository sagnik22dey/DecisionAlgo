async def text_top_robot_section():
    return """
        <section>
            <div class="heading-container">
                <h1>
                    <span>Leading Retailers</span> Across The <br>
                    <span class="text-white">Industry Leverage</span> <span>Our Solutions.</span>
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
                color: var(--primary-gray);
            }

            .heading-container h1 span {
                color: var(--primary-blue);
            }
            .heading-container h1 .text-white {
                color: var(--primary-white);
            }

            /* --- Mobile View Modifications --- */
            @media (max-width: 768px) {
                .heading-container {
                    /* Add more vertical space and horizontal padding for mobile */
                    margin-top: 15vh;
                    margin-bottom: 10vh;
                    padding: 0 5vw;
                }

                .heading-container h1 {
                    /* Use vw for a fluid font-size that scales with screen width */
                    font-size: 8vw;
                    /* Increase line-height for better readability of multi-line text */
                    line-height: 1.4;
                }
            }

        </style>
        
    """