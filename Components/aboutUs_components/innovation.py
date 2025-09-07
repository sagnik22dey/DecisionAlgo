async def innovation_body():
    return """
    <div class="innovation-section">
        <div class="innovation-content-wrapper">
            <!-- Left Column: Text Content -->
            <div class="innovation-text-content">
                <div class="innovation-header">
                    <h1>Award-Winning<br>Innovation</h1>
                    <p>At DecisionAlgo, we turn data into actionable insights that fuel business growth. Recognized by Startup India and backed by industry giants like AWS and DigitalOcean, we empower businesses with cutting-edge AI, automation, and data-driven solutions.</p>
                    <a href="#" class="read-more-btn">
                        <span>Read More</span>
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M2 8H10M10 8L7.33333 5.33333M10 8L7.33333 10.6667M8 14C9.5913 14 11.1174 13.3679 12.2426 12.2426C13.3679 11.1174 14 9.5913 14 8C14 6.4087 13.3679 4.88258 12.2426 3.75736C11.1174 2.63214 9.5913 2 8 2" stroke="black" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </a>
                </div>

                <div class="mission-vision-container">
                    <div class="mission-item">
                        <div class="icon-wrapper">
                            <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <mask id="mask0_370_281" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="25" height="25">
                            <rect x="0.914551" y="0.347656" width="23.7947" height="23.7947" fill="#D9D9D9"/>
                            </mask>
                            <g mask="url(#mask0_370_281)">
                            <path d="M10.5809 21.168C9.7382 21.168 9.01114 20.8747 8.39975 20.2881C7.78836 19.7015 7.44135 18.9951 7.35873 18.1689C6.36729 18.0367 5.54108 17.5988 4.88012 16.8552C4.21915 16.1117 3.88867 15.2359 3.88867 14.2279C3.88867 13.8809 3.93411 13.538 4.025 13.1993C4.11588 12.8606 4.2522 12.5425 4.43397 12.245C4.2522 11.9476 4.11588 11.6336 4.025 11.3032C3.93411 10.9727 3.88867 10.6257 3.88867 10.2621C3.88867 9.25417 4.21915 8.38252 4.88012 7.6472C5.54108 6.91188 6.35902 6.47812 7.33394 6.34593C7.38352 5.5032 7.72226 4.78853 8.35018 4.20193C8.97809 3.61532 9.72167 3.32202 10.5809 3.32202C11.0106 3.32202 11.4113 3.40464 11.7831 3.56988C12.1548 3.73512 12.4977 3.9582 12.8117 4.23911C13.1091 3.9582 13.4479 3.73512 13.8279 3.56988C14.208 3.40464 14.6128 3.32202 15.0424 3.32202C15.9017 3.32202 16.6411 3.61119 17.2608 4.18954C17.8804 4.76788 18.2151 5.47842 18.2646 6.32114C19.2395 6.45334 20.0616 6.89122 20.7308 7.63481C21.4001 8.37839 21.7347 9.25417 21.7347 10.2621C21.7347 10.6257 21.6892 10.9727 21.5984 11.3032C21.5075 11.6336 21.3712 11.9476 21.1894 12.245C21.3712 12.5425 21.5075 12.8606 21.5984 13.1993C21.6892 13.538 21.7347 13.8809 21.7347 14.2279C21.7347 15.2524 21.4001 16.1323 20.7308 16.8676C20.0616 17.603 19.2313 18.0367 18.2398 18.1689C18.1572 18.9951 17.8143 19.7015 17.2112 20.2881C16.6081 20.8747 15.8852 21.168 15.0424 21.168C14.6293 21.168 14.2286 21.0895 13.8403 20.9326C13.452 20.7756 13.1091 20.5566 12.8117 20.2757C12.4977 20.5566 12.1507 20.7756 11.7707 20.9326C11.3906 21.0895 10.994 21.168 10.5809 21.168ZM13.8031 6.54422V17.9458C13.8031 18.2928 13.9229 18.5861 14.1625 18.8257C14.4021 19.0653 14.6954 19.1851 15.0424 19.1851C15.3729 19.1851 15.658 19.053 15.8976 18.7886C16.1372 18.5242 16.2652 18.2267 16.2817 17.8963C15.9347 17.7641 15.6166 17.5864 15.3275 17.3634C15.0383 17.1403 14.778 16.8718 14.5467 16.5578C14.3815 16.3265 14.3195 16.0786 14.3608 15.8142C14.4021 15.5498 14.5384 15.335 14.7698 15.1698C15.0011 15.0046 15.249 14.9426 15.5134 14.9839C15.7778 15.0252 15.9926 15.1615 16.1578 15.3929C16.3396 15.6573 16.5709 15.8597 16.8518 16.0001C17.1327 16.1406 17.4384 16.2108 17.7689 16.2108C18.3142 16.2108 18.781 16.0167 19.1693 15.6283C19.5576 15.24 19.7518 14.7732 19.7518 14.2279C19.7518 14.1453 19.7477 14.0627 19.7394 13.9801C19.7311 13.8974 19.7105 13.8148 19.6774 13.7322C19.3965 13.8974 19.095 14.0214 18.7727 14.104C18.4505 14.1866 18.1159 14.2279 17.7689 14.2279C17.488 14.2279 17.2525 14.1329 17.0625 13.9429C16.8725 13.7529 16.7775 13.5174 16.7775 13.2365C16.7775 12.9556 16.8725 12.7201 17.0625 12.5301C17.2525 12.34 17.488 12.245 17.7689 12.245C18.3142 12.245 18.781 12.0509 19.1693 11.6626C19.5576 11.2742 19.7518 10.8074 19.7518 10.2621C19.7518 9.71684 19.5576 9.25417 19.1693 8.87411C18.781 8.49406 18.3142 8.29577 17.7689 8.27925C17.5871 8.57668 17.3517 8.83694 17.0625 9.06001C16.7733 9.28309 16.4552 9.46072 16.1082 9.59291C15.8438 9.69206 15.5877 9.6838 15.3399 9.56813C15.092 9.45246 14.9268 9.26243 14.8441 8.99805C14.7615 8.73366 14.7739 8.47754 14.8813 8.22968C14.9887 7.98181 15.1746 7.81657 15.439 7.73395C15.6869 7.65133 15.8893 7.50262 16.0463 7.2878C16.2032 7.07299 16.2817 6.82513 16.2817 6.54422C16.2817 6.19721 16.1619 5.90391 15.9223 5.66431C15.6827 5.42471 15.3894 5.30491 15.0424 5.30491C14.6954 5.30491 14.4021 5.42471 14.1625 5.66431C13.9229 5.90391 13.8031 6.19721 13.8031 6.54422ZM11.8202 17.9458V6.54422C11.8202 6.19721 11.7004 5.90391 11.4608 5.66431C11.2212 5.42471 10.9279 5.30491 10.5809 5.30491C10.2339 5.30491 9.94062 5.42471 9.70102 5.66431C9.46142 5.90391 9.34162 6.19721 9.34162 6.54422C9.34162 6.8086 9.41598 7.05233 9.5647 7.27541C9.71341 7.49848 9.9117 7.65133 10.1596 7.73395C10.4239 7.81657 10.614 7.98181 10.7296 8.22968C10.8453 8.47754 10.8618 8.73366 10.7792 8.99805C10.6801 9.26243 10.5066 9.45246 10.2587 9.56813C10.0108 9.6838 9.75472 9.69206 9.49034 9.59291C9.14333 9.46072 8.82524 9.28309 8.53607 9.06001C8.2469 8.83694 8.01143 8.57668 7.82967 8.27925C7.3009 8.29577 6.84235 8.49819 6.45404 8.88651C6.06572 9.27482 5.87156 9.73337 5.87156 10.2621C5.87156 10.8074 6.06572 11.2742 6.45404 11.6626C6.84235 12.0509 7.30916 12.245 7.85445 12.245C8.13536 12.245 8.37083 12.34 8.56086 12.5301C8.75088 12.7201 8.8459 12.9556 8.8459 13.2365C8.8459 13.5174 8.75088 13.7529 8.56086 13.9429C8.37083 14.1329 8.13536 14.2279 7.85445 14.2279C7.50745 14.2279 7.17283 14.1866 6.85061 14.104C6.52839 14.0214 6.22683 13.8974 5.94592 13.7322C5.91287 13.8148 5.89222 13.8974 5.88396 13.9801C5.87569 14.0627 5.87156 14.1453 5.87156 14.2279C5.87156 14.7732 6.06572 15.24 6.45404 15.6283C6.84235 16.0167 7.30916 16.2108 7.85445 16.2108C8.18493 16.2108 8.49063 16.1406 8.77154 16.0001C9.05245 15.8597 9.28379 15.6573 9.46555 15.3929C9.63079 15.1615 9.84561 15.0252 10.11 14.9839C10.3744 14.9426 10.6222 15.0046 10.8536 15.1698C11.0849 15.335 11.2212 15.5498 11.2625 15.8142C11.3039 16.0786 11.2419 16.3265 11.0766 16.5578C10.8453 16.8718 10.5809 17.1444 10.2835 17.3758C9.98606 17.6071 9.66384 17.7889 9.31683 17.9211C9.33336 18.2515 9.46555 18.5448 9.71341 18.801C9.96127 19.0571 10.2504 19.1851 10.5809 19.1851C10.9279 19.1851 11.2212 19.0653 11.4608 18.8257C11.7004 18.5861 11.8202 18.2928 11.8202 17.9458Z" fill="#0C0C0C"/>
                            </g>
                            </svg>

                        </div>
                        <h2>Our Mission</h2>
                        <p>We help businesses leverage AI and data-driven strategies to make smarter decisions, streamline operations, and drive growth.</p>
                    </div>
                    <div class="vision-item">
                        <div class="icon-wrapper">
                            <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <mask id="mask0_370_281" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="25" height="25">
                            <rect x="0.914551" y="0.347656" width="23.7947" height="23.7947" fill="#D9D9D9"/>
                            </mask>
                            <g mask="url(#mask0_370_281)">
                            <path d="M10.5809 21.168C9.7382 21.168 9.01114 20.8747 8.39975 20.2881C7.78836 19.7015 7.44135 18.9951 7.35873 18.1689C6.36729 18.0367 5.54108 17.5988 4.88012 16.8552C4.21915 16.1117 3.88867 15.2359 3.88867 14.2279C3.88867 13.8809 3.93411 13.538 4.025 13.1993C4.11588 12.8606 4.2522 12.5425 4.43397 12.245C4.2522 11.9476 4.11588 11.6336 4.025 11.3032C3.93411 10.9727 3.88867 10.6257 3.88867 10.2621C3.88867 9.25417 4.21915 8.38252 4.88012 7.6472C5.54108 6.91188 6.35902 6.47812 7.33394 6.34593C7.38352 5.5032 7.72226 4.78853 8.35018 4.20193C8.97809 3.61532 9.72167 3.32202 10.5809 3.32202C11.0106 3.32202 11.4113 3.40464 11.7831 3.56988C12.1548 3.73512 12.4977 3.9582 12.8117 4.23911C13.1091 3.9582 13.4479 3.73512 13.8279 3.56988C14.208 3.40464 14.6128 3.32202 15.0424 3.32202C15.9017 3.32202 16.6411 3.61119 17.2608 4.18954C17.8804 4.76788 18.2151 5.47842 18.2646 6.32114C19.2395 6.45334 20.0616 6.89122 20.7308 7.63481C21.4001 8.37839 21.7347 9.25417 21.7347 10.2621C21.7347 10.6257 21.6892 10.9727 21.5984 11.3032C21.5075 11.6336 21.3712 11.9476 21.1894 12.245C21.3712 12.5425 21.5075 12.8606 21.5984 13.1993C21.6892 13.538 21.7347 13.8809 21.7347 14.2279C21.7347 15.2524 21.4001 16.1323 20.7308 16.8676C20.0616 17.603 19.2313 18.0367 18.2398 18.1689C18.1572 18.9951 17.8143 19.7015 17.2112 20.2881C16.6081 20.8747 15.8852 21.168 15.0424 21.168C14.6293 21.168 14.2286 21.0895 13.8403 20.9326C13.452 20.7756 13.1091 20.5566 12.8117 20.2757C12.4977 20.5566 12.1507 20.7756 11.7707 20.9326C11.3906 21.0895 10.994 21.168 10.5809 21.168ZM13.8031 6.54422V17.9458C13.8031 18.2928 13.9229 18.5861 14.1625 18.8257C14.4021 19.0653 14.6954 19.1851 15.0424 19.1851C15.3729 19.1851 15.658 19.053 15.8976 18.7886C16.1372 18.5242 16.2652 18.2267 16.2817 17.8963C15.9347 17.7641 15.6166 17.5864 15.3275 17.3634C15.0383 17.1403 14.778 16.8718 14.5467 16.5578C14.3815 16.3265 14.3195 16.0786 14.3608 15.8142C14.4021 15.5498 14.5384 15.335 14.7698 15.1698C15.0011 15.0046 15.249 14.9426 15.5134 14.9839C15.7778 15.0252 15.9926 15.1615 16.1578 15.3929C16.3396 15.6573 16.5709 15.8597 16.8518 16.0001C17.1327 16.1406 17.4384 16.2108 17.7689 16.2108C18.3142 16.2108 18.781 16.0167 19.1693 15.6283C19.5576 15.24 19.7518 14.7732 19.7518 14.2279C19.7518 14.1453 19.7477 14.0627 19.7394 13.9801C19.7311 13.8974 19.7105 13.8148 19.6774 13.7322C19.3965 13.8974 19.095 14.0214 18.7727 14.104C18.4505 14.1866 18.1159 14.2279 17.7689 14.2279C17.488 14.2279 17.2525 14.1329 17.0625 13.9429C16.8725 13.7529 16.7775 13.5174 16.7775 13.2365C16.7775 12.9556 16.8725 12.7201 17.0625 12.5301C17.2525 12.34 17.488 12.245 17.7689 12.245C18.3142 12.245 18.781 12.0509 19.1693 11.6626C19.5576 11.2742 19.7518 10.8074 19.7518 10.2621C19.7518 9.71684 19.5576 9.25417 19.1693 8.87411C18.781 8.49406 18.3142 8.29577 17.7689 8.27925C17.5871 8.57668 17.3517 8.83694 17.0625 9.06001C16.7733 9.28309 16.4552 9.46072 16.1082 9.59291C15.8438 9.69206 15.5877 9.6838 15.3399 9.56813C15.092 9.45246 14.9268 9.26243 14.8441 8.99805C14.7615 8.73366 14.7739 8.47754 14.8813 8.22968C14.9887 7.98181 15.1746 7.81657 15.439 7.73395C15.6869 7.65133 15.8893 7.50262 16.0463 7.2878C16.2032 7.07299 16.2817 6.82513 16.2817 6.54422C16.2817 6.19721 16.1619 5.90391 15.9223 5.66431C15.6827 5.42471 15.3894 5.30491 15.0424 5.30491C14.6954 5.30491 14.4021 5.42471 14.1625 5.66431C13.9229 5.90391 13.8031 6.19721 13.8031 6.54422ZM11.8202 17.9458V6.54422C11.8202 6.19721 11.7004 5.90391 11.4608 5.66431C11.2212 5.42471 10.9279 5.30491 10.5809 5.30491C10.2339 5.30491 9.94062 5.42471 9.70102 5.66431C9.46142 5.90391 9.34162 6.19721 9.34162 6.54422C9.34162 6.8086 9.41598 7.05233 9.5647 7.27541C9.71341 7.49848 9.9117 7.65133 10.1596 7.73395C10.4239 7.81657 10.614 7.98181 10.7296 8.22968C10.8453 8.47754 10.8618 8.73366 10.7792 8.99805C10.6801 9.26243 10.5066 9.45246 10.2587 9.56813C10.0108 9.6838 9.75472 9.69206 9.49034 9.59291C9.14333 9.46072 8.82524 9.28309 8.53607 9.06001C8.2469 8.83694 8.01143 8.57668 7.82967 8.27925C7.3009 8.29577 6.84235 8.49819 6.45404 8.88651C6.06572 9.27482 5.87156 9.73337 5.87156 10.2621C5.87156 10.8074 6.06572 11.2742 6.45404 11.6626C6.84235 12.0509 7.30916 12.245 7.85445 12.245C8.13536 12.245 8.37083 12.34 8.56086 12.5301C8.75088 12.7201 8.8459 12.9556 8.8459 13.2365C8.8459 13.5174 8.75088 13.7529 8.56086 13.9429C8.37083 14.1329 8.13536 14.2279 7.85445 14.2279C7.50745 14.2279 7.17283 14.1866 6.85061 14.104C6.52839 14.0214 6.22683 13.8974 5.94592 13.7322C5.91287 13.8148 5.89222 13.8974 5.88396 13.9801C5.87569 14.0627 5.87156 14.1453 5.87156 14.2279C5.87156 14.7732 6.06572 15.24 6.45404 15.6283C6.84235 16.0167 7.30916 16.2108 7.85445 16.2108C8.18493 16.2108 8.49063 16.1406 8.77154 16.0001C9.05245 15.8597 9.28379 15.6573 9.46555 15.3929C9.63079 15.1615 9.84561 15.0252 10.11 14.9839C10.3744 14.9426 10.6222 15.0046 10.8536 15.1698C11.0849 15.335 11.2212 15.5498 11.2625 15.8142C11.3039 16.0786 11.2419 16.3265 11.0766 16.5578C10.8453 16.8718 10.5809 17.1444 10.2835 17.3758C9.98606 17.6071 9.66384 17.7889 9.31683 17.9211C9.33336 18.2515 9.46555 18.5448 9.71341 18.801C9.96127 19.0571 10.2504 19.1851 10.5809 19.1851C10.9279 19.1851 11.2212 19.0653 11.4608 18.8257C11.7004 18.5861 11.8202 18.2928 11.8202 17.9458Z" fill="#0C0C0C"/>
                            </g>
                            </svg>
                        </div>
                        <h2>Our Vision</h2>
                        <p>To redefine decision-making worldwide by transforming raw data into game-changing business intelligence.</p>
                    </div>
                </div>
            </div>

            <!-- Right Column: Image Content -->
            <div class="innovation-image-content">
                <div class="image-frame">
                    <img src="../../Resources/Images/AboutUs/award_ceremony.png" alt="Award ceremony for innovation" class="award-image">
                </div>
            </div>
        </div>
        <!-- Decorative Glow -->
        <div class="glow-effect"></div>
    </div>
    
    <script>
        function optimizeInnovationLayout() {
            const isMobile = window.innerWidth <= 768;
            const wrapper = document.querySelector('.innovation-content-wrapper');
            const missionVision = document.querySelector('.mission-vision-container');
            const headline = document.querySelector('.innovation-header h1');
            const mainParagraph = document.querySelector('.innovation-header > p');
            const readMoreBtn = document.querySelector('.read-more-btn');
            const missionVisionItems = document.querySelectorAll('.mission-item, .vision-item');
            const itemHeadings = document.querySelectorAll('.mission-item h2, .vision-item h2');
            const itemParagraphs = document.querySelectorAll('.mission-item p, .vision-item p');
            const icons = document.querySelectorAll('.icon-wrapper svg');

            if (isMobile) {
                // Apply mobile styles
                wrapper.style.flexDirection = 'column';
                wrapper.style.gap = '8vh';
                missionVision.style.flexDirection = 'column';
                missionVision.style.alignItems = 'center';
                missionVision.style.textAlign = 'center';
                missionVision.style.gap = '6vh';
                
                headline.style.fontSize = '12vw';
                mainParagraph.style.fontSize = '4vw';
                readMoreBtn.style.padding = '1.5vh 5vw';
                readMoreBtn.style.fontSize = '4vw';

                missionVisionItems.forEach(item => {
                    item.style.alignItems = 'center';
                });
                itemHeadings.forEach(h2 => h2.style.fontSize = '7vw');
                itemParagraphs.forEach(p => p.style.fontSize = '4vw');
                icons.forEach(svg => {
                    svg.style.width = '6vw';
                    svg.style.height = '6vw';
                });

            } else {
                // Revert to desktop styles
                wrapper.style.flexDirection = 'row';
                wrapper.style.gap = '5vw';
                missionVision.style.flexDirection = 'row';
                missionVision.style.alignItems = 'flex-start';
                missionVision.style.textAlign = 'left';
                missionVision.style.gap = '4vw';

                headline.style.fontSize = '4.5vw';
                mainParagraph.style.fontSize = '1.1vw';
                readMoreBtn.style.padding = '1vh 1.5vw';
                readMoreBtn.style.fontSize = '1vw';
                
                missionVisionItems.forEach(item => {
                    item.style.alignItems = 'flex-start';
                });
                itemHeadings.forEach(h2 => h2.style.fontSize = '2vw');
                itemParagraphs.forEach(p => p.style.fontSize = '1.1vw');
                icons.forEach(svg => {
                    svg.style.width = '2vw';
                    svg.style.height = '2vw';
                });
            }
        }
        window.addEventListener('load', optimizeInnovationLayout);
        window.addEventListener('resize', optimizeInnovationLayout);
    </script>
    """


