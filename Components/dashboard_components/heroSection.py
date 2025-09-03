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
          <!-- left card -->
          <article class="card card-left">
            <header class="card-top">
              <div class="icon-box">
                <img src="https://picsum.photos/seed/a/10/10" alt="icon">
              </div>
              <div class="card-top-text">
                <h3 class="card-title">Data Processed Monthly</h3>
                <p class="card-desc">With billions of data points processed monthly, we empower businesses to transform</p>
              </div>
            </header>

            <div class="metrics">
              <!-- 99.99% -->
              <div class="metric-tile">
                <div class="metric-head">
                  <div class="mini-icon">
                    <img src="" alt="icon">
                  </div>
                  <div class="metric-text">
                    <div class="metric-value">99.99%</div>
                    <div class="metric-label">SLA uptime <br>+ soc 2</div>
                  </div>
                </div>
                <div class="sparkline">
                  <div class="sparkline-gloss"></div>
                  <span class="year-pill">2026</span>
                </div>
              </div>

              <!-- 320% -->
              <div class="metric-tile">
                <div class="metric-head">
                  <div class="mini-icon">
                    <img src="https://picsum.photos/seed/c/10/10" alt="icon">
                  </div>
                  <div class="metric-text">
                    <div class="metric-value">320%</div>
                    <div class="metric-label">Improvement</div>
                  </div>
                </div>
                <div class="sparkline small">
                  <div class="sparkline-gloss"></div>
                </div>
              </div>
            </div>
          </article>

          <!-- right card -->
          <article class="card card-right">
            <header class="card-top">
              <div class="icon-box">
                <img src="https://picsum.photos/seed/d/10/10" alt="icon">
              </div>
              <div class="card-top-text">
                <h3 class="card-title">ROI Improvement</h3>
                <p class="card-desc">Up to 320% improvement in decision-making speed</p>
              </div>
            </header>

            <div class="roi-center">
              <div class="roi-nest outer">
                <div class="roi-nest mid">
                  <div class="roi-nest inner">
                    <div class="roi-icon">
                      <img src="https://picsum.photos/seed/e/14/14" alt="roi">
                    </div>
                  </div>
                </div>
              </div>
            </div>
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

      .card{
        background:linear-gradient(180deg,#050505 0%,#202020 45%,#050505 100%);
        border-radius:1.2vw;
        box-shadow:0 1.4vh 3.2vw rgba(0,0,0,0.35);
        border:0.09vh solid rgba(255,255,255,0.06);
        display:flex;
        flex-direction:column;
        padding:3.5vh 2.5vw;
      }
      .card-left{ flex:0 1 48vw; }
      .card-right{ flex:0 1 28vw; }

      /* card header */
      .card-top{
        display:flex;
        align-items:flex-start;
        gap:1.6vw;
        margin-bottom:3.8vh;
      }
      .icon-box{
        width:3.2vw; height:3.2vw;
        border-radius:0.6vw;
        background:#202020;
        display:flex; justify-content:center; align-items:center;
      }
      .icon-box img{ width:1.2vw; height:1.2vw; filter:brightness(0) invert(1); }

      .card-top-text{ display:flex; flex-direction:column; gap:1.4vh; }
      .card-title{
        font-family:'Poppins',sans-serif; font-weight:500;
        font-size:1.4vw; line-height:1.8vw; color:#fff; margin:0;
      }
      .card-desc{
        font-family:'Poppins',sans-serif; font-weight:400;
        font-size:0.9vw; line-height:1.5vw; color:#BFBFBF; margin:0;
        max-width:26vw;
      }

      /* metrics split */
      .metrics{
        display:flex;
        gap:2.4vw;
        align-items:stretch;
      }
      .metric-tile{
        flex:1;
        background:#202020;
        border-radius:0.8vw;
        padding:2vh 1.5vw;
        display:flex;
        flex-direction:column;
        justify-content:space-between;
        box-shadow:inset 0 -2vh 6vw rgba(0,0,0,0.35);
      }
      .metric-head{ display:flex; gap:1vw; align-items:center; }
      .mini-icon{
        width:2.2vw; height:1.9vw; border-radius:0.4vw; background:#DFDFDF;
        display:flex; align-items:center; justify-content:center;
      }
      .mini-icon img{ width:1vw; height:1vw; filter:brightness(0); }
      .metric-text{ display:flex; flex-direction:column; gap:0.6vh; }
      .metric-value{
        font-family:'Poppins',sans-serif; font-weight:600;
        font-size:1.6vw; line-height:1.8vw; color:#fff;
      }
      .metric-label{
        font-family:'Poppins',sans-serif; font-weight:400;
        font-size:0.75vw; line-height:1.2vw; color:#D9D9D9; text-transform:uppercase;
      }

      /* sparklines */
      .sparkline{
        position:relative;
        margin-top:2.2vh;
        height:10vh;
        border-radius:0.6vw;
        background:linear-gradient(180deg,rgba(32,32,32,0.13) 0%, rgba(255,255,255,0.13) 100%);
        overflow:hidden;
      }
      .sparkline.small{ height:7.5vh; }
      .sparkline::before{
        content:"";
        position:absolute; inset:auto 0 0 0; height:0.3vh;
        background:linear-gradient(90deg,rgba(255,255,255,0.25),rgba(255,255,255,0));
      }
      .sparkline-gloss{
        position:absolute; inset:0;
        background:radial-gradient(100% 140% at 30% 10%, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0) 70%);
      }
      .year-pill{
        position:absolute; bottom: 1.5vh; right: 1.5vw;
        padding:0.6vh 1.2vw; border-radius:0.8vw; background:rgba(21,21,21,0.7); color:#fff;
        font-family:'Poppins',sans-serif; font-size:0.8vw;
        backdrop-filter: blur(2px);
      }

      /* ROI center nested blocks */
      .roi-center{ flex:1; display:flex; align-items:center; justify-content:center; }
      .roi-nest.outer{
        width:14vw; height:14vw; border-radius:1.2vw; background:#202020;
        display:flex; align-items:center; justify-content:center;
      }
      .roi-nest.mid{
        width:10.5vw; height:10.5vw; border-radius:1vw; background:#171717;
        display:flex; align-items:center; justify-content:center;
      }
      .roi-nest.inner{
        width:7.5vw; height:7.5vw; border-radius:0.8vw; background:#101010;
        display:flex; align-items:center; justify-content:center;
        box-shadow:inset 0 1.6vh 4vw rgba(255,255,255,0.05);
      }
      .roi-icon{
        width:3.8vw; height:3.8vw; background:#fff; border-radius:0.5vw;
        display:flex; align-items:center; justify-content:center;
      }
      .roi-icon img{ width:2vw; height:2vw; filter:brightness(0); }

      /* responsive */
      @media (max-width: 80vw){ /* ~768px */
        .hero-title{ font-size:7vw; line-height:8.5vw; }
        .hero-sub{ font-size:3.3vw; line-height:4.5vw; width:90vw; }
        .cta-outline{ width:40vw; height:6.6vh; font-size:3.2vw; border-radius:3vw; }

        .cards-row{ flex-direction:column; gap:4vh; width:92vw; }
        .card-left,.card-right{ flex:1 1 auto; }
        .card{ padding:5vh 4vw; border-radius:4vw; }
        .card-title{ font-size:4.6vw; line-height:5.4vw; }
        .card-desc{ font-size:3.1vw; line-height:4.6vw; max-width:100%; }
        .icon-box{ width:9vw; height:8vw; }
        .icon-box img{ width:3.4vw; height:3.4vw; }
        .mini-icon{ width:7vw; height:6vw; }
        .mini-icon img{ width:3vw; height:3vw; }
        .metric-value{ font-size:7.2vw; line-height:8vw; }
        .metric-label{ font-size:3vw; line-height:3.6vw; }
        .sparkline{ height:14vh; border-radius:3vw; }
        .sparkline.small{ height:11vh; }
        .year-pill{ font-size:3.2vw; border-radius:3vw; }
        .roi-nest.outer{ width:46vw; height:46vw; border-radius:5vw; }
        .roi-nest.mid{ width:36vw; height:36vw; border-radius:4vw; }
        .roi-nest.inner{ width:26vw; height:26vw; border-radius:3vw; }
        .roi-icon{ width:12vw; height:12vw; border-radius:2.6vw; }
        .roi-icon img{ width:6vw; height:6vw; }
      }
    </style>
    """
