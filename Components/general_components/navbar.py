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
               <a href="#" class="nav-link" id="case-studies-link">Case Studies</a>
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

        :root {
            --bg: #111;
            --text: #ffffff;
            --brand: #7ec5f4;
            --nav-timing: 400ms;
            --nav-panel-bg: rgba(20, 20, 20, 0.85); /* Modified for blur effect */
            --nav-panel-bg-solid: #141414;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        html, body {
            overflow-x: hidden; /* Prevents horizontal scroll caused by off-screen menu */
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
            padding: 2vh 5vw; /* Adjusted padding */
            font-family: 'Poppins', sans-serif; 
            font-weight: 600;
        }

        .brand {
            display: flex;
            width: 35vw; /* Slightly reduced for better balance */
            max-width: 150px; /* Added max-width for larger mobile screens */
            height: auto;
            z-index: 1001;
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
            width: 8vw;
            max-width: 35px; /* Cap size on larger mobiles */
            height: 6vw;
            max-height: 28px;
            display: inline-block;
            position: relative;
        }

        .hamburger-inner, .hamburger-inner::before, .hamburger-inner::after {
            width: 100%;
            height: 0.6vw; /* Slightly thicker for visibility */
            max-height: 3px;
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
            top: -2.5vw; /* Spacing relative to viewport width */
            transition: top 0.1s 0.25s ease-in, opacity 0.1s ease-in;
        }
        .hamburger-inner::after {
            bottom: -2.5vw;
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
            width: 80vw; /* Slightly wider for more space */
            height: 100vh;
            
            /* Elegant glassmorphism effect */
            background-color: var(--nav-panel-bg);
            backdrop-filter: blur(1.5vh);
            -webkit-backdrop-filter: blur(1.5vh);
            
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 4vh;
            
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
            font-size: 5vw;
            
            opacity: 0;
            transform: translateY(3vh);
            transition: opacity 0.3s ease, transform 0.3s ease, color 0.2s ease;
        }
        
        .nav a:hover, .nav a.active {
            color: var(--brand); /* Highlight active/hovered link */
        }

        /* Staggered animation for nav items when menu opens */
        .nav.is-active > * {
            opacity: 1;
            transform: translateY(0);
        }
        .nav.is-active .nav-item:nth-child(1), .nav.is-active > a:nth-child(1) { transition-delay: calc(var(--nav-timing) * 0.5); }
        .nav.is-active .nav-item:nth-child(2), .nav.is-active > a:nth-child(2) { transition-delay: calc(var(--nav-timing) * 0.6); }
        .nav.is-active .nav-item:nth-child(3), .nav.is-active > a:nth-child(3) { transition-delay: calc(var(--nav-timing) * 0.7); }
        .nav.is-active .nav-item:nth-child(4), .nav.is-active > a:nth-child(4) { transition-delay: calc(var(--nav-timing) * 0.8); }
        .nav.is-active .nav-item:nth-child(5), .nav.is-active > a:nth-child(5) { transition-delay: calc(var(--nav-timing) * 0.9); }
        .nav.is-active .nav-item:nth-child(6), .nav.is-active > a:nth-child(6) { transition-delay: calc(var(--nav-timing) * 1.0); }
        
        /* Mobile Dropdown */
        .nav-item.dropdown {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }
        .nav-item.dropdown .nav-link::after {
            content: ' ▾';
            display: inline-block;
            font-size: 3vw;
        }
        .dropdown-menu {
            display: none;
            flex-direction: column;
            align-items: center;
            background-color: transparent;
            box-shadow: none;
            width: 100%;
            margin-top: 1.5vh;
            gap: 1.5vh;
        }
        .nav-item.dropdown.is-open .dropdown-menu {
            display: flex;
        }
        .dropdown-menu a {
            font-size: 4vw;
            font-weight: 600; /* Less bold for hierarchy */
            color: rgba(255, 255, 255, 0.8);
            padding: 1vh 0;
            width: 100%;
            text-align: center;
        }
        .dropdown-menu a.active, .dropdown-menu a:hover {
            color: var(--brand);
        }
        
        /* --- DESKTOP STYLES (Unchanged) --- */
        @media (min-width: 993px) {
            .navbar {
                padding: 1.5vw 2vw;
            }

            .brand {
                width: 12rem;
                max-width: 12rem;
            }

            .hamburger {
                display: none;
            }

            .nav {
                position: static;
                width: auto;
                height: auto;
                background-color: transparent;
                backdrop-filter: none;
                -webkit-backdrop-filter: none;
                flex-direction: row;
                justify-content: flex-end;
                align-items: center;
                gap: 0.5rem;
                transform: none;
                transition: none;
            }

            .nav a, .nav .nav-link {
                opacity: 1;
                transform: none;
                transition: opacity 0.2s ease, color 0.2s ease;
                font-size: 1.5rem;
                padding: 0.5rem 1rem;
                position: relative;
            }

            .nav a.active::after, .nav .nav-link.active::after {
                content: '';
                position: absolute;
                left: 1rem;
                bottom: -2px;
                width: calc(100% - 2rem);
                height: 2px;
                background-color: var(--brand);
            }

            .nav-item.dropdown {
                position: relative;
                width: auto;
            }

            .dropdown-menu {
                display: none;
                position: absolute;
                background-color: var(--nav-panel-bg-solid);
                min-width: 240px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                border-radius: 4px;
                margin-top: 0.5rem;
                gap: 0;
            }
            .nav-item.dropdown:hover .dropdown-menu {
                display: flex;
            }
            .nav-item.dropdown .nav-link::after {
                content: '';
            }
            .dropdown-menu a {
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                text-align: left;
                font-size: 1.1rem;
                white-space: normal;
                line-height: 1.4;
                font-weight: 600;
                color: var(--text);
            }
            .dropdown-menu a:hover {
                background-color: #575757;
                opacity: 1;
                color: var(--text);
            }
        }
    </style>
    """