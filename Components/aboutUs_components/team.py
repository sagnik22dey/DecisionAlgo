async def team_body():
    return """
    <div class="team-section">
        <!-- Founder Section -->
        <div class="team-group">
            <h2 class="team-section-title founder-title">Meet The Founder</h2>
            <div class="profile-card founder-card">
                <div class="profile-image-wrapper">
                    <img src="../../Resources/Images/AboutUs/anand.png" alt="Divanshu Anand, Founder & CEO">
                </div>
                <div class="profile-text-content">
                    <h3>Divanshu Anand</h3>
                    <h4>Founder & CEO</h4>
                    <p>With 7+ years of experience, Divanshu has built data science teams, frameworks, and workflows from scratch for startups and Fortune 500 companies alike. His expertise spans across industries, helping businesses solve complex challenges with AI and analytics.<br><br>From collaborating with global brands to revolutionizing data-driven decision-making, his passion for automation, AI, and predictive analytics fuels DecisionAlgo’s success.</p>
                </div>
            </div>
        </div>

        <!-- Experts Section -->
        <div class="team-group">
            <h2 class="team-section-title experts-title">Meet Our Experts</h2>
            <div class="profile-card expert-card expert-card--reverse">
                <div class="profile-image-wrapper">
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
            <div class="profile-card expert-card">
                <div class="profile-image-wrapper">
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
        
        <!-- Decorative Glows -->
        <div class="glow-effect-1"></div>
        <div class="glow-effect-2"></div>
    </div>

    <script>
        function optimizeTeamLayout() {
            const isMobile = window.innerWidth <= 768;
            
            // Select all elements for styling
            const section = document.querySelector('.team-section');
            const cards = document.querySelectorAll('.profile-card');
            const imageWrappers = document.querySelectorAll('.profile-image-wrapper');
            const textContents = document.querySelectorAll('.profile-text-content');
            const sectionTitles = document.querySelectorAll('.team-section-title');
            const h3s = document.querySelectorAll('.profile-text-content h3');
            const h4s = document.querySelectorAll('.profile-text-content h4');
            const psAndLis = document.querySelectorAll('.profile-text-content p, .profile-text-content li');

            if (isMobile) {
                // Apply mobile styles
                section.style.padding = '10vh 0';
                section.style.gap = '8vh';

                sectionTitles.forEach(title => {
                    title.style.fontSize = '12vw';
                    title.style.textAlign = 'center';
                    title.style.marginBottom = '0';
                });

                cards.forEach(card => {
                    card.style.flexDirection = 'column';
                    card.style.padding = '0'; 
                });

                imageWrappers.forEach(wrapper => {
                    wrapper.style.position = 'relative';
                    wrapper.style.height = '50vh';
                    wrapper.style.width = '80vw';
                    wrapper.style.left = 'auto';
                    wrapper.style.right = 'auto';
                    wrapper.style.marginBottom = '-8vh';
                    wrapper.style.alignSelf = 'center';
                });

                textContents.forEach(content => {
                    const parentCard = content.parentElement;
                    content.style.width = '100vw';
                    content.style.marginLeft = '0';
                    content.style.marginRight = '0';
                    content.style.padding = '12vh 8vw 8vw 8vw';
                    content.style.textAlign = 'center';
                    content.style.background = getComputedStyle(parentCard).background;
                });

                h3s.forEach(h3 => h3.style.fontSize = '8vw');
                h4s.forEach(h4 => h4.style.fontSize = '5.5vw');
                psAndLis.forEach(p => p.style.fontSize = '4vw');
                
                document.querySelectorAll('.profile-text-content ul').forEach(ul => {
                    ul.style.textAlign = 'left';
                    ul.style.display = 'inline-block';
                    ul.style.paddingLeft = '5vw';
                });

            } else {
                // Revert to desktop styles by removing inline styles
                section.style.padding = '';
                section.style.gap = '';

                sectionTitles.forEach(title => {
                    title.style.fontSize = '';
                    title.style.marginBottom = '';
                    if (title.classList.contains('founder-title')) {
                        title.style.textAlign = 'right';
                    } else {
                        title.style.textAlign = 'left';
                    }
                });

                cards.forEach(card => {
                    card.style.flexDirection = card.classList.contains('expert-card--reverse') ? 'row-reverse' : 'row';
                    card.style.padding = '';
                });

                imageWrappers.forEach(wrapper => {
                    wrapper.style.position = 'absolute';
                    wrapper.style.height = '';
                    wrapper.style.width = '';
                    wrapper.style.marginBottom = '';
                    wrapper.style.alignSelf = '';
                    
                    const card = wrapper.parentElement;
                    if (card.classList.contains('expert-card--reverse')) {
                        wrapper.style.right = '10vw';
                        wrapper.style.left = 'auto';
                    } else {
                        wrapper.style.left = '10vw';
                        wrapper.style.right = 'auto';
                    }
                });

                textContents.forEach(content => {
                    content.style.width = '';
                    content.style.padding = '';
                    content.style.textAlign = 'left';
                    content.style.background = '';
                    
                    const card = content.parentElement;
                    if (card.classList.contains('expert-card--reverse')) {
                        content.style.marginRight = '45vw';
                        content.style.marginLeft = '0';
                    } else {
                        content.style.marginLeft = '45vw';
                        content.style.marginRight = '0';
                    }
                });

                h3s.forEach(h3 => h3.style.fontSize = '');
                h4s.forEach(h4 => h4.style.fontSize = '');
                psAndLis.forEach(p => p.style.fontSize = '');
                
                document.querySelectorAll('.profile-text-content ul').forEach(ul => {
                    ul.style.textAlign = '';
                    ul.style.display = '';
                    ul.style.paddingLeft = '';
                });
            }
        }
        window.addEventListener('load', optimizeTeamLayout);
        window.addEventListener('resize', optimizeTeamLayout);
    </script>
    """

