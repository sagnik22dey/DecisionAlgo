from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def robot_style():
    return """    
    <style>
        /* General Setup */
        .page-wrapper {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
            
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 1.45%, rgba(48, 48, 48, 0.08) 28.37%, #000000 100%);
        }

        /* Main Container Background */
        .main-container {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        /* Background Glow */
        .glow {
            position: absolute;
            width: 202px;
            height: 329px;
            left: 763px;
            top: 650px;
            background: #FFFFFF;
            opacity: 0.2;
            filter: blur(150px);
            z-index: 1;
        }

        /* Headings */
        .heading-container {
            position: relative;
            width: 90%;
            max-width: 916px;
            text-align: center;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            z-index: 20;
            margin-bottom: 60px;
        }
        
        .heading-container h1 {
            font-weight: 700;
            font-size: 64px;
            line-height: 77px;
            margin: 0;
            color: #EBF0F3;
        }

        .heading-container h2 {
            font-weight: 700;
            font-size: 64px;
            line-height: 77px;
            margin: 0;
            color: #25A6E9; /* Color taken from image, not in CSS */
        }
        
        .content-wrapper {
            position: relative;
            width: 100%;
            max-width: 1728px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 60px;
        }

        /* Robot Image */
        #robot-image {
            position: relative;
            width: 462.18px;
            height: 575.45px;
            z-index: 10;
        }

        .features-wrapper {
            display: flex;
            flex-direction: column;
            gap: 40px;
        }

        /* Feature Boxes */
        .feature-box {
            box-sizing: border-box;
            width: 428px;
            height: 315px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            padding: 35px 25px;
            z-index: 20;
        }

        .feature-header {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 30px;
            margin-bottom: 54px;
        }

        .feature-icon {
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 53px;
            height: 53px;
            background: #0A1015;
            border: 1px solid #3A4046;
            border-radius: 2.55882px;
            flex-shrink: 0;
        }
        
        .feature-icon img {
            width: 31.64px;
            height: 31.64px;
        }

        .feature-box h3 {
            font-weight: 600;
            font-size: 25px;
            line-height: 120%;
            text-transform: capitalize;
            color: #FFFFFF;
            margin: 0;
        }

        .feature-content {
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .feature-content p {
            height: 78px;
            font-weight: 400;
            font-size: 16.4385px;
            line-height: 160%;
            text-transform: capitalize;
            color: #FFFFFF;
            opacity: 0.7;
            margin: 0;
        }

        .show-detail-link {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            font-weight: 400;
            font-size: 18px;
            line-height: 28px;
            text-transform: capitalize;
            color: #FFFFFF;
        }
        
        .show-detail-link svg {
            width: 24px;
            height: 24px;
        }

        /* Buttons */
        .button-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 43px;
            position: relative;
            width: 589px;
            z-index: 20;
        }

        .btn {
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 11px 0;
            width: 273px;
            height: 43px;
            border-radius: 24px;
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            font-size: 16px;
            text-align: center;
            text-transform: capitalize;
            text-decoration: none;
            transition: all 0.2s ease-in-out;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .btn-primary {
            background: #FFFFFF;
            border: 1px solid #DFDFDF;
            color: #000000;
        }

        .btn-secondary {
            border: 1px solid #DFDFDF;
            color: #DFDFDF;
        }
    </style>
"""

async def robot_body():
    return """
    <div class="page-wrapper">
        <div class="main-container"></div>
        <div class="glow"></div>
        
        <div class="heading-container">
            <h1>What We Offer</h1>
            <h2>Smarter, Faster, Automated</h2>
        </div>

        <div class="content-wrapper">
            <div class="features-wrapper">
                <!-- Feature Box 1: Real-Time Dashboards -->
                <div class="feature-box">
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

                <!-- Feature Box 3: AI-Powered Chatbots -->
                <div class="feature-box">
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
            </div>

            <img id="robot-image" src="../../Resources/Images/robotHomepage.png" alt="A sleek black robot with red highlights, symbolizing advanced automation and AI.">
            
            <div class="features-wrapper">
                <!-- Feature Box 2: Data-Driven Reports -->
                <div class="feature-box">
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

                <!-- Feature Box 4: Smart Outsourcing Solutions -->
                <div class="feature-box">
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

        <div class="button-container">
            <a href="#" class="btn btn-primary">See Our Dashboards</a>
            <a href="#" class="btn btn-secondary">Explore More Solutions</a>
        </div>
    </div>
"""
        