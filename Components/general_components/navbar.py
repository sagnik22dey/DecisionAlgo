from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def navbar():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Navbar</title>
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
            background: var(--bg);
            color: var(--text);
            font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, "Helvetica Neue", Arial, sans-serif;
        }

        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            padding-top: 20px;
            padding-bottom:20px;
            padding-right:40px;
            max-width: 1800px;
            margin: 0 auto;
        }

        .brand {
            display:flex;
            width: 357px;
            height: 76px;
            border-radius: 8px;
            object-fit: cover;
        }
        
        .nav {
            margin-left:30px;
            display: flex;
            align-items: center;
            gap: 32px;
            font-size:20px;
        }

        .nav a {
            color: var(--text);
            text-decoration: none;
            font-weight: 800;
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

        @media (max-width: 720px) {
            .navbar {
                flex-wrap: wrap;
                gap: 16px;
            }

            .nav {
                flex-basis: 100%;
                justify-content: space-between;
                gap: 16px;
                overflow-x: auto;
            }
        }
    </style>
</head>

<body>
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
</body>

</html>
    """