async def trans_health_style():
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
        #healthcare-hero {
            position: relative;
            display: flex;
            justify-content: flex-end; /* Align content wrapper to the right */
            align-items: center;
            width: 100vw;
            height: 48vw; /* Creates a ~16:9 aspect ratio */
            max-width: 100vw;
            max-height: 90vh;
            background-image: url('../../Resources/Images/CaseStudies/healthcare/trans_bg.jpg');
            background-size: cover;
            background-position: center left; /* Focus on the left part of the image */
            border-radius: 2vw;
            overflow: hidden; /* Ensures content respects the border radius */
            color: #ffffff;
            transition: all 0.3s ease-in-out;
        }

        /* Dark overlay with a gradient to improve text readability on the right */
        #healthcare-hero::before {
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
            position: relative; /* To appear above the ::before pseudo-element */
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

        #healthcare-hero h1 {
            font-family: 'Exo 2', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 243, 243, 0.58) 0.22%, #EBF3F3 15.65%, #EBF3F3 54.72%, rgba(235, 243, 243, 0.7) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            margin-bottom: 2.5vh;
        }

        #healthcare-hero p {
            line-height: 1.6;
            opacity: 0.9;
            font-size: 1.1rem;
            margin-bottom: 0;
        }

        .cta-button {
            background-color: #ffffff;
            color: #212121;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            padding: 1.5rem 2.5rem;
            border-radius: 5rem;
            font-size: 1rem;
            margin-top: 2rem;
        }

        .cta-button:hover {
            transform: scale(1.05);
        }

        /* --- Mobile View Modifications --- */
        @media (max-width: 768px) {
            #healthcare-hero {
                flex-direction: column;
                justify-content: center;
                align-items: center;
                width: 90vw;
                height: auto;
                min-height: 90vh;
                margin: 5vh auto;
                background-position: center center;
                border-radius: 5vw;
            }

            #healthcare-hero::before {
                background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 20%, rgba(0, 0, 0, 0.1) 70%);
            }

            .text-content-wrapper {
                width: 85vw;
                align-items: center;
                text-align: center;
                padding: 0vh 5vw;
            }

            #healthcare-hero h1 {
                font-size: 6.5vw;
                line-height: 1.25;
                margin-bottom: 4vh;
            }

            #healthcare-hero p {
                font-size: 4vw;
                line-height: 1.5;
                margin-bottom: 5vh;
            }

            .cta-button {
                font-size: 3.5vw;
                padding: 1.5vh 8vw;
                border-radius: 10vw;
                margin-top: 2vh;
            }
        }
    </style>
"""


async def trans_health_body():
    return """
    <section id="healthcare-hero">
        <div class="text-content-wrapper">
            <h1>Revolutionizing Healthcare & Life Science In The Digital Age</h1>
            <p>
                In the realm of healthcare and life sciences, innovation is the cornerstone of
                progress. This sector, dedicated to enhancing the quality of life and advancing
                medical science, plays a pivotal role in shaping the future of healthcare. Here,
                cutting-edge research, breakthrough technologies, and a commitment to improving
                patient care converge. From pharmaceutical advancements to telemedicine, the
                healthcare and life sciences industry is a driving force in improving global health
                outcomes and leading us into a healthier, more informed future.
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