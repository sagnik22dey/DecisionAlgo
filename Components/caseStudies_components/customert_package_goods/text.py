async def text_top_robot_section():
    return """
        <section>
            <div class="heading-container">
                <h1>
                    <span>Leading Enterprises</span> Across Various <br>
                    Consumer Goods <span class="text-white">Corporations</span> <span>Utilize</span> <br>
                    <span>Our Solutions.</span>
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

        </style>
        
    """
