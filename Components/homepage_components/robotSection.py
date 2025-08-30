from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def robot_style():
    return """
    <style>
        /* Base */
        :root{
            --card-w: 428px;
            --card-h: 315px;
            --cards-gap: 40px;
            --canvas-h: 850px; 
            --blue:#25A6E9;
            --ink:#EBF0F3;
            --glass-bg: rgba(255,255,255,0.04);
            --glass-brd: rgba(255, 255, 255, 0.3);
            --ink-70: rgba(255,255,255,0.7);
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
            height:1303px;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 1.45%, rgba(48, 48, 48, 0.08) 28.37%, #000000 100%);
            padding-top:10rem;
            border-radius:85px;
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
            width:1100px;
            height:1100px;
            transform:translate(-50%,-50%);
            background: radial-gradient(50% 50% at 50% 50%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0.02) 45%, rgba(0,0,0,0.00) 70%);
            filter: blur(2px);
            pointer-events:none;
        }
        .main-container::after {
            content: "";
            position: absolute;
            width: 202.11px;
            height: 329px;
            left: 50%;
            top: 60%;
            transform: translateX(-30%);
            background: #FFFFFF;
            opacity: 0.66;
            filter: blur(200px);
        }


        /* Headings */
        .heading-container{
            position:relative;
            width:100%;
            max-width:916px;
            text-align:center;
            letter-spacing:-0.02em;
            text-transform:capitalize;
            z-index:20;
            margin-bottom:12px;
        }
        .heading-container h1{
            font-weight:700;
            font-size:64px;
            line-height:77px;
            margin:0;
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.3) 0.22%, #EBF0F3 15.65%, #EBF0F3 54.72%, rgba(235, 239, 243, 0.72) 79.36%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }
        .heading-container h2{
            font-weight:700;
            font-size:64px;
            line-height:77px;
            margin:0;
            color:var(--blue);
        }

        /* Content row */
        .content-wrapper{
            position:relative;
            width:100%;
            max-width:1728px;
            height:var(--canvas-h);
            margin-top:120px;
        }

        /* Connector overlay (between robot and cards) */
        .connector-vector{
            position:absolute;
            pointer-events:none;
            z-index:15;
        }
        #vector-1{
            left: 21.5%;
            top: 19%;
            transform: rotate(180deg);
        }
        #vector-2{
            left: 23.3%;
            top: 69.5%;
            transform: rotate(180deg);
        }
        #vector-3{
            right: 21.5%;
            top: 19.2%;
        }
        #vector-4{
            right: 20.5%;
            top: 76.5%;
        }

        /* Robot */
        #robot-image{
            position:absolute;
            left:50%;
            top:50%;
            transform:translate(-50%,-50%);
            width:662.18px;
            height:775.45px;
            object-fit:contain;
            z-index:10;
            filter: drop-shadow(0 20px 60px rgba(0,0,0,0.55));
        }

        /* Feature cards (glassy) */
        .feature-box{
            position:absolute;
            width:var(--card-w);
            height:var(--card-h);
            z-index: 20;
            border:1px solid var(--glass-brd);
            border-radius:10px;
            padding:35px 25px;
            background: var(--glass-bg);
            backdrop-filter: blur(8px) saturate(120%);
            -webkit-backdrop-filter: blur(8px) saturate(120%);
            box-shadow: 0 10px 35px rgba(0,0,0,0.35);
        }
        #feature-box-1{ top: 0; left: 0;}
        #feature-box-2{ bottom: 0; left: 0;}
        #feature-box-3{ top: 0; right: 0;}
        #feature-box-4{ bottom: 0; right: 0;}

        .feature-header{
            display:flex;
            align-items:center;
            gap:30px;
            margin-bottom:54px;
        }
        .feature-icon{
            display:flex;
            justify-content:center;
            align-items:center;
            width:53px;
            height:53px;
            background:#0A1015;
            border:1px solid #3A4046;
            border-radius:3px;
            flex-shrink:0;
        }
        .feature-icon img{width:31.64px;height:31.64px}

        .feature-box h3{
            font-weight:600;
            font-size:25px;
            line-height:120%;
            text-transform:capitalize;
            color:#FFFFFF;
            margin:0;
        }

        .feature-content{
            display:flex;
            flex-direction:column;
            gap:25px;
        }
        .feature-content p{
            height:78px;
            font-weight:400;
            font-size:16.4385px;
            line-height:160%;
            text-transform:capitalize;
            color: #FFFFFF;
            opacity: 0.7;
            margin:0;
        }

        .show-detail-link{
            display:flex;
            align-items:center;
            gap:10px;
            text-decoration:none;
            font-weight:400;
            font-size:18px;
            line-height:28px;
            text-transform:capitalize;
            color:#FFFFFF;
            transition:opacity .2s ease, transform .2s ease;
        }
        .show-detail-link:hover{opacity:1; transform:translateY(-1px)}
        .show-detail-link svg{width:24px;height:24px}
    </style>
    """


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
                <svg id="vector-1" class="connector-vector" width="135" height="82" viewBox="0 0 135 82" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M133 8H134.5V6.5H133V8ZM16 8C16 3.58173 12.4183 0 8 0C3.58173 0 0 3.58173 0 8C0 12.4183 3.58173 16 8 16C12.4183 16 16 12.4183 16 8ZM133 82H134.5V8H133H131.5V82H133ZM133 8V6.5H8V8V9.5H133V8Z" fill="#818181" fill-opacity="0.43"/>
                </svg>
                <svg id="vector-2" class="connector-vector" width="95" height="16" viewBox="0 0 95 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M93 8H94.5V6.5H93V8ZM16 8C16 3.58172 12.4183 0 7.99999 0C3.58172 0 -7.62939e-06 3.58172 -7.62939e-06 8C-7.62939e-06 12.4183 3.58172 16 7.99999 16C12.4183 16 16 12.4183 16 8ZM93 10H94.5V8H93H91.5V10H93ZM93 8V6.5H7.99999V8V9.5H93V8Z" fill="#818181" fill-opacity="0.43"/>
                </svg>
                <svg id="vector-3" class="connector-vector" width="120" height="82" viewBox="0 0 120 82" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 8H0.5V6.5H2V8ZM104 8C104 3.58173 107.582 0 112 0C116.418 0 120 3.58173 120 8C120 12.4183 116.418 16 112 16C107.582 16 104 12.4183 104 8ZM2 82H0.5V8H2H3.5V82H2ZM2 8V6.5H112V8V9.5H2V8Z" fill="#818181" fill-opacity="0.43"/>
                </svg>
                <svg id="vector-4" class="connector-vector" width="157" height="16" viewBox="0 0 157 16" fill="none" xmlns="http://www.w3.org/2000/svg">
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
