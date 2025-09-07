async def track_body():
    return """
    <section class="track-section">
        <img class ="glow-top" src="../../Resources/Images/Dashboard/peak_glow.png" alt="background glow"/>
        <div class="parent">
            <div class="title-container">
                <h1>Track What Matters</h1>
            </div>

            <!-- Operations & Efficiency card -->
            <div class="card2 div1">
                <div class="card2-content-upper">
                    <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                    <h2>Operations & Efficiency</h2>
                </div>
                <p>Spot Bottlenecks Before They Hurt Your Business</p>
            </div>

            <!-- Marketing Performance card -->
            <div class="card2 div3">
                <div class="card2-content-upper">
                    <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                    <h2>Marketing Performance</h2>
                </div>
                <p>Measure Clicks, Conversions, And ROI</p>
            </div>

            <!-- Sales & Revenue card -->
            <div class="card2 div4">
                <div class="card2-content-upper">
                    <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                    <h2>Sales & Revenue</h2>
                </div>
                <p>See What's Working, Fix What's Not.</p>
            </div>
            
            <!-- Customer Behavior card -->
            <div class="card2 div5">
                <div class="card2-content-upper">
                    <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                    <h2>Customer Behavior</h2>
                </div>
                <p>Know What Keeps Them Coming Back</p>
            </div>

            <!-- Inventory & Supply Chain card -->
            <div class="card2 div6">
                <div class="card2-content-upper">
                    <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                    <h2>Inventory & Supply Chain</h2>
                </div>
                <p>Stay Stocked. Avoid Over-Ordering</p>
            </div>

            <!-- Laptop Element -->
            <div class="laptop-container div7">
                <img class="laptop-img" src="/Resources/Images/Dashboard/laptop.png" alt="Laptop with analytics dashboard">
            </div>
        </div>
        <img class ="glow-bottom" src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="background glow"/>
    </section>
"""
async def track_style():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600&display=swap');

        /* --- UNCHANGED DESKTOP STYLES (Your Original Code) --- */
        
        .track-section {
            position: relative;
            width: 100%;
            overflow: hidden; /* Prevent horizontal scroll */
            font-family: 'Exo 2', sans-serif;
        }

        .glow-top { /* formerly .glow */
            position: absolute;
            z-index: 0;
            pointer-events: none;
            top: 100vw;
            transform: translateX(-50%);
        }
        
        .glow-bottom { /* formerly .glow2 */
            position: absolute;
            z-index: 0;
            pointer-events: none;
            top: 110vw;
            transform: translateX(150%);
        }
        
        .parent {
            width: 100%;
            height: 100vh;
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            grid-template-rows: repeat(11, 1fr);
            gap: 7vh;
            padding: 0vh 4vw;
            position: relative;
            overflow: hidden;
            font-family: 'Exo 2', sans-serif;
            box-sizing: border-box;
        }

        .title-container {
            grid-area: 1 / 1 / 3 / -1;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            z-index: 1;
        }

        .title-container h1 {
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            font-weight: 600;
            margin: 0;
            color: #FFFFFF;
        }

        .card2 {
            background: rgba(27, 27, 27, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 0.625vw;
            padding: 1.56vw;
            backdrop-filter: blur(0.75vw);
            -webkit-backdrop-filter: blur(0.75vw);
            display: flex;
            flex-direction: column;
            gap: 0.56vw;
            z-index: 1;
        }
        
        .card2-content-upper {
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 1.875vw;
        }
        
        .card2-icon {
            width: 3.31vw;
            height: 3.31vw;
            flex-shrink: 0;
            background: #0A1015;
            border: 1px solid #3A4046;
            border-radius: 0.19vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .card2-icon img {
            width: 1.94vw;
            height: 1.94vw;
        }

        .card2 h2 {
            font-weight: 600;
            font-size: clamp(1.2rem, 1.5vw, 1.56rem);
            line-height: 120%;
            color: #FFFFFF;
            margin: 0;
        }

        .card2 p {
            font-weight: 400;
            font-size: clamp(0.9rem, 1vw, 1.02rem);
            line-height: 160%;
            color: #FFFFFF;
            opacity: 0.7;
            margin: 0;
        }

        .div1 { grid-area: 7 / 2 / 10 / 6; }
        .div3 { grid-area: 4 / 4 / 7 / 8; }
        .div4 {
            grid-area: 3 / 8 / 6 / 12;
            margin-bottom: 1vw;
        }
        .div5 { grid-area: 4 / 12 / 7 / 16; }
        .div6 { grid-area: 7 / 14 / 10 / 18; }
        
        .laptop-container { /* Renamed for clarity */
            grid-area: 6 / 6 / 12 / 16;
            z-index: 10;
            display: flex;
            align-items: flex-end;
            justify-content: center;
        }

        .laptop-img {
            width: 194vw;
            height: auto;
            object-fit: contain;
            object-position: bottom;
            margin-right: 10.7vw;
        }

        /* --- NEW, ELEGANT MOBILE VIEW --- */
        /* This will only apply on screens 767px or smaller */
        @media (max-width: 767px) {
            .parent {
                /* Change layout from grid to a single column flexbox */
                display: flex;
                flex-direction: column;
                align-items: center;
                height: auto; /* Allow height to grow with content */
                min-height: 100vh;
                padding: 5vh 5vw;
                gap: 4vh; /* Vertical gap for clean separation */
            }
            
            /* Reset all grid-specific properties for mobile */
            .title-container, .card2, .laptop-container {
                grid-area: auto;
                position: relative;
                width: 90vw;
                max-width: 100%;
                margin: 0; /* Reset margins */
            }
            
            /* Reorder elements for a logical mobile flow */
            .title-container { order: 1; }
            .laptop-container { order: 2; margin-bottom: 5vh; }
            .div4 { order: 3; } /* Sales */
            .div3 { order: 4; } /* Marketing */
            .div5 { order: 5; } /* Customer */
            .div1 { order: 6; } /* Operations */
            .div6 { order: 7; } /* Inventory */

            .title-container h1 { 
                font-size: 9vw; /* Make title prominent */
            }
            
            .laptop-container {
                align-items: center;
            }
            .laptop-img { 
                width: 130rem; /* Make laptop fit container */
                margin-right: 0; /* Reset desktop margin */
                margin-top: -10vw; /* Add some top margin */
            }
            
            .card2 { 
                padding: 6vw; 
                border-radius: 4vw; /* Softer corners */
                gap: 2vh;
            }
            
            .card2-content-upper {
                gap: 4vw;
            }

            .card2 h2 { 
                font-size: 5.5vw; 
                line-height: 1.3;
            }
            .card2 p { 
                font-size: 4vw; 
                line-height: 1.5;
            }
            .card2-icon {
                width: 12vw;
                height: 12vw;
                border-radius: 2vw;
            }
            .card2-icon img {
                width: 6vw;
                height: 6vw;
            }
            
            /* Reposition glows for a vertical layout */
            .glow-top {
                width: 150vw;
                top: 5vh;
                opacity: 0.3;
                transform: translateX(-50%); /* Center it properly */
            }
            .glow-bottom {
                width: 180vw;
                top: auto; /* Unset top position */
                bottom: -30vh;
                opacity: 0.4;
                transform: translateX(-50%); /* Center it properly */
            }
        }
    </style>
"""