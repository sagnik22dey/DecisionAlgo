async def track_body():
    return """
        <img class ="glow" src="../../Resources/Images/Dashboard/ecliplse_glow.png"/>
        <div class="parent">
        <div class="title-container">
            <h1>Track What Matters</h1>
        </div>

        <!-- Operations & Efficiency card2 -->
        <div class="card2 div1">
            <div class="card2-content-upper">
                <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                <h2>Operations & Efficiency</h2>
            </div>
            <p>Spot Bottlenecks Before They Hurt Your Business</p>
        </div>

        <!-- Marketing Performance card2 -->
        <div class="card2 div3">
            <div class="card2-content-upper">
                <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                <h2>Marketing Performance</h2>
            </div>
            <p>Measure Clicks, Conversions, And ROI</p>
        </div>

        <!-- Sales & Revenue card2 -->
        <div class="card2 div4">
            <div class="card2-content-upper">
                <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                <h2>Sales & Revenue</h2>
            </div>
            <p>See What's Working, Fix What's Not.</p>
        </div>
        
        <!-- Customer Behavior card2 -->
        <div class="card2 div5">
            <div class="card2-content-upper">
                <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                <h2>Customer Behavior</h2>
            </div>
            <p>Know What Keeps Them Coming Back</p>
        </div>

        <!-- Inventory & Supply Chain card2 -->
        <div class="card2 div6">
            <div class="card2-content-upper">
                <div class="card2-icon"><img src="/Resources/Images/HomePage/route.png" alt="icon"></div>
                <h2>Inventory & Supply Chain</h2>
            </div>
            <p>Stay Stocked. Avoid Over-Ordering</p>
        </div>

        <!-- Laptop Element -->
        <div class="div7">
            <img class="laptop-img" src="/Resources/Images/Dashboard/laptop.png" alt="Laptop with analytics dashboard">
        </div>
    </div>
    <img class ="glow2" src="../../Resources/Images/Dashboard/ecliplse_glow.png"/>
"""


async def track_style():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;600&display=swap');
        .glow {
            position: absolute;
            z-index: 0;
            pointer-events: none;
            top: 100vw;;
            transform: translateX(-50%);
        }
        .glow2 {
            position: absolute;
            z-index: 0;
            pointer-events: none;
            top: 110vw;;
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
        }

        .parent::before, .parent::after {
            content: '';
            position: absolute;
            z-index: 0;
            pointer-events: none;
            left: 50%;
            transform: translateX(-50%);
        }

        .parent::before { /* Bottom Eclipse Glow */
            background-image: url('/Resources/Images/Dashboard/ecliplse_glow.png');
            background-repeat: no-repeat;
            background-position: center bottom;
            background-size: contain;
            width: 150%;
            height: 100%;
            bottom: -40%;
            opacity: 0.3;
        }

        .parent::after { /* Top Peak Glow */
            background-image: url('/Resources/Images/Dashboard/peak_glow.png');
            background-repeat: no-repeat;
            background-position: top center;
            background-size: contain;
            width: 100%;
            height: 50%;
            top: 0;
            opacity: 0.2;
        }

        .title-container {
            grid-area: 1 / 1 / 3 / -1;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            z-index: 1;
        }

        h1 {
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            font-weight: 600;
            margin: 0;
            color: #FFFFFF;
           
        }

        .card2 {
            background: rgba(27, 27, 27, 0.6); /* #1B1B1B with transparency */
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 0.625vw;
            padding: 1.56vw;
            backdrop-filter: blur(0.75vw);
            -webkit-backdrop-filter: blur(0.75vw);
            display: flex;
            flex-direction: column;
            gap: 1.56vw;
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
            font-size: clamp(1.2rem, 1.5vw, 1.56rem); /* 25px at 1600px viewport */
            line-height: 120%;
            color: #FFFFFF;
            margin: 0;
        }

        .card2 p {
            font-weight: 400;
            font-size: clamp(0.9rem, 1vw, 1.02rem); /* 16.4px at 1600px viewport */
            line-height: 160%;
            color: #FFFFFF;
            opacity: 0.7;
            margin: 0;
        }

        /* --- Grid Placement --- */
        .div1 { grid-area: 7 / 2 / 10 / 6; }   /* Operations & Efficiency */
        .div3 { grid-area: 4 / 4 / 7 / 8; }   /* Marketing Performance */
        .div4 {
            grid-area: 3 / 8 / 6 / 12;  /* Sales & Revenue */
            margin-bottom: 1vw;
        }
        .div5 { grid-area: 4 / 12 / 7 / 16; } /* Customer Behavior */
        .div6 { grid-area: 7 / 14 / 10 / 18; }/* Inventory & Supply Chain */
        
        .div7 { /* Laptop Container */
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
            /* bottom: 10vh; */
            margin-right: 10.7vw;
        }

        @media (max-width: 900px) {
            .parent {
                display: flex;
                flex-direction: column;
                align-items: center;
                height: auto;
                min-height: 100vh;
                padding: 10vh 5vw 5vh 5vw;
                gap: 2.67vw;
                overflow-x: hidden;
            }
            
            .title-container, .card2, .div7 {
                grid-area: auto;
                position: relative;
                width: 100%;
                max-width: 55.56vw;
            }
            
            .title-container { order: 1; }
            .div7 { order: 2; }
            .div4 { order: 3; }
            .div3 { order: 4; }
            .div5 { order: 5; }
            .div1 { order: 6; }
            .div6 { order: 7; }

            h1 { font-size: 8vw; }
            
            .div7 { margin-bottom: 2.22vw; }

            .laptop-img { max-width: 90vw; }
            
            .card2 { padding: 1.78vw; }
            .card2 h2 { font-size: 1.95vw; }
            .card2 p { font-size: 1.6vw; }
            .card2-icon {
                width: 4.44vw;
                height: 4.44vw;
            }
            .card2-icon img {
                width: 2.67vw;
                height: 2.67vw;
            }
        }
    </style>
"""
