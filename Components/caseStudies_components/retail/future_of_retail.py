async def future_of_retail_style():
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
        #retail-hero {
            position: relative;
            display: flex;
            justify-content: flex-end; /* Align content wrapper to the right */
            align-items: center;
            width: 100vw;
            height: 48vw; /* Creates a ~16:9 aspect ratio */
            max-width: 100vw; 
            max-height: 90vh;
            background-image: url('../../Resources/Images/CaseStudies/retail/future_bg.jpg');
            background-size: cover;
            background-position: center left; /* Focus on the left part of the image */
            border-radius: 2vw;
            overflow: hidden; /* Ensures content respects the border radius */
            color: #ffffff;
            transition: all 0.3s ease-in-out;
        }

        /* Dark overlay with a gradient to improve text readability on the right */
        #retail-hero::before {
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
        .content-wrapper {
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

        .report-tag {
            background-color: #38bdf8;
            color: #ffffff;
            border: none;
            font-weight: 500;
            padding: 0.8vw 1.5vw;
            border-radius: 5vw;
            font-size: 1vw;
            margin-bottom: 2vw;
        }

        #retail-hero h1 {
            font-weight: 700;
            line-height: 1.1;
            font-size: 3.5vw;
            margin-bottom: 2.5vw;
        }

        #retail-hero p {
            line-height: 1.6;
            opacity: 0.9;
            font-size: 1.1vw;
            margin-bottom: 4vw;
        }

        .cta-button {
            background-color: #ffffff;
            color: #000000;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, background-color 0.2s ease;
            padding: 0.5vw 2.5vw;
            border-radius: 5vw;
            font-size: 1vw;
        }

        .cta-button:hover {
            transform: scale(1.05);
        }

        /* --- Mobile View Modifications --- */
        @media (max-width: 768px) {
            #retail-hero {
                flex-direction: column;
                justify-content: center;
                align-items: center;
                width: 90vw;
                height: auto; /* Let height be determined by content */
                min-height: 90vh; /* Ensure it feels full-screen */
                margin: 0vw auto; /* Center the component */
                background-position: center center;
                border-radius: 5vw;
                margin-top: -5vw;
            }

            #retail-hero::before {
                /* Gradient from bottom to top for mobile text readability */
                background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 20%, rgba(0, 0, 0, 0.1) 70%);
                
            }

            .content-wrapper {
                width: 85vw;
                align-items: center;
                text-align: center;
                padding: 0vh 5vw;
            }

            .report-tag {
                font-size: 4vw;
                padding: 1.5vh 5vw;
                border-radius: 10vw;
                margin-bottom: 4vh;
            }

            #retail-hero h1 {
                font-size: 8.5vw;
                line-height: 1.2;
                margin-bottom: 3vh;
            }

            #retail-hero p {
                font-size: 3.5vw;
                line-height: 1.7;
                margin-bottom: 6vh;
            }

            .cta-button {
                font-size: 3.5vw;
                padding: 1.5vh 8vw;
                border-radius: 10vw;
            }
        }
    </style>
"""
async def future_of_retail_body():
    return"""
    <section id="retail-hero">
        <div class="content-wrapper">
            <span class="report-tag">Report</span>
            <h1>Future Of Retail</h1>
            <p>
                In the face of economic challenges and market shifts, the path forward for the
                retail industry is filled with uncertainties. DecisionAlgo has conducted extensive
                research to predict where the industry is headed and provide insights across six
                vital categories. Our research equips retailers to be better prepared and stay ahead
                in the ever-evolving retail landscape. Don't miss the opportunity to access our
                comprehensive research for making informed decisions that keep you at the
                forefront of retail's transformation.
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