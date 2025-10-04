async def locations_body():
    return """
    <div class="locations-section">
        <div class="locations-grid">
            <!-- Location Card: United Kingdom -->
            <div class="location-card">
                <img src="/Images/ContactUs/uk_flag.png" alt="UK Flag" class="location-flag">
                <h2 class="location-title">
                    <span>Beaconsfield</span>
                    United Kingdom
                </h2>
                <div class="location-details">
                    <p>34 Hearnes Meadow, United Kingdom</p>
                    <p>+44 121661 8466</p>
                </div>
                <a href="mailto:communications@decisionalgo.com" class="location-email">communications@decisionalgo.com</a>
            </div>

            <!-- Location Card: Germany -->
            <div class="location-card">
                <img src="/Images/ContactUs/germany_flag.png" alt="Germany Flag" class="location-flag">
                <h2 class="location-title">
                    <span>Baden-Württemberg</span>
                    Germany
                </h2>
                <div class="location-details">
                    <p>Stuttgart</p>
                    <p>+49 1575 5833813</p>
                </div>
                <a href="mailto:communications@decisionalgo.com" class="location-email">communications@decisionalgo.com</a>
            </div>

            <!-- Location Card: India -->
            <div class="location-card">
                <img src="/Images/ContactUs/india_flag.png" alt="India Flag" class="location-flag">
                <h2 class="location-title">
                    <span>South-Delhi</span>
                    India
                </h2>
                <div class="location-details">
                    <p>Sansad Vihar, Dwarka</p>
                    <p>+91 9999 229 872</p>
                </div>
                <a href="mailto:communications@decisionalgo.com" class="location-email">communications@decisionalgo.com</a>
            </div>
        </div>
    </div>

    <script>
        function optimizeLocationsLayout() {
            const isMobile = window.innerWidth <= 768;
            const grid = document.querySelector('.locations-grid');
            const cards = document.querySelectorAll('.location-card');

            if (isMobile) {
                // Apply mobile styles
                grid.style.flexDirection = 'column';
                grid.style.gap = '5vh';
                cards.forEach(card => {
                    card.style.width = '90vw';
                });
            } else {
                // Revert to desktop styles by clearing inline styles
                grid.style.flexDirection = '';
                grid.style.gap = '';
                cards.forEach(card => {
                    card.style.width = '';
                });
            }
        }

        // Run on load and resize
        window.addEventListener('load', optimizeLocationsLayout);
        window.addEventListener('resize', optimizeLocationsLayout);
    </script>
    """


async def locations_style():
    return """
<style>
        /* --- Base & Structural Styles (Theme-Agnostic) --- */
        .locations-section {
            padding: 10vh 5vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .locations-grid {
            display: flex;
            justify-content: center;
            align-items: stretch; /* Make cards same height */
            gap: 2.5vw;
            flex-wrap: wrap;
        }

        .location-card {
            width: 28vw;
            border-radius: 2vw;
            padding: 3vw 2vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            font-family: 'Poppins', sans-serif;
        }
        
        .location-card:hover {
            transform: translateY(-1vw);
        }

        .location-flag {
            height: 11vw;
            width: auto;
            margin-bottom: 3vw;
            border-radius: 0.5vw;
        }

        .location-title {
            font-size: 2.2vw;
            font-weight: 600;
            line-height: 1.2;
            margin-bottom: 1vw;
        }

        .location-title span {
            display: block;
            font-size: 2.2vw;
        }
        
        .location-details {
            font-size: 1.1vw;
            line-height: 1.6;
            margin-bottom: 4vw;
            flex-grow: 1; /* Pushes email to the bottom */
        }
        
        .location-details p {
            margin: 0;
        }

        .location-email {
            font-size: 1.1vw;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        /* --- Theming Section --- */

        /* Light Theme */
        @media (prefers-color-scheme: light) {
            .locations-section {
                background-color: #FFFFFF;
            }
            .location-card {
                background: linear-gradient(145deg, #4dabf7 0%, #2573f5 100%);
                box-shadow: 0 1vw 2vw rgba(37, 150, 244, 0.25);
            }
            .location-card:hover {
                 box-shadow: 0 1.5vw 3vw rgba(37, 150, 244, 0.35);
            }
            .location-flag {
                box-shadow: 0 0.5vw 1vw rgba(0, 0, 0, 0.1);
            }
            .location-title { color: rgba(255, 255, 255, 0.9); }
            .location-title span { color: #FFFFFF; }
            .location-details { color: rgba(255, 255, 255, 0.9); }
            .location-email { color: rgba(255, 255, 255, 0.9); }
            .location-email:hover { color: #FFFFFF; }
        }

        /* Dark Theme */
        @media (prefers-color-scheme: dark) {
            .locations-section {
                background-color: transparent;
            }
            .location-card {
                background: linear-gradient(180deg, rgba(45, 45, 45, 0.5), rgba(30, 30, 30, 0.5));
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 1vw 2vw rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(1.48vw);
                -webkit-backdrop-filter: blur(1.48vw);
            }
            .location-card:hover {
                box-shadow: 0 1.5vw 3vw rgba(0, 0, 0, 0.3);
            }
            .location-flag {
                box-shadow: 0 0.5vw 1vw rgba(0, 0, 0, 0.2);
            }
            .location-title { color: #AAAAAA; }
            .location-title span { color: #FFFFFF; }
            .location-details { color: #CCCCCC; }
            .location-email { color: #AAAAAA; }
            .location-email:hover { color: #FFFFFF; }
        }
        
        /* Responsive Structural Adjustments */
        @media (max-width: 768px) {
            .location-card {
                padding: 5vw 5vw;
                border-radius: 2vw;
            }
            .location-title {
                font-size: 6vw;
            }
            .location-title span {
                font-size: 7vw;
            }
            .location-details, .location-email {
                font-size: 4vw;
            }
        }
</style>
    """