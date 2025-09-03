async def navbar_body():
    return """
    <header class="navbar" role="navigation" aria-label="Main">
        <a href="/" class="brand">
            <img src="/Resources/Images/HomePage/DecisionAlgoLogo.png" alt="DecisionAlgo logo" />
        </a>
        <nav class="nav" id="main-nav">
            <a href="/">Home</a>
            <a href="/dashboard">Dashboards</a>
            <a href="#">Case Studies</a>
            <a href="#">About us</a>
            <a href="#">Pricing</a>
            <a href="#">Contact Us</a>
        </nav>
        <button class="hamburger" id="hamburger-button" aria-label="Open menu" aria-controls="main-nav" aria-expanded="false">
            <span class="hamburger-box">
                <span class="hamburger-inner"></span>
            </span>
        </button>
    </header>
    
    <script>
        // Set active class based on current page
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.nav a');
            const currentPage = window.location.pathname;
            
            navLinks.forEach(link => {
                // Remove any existing active classes
                link.classList.remove('active');
                
                // Add active class to the current page link
                if (link.getAttribute('href') === currentPage) {
                    link.classList.add('active');
                }
                
                // Special case for home page
                if (currentPage === '/' && link.getAttribute('href') === '/') {
                    link.classList.add('active');
                }
            });
        });
        
        const hamburgerButton = document.getElementById('hamburger-button');
        const mainNav = document.getElementById('main-nav');

        hamburgerButton.addEventListener('click', () => {
            const isOpened = hamburgerButton.getAttribute('aria-expanded') === 'true';
            hamburgerButton.setAttribute('aria-expanded', !isOpened);
            mainNav.classList.toggle('is-active');
            hamburgerButton.classList.toggle('is-active');
            // Prevents the page from scrolling when the menu is open
            document.body.classList.toggle('no-scroll');
        });
    </script>
    """

async def navbar_style():
    return """
    <style>
        :root {
            --bg: #111;
            --text: #ffffff;
            --brand: #7ec5f4;
            --nav-timing: 400ms;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            background: var(--bg);
            color: var(--text);
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, sans-serif;
        }
        
        body.no-scroll {
            overflow: hidden;
        }

        /* --- DESKTOP STYLES (Preserved Original Design) --- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background-color: #111;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            padding: 20px 30px;
        }

        .brand {
            display: flex;
            width: 357px;
            height: auto;
            border-radius: 8px;
            z-index: 1001; /* Keeps logo above mobile nav panel */
        }
        
        .brand img {
            width: 100%;
            height: auto;
        }
        
        .nav {
            margin-left: 30px;
            display: flex;
            align-items: center;
            gap: 32px;
            font-size: 20px;
        }

        .nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: 800;
            white-space: nowrap;
        }

        .nav a:last-child {
            padding-right: 20px;
        }

        .nav a:hover {
            opacity: 0.85;
        }

        .nav a.active {
            position: relative;
        }

        .nav a.active::after {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: -6px;
            height: 3px;
            background: var(--text);
            border-radius: 2px;
        }

        /* --- HAMBURGER MENU (Hidden on Desktop) --- */
        .hamburger {
            display: none;
            cursor: pointer;
            padding: 10px;
            margin: -10px; /* Offset padding to maintain alignment */
            border: none;
            background-color: transparent;
            z-index: 1001;
        }

        .hamburger-box {
            width: 30px;
            height: 24px;
            display: inline-block;
            position: relative;
        }

        .hamburger-inner, .hamburger-inner::before, .hamburger-inner::after {
            width: 30px;
            height: 3px;
            background-color: var(--text);
            border-radius: 4px;
            position: absolute;
            transition: transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19);
        }

        .hamburger-inner {
            display: block;
            top: 50%;
            margin-top: -1.5px;
        }
        .hamburger-inner::before, .hamburger-inner::after {
            content: "";
            display: block;
        }
        .hamburger-inner::before {
            top: -10px;
            transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in;
        }
        .hamburger-inner::after {
            bottom: -10px;
            transition: bottom 0.1s 0.25s ease-in, transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19);
        }

        /* Hamburger active state ('X') animation */
        .hamburger.is-active .hamburger-inner {
            transform: rotate(225deg);
            transition-delay: 0.12s;
            transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
        }
        .hamburger.is-active .hamburger-inner::before {
            top: 0;
            opacity: 0;
            transition: top 0.1s ease-out, opacity 0.1s 0.12s ease-out;
        }
        .hamburger.is-active .hamburger-inner::after {
            bottom: 0;
            transform: rotate(-90deg);
            transition: bottom 0.1s ease-out, transform 0.22s 0.12s cubic-bezier(0.215, 0.61, 0.355, 1);
        }

        /* --- MOBILE & TABLET STYLES --- */
        @media (max-width: 992px) {
            .navbar {
                padding: 15px 20px;
            }

            .brand {
                width: 200px; /* Resized logo for smaller screens */
            }
            
            .hamburger {
                display: block; /* Show the hamburger */
            }

            /* Mobile Navigation Panel */
            .nav {
                position: fixed;
                top: 0;
                right: 0;
                width: min(75vw, 400px); /* Responsive width */
                height: 100vh;
                background-color: #1a1a1a;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                gap: 40px;
                font-size: 18px;
                transform: translateX(100%); /* Hide off-screen */
                transition: transform var(--nav-timing) cubic-bezier(0.23, 1, 0.32, 1);
                margin-left: 0;
            }

            .nav.is-active {
                transform: translateX(0); /* Slide into view */
            }

            /* Staggered animation for nav items */
            .nav a {
                opacity: 0;
                transform: translateY(20px);
                transition: opacity 0.3s ease, transform 0.3s ease;
            }
            .nav.is-active a {
                opacity: 1;
                transform: translateY(0);
            }
            .nav.is-active a:nth-child(1) { transition-delay: calc(var(--nav-timing) * 0.5); }
            .nav.is-active a:nth-child(2) { transition-delay: calc(var(--nav-timing) * 0.6); }
            .nav.is-active a:nth-child(3) { transition-delay: calc(var(--nav-timing) * 0.7); }
            .nav.is-active a:nth-child(4) { transition-delay: calc(var(--nav-timing) * 0.8); }
            .nav.is-active a:nth-child(5) { transition-delay: calc(var(--nav-timing) * 0.9); }
            .nav.is-active a:nth-child(6) { transition-delay: calc(var(--nav-timing) * 1.0); }

            .nav a:last-child {
                padding-right: 0;
            }
        }
        
        /* Further adjustments for small mobile screens */
        @media (max-width: 480px) {
            .navbar {
                padding: 10px 15px;
            }
            .brand {
                width: 160px;
            }
        }
    </style>
    """