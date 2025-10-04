async def companies_body():
    return """
    <div class="companies-section">
        <div class="companies-logo-bar">
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/6.png" alt="ChainAware.ai Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/6_l.png" alt="ChainAware.ai Logo">
            </div>
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/7.png" alt="Ferratec Technica Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/7_l.png" alt="Ferratec Technica Logo">
            </div>
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/8.png" alt="Zapnow Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/8_l.png" alt="Zapnow Logo">
            </div>
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/9.png" alt="Edelweiss Connect Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/9_l.png" alt="Edelweiss Connect Logo">
            </div>
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/10.png" alt="Money Lion Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/10_l.png" alt="Money Lion Logo">
            </div>
            <div class="company-logo">
                <img class="logo-dark" src="../../Resources/Images/AboutUs/11.png" alt="SmartCredit.io Logo">
                <img class="logo-light" src="../../Resources/Images/AboutUs/11_l.png" alt="SmartCredit.io Logo">
            </div>
        </div>
    </div>
    """


async def companies_style():
    return """
    <style>
        /* --- Structural & Theme-Agnostic Styles --- */
        .companies-section {
            padding: 5vh 0;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .companies-section::before,
        .companies-section::after {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 85vw;
            height: 0.1vh;
        }

        .companies-section::before { top: 0; }
        .companies-section::after { bottom: 0; }

        .companies-logo-bar {
            display: flex;
            align-items: center;
            justify-content: space-around;
            width: 85vw;
            gap: 2vw;
            transition: all 0.3s ease-in-out;
        }

        .company-logo {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: all 0.3s ease-in-out;
        }

        .company-logo img {
            max-width: 100%;
            max-height: 18vh;
            width: 20vw;
            object-fit: contain;
            
            opacity: 1;
            transition: opacity 0.3s ease, transform 0.3s ease;
        }

        .company-logo img:hover {
            opacity: 1;
            transform: scale(1.1);
        }

        /* --- Theming Section --- */

        

        @media (prefers-color-scheme: light) {
            .companies-section {
                background-color: #FFFFFF;
            }
            .companies-section::before,
            .companies-section::after {
                display: none;
            }
            /* Default (Light Theme) */
            .logo-dark {
                display: none;
            }
            .logo-light {
                display: block;
                filter: grayscale(100%) brightness(100%);
                opacity: 1;
            }
        }

        /* Dark Theme */
        @media (prefers-color-scheme: dark) {
            .companies-section {
                background-color: transparent;
            }
            .companies-section::before,
            .companies-section::after {
                background-color: rgba(255, 255, 255, 0.1);
                display: block;
            }
            .logo-light {
                display: none;
            }
            .logo-dark {
                display: block;
                filter: none;
                opacity: 1;
                filter: grayscale(1) brightness(5);
            }
        }

        /* --- Responsive Structural Adjustments --- */
        @media (max-width: 768px) {
            .companies-section {
                padding: 8vh 0;
            }
            .companies-logo-bar {
                flex-wrap: wrap;
                justify-content: center;
                width: 90vw;
                gap: 5vh 5vw;
            }
            .company-logo {
                flex: 1 0 35%;
                padding: 0 2vw;
                min-width: 35%;
                transform: scale(1.2); /* Scaled up for better visibility */
            }
            .company-logo img {
                max-height: 12vh;
                width: auto;
                max-width: 80%;
            }
            .company-logo img:hover {
                transform: scale(1.05); /* Adjusted hover scale for mobile */
            }
        }

        @media (max-width: 1024px) and (min-width: 769px) { /* Tablet */
            .companies-logo-bar {
                gap: 1.5vw;
                width: 90vw;
            }
            .company-logo img {
                max-height: 16vh;
                width: 18vw;
            }
        }
    </style>
    """
