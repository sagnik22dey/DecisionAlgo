async def robot_body():
    return """
    <div class="page-wrapper">
        <div class="main-container"></div>

        <div class="heading-container">
            <h1>What We Offer</h1>
            <h2>Smarter, Faster, Automated</h2>
        </div>

        <!-- DESKTOP VERSION -->
        <div class="content-wrapper desktop-view" id="desktop-content">
            <!-- Desktop Connectors -->
            <svg id="vector-1" class="connector-vector" width="7.03vw" height="8.59vh" viewBox="0 0 135 82" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M133 8H134.5V6.5H133V8ZM16 8C16 3.58173 12.4183 0 8 0C3.58173 0 0 3.58173 0 8C0 12.4183 3.58173 16 8 16C12.4183 16 16 12.4183 16 8ZM133 82H134.5V8H133H131.5V82H133ZM133 8V6.5H8V8V9.5H133V8Z" fill="#818181" fill-opacity="0.43"/>
            </svg>

            <svg id="vector-2" class="connector-vector" width="5.95vw" height="2.48vh" viewBox="0 0 95 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M93 8H94.5V6.5H93V8ZM16 8C16 3.58172 12.4183 0 7.99999 0C3.58172 0 -7.62939e-06 3.58172 -7.62939e-06 8C-7.62939e-06 12.4183 3.58172 16 7.99999 16C12.4183 16 16 12.4183 16 8ZM93 10H94.5V8H93H91.5V10H93ZM93 8V6.5H7.99999V8V9.5H93V8Z" fill="#818181" fill-opacity="0.43"/>
            </svg>

            <svg id="vector-3" class="connector-vector" width="6.25vw" height="9.59vh" viewBox="0 0 120 82" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 8H0.5V6.5H2V8ZM104 8C104 3.58173 107.582 0 112 0C116.418 0 120 3.58173 120 8C120 12.4183 116.418 16 112 16C107.582 16 104 12.4183 104 8ZM2 82H0.5V8H2H3.5V82H2ZM2 8V6.5H112V8V9.5H2V8Z" fill="#818181" fill-opacity="0.43"/>
            </svg>

            <svg id="vector-4" class="connector-vector" width="8.18vw" height="2.48vh" viewBox="0 0 157 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2 8H0.5V6.5H2V8ZM141 8C141 3.58172 144.582 0 149 0C153.418 0 157 3.58172 157 8C157 12.4183 153.418 16 149 16C144.582 16 141 12.4183 141 8ZM2 10H0.5V8H2H3.5V10H2ZM2 8V6.5H149V8V9.5H2V8Z" fill="#818181" fill-opacity="0.43"/>
            </svg>

            <!-- Desktop Feature Cards -->
            <div id="feature-box-1" class="feature-box desktop-card">
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                    </div>
                    <h3>Real-Time Dashboards</h3>
                </div>
                <div class="feature-content">
                    <p>Ditch The Spreadsheets! Visualize Key Business Metrics In A Single, Dynamic Dashboard That Updates In Real-Time.</p>
                    <a href="#" class="show-detail-link">
                        <span>Show Detail</span>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </a>
                </div>
            </div>

            <div id="feature-box-2" class="feature-box desktop-card">
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                    </div>
                    <h3>AI-Powered Chatbots</h3>
                </div>
                <div class="feature-content">
                    <p>Automate Customer Engagement And Streamline Workflows With Intelligent Chatbots Tailored To Your Needs.</p>
                    <a href="#" class="show-detail-link">
                        <span>Show Detail</span>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </a>
                </div>
            </div>

            <!-- Desktop Robot -->
            <img id="robot-image" class="desktop-robot" src="../../Resources/Images/HomePage/robotHomepage.png" alt="A sleek black robot with red highlights, symbolizing advanced automation and AI.">

            <div id="feature-box-3" class="feature-box desktop-card">
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                    </div>
                    <h3>Data-Driven Reports</h3>
                </div>
                <div class="feature-content">
                    <p>No More Manual Reporting-Get Automated Insights Delivered Weekly & Monthly To Make Informed Decisions Faster.</p>
                    <a href="#" class="show-detail-link">
                        <span>Show Detail</span>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </a>
                </div>
            </div>

            <div id="feature-box-4" class="feature-box desktop-card">
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                    </div>
                    <h3>Smart Outsourcing Solutions</h3>
                </div>
                <div class="feature-content">
                    <p>Scale Your Business Effortlessly By Delegating Time-Consuming Data Processes To Our Expert Team</p>
                    <a href="#" class="show-detail-link">
                        <span>Show Detail</span>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </a>
                </div>
            </div>
        </div>

        <!-- MOBILE VERSION -->
        <div class="content-wrapper mobile-view" id="mobile-content" style="display: none;">
            <div class="features-grid">
                <div class="feature-box mobile-card">
                    <div class="feature-header">
                        <div class="feature-icon">
                            <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                        </div>
                        <h3>Real-Time Dashboards</h3>
                    </div>
                    <div class="feature-content">
                        <p>Ditch The Spreadsheets! Visualize Key Business Metrics In A Single, Dynamic Dashboard That Updates In Real-Time.</p>
                        <a href="#" class="show-detail-link">
                            <span>Show Detail</span>
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                        </a>
                    </div>
                </div>

                <div class="feature-box mobile-card">
                    <div class="feature-header">
                        <div class="feature-icon">
                            <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                        </div>
                        <h3>AI-Powered Chatbots</h3>
                    </div>
                    <div class="feature-content">
                        <p>Automate Customer Engagement And Streamline Workflows With Intelligent Chatbots Tailored To Your Needs.</p>
                        <a href="#" class="show-detail-link">
                            <span>Show Detail</span>
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                        </a>
                    </div>
                </div>

                <!-- Mobile Robot -->
                <div class="robot-container">
                    <img class="mobile-robot" src="../../Resources/Images/HomePage/robotHomepage.png" alt="A sleek black robot with red highlights, symbolizing advanced automation and AI.">
                </div>

                <div class="feature-box mobile-card">
                    <div class="feature-header">
                        <div class="feature-icon">
                            <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                        </div>
                        <h3>Data-Driven Reports</h3>
                    </div>
                    <div class="feature-content">
                        <p>No More Manual Reporting-Get Automated Insights Delivered Weekly & Monthly To Make Informed Decisions Faster.</p>
                        <a href="#" class="show-detail-link">
                            <span>Show Detail</span>
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                        </a>
                    </div>
                </div>

                <div class="feature-box mobile-card">
                    <div class="feature-header">
                        <div class="feature-icon">
                            <img src="../../Resources/Images/HomePage/route.png" alt="route icon">
                        </div>
                        <h3>Smart Outsourcing Solutions</h3>
                    </div>
                    <div class="feature-content">
                        <p>Scale Your Business Effortlessly By Delegating Time-Consuming Data Processes To Our Expert Team</p>
                        <a href="#" class="show-detail-link">
                            <span>Show Detail</span>
                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L18 6M18 6H9M18 6V15" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
async def robot_style():
    return """
    <style>
        /* ============================================================= */
        /* BASE STYLES                                                   */
        /* ============================================================= */
        
        :root {
            --card-w: 20.83vw;
            --card-h: 27.78vh;
            --cards-gap: 2.08vw;
            --canvas-h: 74.07vh;
            --blue: #25A6E9;
            --ink: #EBF0F3;
            --glass-bg: rgba(255,255,255,0.06);
            --glass-brd: rgba(255, 255, 255, 0.2);
            --ink-70: rgba(255,255,255,0.7);
        }

        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            background: #000;
            font-family: 'Exo 2', 'Poppins', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            overflow-x: hidden;
        }

        .page-wrapper {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 1.45%, rgba(48, 48, 48, 0.08) 28.37%, #000000 100%);
            padding: 8.89vh 1.67vw 5.93vh;
            border-radius: 4.43vw;
            overflow: hidden;
        }

        /* Backdrop Effects */
        .main-container {
            position: absolute;
            inset: 0;
            overflow: hidden;
        }

        .main-container::before {
            content: "";
            position: absolute;
            left: 50%;
            top: 54%;
            width: 57.29vw;
            height: 57.29vw;
            transform: translate(-50%, -50%);
            background: radial-gradient(50% 50% at 50% 50%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.02) 45%, rgba(0,0,0,0.00) 70%);
            filter: blur(0.1vw);
            pointer-events: none;
        }

        .main-container::after {
            content: "";
            position: absolute;
            width: 64.53vw;
            height: 60.46vh;
            left: 40%;
            top: 42%;
            transform: translateX(-30%);
            background: #FFFFFF;
            opacity: 0.21;
            filter: blur(25.42vw);
        }

        /* Headings */
        .heading-container {
            position: relative;
            width: 100%;
            max-width: 52.08vw;
            text-align: center;
            letter-spacing: -0.02em;
            z-index: 20;
            margin-bottom: 1.85vh;
        }

        .heading-container h1 {
            font-weight: 700;
            font-size: 2.92vw;
            line-height: 1.1;
            margin: 0 0 0.74vh 0;
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.4) 0.22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, 0.8) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }

        .heading-container h2 {
            font-weight: 700;
            font-size: 2.92vw;
            line-height: 1.1;
            margin: 0;
            color: var(--blue);
        }

        /* ============================================================= */
        /* DESKTOP VIEW (ORIGINAL - UNCHANGED VALUES)                    */
        /* ============================================================= */
        
        .desktop-view {
            position: relative;
            width: 100%;
            max-width: 83.33vw;
            height: var(--canvas-h);
            margin-top: 7.41vh;
        }

        /* Desktop Connectors */
        .connector-vector {
            position: absolute;
            pointer-events: none;
            z-index: 15;
            opacity: 0.6;
        }

        #vector-1 { left: 38%; top: 3%; }
        #vector-2 { left: 32%; bottom: 47%; }
        #vector-3 { right: 32%; top: -1%; }
        #vector-4 { right: 32%; top: 58%; }

        /* Desktop Robot */
        .desktop-robot {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 39.25vw;
            height: 65.81vh;
            object-fit: contain;
            z-index: 10;
            filter: drop-shadow(0 1.85vh 3.125vw rgba(0,0,0,0.6));
        }

        /* Desktop Feature Cards */
        .desktop-card {
            position: absolute;
            width: var(--card-w);
            height: var(--card-h);
            z-index: 20;
            border: 0.05vw solid var(--glass-brd);
            border-radius: 0.625vw;
            padding: 2.96vh 1.46vw;
            background: var(--glass-bg);
            backdrop-filter: blur(0.52vw) saturate(120%);
            -webkit-backdrop-filter: blur(0.52vw) saturate(120%);
            box-shadow: 0 0.74vh 1.67vw rgba(0,0,0,0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .desktop-card:hover {
            transform: translateY(-0.37vh);
            box-shadow: 0 1.11vh 2.08vw rgba(0,0,0,0.4);
        }

        #feature-box-1 { top: -3%; left: 13%; }
        #feature-box-2 { bottom: 15%; left: 7%; }
        #feature-box-3 { top: -3%; right: 7%; }
        #feature-box-4 { bottom: 10%; right: 7%; }

        .feature-header {
            display: flex;
            align-items: center;
            gap: 1.04vw;
            margin-bottom: 2.96vh;
        }

        .feature-icon {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 2.6vw;
            height: 2.6vw;
            background: linear-gradient(135deg, #0A1015 0%, #1a1f25 100%);
            border: 0.05vw solid #3A4046;
            border-radius: 0.42vw;
            flex-shrink: 0;
        }

        .feature-icon img {
            width: 1.46vw;
            height: 1.46vw;
        }

        .desktop-card h3 {
            font-weight: 600;
            font-size: 1.15vw;
            line-height: 1.3;
            color: #FFFFFF;
            margin: 0;
        }

        .feature-content {
            display: flex;
            flex-direction: column;
            gap: 1.04vw;
        }

        .desktop-card .feature-content p {
            font-weight: 400;
            font-size: 0.78vw;
            line-height: 1.5;
            color: rgba(255,255,255,0.8);
            margin: 0;
        }

        .desktop-card .show-detail-link {
            display: flex;
            align-items: center;
            gap: 0.42vw;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.83vw;
            line-height: 1.5;
            color: #FFFFFF;
            transition: opacity .2s ease, transform .2s ease;
            opacity: 0.9;
        }

        .desktop-card .show-detail-link:hover {
            opacity: 1; 
            transform: translateY(-0.09vh);
        }

        .desktop-card .show-detail-link svg {
            width: 1.04vw;
            height: 1.04vw;
            transition: transform 0.2s ease;
        }

        .desktop-card .show-detail-link:hover svg {
            transform: translateX(0.1vw);
        }

        /* ============================================================= */
        /* MOBILE VIEW                                                   */
        /* ============================================================= */
        
        .mobile-view {
            position: static;
            height: auto;
            margin-top: 4vh;
            max-width: 100%;
            width: 100%;
        }

        .features-grid {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6vh;
            position: static;
            height: auto;
        }

        /* Mobile Robot */
        .robot-container {
            display: flex;
            justify-content: center;
            margin: 4vh 0;
        }

        .mobile-robot {
            width: 75vw;
            height: auto;
            max-height: 45vh;
            object-fit: contain;
            filter: drop-shadow(0 2vh 4vw rgba(0,0,0,0.8));
        }

        /* Mobile Feature Cards */
        .mobile-card {
            width: 88vw;
            padding: 6vw;
            border-radius: 3vw;
            border: 0.3vw solid var(--glass-brd);
            background: var(--glass-bg);
            backdrop-filter: blur(2vw) saturate(130%);
            -webkit-backdrop-filter: blur(2vw) saturate(130%);
            box-shadow: 0 2vh 4vw rgba(0,0,0,0.4);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .mobile-card:hover {
            transform: translateY(-1vh);
            box-shadow: 0 3vh 6vw rgba(0,0,0,0.5);
        }

        .mobile-card .feature-header {
            gap: 4vw;
            margin-bottom: 4vh;
        }

        .mobile-card .feature-icon {
            width: 10vw;
            height: 10vw;
            border-radius: 2.5vw;
            border: 0.3vw solid #3A4046;
        }

        .mobile-card .feature-icon img {
            width: 5.5vw;
            height: 5.5vw;
        }

        .mobile-card h3 {
            font-size: 4.5vw;
            line-height: 1.25;
            font-weight: 600;
            color: #FFFFFF;
            margin: 0;
        }

        .mobile-card .feature-content {
            gap: 3vh;
        }

        .mobile-card .feature-content p {
            font-size: 3.8vw;
            line-height: 1.6;
            color: rgba(255,255,255,0.85);
            margin: 0;
        }

        .mobile-card .show-detail-link {
            display: flex;
            align-items: center;
            font-size: 4vw;
            gap: 2vw;
            padding: 1vh 0;
            text-decoration: none;
            font-weight: 500;
            color: #FFFFFF;
            transition: opacity .2s ease, transform .2s ease;
            opacity: 0.9;
        }

        .mobile-card .show-detail-link svg {
            width: 4.5vw;
            height: 4.5vw;
            transition: transform 0.2s ease;
        }

        .mobile-card .show-detail-link:hover {
            transform: translateY(-0.5vh);
            opacity: 1;
        }

        .mobile-card .show-detail-link:hover svg {
            transform: translateX(0.5vw);
        }

        /* Desktop Scaling Adjustments (unchanged) */
        @media (max-width: 90vw) and (min-width: 48.01vw) {
            .desktop-view { max-width: 67.71vw; }
            :root { --card-w: 19.79vw; --card-h: 25.93vh; }
        }

        @media (max-width: 75vw) and (min-width: 48.01vw) {
            .heading-container h1, .heading-container h2 { font-size: 2.5vw; }
            .desktop-view { max-width: 57.29vw; margin-top: 5.56vh; }
            :root { --card-w: 18.75vw; --card-h: 24.07vh; }
        }
    </style>
    """
async def robot_script():
    return """
    <script>
        // Responsive Layout Controller
        class ResponsiveController {
            constructor() {
                this.currentView = null;
                this.breakpoint = 48;
                this.init();
            }

            init() {
                // Set initial view based on screen size
                this.updateView();
                
                // Listen for window resize events
                window.addEventListener('resize', () => {
                    this.handleResize();
                });

                // Listen for orientation changes on mobile devices
                window.addEventListener('orientationchange', () => {
                    setTimeout(() => {
                        this.updateView();
                    }, 100);
                });
            }

            handleResize() {
                // Debounce resize events to prevent excessive calls
                clearTimeout(this.resizeTimeout);
                this.resizeTimeout = setTimeout(() => {
                    this.updateView();
                }, 150);
            }

            updateView() {
                const screenWidth = window.innerWidth;
                const isMobile = screenWidth <= this.breakpoint;
                
                // Only update if the view actually needs to change
                if ((isMobile && this.currentView !== 'mobile') || 
                    (!isMobile && this.currentView !== 'desktop')) {
                    
                    this.toggleView(isMobile);
                }
            }

            toggleView(showMobile) {
                const desktopContent = document.getElementById('desktop-content');
                const mobileContent = document.getElementById('mobile-content');

                if (!desktopContent || !mobileContent) {
                    console.warn('Content containers not found');
                    return;
                }

                if (showMobile) {
                    // Show mobile, hide desktop
                    desktopContent.style.display = 'none';
                    mobileContent.style.display = 'block';
                    this.currentView = 'mobile';
                    
                    // Update page wrapper for mobile
                    this.updatePageWrapper('mobile');
                } else {
                    // Show desktop, hide mobile
                    desktopContent.style.display = 'block';
                    mobileContent.style.display = 'none';
                    this.currentView = 'desktop';
                    
                    // Update page wrapper for desktop
                    this.updatePageWrapper('desktop');
                }

                // Trigger custom event for other scripts that might need to know about the change
                window.dispatchEvent(new CustomEvent('viewChanged', {
                    detail: { view: this.currentView }
                }));
            }

            updatePageWrapper(view) {
                const pageWrapper = document.querySelector('.page-wrapper');
                const headingContainer = document.querySelector('.heading-container');
                
                if (view === 'mobile') {
                    // Apply mobile-specific styles
                    pageWrapper.style.padding = '8vh 4vw 6vh';
                    pageWrapper.style.borderRadius = '0';
                    headingContainer.style.maxWidth = '92vw';
                    headingContainer.style.marginBottom = '6vh';
                    
                    // Update heading font sizes for mobile
                    const h1 = headingContainer.querySelector('h1');
                    const h2 = headingContainer.querySelector('h2');
                    if (h1) h1.style.fontSize = '8.5vw';
                    if (h2) h2.style.fontSize = '8.5vw';
                    
                } else {
                    // Reset to desktop styles
                    pageWrapper.style.padding = '8.89vh 1.67vw 5.93vh';
                    pageWrapper.style.borderRadius = '4.43vw';
                    headingContainer.style.maxWidth = '52.08vw';
                    headingContainer.style.marginBottom = '1.85vh';
                    
                    // Reset heading font sizes for desktop
                    const h1 = headingContainer.querySelector('h1');
                    const h2 = headingContainer.querySelector('h2');
                    if (h1) h1.style.fontSize = '2.92vw';
                    if (h2) h2.style.fontSize = '2.92vw';
                }
            }

            // Public method to manually force a view change (for testing/debugging)
            forceView(viewType) {
                if (viewType === 'mobile' || viewType === 'desktop') {
                    this.toggleView(viewType === 'mobile');
                }
            }

            // Get current view state
            getCurrentView() {
                return this.currentView;
            }
        }

        // Initialize the responsive controller when DOM is loaded
        document.addEventListener('DOMContentLoaded', () => {
            window.responsiveController = new ResponsiveController();
        });

        // Fallback initialization if DOMContentLoaded has already fired
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                window.responsiveController = new ResponsiveController();
            });
        } else {
            window.responsiveController = new ResponsiveController();
        }
    </script>
    """
