from fastapi import APIRouter
from fastapi.responses import HTMLResponse

async def footer_body():
    return """
        <footer class="footer-container">
        <!-- Top Section -->
        <div class="footer-top">
            <!-- As requested, here is a dummy image for the logo -->
            <img src="../../Resources/Images/silver_logo.png" alt="Decisionalgo Logo" class="logo">
            <div class="social-links">
                <a href="#"><span>Instagram</span><span>&rarr;</span></a>
                <a href="#"><span>Facebook</span><span>&rarr;</span></a>
                <a href="#"><span>YouTube</span><span>&rarr;</span></a>
            </div>
        </div>

        <!-- Middle Section -->
        <div class="footer-middle">
            <div class="link-column">
                <h3>Industries</h3>
                <ul>
                    <li>Consumer Packaged Goods</li>
                    <li>Retail</li>
                    <li>Financial Services</li>
                    <li>Insurance</li>
                    <li>Technology, Media & telecom</li>
                    <li>HealthCare & Life Sciences</li>
                </ul>
            </div>
            <div class="link-column">
                <h3>Quick Links</h3>
                <ul>
                    <li>Case Studies</li>
                    <li>About Us</li>
                    <li>Pricing</li>
                    <li>Contact Us</li>
                </ul>
            </div>
        </div>

        <!-- Bottom Section -->
        <div class="footer-bottom">
            <hr class="separator">
            <div class="bottom-content">
                <p class="copyright">&copy; 2024 Decisionalgo. All rights reserved.</p>
                <p class="partner">Digital Partner: Suflex Media</p>
            </div>
        </div>
    </footer>
    
    """
    
    
async def footer_style():
    return """ 
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* General Styles */
        a {
            color: inherit;
            text-decoration: none;
        }

        ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        /* Footer Container */
        .footer-container {
            background: linear-gradient(293.29deg, #090909 0.66%, rgba(37, 37, 37, 0.85) 27.54%, rgba(84, 84, 84, 0.62) 72.03%);
            padding: 60px 80px;
            display: flex;
            flex-direction: column;
            gap: 60px;
            border-radius: 55px 55px 0 0;
        }

        /* Top Section: Logo and Social Links */
        .footer-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 40px;
            padding-left:7rem;
        }

        .logo {
            max-width: 1107px;
            height: 239;
            object-fit: contain;
        }

        .social-links {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding-right:10rem;
        }

        .social-links a {
            font-size: 24px;
            font-weight: 400;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 170px; /* Helps align the arrows */
            transition: opacity 0.3s ease;
            opacity: 0.7;
        }
        .social-links a:hover {
            opacity: 1;
        }


        /* Middle Section: Link Columns */
        .footer-middle {
            display: flex;
            gap: 100px;
            flex-wrap: wrap;
        }

        .link-column{
            padding-left: 3rem;
        }
        .link-column h3 {
            font-size: 32px;
            font-weight: 600;
            margin: 0 0 15px 0;
            background: linear-gradient(90.01deg, #EBF3F3 16.31%, #EBF3F3 94.45%);
            -webkit-background-clip: text;
            -moz-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .link-column ul li {
            font-size: 18px;
            font-weight: 400;
            opacity: 0.7;
        }
        
        .link-column ul li::before {
             content: "• ";
             opacity: 0.8;
        }


        /* Bottom Section: Separator and Credits */
        .footer-bottom {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .separator {
            width: 100%;
            border: 0;
            height: 1px;
            background-color: #DDD7DE;
            opacity: 0.5;
        }

        .bottom-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
        }

        .copyright {
            font-size: 28px;
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90.01deg, rgba(235, 243, 243, 0.3) 0.01%, #EBF3F3 18.63%, #EBF3F3 65.13%, rgba(235, 243, 243, 0.3) 94.45%);
            -webkit-background-clip: text;
            -moz-background-clip: text;
            background-clip: text;
            color: transparent;
            padding-left:4rem;
        }

        .partner {
            font-size: 24px;
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
            padding-right:4rem;
        }

        /* Responsive Adjustments */
        @media (max-width: 1200px) {
            .logo {
                max-width: 450px;
            }
            .copyright {
                font-size: 24px;
            }
            .partner {
                font-size: 20px;
            }
        }
        
        @media (max-width: 992px) {
            .footer-container {
                padding: 50px 40px;
            }
            .footer-top {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 768px) {
            .footer-middle {
                flex-direction: column;
                gap: 40px;
            }
            .bottom-content {
                flex-direction: column;
                align-items: flex-start;
                gap: 15px;
            }
            .copyright {
                font-size: 20px;
            }
            .partner {
                font-size: 18px;
            }
        }
        
        @media (max-width: 576px) {
            .logo {
                max-width: 100%;
            }
             .copyright {
                font-size: 18px;
            }
            .partner {
                font-size: 16px;
            }
            .social-links a {
                font-size: 20px;
            }
            .link-column h3 {
                font-size: 28px;
            }
             .link-column ul li {
                font-size: 16px;
             }
        }
    </style>
    """
    