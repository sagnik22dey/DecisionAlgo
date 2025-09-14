async def navbar_body():
    return """
    <header class="navbar" role="navigation" aria-label="Main">
        <a href="/" class="brand">
            <img src="/Resources/Images/HomePage/DecisionAlgoLogo.png" alt="DecisionAlgo logo" />
        </a>
        <nav class="nav" id="main-nav">
            <a href="/">Home</a>
            <a href="/dashboard">Dashboards</a>
            <div class="nav-item dropdown">
               <a class="nav-link" id="case-studies-link">Case Studies</a>
               <div class="dropdown-menu">
                   <a href="/casestudy/customer_package_goods">Customer Packaged Goods</a>
                   <a href="/casestudy/retail_firm">Retail Firm Adapting to AI Era</a>
                   <a href="/casestudy/finance">Finance</a>
                   <a href="/casestudy/insurance">Insurance</a>
                   <a href="/casestudy/tech_media_telecom">Tech, Media & Telecom</a>
                   <a href="/casestudy/healthcare">Healthcare</a>
               </div>
           </div>
            <a href="/aboutus">About us</a>
            <a href="/pricing">Pricing</a>
            <a href="/contactus">Contact Us</a>
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
            const navLinks = document.querySelectorAll('.nav > a, .nav .dropdown-menu a');
            const currentPage = window.location.pathname;
            const caseStudiesDropdown = document.querySelector('.nav-item.dropdown');
            const caseStudiesLink = document.getElementById('case-studies-link');

            let isCaseStudyPage = false;
            
            // Handle active classes for all nav links
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === currentPage) {
                    link.classList.add('active');
                    if (link.closest('.dropdown-menu')) {
                        isCaseStudyPage = true;
                    }
                }
            });

            // Add active class to "Case Studies" if on a case study page
            if (isCaseStudyPage && caseStudiesLink) {
                caseStudiesLink.classList.add('active');
            }

            // Mobile dropdown toggle
            if (caseStudiesDropdown && window.innerWidth < 993) {
                caseStudiesLink.addEventListener('click', function(e) {
                    e.preventDefault();
                    caseStudiesDropdown.classList.toggle('is-open');
                });
            }
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
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@700&display=swap');

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
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, sans-serif,Exo 2;
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
            padding: 2vh 4vw; /* Zoom-safe padding */
            font-family: 'Poppins', sans-serif; 
            font-weight: 600;
        }

        .brand {
            display: flex;
            width: 40vw; /* Zoom-safe width for mobile */
            max-width: 40vw;
            height: auto;
            z-index: 0;
        }
        
        .brand img {
            width: 100%;
            height: auto;
        }
        
        /* --- HAMBURGER MENU STYLES (Visible on Mobile by default) --- */
        .hamburger {
            display: block;
            cursor: pointer;
            padding: 1vh 1vw; /* Zoom-safe padding */
            border: none;
            background-color: transparent;
            z-index: 1001;
        }

        .hamburger-box {
            width: 8vw; /* Zoom-safe width */
            max-width: 8vw;
            height: 6vw; /* Zoom-safe height */
            max-height: 6vw;
            display: inline-block;
            position: relative;
        }

        .hamburger-inner, .hamburger-inner::before, .hamburger-inner::after {
            width: 100%;
            height: 0.5vh; /* Zoom-safe height */
            background-color: var(--text);
            border-radius: 1vw;
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
            top: -2.5vw; /* Zoom-safe spacing */
            transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in;
        }
        .hamburger-inner::after {
            bottom: -2.5vw; /* Zoom-safe spacing */
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
            width: 75vw; /* Zoom-safe width */
            height: 100vh;
            background-color: var(--nav-panel-bg);
            
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 5vh; /* Zoom-safe gap */
            
            transform: translateX(100%);
            transition: transform var(--nav-timing) cubic-bezier(0.23, 1, 0.32, 1);
        }

        .nav.is-active {
            transform: translateX(0);
        }
        
        .nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: 800;
            white-space: nowrap;
            font-size: 4.5vw; /* Zoom-safe font size for mobile */
            position: relative;

            /* Staggered animation setup */
            opacity: 0;
            transform: translateY(3vh); /* Zoom-safe transform */
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

        /* --- SHARED DROPDOWN STYLES --- */
        .nav-item.dropdown {
            position: relative;
        }

        .dropdown-menu {
            display: none;
            background-color: var(--nav-panel-bg);
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 4px;
        }

        .dropdown-menu a {
            text-decoration: none;
            display: block;
            white-space: normal;
            position: relative;
        }

        .dropdown-menu a:hover {
            background-color: #575757;
            opacity: 1;
        }
        
        /* --- DESKTOP STYLES (min-width: 993px) --- */
        @media (min-width: 993px) {
            .navbar {
                padding: 1.5vw 2vw;
            }

            .brand {
                width: 12vw;
                max-width: 12vw;
            }

            .hamburger {
                display: none;
            }

            .nav {
                position: static;
                width: auto;
                height: auto;
                background-color: transparent;
                flex-direction: row;
                justify-content: flex-end;
                align-items: center;
                gap: 0.5vw;
                transform: none;
                transition: none;
            }

            .nav a {
                opacity: 1;
                transform: none;
                transition: opacity 0.2s ease;
                font-size: 1vw;
                padding: 0.5vw 1vw;
            }

            .dropdown-menu {
                position: absolute;
                min-width: 240px;
                margin-top: 0;
            }

            .dropdown-menu a {
                padding: 12px 16px;
                text-align: left;
                font-size: 1vw;
                line-height: 1.4;
            }

            .nav-item.dropdown:hover .dropdown-menu {
                display: block;
            }

            /* --- DESKTOP UNDERLINE STYLES (REFACTORED) --- */

            /* Underline for standard active nav links (Home, etc.) AND the main "Case Studies" link */
            .nav > a.active::after,
            .nav-item.dropdown > .nav-link.active::after {
                content: '';
                position: absolute;
                left: 1vw;
                right: 1vw;
                bottom: 0.25vw;
                height: 2px;
                background-color: white;
            }

            /* Underline for active links INSIDE the dropdown */
            .dropdown-menu a.active::after {
                content: '';
                position: absolute;
                left: 16px;
                right: 16px;
                bottom: 10px;
                height: 2px;
                background-color: white;
            }

            /* On hover, HIDE the underline from the main "Case Studies" link so only the child's underline is visible. */
            .nav-item.dropdown:hover > .nav-link.active::after {
                background-color: transparent;
            }
        }

        /* --- MOBILE STYLES (max-width: 992px) --- */
        @media (max-width: 992px) {
            .nav-item.dropdown {
                width: 100%;
                text-align: center;
            }
            .nav-item.dropdown .nav-link::after {
                content: ' ▾';
                display: inline-block;
            }
            .dropdown-menu {
                position: static;
                background-color: rgba(255, 255, 255, 0.05);
                box-shadow: none;
                width: 90%;
                margin: 1vh auto 0;
                padding: 1vh 0;
            }
            .nav-item.dropdown.is-open .dropdown-menu {
                display: block;
            }
            .dropdown-menu a {
                font-size: 3.8vw;
                padding: 1.5vh 0;
                text-align: center;
            }

            /* --- MOBILE UNDERLINE STYLES --- */
            .nav a.active::after {
                content: '';
                position: absolute;
                bottom: -5px;
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                height: 2px;
                background-color: white;
            }
            
            /* Hide underline on main 'Case Studies' link when its dropdown is open */
            .nav-item.dropdown.is-open > .nav-link.active::after {
                display: none;
            }
        }
    </style>
    """