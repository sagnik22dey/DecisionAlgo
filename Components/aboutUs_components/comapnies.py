async def companies_body():
    return """
    <div class="companies-section">
        <div class="companies-logo-bar">
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/6.png" alt="ChainAware.ai Logo">
            </div>
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/7.png" alt="Ferratec Technica Logo">
            </div>
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/8.png" alt="Zapnow Logo">
            </div>
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/9.png" alt="Edelweiss Connect Logo">
            </div>
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/10.png" alt="Money Lion Logo">
            </div>
            <div class="company-logo">
                <img src="../../Resources/Images/AboutUs/11.png" alt="SmartCredit.io Logo">
            </div>
        </div>
    </div>

    <script>
        function optimizeCompaniesLayout() {
            const isMobile = window.innerWidth <= 768;
            const logoBar = document.querySelector('.companies-logo-bar');
            const logos = document.querySelectorAll('.company-logo');

            if (isMobile) {
                // Apply mobile-specific styles
                logoBar.style.flexWrap = 'wrap';
                logoBar.style.justifyContent = 'center';
                logoBar.style.gap = '5vh 5vw';
                logoBar.style.width = '90vw';

                logos.forEach(logo => {
                    logo.style.flex = '1 0 35%'; // Creates a two-column layout
                    logo.style.padding = '0 2vw';
                });

            } else {
                // Revert to desktop styles
                logoBar.style.flexWrap = 'nowrap';
                logoBar.style.justifyContent = 'space-around';
                logoBar.style.gap = '2vw';
                logoBar.style.width = '100vw';

                logos.forEach(logo => {
                    logo.style.flex = '1';
                    logo.style.padding = '0';
                });
            }
        }

        // Run the optimization function on load and resize
        window.addEventListener('load', optimizeCompaniesLayout);
        window.addEventListener('resize', optimizeCompaniesLayout);
    </script>
    """


async def companies_style():
    return """
    <style>
        .companies-section {
            background-color: transparent;
            padding: 5vh 0;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Top and Bottom border lines */
        .companies-section::before,
        .companies-section::after {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 85vw;
            height: 0.1vh;
            background-color: rgba(255, 255, 255, 0.1);
        }

        .companies-section::before {
            top: 0;
        }

        .companies-section::after {
            bottom: 0;
        }

        .companies-logo-bar {
            display: flex;
            align-items: center;
            justify-content: space-around; /* Default for desktop */
            width: 85vw; /* Default for desktop */
            gap: 2vw; /* Default for desktop */
            transition: all 0.3s ease-in-out;
        }

        .company-logo {
            flex: 1; /* Default for desktop */
            display: flex;
            justify-content: center;
            align-items: center;
            transition: all 0.3s ease-in-out;
        }

        .company-logo img {
            max-width: 100%;
            max-height: 18vh; /* Controls the vertical size of logos */
            width: 20rem;
            object-fit: contain;
            filter: grayscale(1) brightness(5); /* Ensures logos are white and bright */
            opacity: 0.8;
            transition: opacity 0.3s ease, transform 0.3s ease;
        }

        .company-logo img:hover {
            opacity: 1;
            transform: scale(1.1);
        }
    </style>
    """