async def team_style():
    return """
    <style>
        .team-section {
            background-color: #1c1c1c;
            padding: 15vh 0;
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 10vh;
        }

        .team-group {
            display: flex;
            flex-direction: column;
            gap: 5vh;
        }

        .team-section-title {
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 5vw;
            line-height: 1.2;
            letter-spacing: -0.02em;
            text-transform: capitalize;
            background: linear-gradient(90deg, rgba(235, 240, 243, 0.3) 0%, #EBF0F3 15%, #EBF0F3 55%, rgba(235, 239, 243, 0.72) 80%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            padding: 0 5vw;
        }

        .founder-title { text-align: right; }
        .experts-title { text-align: left; }

        .profile-card {
            display: flex;
            align-items: center;
            position: relative;
            width: 100vw;
            padding: 5vh 0;
            min-height: 40vh;
        }

        .founder-card, .expert-card:nth-of-type(2) {
            background: linear-gradient(90deg, #DCF3FF 0%, #5FC7FB 100%);
        }
        .expert-card:nth-of-type(1) {
            background: linear-gradient(90deg, #5FC7FB 0%, #DCF3FF 100%);
        }

        .expert-card--reverse { flex-direction: row-reverse; }

        .profile-image-wrapper {
            position: absolute;
            bottom: 0;
            height: 55vh;
            width: 35vw;
            z-index: 2;
        }

        .profile-card:not(.expert-card--reverse) .profile-image-wrapper { left: 10vw; }
        .profile-card.expert-card--reverse .profile-image-wrapper { right: 10vw; }

        .profile-image-wrapper img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            object-position: bottom;
            filter: grayscale(100%);
        }

        .profile-text-content {
            color: #000;
            font-family: 'Exo 2', sans-serif;
            position: relative;
            z-index: 1;
            width: 45vw;
        }
        
        .profile-card:not(.expert-card--reverse) .profile-text-content { margin-left: 45vw; padding-left: 5vw; }
        .profile-card.expert-card--reverse .profile-text-content { margin-right: 45vw; padding-left: 5vw; }
        
        .profile-text-content h3 { font-size: 3.5vw; font-weight: 700; line-height: 1.2; }
        .profile-text-content h4 { font-size: 2vw; font-weight: 600; line-height: 1.2; margin: 1vh 0 2vh; }
        .profile-text-content p, .profile-text-content li { font-size: 1.2vw; line-height: 1.5; font-weight: 400; }
        
        .profile-text-content ul {
            list-style-type: none;
            padding-left: 1.5vw;
        }
        .profile-text-content ul li {
            position: relative;
            padding-left: 1.5vw;
            margin-bottom: 1vh;
        }
        .profile-text-content ul li::before {
            content: '-';
            position: absolute;
            left: 0;
            color: #000;
        }
        
        .glow-effect-1, .glow-effect-2 {
            position: absolute;
            width: 10vw;
            height: 20vh;
            background: #FFFFFF;
            opacity: 0.1;
            filter: blur(10vw);
            pointer-events: none;
            z-index: 0;
        }
        .glow-effect-1 { top: 10vh; right: 5vw; }
        .glow-effect-2 { top: 30vh; left: 2vw; }
    </style>
    """