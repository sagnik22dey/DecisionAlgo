async def locations_body():
    return """
    <div class="locations-section">
        <div class="locations-grid">
            <!-- Location Card: United Kingdom -->
            <div class="location-card">
                <img src="../../Resources/Images/ContactUS/uk.png" alt="UK Flag" class="location-flag">
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
                <img src="../../Resources/Images/ContactUS/germany.png" alt="Germany Flag" class="location-flag">
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
                <img src="../../Resources/Images/ContactUS/india.png" alt="India Flag" class="location-flag">
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
            const isMobile = window.innerWidth <= 48;
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
        .locations-section {
            background-color: #1C1C1C;
            padding: 10vh 5vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .locations-grid {
            display: flex;
            justify-content: center;
            align-items: stretch; /* Make cards same height */
            gap: 2.5vw; /* Default for desktop */
            flex-wrap: wrap;
        }

        .location-card {
            width: 28vw; /* Default for desktop */
            background: linear-gradient(180deg, rgba(45, 45, 45, 0.5), rgba(30, 30, 30, 0.5));
            border: 0.1vh solid rgba(255, 255, 255, 0.1);
            border-radius: 2vw;
            padding: 5vh 2vw;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            box-shadow: 0 1vw 2vw rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(1.48vh);
            -webkit-backdrop-filter: blur(1.48vh);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            font-family: 'Poppins', sans-serif;
        }
        
        .location-card:hover {
            transform: translateY(-1vh);
            box-shadow: 0 1.5vw 3vw rgba(0, 0, 0, 0.3);
        }

        .location-flag {
            height: 6vh;
            width: auto;
            margin-bottom: 3vh;
            border-radius: 0.5vw;
            box-shadow: 0 0.5vw 1vw rgba(0, 0, 0, 0.2);
        }

        .location-title {
            font-size: 2.2vw;
            font-weight: 600;
            color: #AAAAAA;
            line-height: 1.2;
            margin-bottom: 4vh;
        }

        .location-title span {
            display: block;
            color: #FFFFFF;
            font-size: 2.2vw;
        }
        
        .location-details {
            font-size: 1.1vw;
            color: #CCCCCC;
            line-height: 1.6;
            margin-bottom: 4vh;
            flex-grow: 1; /* Pushes email to the bottom */
        }
        
        .location-details p {
            margin: 0;
        }

        .location-email {
            font-size: 1.1vw;
            color: #AAAAAA;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .location-email:hover {
            color: #FFFFFF;
        }
        
        /* Font size adjustments for mobile view */
        @media (max-width: 48vw) {
            .location-card {
                padding: 5vh 5vw;
                border-radius: 5vw;
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
