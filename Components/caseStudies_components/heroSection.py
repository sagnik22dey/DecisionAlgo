async def heroSection_body(heroName):
    return f"""
    <section class="pricing-hero-section">
    <h1 class="contact-title">{heroName}</h1>
    </section>
    """

async def heroSection_style():
    return """
    <style>
        /* Ensure a font is available, for example, from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700&display=swap');

        .pricing-hero-section {
            position: relative;
            width: 100%;
            height: 40vh; /* Default height for desktop */
            display: flex;
            justify-content: center;
            align-items: center;
            /* Using a high-quality placeholder image that matches the theme */
            background-image: url('../../Resources/Images/CaseStudies/customer/hero_bg.png');
            background-size: cover;
            background-position: center;
            overflow: hidden;
            transition: height 0.3s ease-in-out;
            margin-top: 5vw;
        }
        .contact-title {
            /* Font and Text Styling */
            font-family: 'Exo 2', sans-serif;
            font-style: normal;
            font-weight: 700;
            line-height: 1.2;
            text-align: center;
            letter-spacing: -0.07em;
            text-transform: capitalize;
            
            /* Gradient Text Effect */
            background: linear-gradient(90deg, rgba(235, 243, 243, 0.5) 6.45%, rgba(235, 243, 243, 0.75) 23.17%, #EBF3F3 51.92%, rgba(235, 243, 243, 0.75) 77.34%, rgba(235, 243, 243, 0.5) 94.95%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-fill-color: transparent;

            /* Responsive font size */
            font-size: clamp(5.92vh, 10vw, 14.22vh);
            scale: 0.8;
        }

        /* --- Mobile View --- */
        @media (max-width: 768px) {
            .pricing-hero-section {
                height: 35vh; /* Optimized height for mobile viewport */
                margin-top: 8vh; /* Adjusted spacing for mobile layout */
            }

            .contact-title {
                /* Larger, more impactful font size for mobile hero */
                font-size: clamp(5vh, 5vw, 5vh);
                letter-spacing: -0.04em; /* Slightly wider for better readability on small screens */
                line-height: 1.1; /* Tighter line height for a compact look */
                padding: 0 3vw; /* Ensures text doesn't touch screen edges */
            }
        }
    </style>
    """