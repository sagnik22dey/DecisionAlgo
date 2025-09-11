async def trans_insurance_style():
    return """
    <style>
        /* --- Base Styles & Resets --- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        /* --- Hero Section Styles --- */
        /* This section contains all the styles for the component.
           The initial values are optimized for desktop view.
           JavaScript will adjust these for mobile view. */

        #insurance-hero {
            position: relative;
            display: flex;
            justify-content: flex-end; /* Align content wrapper to the right */
            align-items: center;
            
            /* Dimensions using vw to maintain aspect ratio */
            width: 100vw;
            height: 48vw; /* Creates a ~16:9 aspect ratio */
            max-width: 100vw; /* Cap the max size on very large screens */
            max-height: 90vh;
            
            /* Background Image */
            background-image: url('../../Resources/Images/CaseStudies/insurance/trans_bg.jpg');
            background-size: cover;
            background-position: center left; /* Focus on the left part of the image */

            border-radius: 2vw;
            overflow: hidden; /* Ensures content respects the border radius */
            color: #ffffff;
            transition: all 0.3s ease-in-out;
        }

        /* Dark overlay with a gradient to improve text readability on the right */
        #insurance-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to right, rgba(0, 0, 0, 0.1) 20%, rgba(0, 0, 0, 0.8) 65%);
            z-index: 1;
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
            
            /* Sizing and padding using viewport units */
            width: 45vw;
            padding: 4vh 5vw 4vh 2vw;
            transition: all 0.3s ease-in-out;
        }

        #insurance-hero h1 {
            /* Revolutionizing Insurance in the Digital Age */
            width: 617px;
            height: 216px;
            font-family: 'Exo 2';
            font-style: normal;
            font-weight: 700;
            font-size: 60px;
            line-height: 72px;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 243, 243, 0.58) 0.22%, #EBF3F3 15.65%, #EBF3F3 54.72%, rgba(235, 243, 243, 0.7) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            /* Inside auto layout */
            flex: none;
            order: 0;
            align-self: stretch;
            flex-grow: 0;
            margin-bottom: 2.5vh;
        }

        #insurance-hero p {
            line-height: 1.6;
            opacity: 0.9;
            
            /* Sizing and spacing using viewport units */
            font-size: 1.1vw;
            margin-bottom: 4vh;
        }

        .cta-button {
            background-color: #ffffff;
            color: #212121;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;

            /* Sizing and spacing using viewport units */
            padding: 1.5vh 2.5vw;
            border-radius: 5vh;
            font-size: 1vw;
            margin-top: 2vh;
        }

        .cta-button:hover {
            transform: scale(1.05);
        }
    </style>
"""


async def trans_insurance_body():
    return """
    <section id="insurance-hero">
        <div class="text-content-wrapper">
            <h1>Revolutionizing Insurance In The Digital Age</h1>
            <p>
                In today's digital era, the insurance sector stands at a crossroads, poised for transformation. It carries not only the capacity but also the responsibility to orchestrate a global response to the ever-evolving economic landscape. Insurers have evolved beyond the realms of mere operational continuity, as they now cultivate fresh competencies to guide customers, partners, and the broader community through present challenges and into an innovative future.
            </p>
            <p>
                To navigate these dynamic times successfully, we recommend initiatives that empower your institution to fortify its customer base, streamline operations, foster trust, and contribute to the strengthening of both the economy and society.
            </p>
            <button class="cta-button">Get in Touch</button>
        </div>
    </section>

    <!-- JavaScript for Responsive Layout Adjustments -->
    <script>
        /**
         * This script handles the responsive layout adjustments.
         * It checks the window width and applies specific styles for mobile or desktop views,
         * fulfilling the requirement to use JavaScript for view optimization.
         * This creates two different layouts ("splits") for the content.
         */
        function adjustLayout() {
            // Define a breakpoint for mobile devices
            const isMobile = window.innerWidth < 768;

            // Select all the elements that need style adjustments
            const heroSection = document.getElementById('insurance-hero');
            const contentWrapper = heroSection.querySelector('.text-content-wrapper');
            const heading = heroSection.querySelector('h1');
            const paragraphs = heroSection.querySelectorAll('p');
            const ctaButton = heroSection.querySelector('.cta-button');

            if (isMobile) {
                // --- APPLY MOBILE STYLES ---

                // Change section layout to be vertical and taller
                heroSection.style.width = '90vw';
                heroSection.style.height = '85vh'; // Taller for mobile content
                heroSection.style.justifyContent = 'center'; // Center the content block
                heroSection.style.backgroundPosition = 'center center';
                                
                // Adjust overlay for better readability in a stacked layout
                heroSection.style.setProperty('--gradient', 'linear-gradient(to top, rgba(0, 0, 0, 0.9) 20%, rgba(0, 0, 0, 0.2) 80%)');
                heroSection.style.background = `var(--gradient), url('../../Resources/Images/CaseStudies/insurance/trans_bg.jpg')`;
                heroSection.style.backgroundSize = 'cover';
                heroSection.style.backgroundPosition = 'center';
                
                // Center the content and make it wider
                contentWrapper.style.width = '80vw';
                contentWrapper.style.alignItems = 'center'; // Center-align items
                contentWrapper.style.textAlign = 'center'; // Center-align text
                contentWrapper.style.padding = '4vh 2vw';
                
                // Adjust font sizes for mobile readability using vw
                heading.style.fontSize = '8vw';
                
                paragraphs.forEach(p => {
                    p.style.fontSize = '3.8vw';
                });
                
                ctaButton.style.fontSize = '4vw';
                ctaButton.style.padding = '1.8vh 6vw';

            } else {
                // --- APPLY DESKTOP STYLES (Revert to original CSS) ---
                
                // Restore section layout
                heroSection.style.width = '100vw';
                heroSection.style.height = '48vw';
                heroSection.style.justifyContent = 'flex-end'; // Right-align content block
                heroSection.style.backgroundPosition = 'center left';
                heroSection.style.scale = '0.9';

                // Restore desktop overlay and background
                heroSection.style.setProperty('--gradient', 'linear-gradient(to right, rgba(0, 0, 0, 0.1) 20%, rgba(0, 0, 0, 0.8) 65%)');
                heroSection.style.background = `var(--gradient), url('../../Resources/Images/CaseStudies/insurance/trans_bg.jpg')`;
                heroSection.style.backgroundSize = 'cover';
                heroSection.style.backgroundPosition = 'center left';


                // Restore content wrapper layout
                contentWrapper.style.width = '45vw';
                contentWrapper.style.alignItems = 'flex-start'; // Left-align items
                contentWrapper.style.textAlign = 'left'; // Left-align text
                contentWrapper.style.padding = '4vh 5vw 4vh 2vw';
                
                // Restore desktop font sizes
                heading.style.fontSize = '3.5vw';
                
                paragraphs.forEach(p => {
                    p.style.fontSize = '1.1vw';
                });
                
                ctaButton.style.fontSize = '1vw';
                ctaButton.style.padding = '1.5vh 2.5vw';
            }
        }

        // Run the function on initial page load
        document.addEventListener('DOMContentLoaded', adjustLayout);

        // Re-run the function whenever the window is resized
        window.addEventListener('resize', adjustLayout);
    </script>
"""