async def innovation_style():
    return """
    <style>
        .innovation-section {
            background-color: #1C1C1C;
            padding: 15vh 5vw;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
            border-top: 0.1vh solid rgba(255, 255, 255, 0.1);
        }

        .innovation-content-wrapper {
            display: flex;
            width: 90vw;
            gap: 5vw; /* Default for desktop */
            align-items: flex-start;
            z-index: 2;
            transition: flex-direction 0.3s ease-in-out, gap 0.3s ease-in-out;
        }

        /* --- Left Column --- */
        .innovation-text-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8vh;
        }

        .innovation-header {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 3vh;
        }

        .innovation-header h1 {
            font-family: 'Exo 2', sans-serif;
            font-weight: 700;
            font-size: 4.5vw;
            line-height: 1.1;
            letter-spacing: -0.02em;
            background: linear-gradient(90deg, rgba(235, 243, 243, 0.54) 0%, #EBF3F3 15%, #EBF3F3 55%, rgba(235, 243, 243, 0.7) 80%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            transition: font-size 0.3s ease-in-out;
        }

        .innovation-header > p {
            font-family: 'Poppins', sans-serif;
            font-size: 1.1vw;
            line-height: 1.6;
            color: #FFFFFF;
            opacity: 0.6;
            max-width: 40vw;
            transition: font-size 0.3s ease-in-out;
        }

        .read-more-btn {
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 1vh 1.5vw;
            gap: 0.5vw;
            background: #5FC7FB;
            border-radius: 0.5vw;
            text-decoration: none;
            color: #000000;
            font-family: 'Exo 2', sans-serif;
            font-weight: 500;
            font-size: 1vw;
            transition: all 0.3s ease-in-out;
        }

        .read-more-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 0.5vw 1vw rgba(95, 199, 251, 0.3);
        }

        .mission-vision-container {
            display: flex;
            gap: 4vw; /* Default for desktop */
            transition: all 0.3s ease-in-out;
        }

        .mission-item, .vision-item {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: flex-start; /* Default for desktop */
            gap: 2vh;
        }

        .icon-wrapper {
            background: #FFFFFF;
            border-radius: 0.3vw;
            padding: 0.8vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .icon-wrapper svg {
            transition: all 0.3s ease-in-out;
        }
        
        .mission-item h2, .vision-item h2 {
            font-family: 'Exo 2', sans-serif;
            font-weight: 500;
            font-size: 2vw;
            color: #FFFFFF;
            transition: font-size 0.3s ease-in-out;
        }
        
        .mission-item p, .vision-item p {
            font-family: 'Poppins', sans-serif;
            font-size: 1.1vw;
            line-height: 1.5;
            color: #FFFFFF;
            opacity: 0.7;
            transition: font-size 0.3s ease-in-out;
        }

        /* --- Right Column --- */
        .innovation-image-content {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .image-frame {
            padding-bottom: 1vw;
            border-right: 0.1vh solid #B4B4B4;
            border-bottom: 0.1vh solid #B4B4B4;
            border-radius: 4.5vw;
            padding-right: 1vw;
        }

        .award-image {
            width: 40vw;
            height: auto;
            display: block;
            border-radius: 3vw;
        }
        
        .glow-effect {
            position: absolute;
            width: 15vw;
            height: 25vh;
            right: 0;
            bottom: -5vh;
            background: #FFFFFF;
            opacity: 0.1;
            filter: blur(15vw);
            z-index: 1;
            pointer-events: none;
        }
    </style>
    """
