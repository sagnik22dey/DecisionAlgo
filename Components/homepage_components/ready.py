async def ready_body():
    return """     
    <main class="viewport-container">
        <!-- Background Elements -->
        <div class="ellipse ellipse-1"></div>
        <div class="ellipse ellipse-2"></div>

        <!-- Left Side: Text and Buttons -->
        <div class="text-container">
            <div class="text-content">
                <h1 class="main-heading">Ready to Make Data Work for You?</h1>
                <p class="sub-heading">Say goodbye to guesswork.</p>
                <p class="description">Let’s turn your business into a data-driven powerhouse!</p>
            </div>
            <div class="buttons-container">
                <a href="#" class="button primary-button">Get a Free Consultation</a>
                <a href="#" class="button secondary-button">Try Our Solutions</a>
            </div>
        </div>

        <!-- Right Side: Images -->
        <div class="image-container">
            <div class="image-box image-box-short">
                <img src="../../Resources/images/Tripple_1.png" alt="Futuristic data dashboard">
            </div>
            <div class="image-box image-box-long">
                 <img src="../../Resources/images/Tripple_2.png" alt="Robotic hand interacting with a digital interface">
            </div>
            <div class="image-box image-box-short">
                 <img src="../../Resources/images/Tripple_3.png" alt="Woman in a modern, futuristic setting">
            </div>
        </div>
    </main>
"""

async def ready_style():
    return """ 
    <!-- Google Fonts Import -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;700&family=Outfit:wght@600&display=swap" rel="stylesheet">
    
    <style>
        .viewport-container {
            position: relative;
            width: 100vw;
            height: 78vh;
            transform: scale(0.8);
            transform-origin: top center;
        }

        /* Blurred Background Ellipses */
        .ellipse {
            position: absolute;
            opacity: 1;
            filter: blur(200px);
        }

        /* Ellipse 4336 (Left) */
        .ellipse-1 {
            width: 202.11px;
            height: 329px;
            left: -187px;
            top: 164px; /* Vertical position normalized from Figma's large canvas value */            
            background: rgba(255, 255, 255, 0.48);
           
        }

        /* Ellipse 4336 (Right) */
        .ellipse-2 {
            width: 202.11px;
            height: 329px;
            left: 1478px;
            top: 105px; /* Vertical position normalized */
            background: rgba(255, 255, 255, 0.49);
            transform: matrix(0.45, 0.89, 0.89, -0.45, 0, 0);
        }

        /* Main Text & Button Container (Frame 2147225631) */
        .text-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 56px;
            position: absolute;
            width: 884px;
            left: 198px;
            top: 230px; /* Adjusted top position for better vertical centering */
        }

        .text-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 21.93px;
            width: 100%;
        }

        /* "Ready to Make Data Work for You?" */
        .main-heading {
            width: 845px;
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 64px;
            line-height: 1.2;
            color: #FFFFFF;
            margin: 0;
        }

        /* "Say goodbye to guesswork." */
        .sub-heading {
            width: 100%;
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 36.5509px;
            line-height: 1.2;
            color: #FFFFFF;
            margin: 0;
        }

        /* "Let’s turn your business into a data-driven powerhouse!" */
        .description {
            width: 100%;
            font-family: 'Exo 2', sans-serif;
            font-weight: 400;
            font-size: 29.2408px;
            line-height: 1.5;
            color: #FFFFFF;
            margin: 0;
        }

        /* Buttons Container */
        .buttons-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 21.93px;
        }

        .button {
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 22px; /* Adjusted from 16px in spec to visually match the image */
            height: 65px;
            box-sizing: border-box;
            border-radius: 182.755px;
            white-space: nowrap;
            padding-left: 43.8611px;
            padding-right: 43.8611px;
            transition: transform 0.2s ease, opacity 0.2s ease;
        }
        
        .button:hover {
            transform: scale(1.03);
            opacity: 0.9;
        }

        /* "Get a Free Consultation" Button */
        .primary-button {
            background: #FFFFFF;
            color: #000000;
        }

        /* "Try Our Solutions" Button */
        .secondary-button {
            border: 1.82755px solid #FFFFFF;
            color: #FFFFFF;
            background: transparent;
        }

        /* Image Column Container (Frame 2147225630) */
        .image-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 14.68px;
            position: absolute;
            width: 313.43px;
            left: 1181px;
            top: 150px; /* Adjusted top position */
            filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
        }

        .image-box {
            box-sizing: border-box;
            width: 313.43px;
            border: 2px solid #616161;
            border-radius: 31.4483px;
            overflow: hidden; /* Ensures the image conforms to the rounded corners */
        }

        .image-box-short {
            height: 146.76px;
        }

        .image-box-long {
            height: 285.13px;
        }

        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* Ensures the image fills the box without distortion */
            filter: grayscale(100%);
        }
    </style>
"""
