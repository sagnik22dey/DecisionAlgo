async def text_top_robot_section():
    return """
        <section>
            <div class="heading-container">
                <h1>
                    <span>AI AND DATA SCIENCE</span> ACROSS DIVERSE <br> INDUSTRIES IN <span>HEALTHCARE</span>
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
                font-family: 'Exo 2';
                font-style: normal;
                font-weight: 700;
                font-size: 4.16vw;
                line-height: 11.4vh;
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

        </style>
        
    """
