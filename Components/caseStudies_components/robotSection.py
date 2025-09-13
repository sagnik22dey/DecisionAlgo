async def robotSection_style():
    return """
<style>

            :root {
            --primary-blue: #5FC7FB;
            --primary-white: #FEFEFE;
            --primary-gray: #CCCCCC;
            --background-dark: #0A0A0A;
            --card-bg: rgba(20, 20, 20, 0.4);
            --card-border: rgba(95, 199, 251, 0.5);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
            .solutions-section {
                width: 100vw;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 5vh 5vw;
                position: relative;
                overflow: hidden;
            }

            .main-content {
                position: relative;
                width: 75vw;
                height: 80vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .robot-container {
                position: relative;
                width: 30vw;
                height: 75vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .robot-image {
                position: absolute;
                height: 100%;
                width: auto;
                object-fit: contain;
                z-index: 2;
            }

            .solution-card {
                box-sizing: border-box;
                position: absolute;
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                padding: 1.5vw;
                gap: 1.5vh;
                width: 13vw;
                height: 10vw;
                background: rgba(10, 10, 10, 0.5);
                border: 0.14vh solid rgba(95, 199, 251, 0.5);
                border-radius: 1vw;
                backdrop-filter: blur(1.77vh);
                -webkit-backdrop-filter: blur(1.77vh);
                z-index: 4;
                transition: transform 0.3s ease, border-color 0.3s ease;
            }
            
            .solution-card:hover {
                transform: scale(1.05);
                border-color: var(--primary-blue);
            }

            .icon-box {
                box-sizing: border-box;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 0.5vw;
                width: 3vw;
                height: 3vw;
                border: 0.14vh solid var(--primary-blue);
                border-radius: 0.5vw;
            }

            .icon-box svg {
                width: 2vw;
                height: 2vw;
                fill: var(--primary-blue);
            }

            .card-text {
                font-size: 1vw;
                line-height: 1.4;
                font-weight: 500;
                text-transform: capitalize;
                color: var(--primary-white);
            }

            /* Positioning the cards for desktop */
            #card-bhc { top: 5vh; left: 0; }
            #card-hw { top: 30vh; left: 0; }
            #card-hc { top: 55vh; left: 0; }
            #card-pfc { top: 10vh; right: 0; }
            #card-pfb { top: 40vh; right: 0; }

            .connector-lines {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 3;
            }
            
            .connector-lines polyline {
                stroke: var(--primary-white);
                stroke-width: 0.15; /* This is relative to the viewBox */
                fill: none;
            }

            .connector-lines circle {
                fill: var(--primary-white);
            }
            .eclipse-glow {
                width: 50vw;
                right: 25%;
                top: 20vh;
                z-index:1;
                position:absolute;
            }

            /* --- Mobile View --- */
            @media (max-width: 768px) {
                .solutions-section {
                    height: auto;
                    min-height: auto;
                    padding: 10vh 5vw;
                    justify-content: flex-start;
                }
                
                .main-content {
                    flex-direction: column;
                    align-items: center;
                    position: static;
                    height: auto;
                    width: 100%;
                    margin-top: 5vh;
                }

                .robot-container {
                    width: 70vw;
                    height: 40vh;
                    margin-bottom: 8vh;
                }

                .solution-card {
                    position: static;
                    width: 90vw;
                    height: auto;
                    min-height: auto;
                    margin-bottom: 4vh;
                    padding: 6vw;
                    gap: 3vh;
                    border-radius: 3vw;
                }

                .icon-box {
                    width: 12vw;
                    height: 12vw;
                    border-radius: 2.5vw;
                }

                .icon-box svg {
                    width: 6vw;
                    height: 6vw;
                }

                .card-text {
                    font-size: 4.5vw;
                    line-height: 1.5;
                }
                
                .eclipse-glow {
                    width: 150vw;
                    right: -25vw;
                    top: 25vh;
                    opacity: 0.3;
                }

                /* Hide desktop-only elements */
                .connector-lines {
                    display: none !important;
                }
            }
</style>
"""


