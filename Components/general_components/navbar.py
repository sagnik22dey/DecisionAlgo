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
                link.classList.remove('active');
                if (link.getAttribute('href') === currentPage) {
                    link.classList.add('active');
                }
            });
        });
        
        // Hamburger menu toggle logic
        const hamburgerButton = document.getElementById('hamburger-button');
        const mainNav = document.getElementById('main-nav');

        hamburgerButton.addEventListener('click', () => {
            const isOpened = hamburgerButton.getAttribute('aria-expanded') === 'true';
            hamburgerButton.setAttribute('aria-expanded', !isOpened);
            mainNav.classList.toggle('is-active');
            hamburgerButton.classList.toggle('is-active');
            // Prevents the page from scrolling when the mobile menu is open
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
            --nav-panel-bg: #1a1a1a;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, sans-serif;
        }
        
        body.no-scroll {
            overflow: hidden;
        }

        /* --- SHARED & MOBILE-FIRST STYLES --- */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            z-index: 1000;
            background-color: var(--bg);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 2vh 4vw; /* Vertical padding scales with height, horizontal with width */
        }

        .brand {
            display: flex;
            width: 40vw; /* Larger logo on mobile */
            max-width: 200px; /* But don't let it get enormous */
            height: auto;
            z-index: 1001; /* Keeps logo above mobile nav panel */
        }
        
        .brand img {
            width: 100%;
            height: auto;
        }
        
        /* --- HAMBURGER MENU STYLES (Visible on Mobile by default) --- */
        .hamburger {
            display: block;
            cursor: pointer;
            padding: 1vh 1vw;
            border: none;
            background-color: transparent;
            z-index: 1001;
        }

        .hamburger-box {
            width: 8vw; /* Scales with screen width */
            max-width: 35px;
            height: 6vw; /* Scales with screen width */
            max-height: 28px;
            display: inline-block;
            position: relative;
        }

        .hamburger-inner, .hamburger-inner::before, .hamburger-inner::after {
            width: 100%;
            height: 0.5vh; /* Scales with screen height */
            max-height: 4px;
            background-color: var(--text);
            border-radius: 2vw;
            position: absolute;
            transition: transform 0.22s cubic-bezier(0.55, 0.055, 0.675, 0.19);
        }

        .hamburger-inner {
            display: block;
            top: 50%;
            transform: translateY(-50%);
        }
        .hamburger-inner::before, .hamburger-inner::after {
            content: "";
            display: block;
        }
        .hamburger-inner::before {
            top: -2.5vw; /* Scales with screen width */
            transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in;
        }
        .hamburger-inner::after {
            bottom: -2.5vw; /* Scales with screen width */
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
        
        /* --- MOBILE NAVIGATION PANEL --- */
        .nav {
            position: fixed;
            top: 0;
            right: 0;
            width: 75vw; /* Takes 75% of the screen width */
            height: 100vh;
            background-color: var(--nav-panel-bg);
            
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 5vh; /* Vertical gap scales with screen height */
            
            transform: translateX(100%); /* Hide off-screen */
            transition: transform var(--nav-timing) cubic-bezier(0.23, 1, 0.32, 1);
        }

        .nav.is-active {
            transform: translateX(0); /* Slide into view */
        }
        
        .nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: 800;
            white-space: nowrap;
            /* Using clamp for fluid typography: min size, preferred (fluid) size, max size */
            font-size: clamp(16px, 4.5vw, 22px); 

            /* Staggered animation setup */
            opacity: 0;
            transform: translateY(3vh);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        
        .nav a:hover {
            opacity: 0.85;
        }

        /* Staggered animation for nav items when menu opens */
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
        
        /* --- DESKTOP STYLES (Applied on screens wider than 992px) --- */
        @media (min-width: 993px) {
            .navbar {
                padding: 1.5vh 2.5vw;
            }

            .brand {
                width: 18vw; /* Adjust logo size for desktop */
                max-width: 360px;
            }

            .hamburger {
                display: none; /* Hide hamburger on desktop */
            }

            /* Revert nav to a horizontal layout for desktop */
            .nav {
                position: static;
                width: auto;
                height: auto;
                background-color: transparent;
                flex-direction: row;
                justify-content: flex-end;
                gap: 2vw; /* Horizontal gap for desktop */
                transform: none; /* Remove slide-in effect */
                transition: none;
            }

            .nav a {
                opacity: 1;
                transform: none;
                transition: opacity 0.2s ease;
                font-size: clamp(16px, 1.1vw, 22px);
            }
        }
    </style>
    """