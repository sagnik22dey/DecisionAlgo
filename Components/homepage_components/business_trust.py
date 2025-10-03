async def trust_body():
    return """ 
  <!-- Desktop view -->
  <section class="trust-section" id="trust-section-desktop" aria-label="Why Businesses Trust Us">
    <div class="top-fade" aria-hidden="true"></div>
    <div class="trust-section-content-wrapper">
      <div class="cta-row">
        <a href="#" class="btn primary">See Our Dashboards</a>
        <a href="#" class="btn ghost">Explore More Solutions</a>
      </div>
      <h2 class="title">
        Why <span class="accent">Businesses</span> Trust Us
      </h2>
      <div class="frame-outline" aria-hidden="true"></div>
      <div class="panel">
        <div class="features">
          <div class="feature-text-box">
            <div class="upper-features">
              <!-- Feature 1 -->
              <div class="feature f1">
                <div class="icon"><img src="/Resources/Images/HomePage/tailoredAi.png" alt="Tailored Solutions Icon"></div>
                <div class="feature-content">
                  <h3>Tailored AI & Data Solutions</h3>
                  <p>We create custom automation & insights for your specific business challenges.</p>
                </div>
              </div>
              <!-- Feature 2 -->
              <div class="feature f2">
                <div class="icon"><img src="/Resources/Images/HomePage/buildToScale.png" alt="Scalability Icon"></div>
                <div class="feature-content">
                  <h3>Built to Scale</h3>
                  <p>Whether you're a startup or an enterprise, our solutions grow with your needs.</p>
                </div>
              </div>
              <!-- Feature 3 -->
              <div class="feature f3">
                <div class="icon"><img src="/Resources/Images/HomePage/costEfficient.png" alt="Cost Efficiency Icon"></div>
                <div class="feature-content">
                  <h3>Cost-Efficient Automation</h3>
                  <p>Save resources by reducing manual tasks with smart automation.</p>
                </div>
              </div>
            </div>
            <div class="lower-features">
              <!-- Feature 4 -->
              <div class="feature f4">
                <div class="icon"><img src="/Resources/Images/HomePage/ironCladSecurity.png" alt="Security Icon"></div>
                <div class="feature-content">
                  <h3>Ironclad Security</h3>
                  <p>Your data is protected with enterprise-grade security & compliance.</p>
                </div>
              </div>
              <!-- Feature 5 -->
              <div class="feature f5">
                <div class="icon"><img src="/Resources/Images/HomePage/provenResult.png" alt="Proven Results Icon"></div>
                <div class="feature-content">
                  <h3>Proven Results</h3>
                  <p>Our client see higher efficiency, smarter decisions, and business growth.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Mobile view -->
  <section class="trust-section" id="trust-section-mobile" aria-label="Why Businesses Trust Us" style="display: none;">
    <div class="top-fade" aria-hidden="true"></div>
    <div class="trust-section-content-wrapper">
      <h2 class="title">
        Why <span class="accent">Businesses</span> Trust Us
      </h2>
      <div class="panel">
        <div class="features">
          <div class="feature-text-box">
            <div class="feature f1">
                <div class="icon"><img src="/Resources/Images/HomePage/tailoredAi.png" alt="Tailored Solutions Icon"></div>
                <div class="feature-content">
                    <h3>Tailored AI & Data Solutions</h3>
                    <p>We create custom automation & insights for your specific business challenges.</p>
                </div>
            </div>
            <div class="feature f2">
                <div class="icon"><img src="/Resources/Images/HomePage/buildToScale.png" alt="Scalability Icon"></div>
                <div class="feature-content">
                    <h3>Built to Scale</h3>
                    <p>Whether you're a startup or an enterprise, our solutions grow with your needs.</p>
                </div>
            </div>
            <div class="feature f3">
                <div class="icon"><img src="/Resources/Images/HomePage/costEfficient.png" alt="Cost Efficiency Icon"></div>
                <div class="feature-content">
                    <h3>Cost-Efficient Automation</h3>
                    <p>Save resources by reducing manual tasks with smart automation.</p>
                </div>
            </div>
            <div class="feature f4">
                <div class="icon"><img src="/Resources/Images/HomePage/ironCladSecurity.png" alt="Security Icon"></div>
                <div class="feature-content">
                    <h3>Ironclad Security</h3>
                    <p>Your data is protected with enterprise-grade security & compliance.</p>
                </div>
            </div>
            <div class="feature f5">
                <div class="icon"><img src="/Resources/Images/HomePage/provenResult.png" alt="Proven Results Icon"></div>
                <div class="feature-content">
                    <h3>Proven Results</h3>
                    <p>Our client see higher efficiency, smarter decisions, and business growth.</p>
                </div>
            </div>
          </div>
        </div>
      </div>
      <div class="cta-row">
        <a href="#" class="btn primary">See Our Dashboards</a>
        <a href="#" class="btn ghost">Explore More Solutions</a>
      </div>
    </div>
  </section>
"""


