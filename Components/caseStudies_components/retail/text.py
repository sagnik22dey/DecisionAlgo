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
            /* --- Default: Dark Mode --- */
            :root {
                --primary-blue: #5FC7FB;
                --primary-white: #FEFEFE;
                --primary-gray: #CCCCCC;
                --background-dark: transparent;
            }
            
            section {
                background-color: var(--background-dark);
                padding: 5vw 0; /* Manages vertical spacing */
            }
        
            .heading-container {
                text-align: center;
            }

            .heading-container h1 {
                font-family: 'Exo 2', sans-serif;
                font-size: 3.2vw;
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

            /* --- Light Mode --- */
            @media (prefers-color-scheme: light) {
                section {
                    background-color: #FFFFFF;
                }

                .heading-container h1 {
                    color: #111111; /* Default text becomes black */
                }

                /* Both span types become blue in light mode to match the image */
                .heading-container h1 span,
                .heading-container h1 .text-white {
                    color: #007AFF;
                }
            }

            /* --- Mobile View Modifications --- */
            @media (max-width: 768px) {
                section {
                    /* Adjust padding for mobile layout */
                    padding: 15vh 5vw 10vh;
                }

                .heading-container h1 {
                    font-size: 5.5vw;
                    line-height: 1.4;
                }
            }
        </style>
    """