async def heroSection_body(heroName):
    return f"""
    <section class="pricing-hero-section">
    <h1 class="contact-title">{heroName}</h1>
    </section>

    <script>
        function optimizePricingBanner() {{
            const title = document.querySelector('.contact-title');
            const section = document.querySelector('.pricing-hero-section');
            if (!title || !section) return;

            const isMobile = window.innerWidth <= 768;

            if (isMobile) {{
                // Apply mobile-specific styles for better impact and fit
                title.style.fontSize = '10rem';
                section.style.height = '20rem';
            }} else {{
                // Apply desktop styles
                title.style.fontSize = '5vw';
                section.style.height = '30vh';
            }}
        }}

        // Run optimization on load and when the window is resized
        window.addEventListener('load', optimizePricingBanner);
        window.addEventListener('resize', optimizePricingBanner);
    </script>
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
        }

        .pricing-hero-title {
            position: relative;
            z-index: 2;
            font-family: 'Poppins', sans-serif;
            font-weight: 900; /* Extra bold for impact */
            font-size: 8vw; /* Default font size for desktop */
            text-transform: uppercase;
            letter-spacing: 0.2vw;
            text-align: center;
            
            /* Metallic gradient effect to match the image */
            background: linear-gradient(180deg, #FFFFFF 40%, #D1D1D1 90%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            
            /* Subtle shadow for depth */
            text-shadow: 0 0.2vw 0.5vw rgba(0, 0, 0, 0.7);
            transition: font-size 0.3s ease-in-out;
        }
    </style>
    """