async def trust_style():
    return """  
<style>
    /* ============================================================= */
    /* THEME VARIABLES                                               */
    /* ============================================================= */
    :root {
        /* Light Theme (Default) */
        --trust-section-bg: #FFFFFF;
        --primary-btn-bg: #2563EB;
        --primary-btn-text: #FFFFFF;
        --primary-btn-border: #2563EB;
        --ghost-btn-bg: transparent;
        --ghost-btn-text: #374151;
        --ghost-btn-border: #6B7280;
        --title-text-color: #111827;
        --title-gradient: none;
        --title-accent: #2563EB;
        --panel-bg: #2563EB;
        --feature-card-bg: #FFFFFF;
        --feature-card-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.1), 0 4px 6px -2px rgba(37, 99, 235, 0.05);
        --feature-text-primary: #111827;
        --feature-text-secondary: #4B5563;
        --icon-bg: transparent;
        --icon-filter: invert(0); /* Keeps source black icons black */
        --dark-mode-element-display: none;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            /* Dark Theme Overrides */
            --trust-section-bg: #000000;
            --primary-btn-bg: #FFFFFF;
            --primary-btn-text: #000000;
            --primary-btn-border: #FFFFFF;
            --ghost-btn-bg: transparent;
            --ghost-btn-text: #DFDFDF;
            --ghost-btn-border: #DFDFDF;
            --title-text-color: #FFFFFF;
            --title-gradient: linear-gradient(90deg, rgba(255, 255, 255, 0.5) 0%, #FFFFFF 25%, #FFFFFF 75%, rgba(255, 255, 255, 0.5) 100%);
            --title-accent: #44B4FF;
            --panel-bg: linear-gradient(103.91deg, rgba(26, 26, 26, 0) 5.34%, rgba(65, 65, 65, 0.28) 35.27%, rgba(109, 109, 109, 0.49) 71.27%, rgba(128, 128, 128, 0.01) 95.55%), #151515;
            --feature-card-bg: transparent;
            --feature-card-shadow: none;
            --feature-text-primary: #FFFFFF;
            --feature-text-secondary: rgba(255, 255, 255, 0.7);
            --icon-bg: transparent;
            --icon-filter: invert(1); /* Makes source black icons white */
            --dark-mode-element-display: block;
        }
    }

    /* ============================================================= */
    /* STRUCTURAL LAYOUT (UNCHANGED SIZES & SPACING)                 */
    /* ============================================================= */
    .trust-section { position: relative; width: 100%; font-family: "Exo-2", "Poppins", sans-serif; }
    #trust-section-desktop { padding: 9.26vh 0 14.81vh; }
    .cta-row { position: relative; left: 50%; transform: translateX(-50%); display: flex; align-items: center; justify-content: center; gap: 2.24vw; z-index: 5; }
    .btn { display: inline-flex; align-items: center; justify-content: center; padding: 1.02vh 1.82vw; line-height: 1.33; cursor: pointer; font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 1.15vw; height: 6.02vh; box-sizing: border-box; border-radius: 9.52vw; white-space: nowrap; transition: transform 0.2s ease; border: 0.05vw solid; text-decoration: none; }
    .title { position: relative; width: 47.7vw; left: 50%; transform: translateX(-50%); margin-top: 7.41vh; font-weight: 700; font-size: 3.33vw; line-height: 4.01vw; text-align: center; letter-spacing: -0.02em; z-index: 5;}
    .panel { position: relative; width: 76.77vw; height: 65.37vh; left: 50%; transform: translateX(-50%); margin-top: 9.26vh; border-radius: 1.46vw; overflow: hidden; }
    .features { position: absolute; inset: 0; }
    .feature-text-box { padding: 5.81vh 2.5vw; display: flex; flex-direction: column; gap: 3.65vw; justify-content: space-evenly; align-items: center; }
    .upper-features, .lower-features { display: flex; justify-content: center; gap: 3.65vw; }
    .lower-features { gap: 12.65vw; }
    
    /* --- THE CORRECTED CARD STYLING --- */
    .feature { display: flex; align-items: flex-start; gap: 1.3vw; position: relative; padding: 2.78vh 2.08vw; box-sizing: border-box; width: 20.42vw; border-radius: 1.2rem; transition: transform 0.2s ease; }
    .feature:hover { transform: translateY(-5px); }

    .feature .icon { width: 2.6vw; height: 2.6vw; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .feature-content { flex-grow: 1; }
    .feature h3 { margin: 0; width: 100%; height: auto; font-family: 'Exo 2'; font-style: normal; font-weight: 500; font-size: 1.52vw; }
    .feature p { margin: 0.5rem 0 0; width: 100%; height: auto; font-family: 'Exo 2'; font-style: normal; font-size: 0.94vw; line-height: 2.04vh; }

    /* ============================================================= */
    /* THEMED VISUAL STYLES (NO LAYOUT CHANGES)                      */
    /* ============================================================= */
    .trust-section { background: var(--trust-section-bg); }
    
    /* Buttons */
    .btn.primary { background: var(--primary-btn-bg); color: var(--primary-btn-text); border-color: var(--primary-btn-border); padding: 1.02vh 2.34vw; }
    .btn.ghost { background: var(--ghost-btn-bg); color: var(--ghost-btn-text); border-color: var(--ghost-btn-border); }
    .btn:hover { transform: translateY(-2px); }

    /* Title */
    .title { color: var(--title-text-color); background: var(--title-gradient); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
    .title .accent { color: var(--title-accent); -webkit-text-fill-color: initial; }

    /* Panel */
    .features { background: var(--panel-bg); }
    
    /* Feature Cards */
    .feature { background: var(--feature-card-bg); box-shadow: var(--feature-card-shadow); }
    
    /* Icon & Text Theming */
    .feature .icon { background: var(--icon-bg); }
    .feature .icon img { width: 1.67vw; height: 1.67vw; filter: var(--icon-filter); }
    .feature h3 { color: var(--feature-text-primary); }
    .feature p { color: var(--feature-text-secondary); }
    
    /* Dark Mode Specific Elements */
    .frame-outline, .top-fade { display: var(--dark-mode-element-display); pointer-events: none; }
    .frame-outline { margin-top: 10.41vh; position: absolute; width: 73.18vw; height: 68.15vh; left: 50%; transform: translateX(-50%); top: 25.93vh; border: 0.05vw solid #FFF; border-bottom: none; border-radius: 3.38vw; z-index: 0; }
    .top-fade { position: absolute; inset: 0 0 auto 0; height: 20.37vh; background: radial-gradient(80% 100% at 50% 0%, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 70%); z-index: 0;}
    
    /* ============================================================= */
    /* MOBILE STYLES (ADAPTED FOR THEMES)                            */
    /* ============================================================= */
    @media (max-width: 768px) {
      #trust-section-desktop { display: none; }
      #trust-section-mobile { display: block; padding: 4rem 1rem 3rem; }
      #trust-section-mobile .cta-row { position: relative; left: auto; transform: none; flex-direction: column; width: 100%; gap: 1rem; margin-top: 3rem; }
      #trust-section-mobile .btn { width: 100%; max-width: 400px; height: auto; padding: 0.9rem 1.5rem; border-radius: 12px; border-width: 1px; font-size: 1rem; }
      #trust-section-mobile .title { position: relative; left: auto; transform: none; width: 100%; font-size: 2.25rem; line-height: 1.2; margin-top: 0; margin-bottom: 2.5rem; }
      #trust-section-mobile .panel { position: relative; left: auto; transform: none; width: 100%; height: auto; margin-top: 0; border-radius: 20px; }
      #trust-section-mobile .features { position: relative; }
      #trust-section-mobile .feature-text-box { padding: 2.5rem 1.5rem; gap: 2.5rem; flex-direction: column; align-items: flex-start; }
      #trust-section-mobile .upper-features, #trust-section-mobile .lower-features { display: none; }
      #trust-section-mobile .feature { width: 100%; height: auto; padding: 0; background: transparent; box-shadow: none; }
      #trust-section-mobile .feature:hover { transform: none; }
      #trust-section-mobile .feature .icon { width: 44px; height: 44px; border-radius: 8px; }
      #trust-section-mobile .feature .icon img { width: 24px; height: 24px; }
      #trust-section-mobile .feature h3 { width: auto; height: auto; font-size: 1.2rem; line-height: 1.3; margin: 0 0 0.5rem 0; }
      #trust-section-mobile .feature p { width: auto; height: auto; font-size: 0.95rem; line-height: 1.5; }
    }
</style>
"""


async def trust_script():
    return """
  <script>
    // This script is no longer necessary with the CSS-based approach,
    // but is kept here to maintain the original file structure.
    // The responsive view is now handled entirely by CSS media queries.
  </script>
"""