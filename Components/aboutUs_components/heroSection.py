async def heroSection_body():
    return """
    <div class="hero-section-container">
        <!-- Background Elements -->
        <div class="grid-overlay"></div>
        <!-- Eclipse Glow Background -->
        <div class="eclipse-glow"></div>
        <!-- Main Content Wrapper -->
        <div class="hero-content-wrapper">
            <!-- Left Section: Image -->
            <div class="hero-image-section">
                <img src="../../Resources/Images/AboutUs/Mask_group.png" alt="Profile of a futuristic android" class="robot-image">
            </div>

            <!-- Right Section: Text Content -->
            <div class="hero-text-section">
                <h1 class="hero-headline">Leading the <span class="highlight">AI & Data Revolution</span></h1>
                <p class="hero-paragraph">At DecisionAlgo, we turn data into actionable insights that fuel business growth. Recognized by Startup India and backed by industry giants like AWS and DigitalOcean, we empower businesses with cutting-edge AI, automation, and data-driven solutions.</p>
                <a href="/contactus" class="hero-cta-button">Discover How We Work</a>
                <div class="hero-keywords">
                    <span>Real-time dashboards</span>
                    <span>AI chatbots</span>
                    <span>Automated reports</span>
                    <span>Intelligent outsourcing</span>
                </div>
            </div>
        </div>
    </div>
    """


async def heroSection_style():
    return """
<style>
    /* --- Structural & Theme-Agnostic Styles --- */
    .hero-section-container {
        width: 100vw;
        margin: auto;
        min-height: 90vh;
        position: relative;
        display: flex;
        align-items: stretch;
        overflow: hidden;
        border-radius: 4vw;
        border-bottom-right-radius: 5vw;
        border-bottom-style: solid;
        border-bottom-width: 1px;
    }
        
    .grid-overlay {
        position: absolute;
        width: 100%; 
        height: 100%; 
        left: 0;
        top: 0;
        border-radius: 2vw;
        border-bottom-right-radius: 5vw;
    }
    
    .eclipse-glow {
        position: absolute;
        width: 70vw;
        height: 70vw;
        left: 57vw;
        top: 36vh;
        transform: translateY(-50%);
        background-image: url('../../Resources/Images/AboutUs/ecliplse_glow.png');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        z-index: 1;
        pointer-events: none;
    }

    .hero-content-wrapper {
        display: flex;
        width: 100%;
        max-width: 100%;
        align-items: stretch;
        position: relative;
        z-index: 2;
        transition: flex-direction 0.3s ease-in-out;
    }

    .hero-image-section {
        flex: 0 0 45vw;
        transition: all 0.3s ease-in-out;
    }

    .robot-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: scale(1.0);
        transform-origin: center;
    }

    .hero-text-section {
        flex: 1;
        padding-left: 5vw;
        padding-right: 5vw;
        justify-content: center;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 2.5vh;
        transition: all 0.3s ease-in-out;
    }

    .hero-headline {
        font-size: 4vw;
        font-weight: 700;
        line-height: 1.2;
    }

    .hero-paragraph {
        font-size: 1vw;
        font-weight: 400;
        line-height: 1.6;
        max-width: 45vw;
    }

    .hero-cta-button {
        display: inline-block;
        font-size: 1vw;
        font-weight: 600;
        text-decoration: none;
        padding: 1.5vh 2.5vw;
        border-radius: 50vw;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .hero-cta-button:hover {
        transform: scale(1.05);
    }

    .hero-keywords {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5vw 1.5vw;
        font-size: 0.9vw;
    }

    .hero-keywords span:not(:last-child)::after {
        content: '|';
        margin-left: 1.5vw;
    }

    /* --- Theming Section --- */

    /* Light Theme */
    @media (prefers-color-scheme: light) {
        .hero-section-container {
            background-color: #FFFFFF;
            border-bottom-color: #E5E7EB;
        }
        .grid-overlay {
            background-image: linear-gradient(to right, rgba(206, 222, 245, 0.7) 2px, transparent 2px), linear-gradient(to bottom, rgba(206, 222, 245, 0.7) 2px, transparent 2px);
            background-size: 3.5vw 3.5vw;
        }
        .eclipse-glow {
            opacity: 0; /* Hide glow in light mode */
        }
        .hero-headline { color: #1F2937; }
        .hero-headline .highlight { color: #2563EB; }
        .hero-paragraph { color: #4B5563; }
        .hero-cta-button {
            background-color: #2563EB;
            color: #FFFFFF;
        }
        .hero-cta-button:hover {
            box-shadow: 0 0.5vw 1.5vw rgba(37, 99, 235, 0.25);
        }
        .hero-keywords { color: #6B7280; }
        .hero-keywords span:not(:last-child)::after { color: #D1D5DB; }
    }

    /* Dark Theme */
    @media (prefers-color-scheme: dark) {
        .hero-section-container {
            background-color: #101010;
            border-bottom-color: #FFFFFF;
        }
        .grid-overlay {
            background: linear-gradient(177.33deg, rgba(15, 15, 15, 0) 5.46%, rgba(0, 0, 0, 0.6006) 53.07%, rgba(0, 0, 0, 0.77) 93.86%);
            background-image: url('../../Resources/Images/HomePage/grid1.png');
        }
        .eclipse-glow {
            opacity: 0.8;
        }
        .hero-headline { color: #FFFFFF; }
        .hero-paragraph { color: rgba(255, 255, 255, 0.8); }
        .hero-cta-button {
            background-color: #FFFFFF;
            color: #101010;
        }
        .hero-cta-button:hover {
            box-shadow: 0 0.5vw 1.5vw rgba(255, 255, 255, 0.2);
        }
        .hero-keywords { color: rgba(255, 255, 255, 0.6); }
        .hero-keywords span:not(:last-child)::after { color: rgba(255, 255, 255, 0.4); }
    }

    /* --- Mobile Styles --- */
    @media (max-width: 768px) {
        .eclipse-glow { display: none; }
        .hero-section-container { min-height: 100vh; border-radius: 0; }
        .hero-content-wrapper { flex-direction: column; }
        .hero-image-section { display: none; }
        .hero-text-section {
            flex: 1;
            padding: 5vw;
            text-align: center;
            align-items: center;
            order: 2;
        }
        .hero-headline { font-size: 8vw; }
        .hero-paragraph { font-size: 4vw; max-width: 90vw; }
        .hero-cta-button { font-size: 4vw; padding: 3vw 6vw; }
        .hero-keywords { font-size: 3.5vw; justify-content: center; }
    }
</style>
    """

async def heroSection_script():
    return ""