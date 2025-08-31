async def robot_body():
    return """
    <div class="page-wrapper">
        <div class="main-container"></div>

        <div class="heading-container">
            <h1>What We Offer</h1>
            <h2>Smarter, Faster, Automated</h2>
        </div>

        <div class="content-wrapper">
                <!-- Connectors -->
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


            <div id="feature-box-1" class="feature-box">
                <!-- Real-Time Dashboards -->
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/route.png" alt="route icon">
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
            <div id="feature-box-2" class="feature-box">
                <!-- AI-Powered Chatbots -->
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/route.png" alt="route icon">
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

            <!-- Robot -->
            <img id="robot-image" src="../../Resources/Images/robotHomepage.png" alt="A sleek black robot with red highlights, symbolizing advanced automation and AI.">

            <div id="feature-box-3" class="feature-box">
                <!-- Data-Driven Reports -->
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/route.png" alt="route icon">
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
            <div id="feature-box-4" class="feature-box">
                <!-- Smart Outsourcing Solutions -->
                <div class="feature-header">
                    <div class="feature-icon">
                        <img src="../../Resources/Images/route.png" alt="route icon">
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
    """

async def robot_style():
    return """
    <style>
        /* Base */
        :root{
            --card-w: 20.83vw; /* Original: 400px */
            --card-h: 27.78vh; /* Original: 300px */
            --blue:#25A6E9;
            --glass-bg: rgba(255,255,255,0.06);
            --glass-brd: rgba(255, 255, 255, 0.2);
        }
        *{box-sizing:border-box}
        html,body{
            margin:0;
            padding:0;
            background:#000;
            font-family: 'Exo 2', 'Poppins', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
        }

        /* Page wrapper */
        .page-wrapper{
            position:relative;
            width:100%;
            display:flex;
            flex-direction:column;
            align-items:center;
            min-height: 111.11vh; /* Original: 1200px */
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 1.45%, rgba(48, 48, 48, 0.08) 28.37%, #000000 100%);
            padding: 8.89vh 1.67vw 5.93vh; /* Original: 6rem 2rem 4rem */
            border-radius: 4.43vw; /* Original: 85px */
            overflow:hidden;
        }

        /* Backdrop halo behind the robot area */
        .main-container{
            position:absolute;
            inset:0;
            overflow:hidden;
        }
        .main-container::before{
            content:"";
            position:absolute;
            left:50%;
            top:54%;
            width: 57.29vw; /* Original: 1100px */
            height: 57.29vw; /* Kept aspect ratio */
            transform:translate(-50%,-50%);
            background: radial-gradient(50% 50% at 50% 50%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.02) 45%, rgba(0,0,0,0.00) 70%);
            filter: blur(0.1vw); /* Original: 2px */
            pointer-events:none;
        }
        .main-container::after {
            content: "";
            position: absolute;
            width: 10.53vw; /* Original: 202.11px */
            height: 30.46vh; /* Original: 329px */
            left: 50%;
            top: 60%;
            transform: translateX(-30%);
            background: #FFFFFF;
            opacity: 0.66;
            filter: blur(10.42vw); /* Original: 200px */
        }


        /* Headings */
        .heading-container{
            position:relative;
            width:100%;
            max-width: 52.08vw; /* Original: 1000px */
            text-align:center;
            letter-spacing:-0.02em;
            z-index:20;
            margin-bottom: 1.85vh; /* Original: 20px */
        }
        .heading-container h1{
            font-weight:700;
            font-size: 2.92vw; /* Original: 56px */
            line-height:1.1;
            margin:0 0 0.74vh 0; /* Original: 8px */
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.4) 0.22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, 0.8) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }
        .heading-container h2{
            font-weight:700;
            font-size: 2.92vw; /* Original: 56px */
            line-height:1.1;
            margin:0;
            color:var(--blue);
        }

        /* Content row */
        .content-wrapper{
            position:relative;
            width:100%;
            max-width: 83.33vw; /* Original: 1600px */
            height: 74.07vh; /* Original: 800px */
            margin-top: 7.41vh; /* Original: 80px */
        }

        /* Connector overlay (between robot and cards) */
        .connector-vector{
            position:absolute;
            pointer-events:none;
            z-index:15;
            opacity:0.6;
        }
        #vector-1{ left: 38%; top: 3%; }
        #vector-2{ left: 32%; bottom: 47%; }
        #vector-3{ right: 32%; top: -1%; }
        #vector-4{ right: 32%; top: 58%; }

        /* Robot */
        #robot-image{
            position:absolute;
            left:50%;
            top:50%;
            transform:translate(-50%,-50%);
            width: 31.25vw; /* Original: 600px */
            height: auto;
            object-fit:contain;
            z-index:10;
            filter: drop-shadow(0 1.85vh 3.125vw rgba(0,0,0,0.6)); /* Original: 0 20px 60px */
        }

        /* Feature cards (glassy) */
        .feature-box{
            position:absolute;
            width:var(--card-w);
            height:var(--card-h);
            z-index: 20;
            border: 1px solid var(--glass-brd);
            border-radius: 12px;
            padding: 32px 28px;
            background: var(--glass-bg);
            backdrop-filter: blur(10px) saturate(120%);
            -webkit-backdrop-filter: blur(10px) saturate(120%);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .feature-box:hover{
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.4);
        }
        #feature-box-1{ top: -3%; left: 13%; }
        #feature-box-2{ bottom: 15%; left: 7%; }
        #feature-box-3{ top: -3%; right: 7%; }
        #feature-box-4{ bottom: 10%; right: 7%; }

        .feature-header{
            display:flex;
            align-items:center;
            gap: 20px;
            margin-bottom: 32px;
        }
        .feature-icon{
            display:flex;
            justify-content:center;
            align-items:center;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #0A1015 0%, #1a1f25 100%);
            border: 1px solid #3A4046;
            border-radius: 8px;
            flex-shrink:0;
        }
        .feature-icon img{ width: 28px; height: 28px; }

        .feature-box h3{
            font-weight:600;
            font-size: 1.375rem; /* 22px */
            line-height:1.3;
            color:#FFFFFF;
            margin:0;
        }

        .feature-content{
            display:flex;
            flex-direction:column;
            gap: 20px;
        }
        .feature-content p{
            font-weight:400;
            font-size: 0.9375rem; /* 15px */
            line-height:1.5;
            color: rgba(255,255,255,0.8);
            margin:0;
        }

        .show-detail-link{
            display:flex;
            align-items:center;
            gap: 8px;
            text-decoration:none;
            font-weight:500;
            font-size: 1rem; /* 16px */
            line-height:1.5;
            color:#FFFFFF;
            transition:opacity .2s ease, transform .2s ease;
            opacity:0.9;
        }
        .show-detail-link:hover{
            opacity:1; 
            transform:translateY(-1px);
        }
        .show-detail-link svg{
            width: 20px;
            height: 20px;
            transition: transform 0.2s ease;
        }
        .show-detail-link:hover svg{
            transform: translateX(2px);
        }
        
        /* Tablet & smaller desktop adjustments */
        @media (max-width: 1400px) {
            #feature-box-1{ top: -3%; left: 10%; }
            #feature-box-2{ bottom: 15%; left: 4%; }
            #feature-box-3{ top: -3%; right: 4%; }
            #feature-box-4{ bottom: 10%; right: 4%; }
        }

        @media (max-width: 1200px) {
            .heading-container h1,
            .heading-container h2 {
                font-size: 2.5vw;
            }
             #feature-box-1{ left: 5%; }
             #feature-box-2{ left: 1%; }
             #feature-box-3{ right: 1%; }
             #feature-box-4{ right: 1%; }
        }

        /* --- MOBILE STYLES --- */
        @media (max-width: 992px) {
            .page-wrapper {
                padding: 4rem 1.5rem;
                min-height: auto;
            }

            .heading-container {
                max-width: 100%;
            }

            .heading-container h1,
            .heading-container h2 {
                font-size: 2rem; /* 32px */
            }

            .content-wrapper {
                position: static;
                height: auto;
                margin-top: 3rem;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 2rem;
            }

            .connector-vector {
                display: none;
            }

            #robot-image {
                position: static;
                transform: none;
                width: 70vw;
                max-width: 350px;
                height: auto;
                order: 3; /* Places robot in the middle */
            }
            
            .feature-box {
                position: static !important; /* Override inline styles if any */
                transform: none !important;
                width: 100%;
                max-width: 450px;
                height: auto;
                padding: 24px;
            }

            #feature-box-1 { order: 1; }
            #feature-box-2 { order: 2; }
            #feature-box-3 { order: 4; }
            #feature-box-4 { order: 5; }

            .feature-box:hover {
                transform: none !important;
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            }
            
            .feature-header {
                gap: 16px;
                margin-bottom: 24px;
            }

            .feature-box h3 {
                font-size: 1.25rem; /* 20px */
            }

            .feature-content p {
                font-size: 1rem; /* 16px */
            }
        }
    </style>
    """