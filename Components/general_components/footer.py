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
            padding: 5.56vh 4.17vw; /* Original: 60px 80px */
            display: flex;
            flex-direction: column;
            gap: 5.56vh; /* Original: 60px */
            border-radius: 2.86vw 2.86vw 0 0; /* Original: 55px */
        }

        /* Top Section: Logo and Social Links */
        .footer-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 2.08vw; /* Original: 40px */
            padding-left: 5.83vw; /* Original: 7rem */
        }

        .logo {
            max-width: 57.66vw; /* Original: 1107px */
            height: 22.13vh; /* Original: 239px */
            object-fit: contain;
        }

        .social-links {
            display: flex;
            flex-direction: column;
            gap: 1.85vh; /* Original: 20px */
            padding-right: 8.33vw; /* Original: 10rem */
        }

        .social-links a {
            font-size: 1.25vw; /* Original: 24px */
            font-weight: 400;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 8.85vw; /* Original: 170px */
            transition: opacity 0.3s ease;
            opacity: 0.7;
        }
        .social-links a:hover {
            opacity: 1;
        }


        /* Middle Section: Link Columns */
        .footer-middle {
            display: flex;
            gap: 5.21vw; /* Original: 100px */
            flex-wrap: wrap;
        }

        .link-column{
            padding-left: 2.5vw; /* Original: 3rem */
        }
        
        .link-column h3 {
            font-size: 1.67vw; /* Original: 32px */
            font-weight: 600;
            margin: 0 0 1.39vh 0; /* Original: 15px */
            background: linear-gradient(90.01deg, #EBF3F3 16.31%, #EBF3F3 94.45%);
            -webkit-background-clip: text;
            -moz-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .link-column ul li {
            font-size: 0.94vw; /* Original: 18px */
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
            gap: 2.78vh; /* Original: 30px */
        }

        .separator {
            width: 100%;
            border: 0;
            height: 0.09vh; /* Original: 1px */
            background-color: #DDD7DE;
            opacity: 0.5;
        }

        .bottom-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.04vw; /* Original: 20px */
        }

        .copyright {
            font-size: 1.46vw; /* Original: 28px */
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90.01deg, rgba(235, 243, 243, 0.3) 0.01%, #EBF3F3 18.63%, #EBF3F3 65.13%, rgba(235, 243, 243, 0.3) 94.45%);
            -webkit-background-clip: text;
            -moz-background-clip: text;
            background-clip: text;
            color: transparent;
            padding-left: 3.33vw; /* Original: 4rem */
        }

        .partner {
            font-size: 1.25vw; /* Original: 24px */
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
            padding-right: 3.33vw; /* Original: 4rem */
        }

        /* Responsive Adjustments */
        @media (max-width: 62.5vw) { /* Original: 1200px */
            .logo {
                max-width: 23.44vw; /* Original: 450px */
            }
            .copyright {
                font-size: 1.25vw; /* Original: 24px */
            }
            .partner {
                font-size: 1.04vw; /* Original: 20px */
            }
        }
        
        @media (max-width: 51.67vw) { /* Original: 992px */
            .footer-container {
                padding: 4.63vh 2.08vw; /* Original: 50px 40px */
            }
            .footer-top {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 40vw) { /* Original: 768px */
            .footer-middle {
                flex-direction: column;
                gap: 3.7vh; /* Original: 40px */
            }
            .bottom-content {
                flex-direction: column;
                align-items: flex-start;
                gap: 1.39vh; /* Original: 15px */
            }
            .copyright {
                font-size: 1.04vw; /* Original: 20px */
            }
            .partner {
                font-size: 0.94vw; /* Original: 18px */
            }
        }
        
        @media (max-width: 30vw) { /* Original: 576px */
            .logo {
                max-width: 100%;
            }
             .copyright {
                font-size: 0.94vw; /* Original: 18px */
            }
            .partner {
                font-size: 0.83vw; /* Original: 16px */
            }
            .social-links a {
                font-size: 1.04vw; /* Original: 20px */
            }
            .link-column h3 {
                font-size: 1.46vw; /* Original: 28px */
            }
             .link-column ul li {
                font-size: 0.83vw; /* Original: 16px */
             }
        }
    </style>
    """