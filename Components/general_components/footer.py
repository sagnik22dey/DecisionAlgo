async def footer_body():
    return """
        <footer class="footer-container">
            <!-- Top Section: Logo & Social Links -->
            <div class="footer-top">
                <img src="../../Resources/Images/HomePage/silver_logo.png" alt="Decisionalgo Logo" class="logo">
                <div class="social-links">
                    <a href="#">
                        <span>Instagram</span>
                        <span class="social-arrow">
                            <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                    </a>
                    <a href="#">
                        <span>Facebook</span>
                        <span class="social-arrow">
                           <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                    </a>
                    <a href="#">
                        <span>YouTube</span>
                        <span class="social-arrow">
                            <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </span>
                    </a>
                </div>
            </div>

            <!-- Middle Section: Link Columns -->
            <div class="footer-middle">
                <div class="link-column">
                    <h3>Industries</h3>
                    <ul>
                        <li><a href="/casestudy/customer_package_goods" style="color: white; text-decoration: none;">Consumer Packaged Goods</a></li>
                        <li><a href="/casestudy/retail_firm" style="color: white; text-decoration: none;">Retail</a></li>
                        <li><a href="/casestudy/financial" style="color: white; text-decoration: none;">Financial Services</a></li>
                        <li><a href="/casestudy/insurance" style="color: white; text-decoration: none;">Insurance</a></li>
                        <li><a href="/casestudy/tech_media_telecom" style="color: white; text-decoration: none;">Technology, Media & Telecom</a></li>
                        <li><a href="/casestudy/healthcare" style="color: white; text-decoration: none;">HealthCare & Life Sciences</a></li>
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

            <!-- Mobile Social Links Section (Hidden on Desktop) -->
            <div class="mobile-social-links">
                <a href="#">
                    <span>Instagram</span>
                    <span class="social-arrow">
                        <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </span>
                </a>
                <a href="#">
                    <span>Facebook</span>
                    <span class="social-arrow">
                       <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </span>
                </a>
                <a href="#">
                    <span>YouTube</span>
                    <span class="social-arrow">
                        <svg viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </span>
                </a>
            </div>

            <!-- Bottom Section: Copyright Info -->
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
        /* --- Base & Desktop Styles --- */
        
        .footer-container {
            font-family: 'Exo 2', sans-serif;
            background: linear-gradient(293.29deg, #090909 0.66%, rgba(37, 37, 37, 0.85) 27.54%, rgba(84, 84, 84, 0.62) 72.03%);
            display: flex;
            flex-direction: column;
            border-radius: 3vw 3vw 0 0;
            color: #ffffff;
            padding: 4vh 5vw;
            gap: 4vh;
            box-sizing: border-box;
            border-top: 0.1vh solid #DDD7DE;
        }

        .footer-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 2vw;
            padding-left: 3.5vw;
        }

        .logo {
            width: 50vw;
            max-width: 50vw; /* Max size for very large screens */
            height: auto;
            object-fit: contain;
        }

        .social-links {
            display: flex;
            flex-direction: column;
            gap: 2vh;
            padding-right: 5vw;
        }

        .social-links a {
            font-size: 1.2vw;
            font-weight: 400;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 9vw;
            transition: opacity 0.3s ease;
            opacity: 0.7;
            text-decoration: none;
            color: inherit;
        }

        .social-links a:hover {
            opacity: 1;
        }
        
        .social-arrow svg {
            width: 1.2vw;
            height: auto;
        }

        /* Hide mobile social links on desktop */
        .mobile-social-links {
            display: none;
        }

        .footer-middle {
            display: flex;
            gap: 5vw;
            flex-wrap: wrap;
        }

        .link-column {
            padding-left: 1.5vw;
        }
        
        .link-column h3 {
            font-size: 1.5vw;
            font-weight: 600;
            margin: 0 0 2vh 0;
            background: linear-gradient(90.01deg, #EBF3F3 16.31%, #EBF3F3 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .link-column ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .link-column ul li {
            font-size: 0.9vw;
            font-weight: 400;
            opacity: 0.7;
            line-height: 1.8;
            padding-left: 0.5vw;
        }
        
        .link-column ul li::before {
             content: "•";
             margin-right: 0.5vw;
             opacity: 0.8;
        }

        .footer-bottom {
            display: flex;
            flex-direction: column;
            gap: 3vh;
        }

        .separator {
            width: 100%;
            border: 0;
            height: 0.1vh;
            background-color: #DDD7DE;
            opacity: 0.5;
        }

        .bottom-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.5vw;
        }

        .copyright {
            font-size: 1.3vw;
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90.01deg, rgba(235, 243, 243, 0.3) 0.01%, #EBF3F3 18.63%, #EBF3F3 65.13%, rgba(235, 243, 243, 0.3) 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            padding-left: 2vw;
        }

        .partner {
            font-size: 1.1vw;
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
            padding-right: 2vw;
        }

        /* --- Elegant & Aesthetic Mobile View --- */
        @media (max-width: 48vw) {
            .footer-container {
                padding: 8vh 6vw;
                gap: 6vh;
                border-radius: 8vw 8vw 0 0;
                display: flex;
                flex-direction: column;
            }

            .footer-top {
                display: flex;
                flex-direction: column;
                align-items: center; /* Center logo */
                gap: 6vh;
                padding: 0; /* Reset padding */
                order: 1; /* Logo section first */
            }
            
            .logo {
                width: 50vw; /* Larger, more prominent logo */
                max-width: 26.04vw;
            }
            
            /* Hide original social links in footer-top for mobile */
            .footer-top .social-links {
                display: none;
            }

            .footer-middle {
                flex-direction: row; /* Display link columns side by side */
                justify-content: space-between; /* Space them evenly */
                text-align: center; /* Center headings and links */
                gap: 8vw; /* Adequate spacing between columns */
                order: 2; /* Middle section second */
            }
            
            .link-column {
                padding: 0;
                flex: 1; /* Each column takes equal space */
                min-width: 0; /* Allow shrinking if needed */
            }

            .link-column h3 {
                font-size: 5.5vw;
                margin-bottom: 2vh;
                text-align: left;
            }

            .link-column ul li {
                font-size: 3.5vw; /* Slightly smaller font for better fit */
                line-height: 1.8; /* Tighter line height for mobile */
                padding-left: 0;
                text-align: left;
            }
            
            .link-column ul li::before {
                content: ""; /* Remove bullet points for cleaner look */
                margin-right: 0;
            }
            
            /* Show and style mobile social links */
            .mobile-social-links {
                display: flex;
                flex-direction: row;
                justify-content: center;
                gap: 8vw;
                padding: 0;
                width: 100%;
                order: 3; /* Position after footer-middle */
            }

            .mobile-social-links a {
                font-size: 4vw;
                font-weight: 400;
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: auto;
                transition: opacity 0.3s ease;
                opacity: 0.7;
                text-decoration: none;
                color: inherit;
            }

            .mobile-social-links a:hover {
                opacity: 1;
            }
            
            .mobile-social-links .social-arrow {
                display: none; /* Hide arrow icon for a cleaner mobile look */
            }

            .footer-bottom {
                order: 4; /* Bottom section is last */
                gap: 3vh;
            }
            
            .bottom-content {
                flex-direction: column; /* Stack copyright and partner */
                text-align: center;
                gap: 1.5vh;
            }

            .copyright {
                font-size: 4vw;
                padding: 0;
            }

            .partner {
                font-size: 3.5vw;
                padding: 0;
            }
        }
    </style>
    """

async def footer_script():
    return "" # No script is needed with the pure CSS solution