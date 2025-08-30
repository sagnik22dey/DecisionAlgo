async def trust_body():
    return """ 
  <section class="trust-section" aria-label="Why Businesses Trust Us">
    <div class="top-fade" aria-hidden="true"></div>

    <!-- CTAs -->
    <div class="cta-row">
      <a href="#" class="btn primary">See Our Dashboards</a>
      <a href="#" class="btn ghost">Explore More Solutions</a>
    </div>

    <!-- Title -->
    <h2 class="title">
      Why <span class="accent">Businesses</span> Trust Us
    </h2>

    <!-- Layered frames -->
    <div class="frame-outline" aria-hidden="true"></div>

    <!-- Main panel -->
    <div class="panel">
      <div class="features">
      <div class="feature-text-box">
        <!-- Feature 1 -->
        <div class="feature f1">
          <div class="icon"></div>
          <div class="feature-content">
            <h3>Tailored AI & Data Solutions</h3>
            <p>We create custom automation & insights for your specific business challenges.</p>
          </div>
        </div>

        <!-- Feature 2 -->
        <div class="feature f2">
          <div class="icon"></div>
          <div class="feature-content">
            <h3>Built to Scale</h3>
            <p>Whether you’re a startup or an enterprise, our solutions grow with your needs.</p>
          </div>
        </div>

        <!-- Feature 3 -->
        <div class="feature f3">
          <div class="icon"></div>
          <div class="feature-content">
            <h3>Cost-Efficient Automation</h3>
            <p>Save resources by reducing manual tasks with smart automation.</p>
          </div>
        </div>

        <!-- Feature 4 -->
        <div class="feature f4">
          <div class="icon"></div>
          <div class="feature-content">
            <h3>Ironclad Security</h3>
            <p>Your data is protected with enterprise-grade security & compliance.</p>
          </div>
        </div>

        <!-- Feature 5 -->
        <div class="feature f5">
          <div class="icon"></div>
          <div class="feature-content">
            <h3>Proven Results </h3>
            <p>Our client see higher efficiency, smarter decisions, and business growth.</p>
          </div>
        </div>
      </div>
      </div>
    </div>
  </section>
"""


async def trust_style():
    return """  
<style>
    /* Base/reset */
    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body {
      margin: 0;
      background: #000000;
      color: #FFFFFF;
      font-family: "Exo 2", "Poppins", system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    a { color: inherit; text-decoration: none; }

    /* Section wrapper */
    .trust-section {
      position: relative;
      width: 100%;
      min-width: 1474px;
      padding: 100px 0 160px; /* Adjusted top padding */
    }

    /* CTAs row */
    .cta-row {
      position: relative;
      width: auto; /* Let flexbox determine width */
      left: 50%;
      transform: translateX(-50%);
      top: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 43px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      height: 43px;
      padding: 11px 35px; /* Adjusted horizontal padding */
      border-radius: 24px;
      border: 1px solid #DFDFDF;
      font-family: "Poppins", system-ui, Arial, sans-serif;
      font-weight: 400;
      font-size: 16px;
      line-height: 1.33;
      white-space: nowrap;
      cursor: pointer;
      user-select: none;
    }
    .btn.primary {
      background: #FFFFFF;
      color: #000000;
      padding: 11px 45px; /* Custom padding for this button */
    }
    .btn.ghost {
      background: transparent;
      color: #DFDFDF;
    }

    /* Heading */
    .title {
      position: relative;
      width: 916px;
      height: auto;
      left: 50%;
      transform: translateX(-50%);
      margin-top: 80px; /* Increased margin */
      font-weight: 700;
      font-size: 64px;
      line-height: 77px;
      text-align: center;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg,
        rgba(255, 255, 255, 0.5) 0%,
        #FFFFFF 25%,
        #FFFFFF 75%,
        rgba(255, 255, 255, 0.5) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .title .accent {
      -webkit-text-fill-color: initial;
      background: none;
      color: #44B4FF;
    }

    /* Layered frames behind the features panel */
    .frame-outline {
      margin-top:5rem;
      position: absolute;
      width: 1405px;
      height: 736px;
      left: 50%;
      transform: translateX(-50%);
      top: 280px;
      border: 1px solid rgba(255, 255, 255, 255);
      border-bottom: none;
      border-radius: 65px;
    }
    .panel {
      position: relative;
      width: 1474px;
      height: 706px;
      left: 50%;
      transform: translateX(-50%);
      margin-top: 100px;
      background: #181818;
      border-radius: 28px;
      overflow: hidden;
    }

    /* Features container */
    .features {
      position: absolute;
      inset: 0;
      background: linear-gradient(103.91deg, rgba(26, 26, 26, 0) 5.34%, rgba(65, 65, 65, 0.28) 35.27%, rgba(109, 109, 109, 0.49) 71.27%, rgba(128, 128, 128, 0.01) 95.55%), #151515;
    }
    
    .feature-text-box{
          padding: 10rem 3rem;
          display: flex;
          flex-wrap: wrap;
          gap: 70px;
          justify-content: space-evenly;
        }
        
        .feature {
          color: #FFFFFF;
          display: flex;
          align-items: flex-start;
          gap: 25px;
        }
    .feature .icon {
      width: 50px;
      height: 50px;
      border-radius: 5px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      flex-shrink: 0;
    }
    /* NOTE: Replaced placeholder icons with SVGs */
    .feature .icon {
      background-size: 32px 32px;
      background-position: center;
      background-repeat: no-repeat;
    }
    .f1 .icon {
      background-image: url("/Resources/Images/tailoredAi.png");
    }
    .f2 .icon {
    background-image: url("/Resources/Images/buildToScale.png");
    }
    .f3 .icon {
    background-image: url("/Resources/Images/costEfficient.png");
    }
    .f4 .icon {
      background-image: url("/Resources/Images/ironCladSecurity.png");
    }
    .f5 .icon {
      background-image: url("/Resources/Images/provenResult.png");
    }
    .feature-content {
      /* This is a container for the text content */
    }
    .feature h3 {
      margin: 0px;
      position: flex;
      width: 264.02px;
      height: 58px;
      font-family: 'Exo 2';
      font-style: normal;
      font-weight: 400;
      font-size: 29.2104px;
      /* or 29px */

      color: #FFFFFF;
    }
    /* Tailored AI & Data Solutions */




    .feature p {
      margin: 0;
      width: 301.09px;
      height: 66px;
      font-family: 'Exo 2';
      font-style: normal;
      font-size: 17.9756px;
      line-height: 22px;
      color: #FFFFFF;
      opacity: 0.7;
      }

    /* Utility (demo background gradient at top like the screenshot) */
    .top-fade {
      position: absolute;
      inset: 0 0 auto 0;
      height: 220px;
      background: radial-gradient(80% 100% at 50% 0%, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 70%);
      pointer-events: none;
    }
    .f1{
      width: 392px;
      height: 150px;
    }
    f2{
      width: 392px;
      height: 150px;
    }
    .f3{
      width: 392px;
      height: 150px;
    }
    .f4{
      width: 392px;
      height: 150px;
    }
    .f5{
      width: 392px;
      height: 150px;
    }
  </style>
  """
