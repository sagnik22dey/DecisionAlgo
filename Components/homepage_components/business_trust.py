async def trust_body():
    return """ 
  
  <!-- Desktop view -->
  <section class="trust-section" id="trust-section-desktop" aria-label="Why Businesses Trust Us">
    <div class="top-fade" aria-hidden="true"></div>
    <!-- This wrapper helps reorder content on mobile using CSS flexbox's 'order' property -->
    <div class="trust-section-content-wrapper">
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
            <div class = "upper-features">
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
                  <p>Whether you're a startup or an enterprise, our solutions grow with your needs.</p>
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
            </div>
            <div class = "lower-features">
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
                  <h3>Proven Results </h3>
                  <p>Our client see higher efficiency, smarter decisions, and business growth.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> <!-- End of content-wrapper -->
  </section>

  <!-- Mobile view -->
  <section class="trust-section" id="trust-section-mobile" aria-label="Why Businesses Trust Us" style="display: none;">
    <div class="top-fade" aria-hidden="true"></div>
    <!-- This wrapper helps reorder content on mobile using CSS flexbox's 'order' property -->
    <div class="trust-section-content-wrapper">
      <!-- Title comes first on mobile -->
      <h2 class="title">
        Why <span class="accent">Businesses</span> Trust Us
      </h2>
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
                <p>Whether you're a startup or an enterprise, our solutions grow with your needs.</p>
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
                <h3>Proven Results </h3>
                <p>Our client see higher efficiency, smarter decisions, and business growth.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- CTAs come last on mobile -->
      <div class="cta-row">
        <a href="#" class="btn primary">See Our Dashboards</a>
        <a href="#" class="btn ghost">Explore More Solutions</a>
      </div>
    </div> <!-- End of content-wrapper -->
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
    
    /* Desktop Styles */
    #trust-section-desktop {
      position: relative;
      width: 100%;
      min-width: 76.77vw; /* Original: 1474px */
      padding: 9.26vh 0 14.81vh; /* Original: 100px 0 160px */
    }
    
    /* Mobile Styles */
    #trust-section-mobile {
      position: relative;
      width: 100%;
      padding: 4rem 1rem 3rem;
    }
    
    /* CTAs row */
    .cta-row {
      position: relative;
      width: auto; 
      left: 50%;
      transform: translateX(-50%);
      top: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 2.24vw; /* Original: 43px */
    }
    
    /* Mobile CTA row overrides */
    #trust-section-mobile .cta-row {
      left: auto;
      transform: none;
      flex-direction: column;
      width: 100%;
      gap: 1rem;
      margin-top: 3rem;
    }
    
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      height: 3.98vh; /* Original: 43px */
      padding: 1.02vh 1.82vw; /* Original: 11px 35px */
      border: 0.05vw solid #DFDFDF; /* Original: 1px */
      line-height: 1.33;
      cursor: pointer;
      user-select: none;
      display: flex;
      justify-content: center;
      align-items: center;
      text-decoration: none;
      font-family: 'Outfit', sans-serif;
      font-weight: 600;
      font-size: 1.15vw;
      height: 6.02vh;
      box-sizing: border-box;
      border-radius: 9.52vw;
      white-space: nowrap;
      transition: transform 0.2s ease, opacity 0.2s ease;
    }
    
    /* Mobile button overrides */
    #trust-section-mobile .btn {
      width: 100%;
      max-width: 400px;
      height: auto;
      padding: 0.9rem 1.5rem;
      border-radius: 12px;
      border: 1px solid #DFDFDF;
      font-size: 1rem;
    }
    
    .btn.primary {
      background: #FFFFFF;
      color: #000000;
      padding: 1.02vh 2.34vw; /* Original: 11px 45px */
    }
    
    #trust-section-mobile .btn.primary {
      padding: 0.9rem 1.5rem;
    }
    
    .btn.ghost {
      background: transparent;
      color: #DFDFDF;
    }
    
    /* Heading */
    .title {
      position: relative;
      width: 47.7vw; /* Original: 916px */
      height: auto;
      left: 50%;
      transform: translateX(-50%);
      margin-top: 7.41vh; /* Original: 80px */
      font-weight: 700;
      font-size: 3.33vw; /* Original: 64px */
      line-height: 4.01vw; /* Original: 77px */
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
    
    /* Mobile title overrides */
    #trust-section-mobile .title {
      left: auto;
      transform: none;
      width: 100%;
      font-size: 2.25rem;
      line-height: 1.2;
      margin-top: 0;
      margin-bottom: 2.5rem;
    }
    
    .title .accent {
      -webkit-text-fill-color: initial;
      background: none;
      color: #44B4FF;
    }
    
    /* Layered frames behind the features panel */
    .frame-outline {
      margin-top: 7.41vh; /* Original: 5rem */
      position: absolute;
      width: 73.18vw; /* Original: 1405px */
      height: 68.15vh; /* Original: 736px */
      left: 50%;
      transform: translateX(-50%);
      top: 25.93vh; /* Original: 280px */
      border: 0.05vw solid rgba(255, 255, 255, 255); /* Original: 1px */
      border-bottom: none;
      border-radius: 3.38vw; /* Original: 65px */
    }
    
    /* Hide frame outline on mobile */
    #trust-section-mobile .frame-outline {
      display: none;
    }
    
    .panel {
      position: relative;
      width: 76.77vw; /* Original: 1474px */
      height: 65.37vh; /* Original: 706px */
      left: 50%;
      transform: translateX(-50%);
      margin-top: 9.26vh; /* Original: 100px */
      background: #181818;
      border-radius: 1.46vw; /* Original: 28px */
      overflow: hidden;
    }
    
    /* Mobile panel overrides */
    #trust-section-mobile .panel {
      left: auto;
      transform: none;
      width: 100%;
      height: auto;
      margin-top: 0;
      border-radius: 20px;
    }
    
    /* Features container */
    .features {
      position: absolute;
      inset: 0;
      background: linear-gradient(103.91deg, rgba(26, 26, 26, 0) 5.34%, rgba(65, 65, 65, 0.28) 35.27%, rgba(109, 109, 109, 0.49) 71.27%, rgba(128, 128, 128, 0.01) 95.55%), #151515;
    }
    
    /* Mobile features overrides */
    #trust-section-mobile .features {
      position: relative;
      inset: auto;
    }
    
    .feature-text-box{
      padding: 14.81vh 2.5vw; /* Original: 10rem 3rem */
      display: flex;
      flex-direction: column; /* Stack feature groups vertically */
      flex-wrap: wrap;
      gap: 3.65vw; /* Original: 70px */
      justify-content: space-evenly;
      align-items: center; /* Center the feature groups */
    }
    
    /* Mobile feature text box overrides */
    #trust-section-mobile .feature-text-box {
      padding: 2.5rem 1.5rem;
      gap: 2.5rem;
      align-items: flex-start;
      justify-content: flex-start;
    }
    
    .upper-features {
      display: flex;
      justify-content: center;
      gap: 3.65vw; /* Maintain the same gap as the parent */
      margin-top: -3vh;
    }
    .lower-features {
      margin-top: 7.65vh;
      display: flex;
      justify-content: center;
      gap: 12.65vw; /* Maintain the same gap as the parent */
    }
    
    /* Hide upper/lower features structure on mobile */
    #trust-section-mobile .upper-features,
    #trust-section-mobile .lower-features {
      display: none;
    }
    
    .feature {
      color: #FFFFFF;
      display: flex;
      align-items: flex-start;
      gap: 1.3vw; /* Original: 25px */
    }
    
    /* Mobile feature overrides */
    #trust-section-mobile .feature {
      gap: 1rem;
    }
    
    .feature .icon {
      width: 2.6vw; /* Original: 50px */
      height: 2.6vw; /* Original: 50px, using vw to maintain aspect ratio */
      border-radius: 0.26vw; /* Original: 5px */
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      flex-shrink: 0;
    }
    
    /* Mobile icon overrides */
    #trust-section-mobile .feature .icon {
      width: 44px;
      height: 44px;
      border-radius: 8px;
      background-size: 24px 24px;
    }
    
    .feature .icon {
      background-size: 1.67vw 1.67vw; /* Original: 32px 32px */
      background-position: center;
      background-repeat: no-repeat;
    }
    .f1 .icon { background-image: url("/Resources/Images/HomePage/tailoredAi.png"); }
    .f2 .icon { background-image: url("/Resources/Images/HomePage/buildToScale.png"); }
    .f3 .icon { background-image: url("/Resources/Images/HomePage/costEfficient.png"); }
    .f4 .icon { background-image: url("/Resources/Images/HomePage/ironCladSecurity.png"); }
    .f5 .icon { background-image: url("/Resources/Images/HomePage/provenResult.png"); }
    
    .feature-content {
      /* This is a container for the text content */
    }
    
    /* Mobile feature content overrides */
    #trust-section-mobile .feature-content {
      flex: 1;
    }
    
    .feature h3 {
      margin: 0;
      width: 13.75vw; /* Original: 264.02px */
      height: 5.37vh; /* Original: 58px */
      font-family: 'Exo 2';
      font-style: normal;
      font-weight: 400;
      font-size: 1.52vw; /* Original: 29.2104px */
      color: #FFFFFF;
    }
    
    /* Mobile h3 overrides */
    #trust-section-mobile .feature h3 {
      width: auto;
      height: auto;
      font-size: 1.2rem;
      line-height: 1.3;
      margin: 0 0 0.5rem 0;
    }
    
    .feature p {
      margin: 0;
      width: 15.68vw; /* Original: 301.09px */
      height: 6.11vh; /* Original: 66px */
      font-family: 'Exo 2';
      font-style: normal;
      font-size: 0.94vw; /* Original: 17.9756px */
      line-height: 2.04vh; /* Original: 22px */
      color: #FFFFFF;
      opacity: 0.7;
    }
    
    /* Mobile p overrides */
    #trust-section-mobile .feature p {
      width: auto;
      height: auto;
      font-size: 0.95rem;
      line-height: 1.5;
    }
    
    /* Utility (demo background gradient at top like the screenshot) */
    .top-fade {
      position: absolute;
      inset: 0 0 auto 0;
      height: 20.37vh; /* Original: 220px */
      background: radial-gradient(80% 100% at 50% 0%, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 70%);
      pointer-events: none;
    }
    .f1, .f2, .f3, .f4, .f5 {
      width: 20.42vw; /* Original: 392px */
      height: 13.89vh; /* Original: 150px */
    }
    
    /* Mobile feature size overrides */
    #trust-section-mobile .f1, 
    #trust-section-mobile .f2, 
    #trust-section-mobile .f3, 
    #trust-section-mobile .f4, 
    #trust-section-mobile .f5 {
      width: 100%;
      height: auto;
    }
</style>
"""
async def trust_script():
    return """
  <script>
function toggleTrustSectionView() {
    const desktopSection = document.getElementById('trust-section-desktop');
    const mobileSection = document.getElementById('trust-section-mobile');
    
    // Check current viewport width
    const isMobileView = window.innerWidth <= 768;
    
    if (isMobileView) {
        // Show mobile, hide desktop
        if (desktopSection) desktopSection.style.display = 'none';
        if (mobileSection) mobileSection.style.display = 'block';
    } else {
        // Show desktop, hide mobile
        if (desktopSection) desktopSection.style.display = 'block';
        if (mobileSection) mobileSection.style.display = 'none';
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', toggleTrustSectionView);

// Listen for window resize events
window.addEventListener('resize', toggleTrustSectionView);

// Optional: Manual toggle function (can be called from buttons or other triggers)
function manualToggleTrustSection() {
    const desktopSection = document.getElementById('trust-section-desktop');
    const mobileSection = document.getElementById('trust-section-mobile');
    
    if (desktopSection && mobileSection) {
        const isDesktopVisible = desktopSection.style.display !== 'none';
        
        if (isDesktopVisible) {
            desktopSection.style.display = 'none';
            mobileSection.style.display = 'block';
        } else {
            desktopSection.style.display = 'block';
            mobileSection.style.display = 'none';
        }
    }
}
</script>
"""