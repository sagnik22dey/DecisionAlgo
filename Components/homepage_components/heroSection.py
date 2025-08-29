from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def heroSection_body():
    return """
    <div class="hero-section-container">
        <!-- Background and Decorative Elements -->
        <div class="bg-dark"></div>
        <div class="grid-container"></div>
        <div class="gradient-overlay"></div>
        <div class="glow-bottom"></div>
        
        <!-- Foreground Content (Text and Button) -->
        <div class ="hero-content-container">
        <div class="hero-content">
            <h1>Is your Business drowning in Data but, Starving for Insights?</h1>
            <p>Transform frustration into fortune with AI solutions that eliminate data headaches, accelerate decision-making, and drive measurable ROI.</p>
            <a href="#" class="cta-button">
                <span>Discover How</span>
            </a>
        </div>
        </div>
    </div>
"""

async def heroSection_style():
    return """    
    <style>
        /* The main container for the hero section to provide a positioning context */
        .hero-section-container {
            position: relative; /* Changed from absolute */
            width: 100%;
            /* overflow: hidden; */ /* To contain the glows */
            display: flex; /* Use flexbox to align content */
            flex-direction: column;
            justify-content: center; /* Vertically center content */
            align-items: center; /* Horizontally center content */
            padding-top: 15rem; /* Add some top padding to move content down from the top of the container */
            padding-bottom: 15rem; /* Add some bottom padding */
            box-sizing: border-box; /* Include padding in width/height calculation */
        }

        /* Rectangle 29: Base background color layer */
        .bg-dark {
            position: absolute;
            width: 100%; /* Changed from fixed width */
            height: 100%; /* Changed from fixed height */
            left: 0px;
            top: 0px; /* Changed from 151px */
            background: #111111;
        }

        /* Ellipse 4335: Top white glow effect */
        .hero-section-container::before {
            content: '';
            position: absolute;
            width: 350px;
            height: 350px;
            left: 50%; /* Centered horizontally */
            top: -100px; /* Adjusted to be higher but still visible */
            background: #FFFFFF;
            opacity: 0.2;
            filter: blur(200px);
            transform: translateX(-50%); /* For horizontal centering */
            z-index: 1;
        }

        /* Rectangle 41: Gradient overlay with rounded corners */
        .gradient-overlay {
            position: absolute;
            width: 100%; /* Changed from fixed width */
            height: 100%; /* Changed from fixed height */
            left: 0px;
            top: 0px; /* Changed from 144px */
            background: linear-gradient(177.33deg, rgba(15, 15, 15, 0) 5.46%, rgba(0, 0, 0, 0.6006) 53.07%, rgba(0, 0, 0, 0.77) 93.86%);
            border-radius: 65px;
            border-bottom: solid 1px;
            border-color:#f0f0f0;
        }

        /* Rectangle 14: The grid pattern container with border */
        .grid-container {
            box-sizing: border-box;
            position: absolute;
            width: 100%; /* Changed from fixed width */
            height: 100%; /* Changed from fixed height */
            left: 0px; /* Changed from -14px */
            top: 0px; /* Changed from 151px */
            /* Using the image path you provided */
            background-image: url('../../Resources/Images/rectanglebox_bg.png');
        }

        /* Ellipse 2: Bottom white glow effect */
        .glow-bottom {
            position: absolute;
            width: 800px;
            height: 800px;
            left: 50%; /* Centered horizontally */
            bottom: -400px; /* Positioned to span sections */
            background: #FFFFFF;
            opacity: 0.25;
            filter: blur(250px);
            transform: translateX(-50%);
            border-radius: 50%;
        }

        .hero-content-container{
            margin-right: 600px;
        }
        /* Frame 2147225626: Container for all text content */
        .hero-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 0px; /* Added horizontal padding for spacing from edges */
            gap: 33px;
            position: relative; /* Changed from absolute, to flow within flex container */
            max-width: 971px; /* Keep max-width, but add fluid width */
            width: 100%; /* Make it responsive */
            z-index: 10; /* Ensure text is on top of all background elements */
        }
        

        /* Main Headline: "Is your Business..." */
        .hero-content h1 {
            /* Removed fixed width and height */
            font-family: 'Exo 2', sans-serif;
            font-style: normal;
            font-weight: 700;
            font-size: 72px;
            line-height: 86px;
            letter-spacing: -0.04em;
            color: #FFFFFF;
            text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            /* Layout properties from CSS */
            flex: none;
            order: 0;
            align-self: stretch;
            flex-grow: 0;
            margin: 0; /* Reset default margin */
        }

        /* Paragraph: "Transform frustration..." */
        .hero-content p {
            /* Removed fixed width and height */
            font-family: 'Poppins', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 24px;
            line-height: 150%;
            color: #FFFFFF;
            /* Layout properties from CSS */
            flex: none;
            order: 1;
            align-self: stretch;
            flex-grow: 0;
            margin: 0; /* Reset default margin */
        }

        /* Frame 5: The call-to-action button */
        .cta-button {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            padding: 8.40541px 42.027px;
            gap: 16.81px;
            width: 193px;
            height: 46px;
            background: #FFFFFF;
            box-shadow: 0px 6.72433px 6.72433px rgba(0, 0, 0, 0.25);
            border-radius: 100px;
            /* Layout properties from CSS */
            flex: none;
            order: 2;
            flex-grow: 0;
            /* Additional styles for link behavior */
            text-decoration: none;
            box-sizing: border-box;
        }

        /* Text inside the button: "Discover How" */
        .cta-button span {
            width: 131px;
            height: 35px;
            font-family: 'Jost', sans-serif;
            font-style: normal;
            font-weight: 400;
            font-size: 24px;
            line-height: 35px;
            display: flex;
            align-items: center;
            letter-spacing: -0.04em;
            color: #111111;
            /* Layout properties from CSS */
            flex: none;
            order: 0;
            flex-grow: 0;
        }
    </style>
    """ 