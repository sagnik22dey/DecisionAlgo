async def team_body():
    return """
    <div class="eclipse-glow-1">
        <img src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="Mahak Dhameja, VP, Strategy Advisor">
    </div>
    <div class="eclipse-glow-2">
        <img src="../../Resources/Images/Dashboard/ecliplse_glow.png" alt="Mahak Dhameja, VP, Strategy Advisor">
    </div>
    <div class="team-section">        
        <!-- Founder Section -->
        <div class="team-group">
            <div class="section-bar">
                <h2 class="team-section-title founder-title">Meet The <span class="highlight">Founder</span></h2>
            </div>

            <div class="profile-card founder-card">
                <div class="profile-image-wrapper founder-image">
                    <img src="../../Resources/Images/AboutUs/anand.png" alt="Divanshu Anand, Founder & CEO">
                </div>
                <div class="profile-text-content">
                    <h3>Divanshu Anand</h3>
                    <h4>Founder & CEO</h4>
                    <p>With 7+ years of experience, Divanshu has built data science teams, frameworks, and workflows from scratch for startups and Fortune 500 companies alike. His expertise spans across industries, helping businesses solve complex challenges with AI and analytics.</p>
                    <p>From collaborating with global brands to revolutionizing data-driven decision-making, his passion for automation, AI, and predictive analytics fuels DecisionAlgo’s success.</p>
                </div>
            </div>
        </div>

        <!-- Experts Section -->
        <div class="team-group">
            <div class="section-bar">
                <h2 class="team-section-title experts-title">Meet Our <span class="highlight">Experts</span></h2>
            </div>

            <!-- Vishal (image right) -->
            <div class="profile-card expert-card expert-card--reverse">
                <div class="profile-image-wrapper profile-image-right">
                    <img src="../../Resources/Images/AboutUs/vishal.png" alt="Dr. Vishal Vaibhav, VP, Systems Architect Advisor">
                </div>
                <div class="profile-text-content">
                    <h3>Dr. Vishal Vaibhav</h3>
                    <h4>VP, Systems Architect Advisor</h4>
                    <ul>
                        <li>BTech from IIT Delhi</li>
                        <li>Dual PhDs from FAU Erlangen-Nürnberg & Max Planck Institute</li>
                        <li>Professor at IIT Delhi</li>
                        <li>Researcher & Innovator in emerging tech</li>
                    </ul>
                </div>
            </div>

            <!-- Mahak (image left) -->
            <div class="profile-card expert-card expert-card--normal">
                <div class="profile-image-wrapper profile-image-left">
                    <img src="../../Resources/Images/AboutUs/mahak.png" alt="Mahak Dhameja, VP, Strategy Advisor">
                </div>
                <div class="profile-text-content">
                    <h3>Mahak Dhameja</h3>
                    <h4>VP, Strategy Advisor</h4>
                    <ul>
                        <li>8+ years in global tech strategy advisory</li>
                        <li>Oxford MBA - A world-class business leader trained at one of the most prestigious institutions.</li>
                        <li>BITS Pilani Engineer – A strong foundation in innovation and technology.</li>
                        <li>Passionate about scaling startups & driving sustainability</li>
                    </ul>
                </div>
            </div>
        </div>

    </div>

    <script>
        // Mobile/desktop optimizer (vw/vh only)
        function optimizeTeamLayout(){
            const isMobile = window.innerWidth <= 768;

            const section = document.querySelector('.team-section');
            if (!section) return;
            const cards = section.querySelectorAll('.profile-card');
            const imageWrappers = section.querySelectorAll('.profile-image-wrapper');
            const textContents = section.querySelectorAll('.profile-text-content');
            const titles = section.querySelectorAll('.team-section-title');

            if(isMobile){
                section.style.gap = '8vh';
                titles.forEach(t=>{
                    t.style.fontSize = '12vw';
                    t.style.textAlign = 'center';
                });

                cards.forEach(card=>{
                    card.style.flexDirection = 'column';
                    card.style.minHeight = '78vh';
                    card.style.padding = '0';
                    card.style.background = 'none';
                });

                imageWrappers.forEach(w=>{
                    w.style.position = 'relative';
                    w.style.height = '44vh';
                    w.style.width  = '86vw';
                    w.style.left = 'auto';
                    w.style.right = 'auto';
                    w.style.bottom = 'auto';
                    w.style.margin = '0 auto -8vh auto';
                });

                textContents.forEach(c=>{
                    const parent = c.closest('.profile-card');
                    c.style.width = '100vw';
                    c.style.margin = '0';
                    c.style.padding = '14vh 7vw 8vh 7vw';
                    c.style.textAlign = 'center';

                    // Apply the matching gradient to the text block itself on mobile
                    if(parent.classList.contains('expert-card--reverse')){
                        c.style.background = 'linear-gradient(90deg, #5FC7FB 0%, #D7F2FF 100%)';
                    }else{
                        c.style.background = 'linear-gradient(90deg, #DCF3FF 0%, #5FC7FB 100%)';
                    }
                });

                document.querySelectorAll('.profile-text-content ul').forEach(ul=>{
                    ul.style.textAlign = 'left';
                    ul.style.display = 'inline-block';
                    ul.style.paddingLeft = '5vw';
                });
            }else{
                // clear inline overrides
                section.style.gap = '';
                titles.forEach(t=>{ t.style.cssText=''; });
                cards.forEach(card=>{ card.style.cssText=''; });
                imageWrappers.forEach(w=>{ w.style.cssText=''; });
                textContents.forEach(c=>{ c.style.cssText=''; });
                document.querySelectorAll('.profile-text-content ul').forEach(ul=>{ ul.style.cssText=''; });
            }
        }

        window.addEventListener('load', optimizeTeamLayout);
        window.addEventListener('resize', optimizeTeamLayout);
    </script>
    """
