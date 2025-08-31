async def navbar_body():
    return """
    <header class="navbar" role="navigation" aria-label="Main">
        <a href="#" class="brand">
            <img src="/Resources/Images/DecisionAlgoLogo.png" alt="DecisionAlgo logo" />
        </a>
        <nav class="nav">
            <a href="#" class="active">Home</a>
            <a href="#">Dashboards</a>
            <a href="#">Case Studies</a>
            <a href="#">About us</a>
            <a href="#">Pricing</a>
            <a href="#">Contact Us</a>
        </nav>
    </header>
    """

async def navbar_style():
    return """
    <style>
        :root {
            --bg: #111;
            --text: #ffffff;
            --brand: #7ec5f4;
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
            gap: 1.25vw; /* Original: 24px */
            padding-top: 1.85vh; /* Original: 20px */
            padding-bottom: 1.85vh; /* Original: 20px */
            padding-right: 1.04vw; /* Original: 20px */
            padding-left: 1.56vw; /* Original: 30px */
            max-width: 100vw;
        }

        .brand {
            display:flex;
            width: 18.6vw; /* Original: 357px */
            height: 7.0vh; /* Original: 76px */
            border-radius: 0.42vw; /* Original: 8px */
            object-fit: cover;
        }
        
        .nav {
            margin-left: 1.56vw; /* Original: 30px */
            display: flex;
            align-items: center;
            gap: 1.67vw; /* Original: 32px */
            font-size: 1.04vw; /* Original: 20px */
        }

        .nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: 800;
        }

        .nav a:last-child {
            padding-right: 1.04vw; /* Original: 20px */
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
            bottom: -0.56vh; /* Original: -6px */
            height: 0.28vh; /* Original: 3px */
            background: var(--text);
            border-radius: 0.1vw; /* Original: 2px */
        }

        /* Changed the breakpoint to be responsive as well */
        @media (max-width: 37.5vw) { /* Original: 720px */
            .navbar {
                flex-wrap: wrap;
                gap: 0.83vw; /* Original: 16px */
            }

            .nav {
                flex-basis: 100%;
                justify-content: space-between;
                gap: 0.83vw; /* Original: 16px */
                overflow-x: auto;
            }
        }
    </style>
    """