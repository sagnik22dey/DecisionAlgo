async def heroSection_body():
    return """
    <div class="hero-section-container">
        <!-- Background layers -->
        <div class="bg-dark"></div>
        <div class="grid-container"></div>
        <div class="gradient-overlay"></div>
        <div class="glow-bottom"></div>

        <div class="hero-content">
            <!-- Centered headline & CTA -->
            <div class="hero-head">
              <h1 class="hero-title">
                See Your Business in Real-Time. <span class="accent">ANYTIME.</span>
              </h1>
              <p class="hero-sub">Tired of messy spreadsheets?</p>
              <p class="hero-sub">Get all the key metrics in one sleek, interactive dashboard.</p>
              <p class="hero-sub hero-sub-last">No more digging for data—just clear, instant insights.</p>
              <a href="#" class="cta-outline">Try A Live Demo</a>
            </div>
        </div>

        <!-- Cards row -->
        <div class="cards-row">
          <img class="peak-glow" src="../../Resources/Images/Dashboard/peak_glow.png" alt="peak glow">
          <img class="eclipse-glow" src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="eclipse glow">
          
          <!-- Left card -->
          <article class="card-item card-left">
           <img src="../../Resources/Images/Dashboard/dashboard_left_card.png" alt="Sales performance dashboard card">
          </article>

          <!-- Right card -->
          <article class="card-item card-right">
            <img src="../../Resources/Images/Dashboard/dashboard_right_card.png" alt="User activity dashboard card">
          </article>
        </div>
    </div>
    """
    
async def heroSection_style():
    return """
    <style>
      /* --- Base & Desktop Styles --- */
      .hero-section-container {
        margin-top: 2vh;
        margin-bottom: -25vh; /* Pulls subsequent content up */
        position: relative;
        width: 100vw;
        min-height: 50vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding-top: 10vh;
        padding-bottom: 10vh;
        overflow: hidden;
        box-sizing: border-box;
      }

      .hero-content {
        position: relative;
        z-index: 4;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5vh;
        background-image: url(../../Resources/Images/HomePage/grid1.png);
        border-bottom: 0.1vw solid #FFFFFF;
        border-radius: 3vw;
        box-sizing: border-box;
      }

      /* Background layers */
      .bg-dark, .grid-container, .gradient-overlay, .glow-bottom {
        inset: 0;
        position: absolute;
        width: 100vw;
        height: 100vh;
        border-radius: 3.38vw;
      }
      .bg-dark { z-index: 1; }
      .grid-container { z-index: 2; background-size: cover; }
      .gradient-overlay { z-index: 3; }
      .glow-bottom { z-index: 1; }

      /* Content wrapper */
      .hero-head {
        position: relative;
        z-index: 4;
        width: 70vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5vh;
        margin-top: 8vh;
      }

      .hero-title {
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        font-size: 3.8vw;
        line-height: 1.25;
        letter-spacing: -0.02em;
        color: #fff;
        text-align: center;
        text-shadow: 0 0.5vh 0.5vw rgba(0, 0, 0, 0.25);
        margin: 0;
      }

      .hero-title .accent {
        color: #4AA6ED;
      }

      .hero-sub {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.5vw;
        line-height: 1.5;
        color: #eaeaea;
        margin: 0;
        text-align: center;
        opacity: 0.9;
      }
      
      .hero-sub-last {
          margin-top: 1.5vh;
      }

      .cta-outline {
        margin-top: 4vh;
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 12vw;
        height: 5.5vh;
        border: 0.1vw solid #DFDFDF;
        border-radius: 1.8vw;
        font-family: 'Poppins', sans-serif;
        font-size: 1.2vw;
        color: #DFDFDF;
        text-decoration: none;
        transition: transform 0.3s ease, background-color 0.3s ease;
      }

      .cta-outline:hover {
        transform: translateY(-0.4vh);
        background: rgba(255, 255, 255, 0.06);
      }

      /* Cards row */
      .cards-row {
        position: relative;
        z-index: 4;
        width: 80vw;
        display: flex;
        gap: 2vw;
        align-items: flex-start; /* Align to the top */
        justify-content: center;
        top: -15vw;
      }

      .peak-glow,
      .eclipse-glow {
        position: absolute;
        pointer-events: none;
        z-index: 1;
        transition: all 0.5s ease;
      }

      .peak-glow {
        width: 32vw;
        left: 0vw;
        top: -44vh;
      }

      .eclipse-glow {
        width: 50vw;
        right: 13vw;
        top: -20vh;
      }

      .card-item {
        position: relative;
        z-index: 2;
        flex-shrink: 0; /* Prevent shrinking */
      }
      
      .card-item img {
        width: 100%;
        height: auto;
        display: block;
      }

      .card-left {
        width: 38.8vw;
      }
      
      .card-right {
        width: 27.3vw;
      }

      /* --- Tablet View --- */
      @media (max-width: 1024px) {
        .hero-head {
            width: 85vw;
            margin-top: 6vh;
        }
        .hero-title { font-size: 5vw; }
        .hero-sub { font-size: 2vw; }
        .cta-outline { 
            width: 20vw; 
            height: 6vh;
            font-size: 1.8vw;
            border-radius: 3vw; 
        }
        .cards-row {
            width: 90vw;
            top: -18vw;
        }
      }

      /* --- Mobile View (Redesigned for Elegance) --- */
      @media (max-width: 767px) {
        .hero-section-container {
            margin-bottom: -45vh; /* Adjust negative margin for stacked layout */
            padding-top: 8vh;
        }
        .hero-content {
            height: 72vh; 
        }

        .hero-head {
            width: 90vw;
            gap: 2vh;
            margin-top: 5vh;
        }

        .hero-title {
            font-size: 9vw;
            line-height: 1.3;
        }

        .hero-sub {
            font-size: 4vw;
            line-height: 1.6;
            font-weight: 500; /* Slightly thinner for modern feel */
        }
        
        .hero-sub-last {
            margin-top: 2vh;
        }

        .cta-outline {
            width: 55vw;
            height: 7vh;
            font-size: 4vw;
            border-radius: 5vw;
            margin-top: 5vh;
            border-width: 0.3vw;
        }

        .cards-row {
            flex-direction: column;
            width: 90vw;
            gap: 4vh;
            top: -88vw; /* Adjust overlap for vertical stack */
        }
        
        .card-left,
        .card-right {
            width: 100%; /* Cards take full width of the row */
        }
        
        /* Reposition glows for a nice ambient background effect */
        .peak-glow {
            width: 80vw;
            left: -25vw;
            top: -10vh;
            opacity: 0.7;
        }

        .eclipse-glow {
            width: 110vw;
            right: -40vw;
            top: 25vh;
            opacity: 0.8;
        }
      }
    </style>
    """