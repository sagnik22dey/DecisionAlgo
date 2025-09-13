async def trans_Finance_style():
    return """
    <style>
        /* --- Base Styles & Resets --- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        /* --- Hero Section Styles (Desktop First) --- */
        #finance-hero {
            position: relative;
            display: flex;
            justify-content: flex-end; /* Align content wrapper to the right */
            align-items: center;
            width: 100vw;
            height: 48vw; /* Creates a ~16:9 aspect ratio */
            max-width: 100vw;
            max-height: 90vh;
            background-image: url('../../Resources/Images/CaseStudies/finance/trans_bg.jpg');
            background-size: cover;
            background-position: center left; /* Focus on the left part of the image */
            border-radius: 2vw;
            overflow: hidden; /* Ensures content respects the border radius */
            color: #ffffff;
            transition: all 0.3s ease-in-out;
        }

        /* Dark overlay with a gradient to improve text readability on the right */
        #finance-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to right, rgba(0, 0, 0, 0.1) 20%, rgba(0, 0, 0, 0.8) 65%);
            z-index: 1;
            transition: background 0.5s ease-in-out;
        }

        /* Wrapper for all the text content */
        .text-content-wrapper {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start; /* Left-aligns the content within the wrapper */
            text-align: left;
            width: 45vw;
            padding: 4vh 5vw 4vh 2vw;
            transition: all 0.3s ease-in-out;
        }

        #finance-hero h1 {
            font-weight: 700;
            line-height: 1.1;
            font-size: 3.5rem;
            margin-bottom: 2.5rem;
        }

        #finance-hero p {
            line-height: 1.6;
            opacity: 0.9;
            font-size: 1.1rem;
            margin-bottom: 4rem;
        }

        .cta-button {
            background-color: #ffffff;
            color: #212121;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            padding: 0.5rem 2.5rem;
            border-radius: 5rem;
            font-size: 1rem;
            margin-top: 2rem;
        }

        .cta-button:hover {
            transform: scale(1.05);
        }

        /* --- Mobile View Modifications --- */
        /* This media query applies styles only for screens smaller than 768px */
        @media (max-width: 768px) {
            #finance-hero {
                /* Adjust layout for vertical stacking */
                flex-direction: column;
                justify-content: center; /* Center content vertically */
                align-items: center;     /* Center content horizontally */
                
                /* Set a more mobile-friendly size with some margin */
                width: 90vw;
                height: auto; /* Let content define the height */
                min-height: 90vh; /* Ensure it's almost full screen */
                margin: 5vh auto; /* Center the component on the page */
                background-position: center center; /* Center the background image */
                border-radius: 5vw; /* Prettier border radius for mobile */
            }

            /* Adjust overlay to protect text at the bottom-center */
            #finance-hero::before {
                background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 20%, rgba(0, 0, 0, 0.1) 70%);
            }

            .text-content-wrapper {
                /* Center text and make it take up more of the screen width */
                width: 85vw;
                align-items: center;
                text-align: center;
                padding: 0vh 5vw; /* Balanced padding */
            }

            #finance-hero h1 {
                /* Fluid font size that scales with screen width */
                font-size: 6vw;
                line-height: 1.2;
                margin-bottom: 2.5vh;
            }

            #finance-hero p {
                /* Fluid font size for paragraphs */
                font-size: 4vw;
                line-height: 1.2;
                margin-bottom: 3vh; /* Adjust spacing between paragraphs */
            }
            
            #finance-hero p:last-of-type {
                margin-bottom: 5vh; /* More space before the button */
            }

            .cta-button {
                /* Fluid sizing for the button */
                font-size: 3.5vw;
                padding: 1.5vh 8vw;
                border-radius: 10vw;
                margin-top: 2vh;
            }
        }
    </style>
"""


async def trans_Finance_body():
    return """
    <section id="finance-hero">
        <div class="text-content-wrapper">
            <h1>Transforming Finance In The Digital Era</h1>
            <p>
                In today's digital era, the financial sector stands at a crossroads, poised for transformation. It carries not only the capacity but also the responsibility to orchestrate a global response to the ever-evolving economic landscape. Banks have evolved beyond the realms of mere operational continuity, as they now cultivate fresh competencies to guide customers, partners, and the broader community through present challenges and into an innovative future.
            </p>
            <p>
                To navigate these dynamic times successfully, we recommend initiatives that empower your institution to fortify its customer base, streamline operations, foster trust, and contribute to the strengthening of both the economy and society.
            </p>
            <button class="cta-button">Get in Touch</button>
        </div>
    </section>

    <!-- 
        JavaScript for layout adjustments has been removed and replaced 
        with a pure CSS media query solution in the style section for 
        better performance, elegance, and maintainability.
    -->
"""