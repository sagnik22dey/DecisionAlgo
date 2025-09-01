async def footer_body():
    return """
        <!-- Desktop Footer -->
        <footer class="footer-container desktop-footer">
            <!-- Top Section -->
            <div class="footer-top">
                <!-- As requested, here is a dummy image for the logo -->
                <img src="../../Resources/Images/silver_logo.png" alt="Decisionalgo Logo" class="logo">
                <div class="social-links">
                    <a href="#"><span>Instagram</span><span><svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg></span></a>
                    <a href="#"><span>Facebook</span><span><svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg></span></a>
                    <a href="#"><span>YouTube</span><span><svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3.75 12.5L20.25 12.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13.5 5.75V5.75C14.6595 8.55205 16.8074 10.8309 19.5361 12.1538L20.25 12.5L19.1908 13.0777C16.6674 14.4542 14.6674 16.6233 13.5 19.25V19.25" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg></span></a>
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
        
        <!-- Mobile Footer (Updated Structure) -->
        <footer class="footer-container mobile-footer">
            <!-- Main Content: Logo + Link Columns -->
            <div class="mobile-main-content">
                <img src="../../Resources/Images/silver_logo.png" alt="Decisionalgo Logo" class="logo mobile-logo">
                <div class="mobile-links-wrapper">
                    <div class="link-column mobile-column">
                        <h3 class="mobile-heading">Industries</h3>
                        <ul class="mobile-list">
                            <li class="mobile-item">Consumer Packaged Goods</li>
                            <li class="mobile-item">Retail</li>
                            <li class="mobile-item">Financial Services</li>
                            <li class="mobile-item">Insurance</li>
                            <li class="mobile-item">Technology, Media & telecom</li>
                            <li class="mobile-item">HealthCare & Life Sciences</li>
                        </ul>
                    </div>
                    <div class="link-column mobile-column">
                        <h3 class="mobile-heading">Quick Links</h3>
                        <ul class="mobile-list">
                            <li class="mobile-item">Case Studies</li>
                            <li class="mobile-item">About Us</li>
                            <li class="mobile-item">Pricing</li>
                            <li class="mobile-item">Contact Us</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Social Links Section -->
            <div class="social-links mobile-social">
                <a href="#" class="mobile-social-link"><span>Instagram</span></a>
                <a href="#" class="mobile-social-link"><span>Facebook</span></a>
                <a href="#" class="mobile-social-link"><span>YouTube</span></a>
            </div>

            <!-- Mobile Bottom Section -->
            <div class="footer-bottom mobile-bottom">
                <hr class="separator mobile-separator">
                <div class="bottom-content mobile-content">
                    <p class="copyright mobile-copyright">&copy; 2024 Decisionalgo. All rights reserved.</p>
                    <p class="partner mobile-partner">Digital Partner: Suflex Media</p>
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

        /* Base Footer Container */
        .footer-container {
            font-family: 'Exo 2', sans-serif;
            background: linear-gradient(293.29deg, #090909 0.66%, rgba(37, 37, 37, 0.85) 27.54%, rgba(84, 84, 84, 0.62) 72.03%);
            display: flex;
            flex-direction: column;
            border-radius: 55px 55px 0 0;
            color: #ffffff;
        }

        /* Desktop Footer Styles */
        .desktop-footer {
            padding: 3.75rem 5rem; /* 60px 80px */
            gap: 3.75rem; /* 60px */
            display: block;
        }

        .desktop-footer .footer-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 2.5rem; /* 40px */
            padding-left: 7rem;
        }

        .desktop-footer .logo {
            max-width: 100vh;
            height: auto;
            object-fit: contain;
        }

        .desktop-footer .social-links {
            display: flex;
            flex-direction: column;
            gap: 1.25rem; /* 20px */
            padding-right: 10rem;
        }

        .desktop-footer .social-links a {
            font-size: 1.25rem; /* 20px */
            font-weight: 400;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 170px;
            transition: opacity 0.3s ease;
            opacity: 0.7;
        }

        .desktop-footer .social-links a:hover {
            opacity: 1;
        }

        .desktop-footer .footer-middle {
            display: flex;
            gap: 6.25rem; /* 100px */
            flex-wrap: wrap;
        }

        .desktop-footer .link-column {
            padding-left: 3rem;
        }
        
        .desktop-footer .link-column h3 {
            font-size: 1.75rem; /* 28px */
            font-weight: 600;
            margin: 0 0 1rem 0; /* 16px */
            background: linear-gradient(90.01deg, #EBF3F3 16.31%, #EBF3F3 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .desktop-footer .link-column ul li {
            font-size: 1rem; /* 16px */
            font-weight: 400;
            opacity: 0.7;
            line-height: 1.8;
            padding-left: 0.5rem;
        }
        
        .desktop-footer .link-column ul li::before {
             content: "•";
             margin-right: 0.5rem;
             opacity: 0.8;
        }

        .desktop-footer .footer-bottom {
            display: flex;
            flex-direction: column;
            gap: 1.875rem; /* 30px */
        }

        .desktop-footer .separator {
            width: 100%;
            border: 0;
            height: 1px;
            background-color: #DDD7DE;
            opacity: 0.5;
        }

        .desktop-footer .bottom-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.25rem; /* 20px */
        }

        .desktop-footer .copyright {
            font-size: 1.5rem; /* 24px */
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90.01deg, rgba(235, 243, 243, 0.3) 0.01%, #EBF3F3 18.63%, #EBF3F3 65.13%, rgba(235, 243, 243, 0.3) 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            padding-left: 4rem;
        }

        .desktop-footer .partner {
            font-size: 1.25rem; /* 20px */
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
            padding-right: 4rem;
        }

        /* Mobile Footer Styles (Updated) */
        .mobile-footer {
            padding: 2.5rem 1.5rem; /* 40px 24px */
            gap: 2.5rem; /* 40px */
            border-radius: 40px 40px 0 0;
            display: none;
        }

        .mobile-footer .mobile-main-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2.5rem; /* 40px */
            width: 100%;
        }

        .mobile-footer .mobile-logo {
            max-width: 220px; /* Reduced logo size */
        }

        .mobile-footer .mobile-links-wrapper {
            display: flex;
            justify-content: space-around;
            width: 100%;
            gap: 1.5rem; /* Space between the two columns */
        }

        .mobile-footer .mobile-social {
            display: flex;
            flex-direction: row; /* Display links side-by-side */
            justify-content: center;
            align-items: center;
            gap: 1.5rem; /* Space between links */
            flex-wrap: wrap;
        }

        .mobile-footer .mobile-social-link {
            font-size: 1rem; /* 16px */
            font-weight: 400;
            opacity: 0.7;
            transition: opacity 0.3s ease;
        }

        .mobile-footer .mobile-social-link:hover {
            opacity: 1;
        }

        .mobile-footer .mobile-column {
            text-align: left; /* Align column content to the left */
        }
        
        .mobile-footer .mobile-heading {
            font-size: 1.5rem; /* 24px */
            font-weight: 600;
            margin: 0 0 1rem 0;
            background: linear-gradient(90.01deg, #EBF3F3 16.31%, #EBF3F3 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-align: center; /* Keep heading centered */
        }

        .mobile-footer .mobile-list {
            display: flex;
            flex-direction: column;
        }

        .mobile-footer .mobile-item {
            font-size: 0.9rem; /* 14.4px */
            font-weight: 400;
            opacity: 0.7;
            line-height: 1.8;
        }

        .mobile-footer .mobile-item::before {
             content: "•";
             margin-right: 0.5rem;
             opacity: 0.8;
        }

        .mobile-footer .mobile-bottom {
            display: flex;
            flex-direction: column;
            gap: 1.875rem; /* 30px */
        }

        .mobile-footer .mobile-separator {
            width: 100%;
            border: 0;
            height: 1px;
            background-color: #DDD7DE;
            opacity: 0.5;
        }

        .mobile-footer .mobile-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem; /* 16px */
            text-align: center;
        }

        .mobile-footer .mobile-copyright {
            font-size: 1.2rem; /* 19px */
            font-weight: 700;
            margin: 0;
            background: linear-gradient(90.01deg, rgba(235, 243, 243, 0.3) 0.01%, #EBF3F3 18.63%, #EBF3F3 65.13%, rgba(235, 243, 243, 0.3) 94.45%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .mobile-footer .mobile-partner {
            font-size: 1rem; /* 16px */
            font-weight: 400;
            margin: 0;
            opacity: 0.9;
        }
    </style>
    """
async def footer_script():
    return """
    <script>
        function toggleFooterView() {
            const desktopFooter = document.querySelector('.desktop-footer');
            const mobileFooter = document.querySelector('.mobile-footer');
            
            function checkScreenSize() {
                const isMobile = window.innerWidth <= 768;
                
                if (isMobile) {
                    desktopFooter.style.display = 'none';
                    mobileFooter.style.display = 'flex';
                } else {
                    desktopFooter.style.display = 'flex';
                    mobileFooter.style.display = 'none';
                }
            }
            
            // Check on initial load
            checkScreenSize();
            
            // Check on window resize
            window.addEventListener('resize', checkScreenSize);
        }
        
        // Initialize footer toggle when DOM is loaded
        document.addEventListener('DOMContentLoaded', toggleFooterView);
    </script>
    """