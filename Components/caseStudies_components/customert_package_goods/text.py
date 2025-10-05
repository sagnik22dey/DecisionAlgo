async def style_top_robot_section():
    return """
        <style>
            /* --- Default: Dark Mode --- */
            :root {
                --primary-blue: #5FC7FB;
                --primary-white: #FEFEFE;
                --primary-gray: #CCCCCC;
                --background-dark: #0A0A0A;
            }

            .heading-section-wrapper {
                background-color: var(--background-dark);
                padding: 5vw 0;
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
                .heading-section-wrapper {
                    background-color: #FFFFFF;
                }

                .heading-container h1 {
                    color: #111111; /* Default text becomes black */
                }

                /* In light mode, all spans become blue to match the image */
                .heading-container h1 span,
                .heading-container h1 .text-white {
                    color: #007AFF;
                }
            }

            /* --- Mobile View --- */
            @media (max-width: 768px) {
                .heading-section-wrapper {
                    padding: 10vh 5vw;
                }

                .heading-container h1 {
                    font-size: 4.3vw;
                    line-height: 1.3;
                }
            }
        </style>
    """


async def text_top_robot_section():
    return """
        <section class="heading-section-wrapper">
            <div class="heading-container">
                <h1>
                    <span>Leading Enterprises</span> Across Various <br>
                    Consumer Goods <span class="text-white">Corporations</span> <span>Utilize</span> <br>
                    <span>Our Solutions.</span>
                </h1>
            </div>
        </section>
    """