async def team_style():
    return """
    <style>
        /* --- Default: Dark Mode --- */
        .eclipse-glow-1 {
            margin-top: -27vw;
            z-index: 5;
            position: absolute;
            margin-left: -43.22vw;
        }
        .eclipse-glow-2 {
            margin-top: -44vw;
            z-index: 5;
            position: absolute;
            margin-left: 65vw;
        }
        .team-section{
            background-color:transparent;
            padding:15vh 0;
            position:relative;
            overflow:hidden;
            display:flex;
            flex-direction:column;
            gap:10vh;
            width:100vw;
        }

        .team-group{
            display:flex;
            flex-direction:column;
            gap:5vh;
            width:100vw;
        }

        .section-bar{
            width:100vw;
            background:transparent;
            padding:6vh 0 4vh 0;
        }

        .team-section-title{
            font-family:'Exo 2',sans-serif;
            font-weight:700;
            font-size:5vw;
            line-height:1.15;
            letter-spacing:-0.02em;
            text-transform:capitalize;
            background:linear-gradient(90deg, rgba(235,240,243,0.3) 0%, #EBF0F3 15%, #EBF0F3 55%, rgba(235,239,243,0.72) 80%);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
            background-clip:text;
            text-fill-color:transparent;
            padding:0 5vw;
            width:100vw;
        }
        .founder-title{text-align:right;}
        .experts-title{text-align:left;}

        .profile-card{
            display:flex;
            align-items:center;
            position:relative;
            width:100vw;
            min-height:62vh;
            padding:6vh 0;
        }

        .founder-card,
        .expert-card--normal{
            background:linear-gradient(90deg, #DCF3FF 0%, #5FC7FB 100%);
        }

        .expert-card--reverse{
            background:linear-gradient(90deg, #5FC7FB 0%, #D7F2FF 100%);
            flex-direction:row-reverse;
            margin-bottom:20vw;
            margin-top:5vw;
        }

        .profile-image-wrapper{
            position:absolute;
            height:100vh;
            width:39vw;
            z-index:2;
        }
        .profile-card:not(.expert-card--reverse) .profile-image-wrapper{ bottom:4.65vw;}
        .profile-card:not(.expert-card--reverse):not(.expert-card--normal) .profile-image-wrapper{ bottom:4.5vw;}
        .profile-card.expert-card--reverse .profile-image-wrapper{right:8vw; bottom:4.65vw;}

        .profile-image-wrapper img{
            width:100%;
            height:100%;
            object-fit:contain;
            object-position:bottom;
            filter:grayscale(100%);
            scale:1.19;
        }

        .profile-text-content{
            color:#000;
            font-family:'Exo 2',sans-serif;
            position:relative;
            z-index:1;
            width:44vw;
            padding:0 5vw;
        }
        .profile-card:not(.expert-card--reverse) .profile-text-content{ margin-left:48vw; }
        .profile-card.expert-card--reverse .profile-text-content{ margin-right:48vw; margin-left:0; }

        .profile-text-content h3{ font-size:3.2vw; font-weight:700; line-height:1.2; }
        .profile-text-content h4{ font-size:1.85vw; font-weight:600; line-height:1.2; margin:1.5vw 0 3vw 0; }
        .profile-text-content p, .profile-text-content li{ font-size:1.15vw; line-height:1.55; font-weight:400; }

        .profile-text-content ul{ list-style-type:none; padding-left:1.6vw; margin:0; }
        .profile-text-content ul li{ position:relative; padding-left:1.6vw; margin-bottom:1.2vh; }
        .profile-text-content ul li::before{ content:'-'; position:absolute; left:0; color:#000; }
        
        /* --- Light Mode --- */
        @media (prefers-color-scheme: light) {
            .eclipse-glow-1,
            .eclipse-glow-2 {
                display: none;
            }

            .team-section-title {
                background: none;
                -webkit-background-clip: unset;
                -webkit-text-fill-color: unset;
                background-clip: unset;
                text-fill-color: unset;
                color: #111;
            }

            .team-section-title .highlight {
                color: #3898F2; /* Blue color for the highlighted word */
            }
            
            .team-section {
                 background-color: #FFFFFF; /* Ensures a white background for light mode */
            }
        }
        
        /* Mobile Styles */
        @media (max-width: 768px) {
            .eclipse-glow-1,
            .eclipse-glow-2 {
                display: none;
            }

            .image-frame {
                margin-left: 4vw;
            }

            .team-section {
                gap: 8vh;
                padding: 0vh 0;
            }

            .team-section-title {
                font-size: 12vw;
                text-align: center !important;
                padding: 0 5vw;
            }

            .profile-card {
                flex-direction: column !important;
                min-height: 0vh;
                padding: 0;
                background: none !important;
                margin-bottom: 0 !important;
                margin-top: -18vh !important;
            }

            .profile-image-wrapper {
                position: relative !important;
                height: 44vh;
                width: 86vw;
                left: auto !important;
                right: auto !important;
                bottom: auto !important;
                margin: 0 auto -8vh auto;
            }

            .profile-image-wrapper img {
                scale: 0.8;
                object-fit: cover;
                border: 0.14vh solid white;
                border-radius: 9vw;
                margin-top: 10vh;
                background-color: black;
                object-position: top;
            }

            .profile-text-content {
                width: 100vw !important;
                margin: 0 !important;
                padding: 14vh 7vw 8vh 7vw;
                text-align: center;
                background: linear-gradient(90deg, #DCF3FF 0%, #5FC7FB 100%);
            }

            .expert-card--reverse .profile-text-content {
                background: linear-gradient(90deg, #5FC7FB 0%, #D7F2FF 100%) !important;
            }

            .profile-text-content h3 {
                font-size: 8vw;
                margin-bottom: 2vh;
            }

            .profile-text-content h4 {
                font-size: 5vw;
                margin: 1vh 0 3vh 0;
            }

            .profile-text-content p,
            .profile-text-content li {
                font-size: 4vw;
                line-height: 1.6;
            }

            .profile-text-content ul {
                text-align: left;
                display: inline-block;
                padding-left: 5vw;
                margin-top: 2vh;
            }

            .profile-text-content ul li {
                padding-left: 4vw;
                margin-bottom: 1.5vh;
            }
        }

        /* Tablet Styles */
        @media (max-width: 1024px) and (min-width: 769px) {
            .team-section-title {
                font-size: 6vw;
            }

            .profile-text-content h3 {
                font-size: 4vw;
            }

            .profile-text-content h4 {
                font-size: 2.2vw;
            }

            .profile-text-content p,
            .profile-text-content li {
                font-size: 1.4vw;
            }

            .profile-image-wrapper {
                width: 45vw;
            }

            .profile-text-content {
                width: 50vw;
            }

            .profile-card:not(.expert-card--reverse) .profile-text-content {
                margin-left: 45vw;
            }

            .profile-card.expert-card--reverse .profile-text-content {
                margin-right: 45vw;
            }
        }
    </style>
    """