async def robotSection_body(folderName,text1,text2,text3,text4,text5):
    part1 = f"""
        <img class="eclipse-glow" src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="eclipse glow">
        <section class="solutions-section">

            <div class="main-content">
                <!-- SVG lines will be drawn here by JavaScript for desktop -->
                <svg class="connector-lines" viewBox="0 0 100 100" preserveAspectRatio="none">
                    <polyline id="line-for-card-bhc"></polyline>
                    <path class="connector-dot" id="start-dot-for-card-bhc"></path>
                    <path class="connector-dot" id="end-dot-for-card-bhc"></path>
                    
                    <polyline id="line-for-card-hw"></polyline>
                    <path class="connector-dot" id="start-dot-for-card-hw"></path>
                    <path class="connector-dot" id="end-dot-for-card-hw"></path>

                    <polyline id="line-for-card-hc"></polyline>
                    <path class="connector-dot" id="start-dot-for-card-hc"></path>
                    <path class="connector-dot" id="end-dot-for-card-hc"></path>

                    <polyline id="line-for-card-pfc"></polyline>
                    <path class="connector-dot" id="start-dot-for-card-pfc"></path>
                    <path class="connector-dot" id="end-dot-for-card-pfc"></path>

                    <polyline id="line-for-card-pfb"></polyline>
                    <path class="connector-dot" id="start-dot-for-card-pfb"></path>
                    <path class="connector-dot" id="end-dot-for-card-pfb"></path>
                </svg>
                
                <div class="robot-container">
                    <img src="../../Resources/Images/CaseStudies/{folderName}/robot.png" alt="Advanced Solutions Robot" class="robot-image">
                </div>

                <!-- Card 1 -->
                <div class="solution-card" id="card-bhc">
                    <div class="icon-box">
                    <svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_374_551" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257812" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_374_551)">
                    <path d="M18.2259 30.2042C16.8284 30.2042 15.5119 29.9858 14.2766 29.5491C13.0413 29.1124 11.9121 28.4947 10.8889 27.6961L8.79257 29.755C8.51805 30.0295 8.16867 30.1668 7.74442 30.1668C7.32017 30.1668 6.97079 30.0295 6.69628 29.755C6.42176 29.4805 6.2845 29.1311 6.2845 28.7069C6.2845 28.2826 6.42176 27.9332 6.69628 27.6587L8.75514 25.5999C7.95655 24.5767 7.33889 23.4412 6.90216 22.1934C6.46543 20.9456 6.24707 19.6229 6.24707 18.2254C6.24707 14.8813 7.40752 12.0488 9.72841 9.72793C12.0493 7.40703 14.8818 6.24658 18.2259 6.24658H30.2047V18.2254C30.2047 21.5695 29.0443 24.402 26.7234 26.7229C24.4025 29.0438 21.57 30.2042 18.2259 30.2042ZM18.2259 27.2095C20.7215 27.2095 22.8427 26.3361 24.5896 24.5891C26.3365 22.8422 27.21 20.721 27.21 18.2254V9.24129H18.2259C15.7303 9.24129 13.6091 10.1147 11.8621 11.8617C10.1152 13.6086 9.24177 15.7298 9.24177 18.2254C9.24177 19.1987 9.39151 20.1283 9.69098 21.0142C9.99045 21.9001 10.4022 22.705 10.9263 23.4287L18.6751 15.6799C18.9496 15.4054 19.299 15.2681 19.7232 15.2681C20.1475 15.2681 20.4969 15.4054 20.7714 15.6799C21.0709 15.9794 21.2206 16.335 21.2206 16.7468C21.2206 17.1585 21.0709 17.5142 20.7714 17.8136L13.0226 25.5624C13.7463 26.0865 14.5511 26.492 15.4371 26.779C16.323 27.066 17.2526 27.2095 18.2259 27.2095Z" fill="#5FC7FB"/>
                    </g>
                    </svg>
                    </div>
                    <p class="card-text">{text1}</p>
                </div>
                <!-- Card 2 -->
                <div class="solution-card" id="card-hw">
                    <div class="icon-box">
                    <svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_374_551" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257812" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_374_551)">
                    <path d="M18.2259 30.2042C16.8284 30.2042 15.5119 29.9858 14.2766 29.5491C13.0413 29.1124 11.9121 28.4947 10.8889 27.6961L8.79257 29.755C8.51805 30.0295 8.16867 30.1668 7.74442 30.1668C7.32017 30.1668 6.97079 30.0295 6.69628 29.755C6.42176 29.4805 6.2845 29.1311 6.2845 28.7069C6.2845 28.2826 6.42176 27.9332 6.69628 27.6587L8.75514 25.5999C7.95655 24.5767 7.33889 23.4412 6.90216 22.1934C6.46543 20.9456 6.24707 19.6229 6.24707 18.2254C6.24707 14.8813 7.40752 12.0488 9.72841 9.72793C12.0493 7.40703 14.8818 6.24658 18.2259 6.24658H30.2047V18.2254C30.2047 21.5695 29.0443 24.402 26.7234 26.7229C24.4025 29.0438 21.57 30.2042 18.2259 30.2042ZM18.2259 27.2095C20.7215 27.2095 22.8427 26.3361 24.5896 24.5891C26.3365 22.8422 27.21 20.721 27.21 18.2254V9.24129H18.2259C15.7303 9.24129 13.6091 10.1147 11.8621 11.8617C10.1152 13.6086 9.24177 15.7298 9.24177 18.2254C9.24177 19.1987 9.39151 20.1283 9.69098 21.0142C9.99045 21.9001 10.4022 22.705 10.9263 23.4287L18.6751 15.6799C18.9496 15.4054 19.299 15.2681 19.7232 15.2681C20.1475 15.2681 20.4969 15.4054 20.7714 15.6799C21.0709 15.9794 21.2206 16.335 21.2206 16.7468C21.2206 17.1585 21.0709 17.5142 20.7714 17.8136L13.0226 25.5624C13.7463 26.0865 14.5511 26.492 15.4371 26.779C16.323 27.066 17.2526 27.2095 18.2259 27.2095Z" fill="#5FC7FB"/>
                    </g>
                    </svg>
                    </div>
                    <p class="card-text">{text2}</p>
                </div>
                <!-- Card 3 -->
                <div class="solution-card" id="card-hc">
                    <div class="icon-box">
                    <svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_374_551" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257812" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_374_551)">
                    <path d="M18.2259 30.2042C16.8284 30.2042 15.5119 29.9858 14.2766 29.5491C13.0413 29.1124 11.9121 28.4947 10.8889 27.6961L8.79257 29.755C8.51805 30.0295 8.16867 30.1668 7.74442 30.1668C7.32017 30.1668 6.97079 30.0295 6.69628 29.755C6.42176 29.4805 6.2845 29.1311 6.2845 28.7069C6.2845 28.2826 6.42176 27.9332 6.69628 27.6587L8.75514 25.5999C7.95655 24.5767 7.33889 23.4412 6.90216 22.1934C6.46543 20.9456 6.24707 19.6229 6.24707 18.2254C6.24707 14.8813 7.40752 12.0488 9.72841 9.72793C12.0493 7.40703 14.8818 6.24658 18.2259 6.24658H30.2047V18.2254C30.2047 21.5695 29.0443 24.402 26.7234 26.7229C24.4025 29.0438 21.57 30.2042 18.2259 30.2042ZM18.2259 27.2095C20.7215 27.2095 22.8427 26.3361 24.5896 24.5891C26.3365 22.8422 27.21 20.721 27.21 18.2254V9.24129H18.2259C15.7303 9.24129 13.6091 10.1147 11.8621 11.8617C10.1152 13.6086 9.24177 15.7298 9.24177 18.2254C9.24177 19.1987 9.39151 20.1283 9.69098 21.0142C9.99045 21.9001 10.4022 22.705 10.9263 23.4287L18.6751 15.6799C18.9496 15.4054 19.299 15.2681 19.7232 15.2681C20.1475 15.2681 20.4969 15.4054 20.7714 15.6799C21.0709 15.9794 21.2206 16.335 21.2206 16.7468C21.2206 17.1585 21.0709 17.5142 20.7714 17.8136L13.0226 25.5624C13.7463 26.0865 14.5511 26.492 15.4371 26.779C16.323 27.066 17.2526 27.2095 18.2259 27.2095Z" fill="#5FC7FB"/>
                    </g>
                    </svg>
                    </div>
                    <p class="card-text">{text3}</p>
                </div>
                <!-- Card 4 -->
                <div class="solution-card" id="card-pfc">
                    <div class="icon-box">
                    <svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_374_551" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257812" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_374_551)">
                    <path d="M18.2259 30.2042C16.8284 30.2042 15.5119 29.9858 14.2766 29.5491C13.0413 29.1124 11.9121 28.4947 10.8889 27.6961L8.79257 29.755C8.51805 30.0295 8.16867 30.1668 7.74442 30.1668C7.32017 30.1668 6.97079 30.0295 6.69628 29.755C6.42176 29.4805 6.2845 29.1311 6.2845 28.7069C6.2845 28.2826 6.42176 27.9332 6.69628 27.6587L8.75514 25.5999C7.95655 24.5767 7.33889 23.4412 6.90216 22.1934C6.46543 20.9456 6.24707 19.6229 6.24707 18.2254C6.24707 14.8813 7.40752 12.0488 9.72841 9.72793C12.0493 7.40703 14.8818 6.24658 18.2259 6.24658H30.2047V18.2254C30.2047 21.5695 29.0443 24.402 26.7234 26.7229C24.4025 29.0438 21.57 30.2042 18.2259 30.2042ZM18.2259 27.2095C20.7215 27.2095 22.8427 26.3361 24.5896 24.5891C26.3365 22.8422 27.21 20.721 27.21 18.2254V9.24129H18.2259C15.7303 9.24129 13.6091 10.1147 11.8621 11.8617C10.1152 13.6086 9.24177 15.7298 9.24177 18.2254C9.24177 19.1987 9.39151 20.1283 9.69098 21.0142C9.99045 21.9001 10.4022 22.705 10.9263 23.4287L18.6751 15.6799C18.9496 15.4054 19.299 15.2681 19.7232 15.2681C20.1475 15.2681 20.4969 15.4054 20.7714 15.6799C21.0709 15.9794 21.2206 16.335 21.2206 16.7468C21.2206 17.1585 21.0709 17.5142 20.7714 17.8136L13.0226 25.5624C13.7463 26.0865 14.5511 26.492 15.4371 26.779C16.323 27.066 17.2526 27.2095 18.2259 27.2095Z" fill="#5FC7FB"/>
                    </g>
                    </svg>
                    </div>
                    <p class="card-text">{text4}</p>
                </div>
                <!-- Card 5 -->
                <div class="solution-card" id="card-pfb">
                    <div class="icon-box">
                    <svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_374_551" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257812" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_374_551)">
                    <path d="M18.2259 30.2042C16.8284 30.2042 15.5119 29.9858 14.2766 29.5491C13.0413 29.1124 11.9121 28.4947 10.8889 27.6961L8.79257 29.755C8.51805 30.0295 8.16867 30.1668 7.74442 30.1668C7.32017 30.1668 6.97079 30.0295 6.69628 29.755C6.42176 29.4805 6.2845 29.1311 6.2845 28.7069C6.2845 28.2826 6.42176 27.9332 6.69628 27.6587L8.75514 25.5999C7.95655 24.5767 7.33889 23.4412 6.90216 22.1934C6.46543 20.9456 6.24707 19.6229 6.24707 18.2254C6.24707 14.8813 7.40752 12.0488 9.72841 9.72793C12.0493 7.40703 14.8818 6.24658 18.2259 6.24658H30.2047V18.2254C30.2047 21.5695 29.0443 24.402 26.7234 26.7229C24.4025 29.0438 21.57 30.2042 18.2259 30.2042ZM18.2259 27.2095C20.7215 27.2095 22.8427 26.3361 24.5896 24.5891C26.3365 22.8422 27.21 20.721 27.21 18.2254V9.24129H18.2259C15.7303 9.24129 13.6091 10.1147 11.8621 11.8617C10.1152 13.6086 9.24177 15.7298 9.24177 18.2254C9.24177 19.1987 9.39151 20.1283 9.69098 21.0142C9.99045 21.9001 10.4022 22.705 10.9263 23.4287L18.6751 15.6799C18.9496 15.4054 19.299 15.2681 19.7232 15.2681C20.1475 15.2681 20.4969 15.4054 20.7714 15.6799C21.0709 15.9794 21.2206 16.335 21.2206 16.7468C21.2206 17.1585 21.0709 17.5142 20.7714 17.8136L13.0226 25.5624C13.7463 26.0865 14.5511 26.492 15.4371 26.779C16.323 27.066 17.2526 27.2095 18.2259 27.2095Z" fill="#5FC7FB"/>
                    </g>
                    </svg>
                    </div>
                    <p class="card-text">{text5}</p>
                </div>

            </div>
        </section>
    """
    
    script = """
        <style>
            .connector-lines polyline {
                fill: none;
                stroke: white;
                stroke-width: 0.15;
            }
            .connector-lines .connector-dot {
                stroke: white;
                stroke-linecap: round;
                stroke-width: 1vh; /* This determines the dot's diameter */
                /* This key property ensures the stroke (our dot) isn't distorted by scaling */
                vector-effect: non-scaling-stroke;
            }
        </style>

        <script>
            document.addEventListener('DOMContentLoaded', () => {

                function drawLines() {
                    // This function is only for desktop view
                    if (window.innerWidth <= 768) {
                        const svg = document.querySelector('.connector-lines');
                        if(svg) svg.style.display = 'none';
                        return;
                    }

                    const svg = document.querySelector('.connector-lines');
                    if(svg) svg.style.display = 'block';

                    const container = document.querySelector('.main-content');
                    if (!container) return;
                    
                    const cards = document.querySelectorAll('.solution-card');
                    const containerRect = container.getBoundingClientRect();
                    
                    // Define target points on the robot image relative to the container
                    // Values are in percentage (x, y)
                    const targets = {
                        'card-bhc': { x: 40, y: 25 },
                        'card-hw':  { x: 38, y: 50 },
                        'card-hc':  { x: 42, y: 80 },
                        'card-pfc': { x: 60, y: 35 },
                        'card-pfb': { x: 62, y: 65 }
                    };

                    cards.forEach(card => {
                        const cardId = card.id;
                        const line = document.getElementById(`line-for-${cardId}`);
                        const startDot = document.getElementById(`start-dot-for-${cardId}`);
                        const endDot = document.getElementById(`end-dot-for-${cardId}`);

                        if (!line || !startDot || !endDot) return;

                        const cardRect = card.getBoundingClientRect();
                        const target = targets[cardId];

                        // Determine if the card is on the left or right side
                        const isLeftSide = (cardRect.left - containerRect.left) < (containerRect.width / 2);

                        // Calculate the line's starting point from the card's edge
                        let startX, startY;
                        if (isLeftSide) {
                            startX = (cardRect.right - containerRect.left) / containerRect.width * 100;
                        } else {
                            startX = (cardRect.left - containerRect.left) / containerRect.width * 100;
                        }
                        startY = (cardRect.top - containerRect.top + cardRect.height / 2) / containerRect.height * 100;
                        
                        // Calculate an intermediate point to create the "elbow" in the line
                        const horizontalSegmentLength = 8; // in percentage of container width
                        let midX = isLeftSide ? startX + horizontalSegmentLength : startX - horizontalSegmentLength;
                        
                        // Set SVG attributes
                        line.setAttribute('points', `${startX},${startY} ${midX},${startY} ${target.x},${target.y}`);
                        
                        // Use a zero-length path with a round cap to create a perfect circle dot at both ends
                        startDot.setAttribute('d', `M ${startX},${startY} h 0`);
                        endDot.setAttribute('d', `M ${target.x},${target.y} h 0`);
                });
                }

                // Initial call
                drawLines();

                // Recalculate on resize
                window.addEventListener('resize', drawLines);
            });
        </script>
    """
    return part1 + script