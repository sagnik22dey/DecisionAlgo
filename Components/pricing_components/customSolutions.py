async def custom_solutions_body():
    return """

    <section class="custom-solutions-container">
        <div class="solutions-background-card"></div>
        <section class="custom-solutions-section">
            <h1 class="solutions-headline">CUSTOM SOLUTIONS</h1>
            <ol class="solutions-list">
                <li>Customized services to fit your unique needs.</li>
                <li>Dashboards designed specifically for your business requirements.</li>
                <li>Single-point contact for personalized and responsive assistance.</li>
            </ol>
            <p class="solutions-tagline">
                Let's connect and take your business to the next level!
            </p>
            <a href="#" class="consultation-btn">Free 1:1 Consultation</a>
        </section>
    </section>

    <script>
        function optimizeCustomSolutionsLayout() {
            const isMobile = window.innerWidth <= 768;
            const section = document.querySelector('.custom-solutions-section');
            const headline = document.querySelector('.solutions-headline');
            const list = document.querySelector('.solutions-list');
            const tagline = document.querySelector('.solutions-tagline');
            const button = document.querySelector('.consultation-btn');
            const backgroundCard = document.querySelector('.solutions-background-card');

            if (isMobile) {
                // Apply mobile styles for a beautiful and elegant layout
                
                // Adjust main section for better spacing on mobile
                section.style.width = '90vw';
                section.style.padding = '8vh 7vw';
                section.style.gap = '3vh';

                // Properly center the background card vertically
                backgroundCard.style.top = '105vw';
                
                // Refine typography for readability and visual appeal
                headline.style.fontSize = '6.5vw';
                headline.style.lineHeight = '1.2';

                list.style.fontSize = '1.7vw';
                list.style.lineHeight = '1.7'; // Increase for better readability
                list.style.maxWidth = '80%';
                list.style.scale = 1.2;

                tagline.style.fontSize = '4vw';
                tagline.style.lineHeight = '1.5';
                
                // Enhance the call-to-action button
                button.style.fontSize = '4.2vw';
                button.style.padding = '1.5vh 5vw';
                button.style.marginTop = '1vh';

            } else {
                // Revert to desktop styles by clearing all inline styles
                section.style.cssText = '';
                headline.style.cssText = '';
                list.style.cssText = '';
                tagline.style.cssText = '';
                button.style.cssText = '';
                backgroundCard.style.cssText = '';
            }
        }
        window.addEventListener('load', optimizeCustomSolutionsLayout);
        window.addEventListener('resize', optimizeCustomSolutionsLayout);
    </script>
    """

async def custom_solutions_style():
    return """
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;700;800&family=Poppins:wght@400;500;700&family=Urbanist:wght@400;700&display=swap");

        .custom-solutions-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            padding: 10vh 5vw;
            background-color: transparent;
            box-sizing: border-box;
        }

        .solutions-background-card {
            position: absolute;
            width: 82vw;
            height: 105%;
            border-top: 0.15vw solid rgba(255, 255, 255, 255);
            border-radius: 3vw;
            top: 24vw;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 1;
        }

        .custom-solutions-section {
            position: relative;
            z-index: 2;
            width: 88vw;
            padding: 8vh 5vw; /* Default for desktop */
            text-align: center;
            border-radius: 2.5vw;
            background: linear-gradient(160deg, #2E2E2E 0%, #222222 100%);
            box-shadow: inset 0 0.1vw 0.2vw rgba(255, 255, 255, 0.05), 0 1vw 3vw rgba(0, 0, 0, 0.6);
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1vh;
            font-family: 'Poppins', sans-serif;
        }

        .solutions-headline {
            font-size: 4vw; /* Default for desktop */
            font-weight: 700;
            text-transform: uppercase;
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.3) 8.85%, #EBF0F3 22.59%, #EBF0F3 57.4%, rgba(235, 239, 243, 0.72) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }

        .solutions-list {
            list-style-position: inside;
            text-align: left;
            font-size: 1.6vw;
            line-height: 1;
            color: rgba(255, 255, 255, 0.85);
            padding: 0;
            margin-top: 4vh;
            margin-bottom: 1.5vh;
            max-width: 90%;
        }
        
        .solutions-list li {
            margin-bottom: 1.5vh;
        }
        
        .solutions-list li::marker {
            color: rgba(255, 255, 255, 0.9);
            font-weight: 700;
        }

        .solutions-tagline {
            font-size: 2.3vw; /* Default for desktop */
            font-weight: 500;
            color: #FFFFFF;
            margin: 0;
        }

        .consultation-btn {
            display: inline-block;
            padding: 1vw 1.5vw; /* Default for desktop */
            background-color: #FFFFFF;
            color: #000000;
            font-size: 1.2vw; /* Default for desktop */
            font-weight: 500;
            text-decoration: none;
            border-radius: 50vw;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            margin-top:2vh;
        }

        .consultation-btn:hover {
            box-shadow: 0 0.5vw 2vw rgba(255, 255, 255,0.88);
        }
        
        @media (max-width: 768px) {
            .custom-solutions-container{
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                padding: 10vh 5vw;
                background-color: transparent;
                box-sizing: border-box;
                margin-top: -30vw;
            }
            
        )
    </style>
    """