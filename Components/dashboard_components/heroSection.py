async def heroSection_body():
    return """
    <div class="hero-section-container">
        <!-- keep background layers exactly as before -->
        <div class="bg-dark"></div>
        <div class="grid-container"></div>
        <div class="gradient-overlay"></div>
        <div class="glow-bottom"></div>

        <div class="hero-content">
        <!-- centered headline & CTA -->
        <div class="hero-head">
          <h1 class="hero-title">
            See Your Business in Real-Time. <span class="accent">ANYTIME.</span>
          </h1>
          <p class="hero-sub">Tired of messy spreadsheets?</p>
          <p class="hero-sub">Get all the key metrics in one sleek, interactive dashboard.</p>
          <p class="hero-sub" style="margin-top: 1.5vw;">No more digging for data—just clear, instant insights.</p>
          <a href="#" class="cta-outline">Try A Live Demo</a>
        </div>
       </div>
        <!-- cards row -->
        <div class="cards-row">
          <img class="peak-glow" src="../../Resources/Images/Dashboard/peak_glow.png" alt="peak glow">
          <img class="eclipse-glow" src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="eclipse glow">
          <!-- left card -->
          <article class="card card-left">
           <img src="../../Resources/Images/Dashboard/dashboard_left_card.png" alt="card image">
          </article>

          <!-- right card -->
          <article class="card card-right">
            <img src="../../Resources/Images/Dashboard/dashboard_right_card.png" alt="card image">
          </article>
        </div>
    </div>
    """

async def heroSection_style():
    return """
    <style>
      /* keep original container metrics */
      .hero-section-container{
        margin-top:10vh;
        margin-bottom:10vh;
        position:relative;
        width:100vw;
        min-height:50vh;
        display:flex;
        flex-direction:column;
        justify-content:flex-start;
        align-items:center;
        padding-top:10vh;
        padding-bottom:10vh;
        overflow:hidden;
      }

      .hero-content {
        position: relative;
        z-index: 4;
        width: 100vw;
        height:80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5vh;
        margin-bottom: 5vh;
        background-image: url('../../Resources/Images/HomePage/grid1.png');
        border-bottom: solid #ffffff;
        border-radius: 3vw;
      }

      /* preserve background layers from your code */
      .bg-dark,.grid-container,.gradient-overlay,.glow-bottom{
        inset:0;
        position:absolute;
        width:100vw;
        height:100vh;
        border-radius:3.38vw;
      }
      .bg-dark{ z-index:1; }
      .grid-container{ z-index:2; background-size:cover; }
      .gradient-overlay{ z-index:3; }
      .glow-bottom{ z-index:1; }

      /* content wrapper */
      .hero-head{
        position:relative;
        z-index:4;
        width:70vw;
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:1.5vh;
        margin-bottom:1vh;
      }
      .hero-title{
        font-family:'Exo 2',sans-serif;
        font-weight:600;
        font-size:3.78vw;
        line-height:4.8vw;
        letter-spacing:-0.02em;
        color:#fff;
        text-align:center;
        text-shadow:0 0.5vh 0.5vw rgba(0,0,0,0.25);
        margin:0;
      }
      .hero-title .accent{ color:#4AA6ED; }
      .hero-sub{
        font-family:'Poppins',sans-serif;
        font-weight:700;
        font-size:1.5vw;
        line-height:1.8vw;
        color:#eaeaea;
        margin:0;
        text-align:center;
        opacity:0.9;
      }
      .cta-outline{
        margin-top:2.8vh;
        display:inline-flex;
        justify-content:center;
        align-items:center;
        width:12vw;
        height:5.5vh;
        border:0.09vh solid #DFDFDF;
        border-radius:1.8vw;
        font-family:'Poppins',sans-serif;
        font-size:1.2vw;
        color:#DFDFDF;
        text-decoration:none;
        transition:transform 0.2s ease, background 0.2s ease;
      }
      .cta-outline:hover{ transform:translateY(-0.4vh); background:rgba(255,255,255,0.06); }

      /* cards row */
      .cards-row{
        position:relative;
        z-index:4;
        width:80vw;
        display:flex;
        gap:2vw;
        align-items:stretch;
        justify-content:center;
        top: -15vw;
      }

      .peak-glow,
      .eclipse-glow {
        position: absolute;
        pointer-events: none;
        z-index: 1;
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

      .card{
        position: relative;
        z-index: 2;
        background:linear-gradient(180deg,#050505 0%,#202020 45%,#050505 100%);
        border-radius:1.2vw;
        box-shadow:0 1.4vh 3.2vw rgba(0,0,0,0.35);
        border:0.09vh solid rgba(255,255,255,0.06);
        display:flex;
        flex-direction:column;
        
      }
      .card-left{ /* 745px / 1920px = 0.388vw, 475px / 1080px = 0.44vh */
        width: 38.8vw;
        height: 44vh;
        flex-shrink: 0; /* Prevent shrinking below the fixed width */
      }
      .card-right{ /* 525px / 1920px = 0.273vw, 475px / 1080px = 0.44vh */
        width: 27.3vw;
        height: 44vh;
        flex-shrink: 0; /* Prevent shrinking below the fixed width */
      }

      /* responsive */
      @media (max-width: 80vw){ /* ~768px */
        .hero-title{ font-size:7vw; line-height:8.5vw; }
        .hero-sub{ font-size:3.3vw; line-height:4.5vw; width:90vw; }
        .cta-outline{ width:40vw; height:6.6vh; font-size:3.2vw; border-radius:3vw; }

        .cards-row{ flex-direction:column; gap:4vh; width:92vw; }
        .card-left,.card-right{ flex:1 1 auto; }
        .card{ padding:5vh 4vw; border-radius:4vw; }
      }
    </style>
    """