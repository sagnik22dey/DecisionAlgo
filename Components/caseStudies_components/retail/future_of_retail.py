async def future_of_retail_style():
    return """
<style>
        /* --- Base Styles & Resets --- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }


        /* --- Hero Section Styles --- */
        /* This section contains all the styles for the component.
           The initial values are optimized for desktop view.
           JavaScript will adjust these for mobile view. */
        #retail-hero {
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
            
            /* Sizing and padding using viewport units */
            width: 45vw;
            padding: 4vh 5vw 4vh 2vw;
            transition: all 0.3s ease-in-out;
        }

        .report-tag {
            background-color: #38bdf8;
            color: #ffffff;
            border: none;
            font-weight: 500;
            
            /* Sizing and spacing using viewport units */
            padding: 0.8vh 1.5vw;
            border-radius: 5vh;
            font-size: 1vw;
            margin-bottom: 2vh;
        }

        #retail-hero h1 {
            font-weight: 700;
            line-height: 1.1;

            /* Sizing and spacing using viewport units */
            font-size: 3.5vw;
            margin-bottom: 2.5vh;
        }

        #retail-hero p {
            line-height: 1.6;
            opacity: 0.9;
            
            /* Sizing and spacing using viewport units */
            font-size: 1.1vw;
            margin-bottom: 4vh;
        }

        .cta-button {
            background-color: #ffffff;
            color: #000000;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, background-color 0.2s ease;
            
            /* Sizing and spacing using viewport units */
            padding: 1.5vh 2.5vw;
            border-radius: 5vh;
            font-size: 1vw;
        }

        .cta-button:hover {
            transform: scale(1.05);
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

    <script>
        /**
         * This script handles the responsive layout adjustments.
         * It checks the window width and applies specific styles for mobile or desktop views,
         * fulfilling the requirement to use JavaScript for view optimization.
         * This creates two different layouts ("splits") for the content.
         */
        function adjustLayout() {
            // Define a breakpoint for mobile devices
            const isMobile = window.innerWidth < 48;

            // Select all the elements that need style adjustments
            const heroSection = document.getElementById('retail-hero');
            const contentWrapper = heroSection.querySelector('.content-wrapper');
            const reportTag = heroSection.querySelector('.report-tag');
            const heading = heroSection.querySelector('h1');
            const paragraph = heroSection.querySelector('p');
            const ctaButton = heroSection.querySelector('.cta-button');
            const overlay = heroSection.style; // We will modify the pseudo-element via a class or direct style changes if possible

            if (isMobile) {
                // --- APPLY MOBILE STYLES ---

                // Change section layout to be vertical and taller
                heroSection.style.width = '90vw';
                heroSection.style.height = '85vh'; // Taller for mobile content
                heroSection.style.justifyContent = 'center'; // Center the content block
                heroSection.style.backgroundPosition = 'center center'; 
                                
                // Adjust overlay for better readability in a stacked layout
                heroSection.style.setProperty('--gradient', 'linear-gradient(to top, rgba(0, 0, 0, 0.9) 20%, rgba(0, 0, 0, 0.2) 80%)');
                heroSection.style.background = `var(--gradient), url('../../Resources/Images/CaseStudies/retail/future_bg.jpg')`;
                heroSection.style.backgroundSize = 'cover';
                heroSection.style.backgroundPosition = 'center';
                
                // Center the content and make it wider
                contentWrapper.style.width = '80vw';
                contentWrapper.style.alignItems = 'center'; // Center-align items
                contentWrapper.style.textAlign = 'center'; // Center-align text
                contentWrapper.style.padding = '4vh 2vw';
                
                // Adjust font sizes for mobile readability using vw
                reportTag.style.fontSize = '3.5vw';
                reportTag.style.padding = '1vh 4vw';

                heading.style.fontSize = '8vw';
                
                paragraph.style.fontSize = '3.8vw';
                
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
                heroSection.style.background = `var(--gradient), url('../../Resources/Images/CaseStudies/retail/future_bg.jpg')`;
                heroSection.style.backgroundSize = 'cover';
                heroSection.style.backgroundPosition = 'center left';


                // Restore content wrapper layout
                contentWrapper.style.width = '45vw';
                contentWrapper.style.alignItems = 'flex-start'; // Left-align items
                contentWrapper.style.textAlign = 'left'; // Left-align text
                contentWrapper.style.padding = '4vh 5vw 4vh 2vw';
                
                // Restore desktop font sizes
                reportTag.style.fontSize = '1vw';
                reportTag.style.padding = '0.8vh 1.5vw';

                heading.style.fontSize = '3.5vw';
                
                paragraph.style.fontSize = '1.1vw';
                
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