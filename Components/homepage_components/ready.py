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
            min-height: 100vh; /* Changed from fixed height and scale to be a full-height section */
            display: flex; /* Using Flexbox for a robust and responsive layout */
            align-items: center;
            justify-content: center;
            gap: 5vw;
            padding: 5vh 5vw;
            overflow: hidden; /* Prevents background ellipses from causing scrollbars */
            box-sizing: border-box;
        }

        /* Blurred Background Ellipses */
        .ellipse {
            position: absolute;
            opacity: 1;
            filter: blur(10.42vw); /* Original: 200px */
            z-index: -1;
        }

        /* Ellipse 1 (Left) */
        .ellipse-1 {
            width: 10.53vw; /* Original: 202.11px */
            height: 30.46vh; /* Original: 329px */
            left: 5vw;
            top: 20vh;          
            background: rgba(255, 255, 255, 0.48);
        }

        /* Ellipse 2 (Right) */
        .ellipse-2 {
            width: 10.53vw; /* Original: 202.11px */
            height: 30.46vh; /* Original: 329px */
            right: 5vw;
            top: 15vh;
            background: rgba(255, 255, 255, 0.49);
            transform: matrix(0.45, 0.89, 0.89, -0.45, 0, 0);
        }

        /* Main Text & Button Container */
        .text-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 5.18vh; /* Original: 56px */
            width: 46vw; /* Original: 884px */
            max-width: 46vw;
        }

        .text-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 2.03vh; /* Original: 21.93px */
            width: 100%;
        }

        /* "Ready to Make Data Work for You?" */
        .main-heading {
            width: 100%; /* Changed from fixed width */
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 3.33vw; /* Original: 64px */
            line-height: 1.2;
            color: #FFFFFF;
            margin: 0;
        }

        /* "Say goodbye to guesswork." */
        .sub-heading {
            width: 100%;
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 1.9vw; /* Original: 36.55px */
            line-height: 1.2;
            color: #FFFFFF;
            margin: 0;
        }

        /* "Let’s turn your business into a data-driven powerhouse!" */
        .description {
            width: 100%;
            font-family: 'Exo 2', sans-serif;
            font-weight: 400;
            font-size: 1.52vw; /* Original: 29.24px */
            line-height: 1.5;
            color: #FFFFFF;
            margin: 0;
        }

        /* Buttons Container */
        .buttons-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 1.14vw; /* Original: 21.93px */
            flex-wrap: wrap; /* Allows buttons to wrap on smaller screens */
        }

        .button {
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 1.15vw; /* Original: 22px */
            height: 6.02vh; /* Original: 65px */
            box-sizing: border-box;
            border-radius: 9.52vw; /* Original: 182.755px */
            white-space: nowrap;
            padding-left: 2.28vw; /* Original: 43.86px */
            padding-right: 2.28vw; /* Original: 43.86px */
            transition: transform 0.2s ease, opacity 0.2s ease;
        }
        
        .button:hover {
            transform: scale(1.03);
            opacity: 0.9;
        }

        .primary-button {
            background: #FFFFFF;
            color: #000000;
        }

        .secondary-button {
            border: 0.1vw solid #FFFFFF; /* Original: 1.82px */
            color: #FFFFFF;
            background: transparent;
        }

        /* Image Column Container */
        .image-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 1.36vh; /* Original: 14.68px */
            width: 16.32vw; /* Original: 313.43px */
            filter: drop-shadow(0 0.37vh 0.21vw rgba(0, 0, 0, 0.25)); /* Original: 0px 4px 4px */
        }

        .image-box {
            box-sizing: border-box;
            width: 100%; /* Fills the container */
            border: 0.1vw solid #616161; /* Original: 2px */
            border-radius: 1.64vw; /* Original: 31.44px */
            overflow: hidden;
        }

        .image-box-short {
            height: 13.59vh; /* Original: 146.76px */
        }

        .image-box-long {
            height: 26.4vh; /* Original: 285.13px */
        }

        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(100%);
        }
    </style>
"""