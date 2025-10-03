async def dashboard_love_body():
    return """ 
    <section class="features-section">
        <h2 class="section-title">
            Why You'll Love Our <span class="highlight">Dashboards</span>
        </h2>

        <div class="features-grid">

            <!-- Card 1: Everything In One Place -->
            <div class="feature-card">
                <div class="icon-container">
                    <!-- SVG for slashed leaf icon -->
                    <svg viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_369_1993" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257568" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_369_1993)">
                    <path d="M18.2256 30.2042C16.8281 30.2042 15.5117 29.9858 14.2764 29.5491C13.0411 29.1124 11.9118 28.4947 10.8886 27.6961L8.79232 29.755C8.51781 30.0295 8.16843 30.1668 7.74418 30.1668C7.31993 30.1668 6.97055 30.0295 6.69603 29.755C6.42152 29.4805 6.28426 29.1311 6.28426 28.7069C6.28426 28.2826 6.42152 27.9332 6.69603 27.6587L8.75489 25.5999C7.9563 24.5767 7.33865 23.4412 6.90192 22.1934C6.46519 20.9456 6.24683 19.6229 6.24683 18.2254C6.24683 14.8813 7.40727 12.0488 9.72817 9.72793C12.0491 7.40703 14.8816 6.24658 18.2256 6.24658H30.2045V18.2254C30.2045 21.5695 29.044 24.402 26.7231 26.7229C24.4022 29.0438 21.5697 30.2042 18.2256 30.2042ZM18.2256 27.2095C20.7212 27.2095 22.8425 26.3361 24.5894 24.5891C26.3363 22.8422 27.2098 20.721 27.2098 18.2254V9.24129H18.2256C15.7301 9.24129 13.6088 10.1147 11.8619 11.8617C10.115 13.6086 9.24153 15.7298 9.24153 18.2254C9.24153 19.1987 9.39127 20.1283 9.69074 21.0142C9.99021 21.9001 10.402 22.705 10.9261 23.4287L18.6748 15.6799C18.9494 15.4054 19.2987 15.2681 19.723 15.2681C20.1472 15.2681 20.4966 15.4054 20.7711 15.6799C21.0706 15.9794 21.2203 16.335 21.2203 16.7468C21.2203 17.1585 21.0706 17.5142 20.7711 17.8136L13.0223 25.5624C13.7461 26.0865 14.5509 26.492 15.4368 26.779C16.3228 27.066 17.2524 27.2095 18.2256 27.2095Z" class="svg-path" fill="#5FC7FB"/>
                    </g>
                    </svg>
                </div>
                <h3>Everything In<br>One Place</h3>
                <p>Track Sales Performance,<br>And Trends At A Glance</p>
            </div>

            <!-- Card 2: Live Updates -->
            <div class="feature-card">
                <div class="icon-container">
                    <!-- SVG for linked rings icon -->
                    <svg viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_369_2001" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257568" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_369_2001)">
                    <path d="M13.7339 33.1996C12.2865 33.1996 10.9264 32.9251 9.65362 32.3761C8.38087 31.827 7.27034 31.0784 6.32201 30.13C5.37369 29.1817 4.62501 28.0712 4.07599 26.7984C3.52696 25.5257 3.25244 24.1656 3.25244 22.7181C3.25244 20.6967 3.77651 18.85 4.82466 17.1779C5.87281 15.5059 7.24538 14.2331 8.94238 13.3597C9.4415 12.3864 10.0592 11.5317 10.7954 10.7955C11.5316 10.0593 12.3863 9.44162 13.3596 8.9425C14.1831 7.2455 15.4434 5.87293 17.1404 4.82478C18.8374 3.77664 20.6966 3.25256 22.718 3.25256C24.1655 3.25256 25.5256 3.52708 26.7983 4.07611C28.0711 4.62514 29.1816 5.37381 30.1299 6.32214C31.0782 7.27046 31.8269 8.381 32.3759 9.65375C32.925 10.9265 33.1995 12.2866 33.1995 13.734C33.1995 15.8553 32.6754 17.727 31.6273 19.3491C30.5791 20.9712 29.2066 22.219 27.5096 23.0925C27.0104 24.0658 26.3928 24.9205 25.6566 25.6567C24.9204 26.3929 24.0656 27.0106 23.0924 27.5097C22.2189 29.2067 20.9462 30.5792 19.2741 31.6274C17.6021 32.6755 15.7553 33.1996 13.7339 33.1996ZM13.7339 30.2049C14.5575 30.2049 15.3498 30.0801 16.111 29.8306C16.8721 29.581 17.5771 29.2067 18.226 28.7076C16.7785 28.7076 15.4184 28.433 14.1457 27.884C12.8729 27.335 11.7624 26.5863 10.8141 25.638C9.86575 24.6897 9.11707 23.5791 8.56804 22.3064C8.01901 21.0336 7.7445 19.6735 7.7445 18.2261C7.24538 18.8749 6.87104 19.5799 6.62148 20.3411C6.37193 21.1023 6.24715 21.8946 6.24715 22.7181C6.24715 23.7663 6.44679 24.7396 6.84609 25.638C7.24538 26.5364 7.78193 27.3225 8.45574 27.9963C9.12955 28.6701 9.91566 29.2067 10.8141 29.606C11.7125 30.0053 12.6858 30.2049 13.7339 30.2049ZM18.226 25.7129C19.0495 25.7129 19.8543 25.5881 20.6404 25.3385C21.4266 25.089 22.144 24.7146 22.7929 24.2155C21.3205 24.2155 19.9479 23.9347 18.6752 23.3732C17.4024 22.8117 16.2919 22.0568 15.3436 21.1085C14.3952 20.1602 13.6403 19.0496 13.0788 17.7769C12.5173 16.5041 12.2366 15.1316 12.2366 13.6592C11.7374 14.308 11.3631 15.0255 11.1135 15.8116C10.864 16.5977 10.7392 17.4025 10.7392 18.2261C10.7392 19.2742 10.9326 20.2475 11.3194 21.1459C11.7062 22.0443 12.249 22.8304 12.9478 23.5043C13.6216 24.203 14.4077 24.7458 15.3061 25.1326C16.2045 25.5194 17.1778 25.7129 18.226 25.7129ZM22.718 21.2208C23.1672 21.2208 23.5977 21.1834 24.0095 21.1085C24.4213 21.0336 24.8393 20.9213 25.2635 20.7716C25.8126 19.2742 25.8937 17.833 25.5068 16.448C25.12 15.0629 24.4525 13.8962 23.5041 12.9479C22.5558 11.9996 21.3891 11.332 20.0041 10.9452C18.619 10.5584 17.1778 10.6395 15.6805 11.1885C15.5307 11.6128 15.4184 12.0308 15.3436 12.4426C15.2687 12.8543 15.2313 13.2848 15.2313 13.734C15.2313 14.7822 15.4247 15.7555 15.8115 16.6539C16.1983 17.5523 16.7411 18.3384 17.4399 19.0122C18.1137 19.711 18.8998 20.2538 19.7982 20.6406C20.6966 21.0274 21.6699 21.2208 22.718 21.2208ZM28.7074 18.301C29.2066 17.6521 29.5809 16.9346 29.8304 16.1485C30.08 15.3624 30.2048 14.5576 30.2048 13.734C30.2048 12.6859 30.0114 11.7126 29.6246 10.8142C29.2377 9.91578 28.695 9.12967 27.9962 8.45586C27.3224 7.7571 26.5363 7.21431 25.6379 6.82749C24.7394 6.44068 23.7662 6.24727 22.718 6.24727C21.8446 6.24727 21.0273 6.37205 20.2661 6.62161C19.505 6.87117 18.8 7.2455 18.1511 7.74462C19.6235 7.74462 20.9961 8.02537 22.2688 8.58688C23.5416 9.14839 24.6521 9.9033 25.6004 10.8516C26.5487 11.8 27.3037 12.9105 27.8652 14.1832C28.4267 15.456 28.7074 16.8286 28.7074 18.301Z" class="svg-path" fill="#5FC7FB"/>
                    </g>
                    </svg>
                </div>
                <h3>Live Updates</h3>
                <p>No Delay, No Outdated<br>Reports. Just Real-Time<br>Insights.</p>
            </div>

            <!-- Card 3: Custom-Built For You -->
            <div class="feature-card">
                <div class="icon-container">
                    <!-- SVG for user icon -->
                    <svg viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_369_2009" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257568" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_369_2009)">
                    <path d="M18.2258 18.2254C19.9979 18.2254 21.4955 17.6358 22.7186 16.4567C23.9416 15.2776 24.5532 13.8052 24.5532 12.039C24.5532 10.2728 23.9416 8.79744 22.7186 7.61226C21.4955 6.42708 19.9979 5.83447 18.2258 5.83447C16.4538 5.83447 14.9562 6.42708 13.7331 7.61226C12.5101 8.79744 11.8986 10.2728 11.8986 12.039C11.8986 13.8052 12.5101 15.2776 13.7331 16.4567C14.9562 17.6358 16.4538 18.2254 18.2258 18.2254ZM18.2258 15.2307C17.2274 15.2307 16.3888 14.8875 15.7099 14.195C15.031 13.5026 14.6916 12.8288 14.6916 12.1738C14.6916 11.3004 15.0123 10.5709 15.6536 9.98522C16.295 9.39957 17.1517 9.10674 18.2258 9.10674C19.275 9.10674 20.1429 9.39957 20.828 9.98522C21.5131 10.5709 21.8557 11.3004 21.8557 12.1738C21.8557 12.8288 21.5162 13.5026 20.8373 14.195C20.1584 14.8875 19.3018 15.2307 18.2258 15.2307ZM18.2258 30.6163C15.8299 30.6163 13.628 30.1345 11.6201 29.1709C9.61217 28.2073 7.97868 26.8906 6.71962 25.2208C5.46056 23.551 4.83105 21.675 4.83105 19.5927C4.83105 19.2932 4.90243 19.0187 5.04519 18.7691C5.18795 18.5196 5.37761 18.32 5.61418 18.1702C5.85074 18.0205 6.10228 17.9456 6.36878 17.9456H29.933C30.2225 17.9456 30.487 18.0205 30.7276 18.1702C30.9681 18.32 31.1578 18.5196 31.2965 18.7691C31.4352 19.0187 31.5046 19.2932 31.5046 19.5927C31.5046 21.675 30.8751 23.551 29.616 25.2208C28.357 26.8906 26.7235 28.2073 24.7155 29.1709C22.7076 30.1345 20.5058 30.6163 18.2258 30.6163ZM18.2258 27.6216C21.8496 27.6216 24.6976 26.683 26.7698 24.8058C28.842 22.9286 28.842 21.3653 28.5925 20.9403H7.71C7.46049 21.3653 7.46049 22.9286 9.5327 24.8058C11.6049 26.683 14.4529 27.6216 18.2258 27.6216Z" class="svg-path" fill="#5FC7FB"/>
                    </g>
                    </svg>
                </div>
                <h3>Custom-Built For<br>You</h3>
                <p>Tailored Dashboards, Zero<br>Clutter</p>
            </div>

            <!-- Card 4: Easy To Use -->
            <div class="feature-card">
                <div class="icon-container">
                    <!-- SVG for power icon -->
                    <svg viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <mask id="mask0_369_2017" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="37" height="37">
                    <rect x="0.257568" y="0.257446" width="35.9365" height="35.9365" fill="#D9D9D9"/>
                    </mask>
                    <g mask="url(#mask0_369_2017)">
                    <path d="M16.9276 31.2155V28.2208H19.524V31.2155H16.9276ZM11.1681 26.6534L13.2504 24.5851L15.1158 26.4505L13.0335 28.5188L11.1681 26.6534ZM21.3359 26.4505L23.2013 24.5851L25.2836 26.6534L23.2013 28.5188L21.3359 26.4505ZM18.2258 23.0033C17.0717 23.0033 16.0392 22.5856 15.1283 21.7503C14.2173 20.9149 13.7618 19.8825 13.7618 18.6532C13.7618 17.524 14.1287 16.5165 14.8625 15.6305C15.5962 14.7446 16.5855 14.077 17.8299 13.6279V5.23499H18.6217V13.6279C19.866 14.077 20.8554 14.7446 21.5891 15.6305C22.3229 16.5165 22.6898 17.524 22.6898 18.6532C22.6898 19.8825 22.2343 20.9149 21.3234 21.7503C20.4124 22.5856 19.3799 23.0033 18.2258 23.0033ZM7.97394 20.2198V17.6234H4.83105V20.2198H7.97394ZM28.4777 20.2198V17.6234H31.6206V20.2198H28.4777ZM13.0335 7.9366L15.1158 10.0049L13.2504 11.8703L11.1681 9.802L13.0335 7.9366ZM23.2013 10.0049L25.2836 7.9366L23.2013 6.065L21.3359 7.9366L23.2013 10.0049Z" class="svg-path" fill="#5FC7FB"/>
                    </g>
                    </svg>
                </div>
                <h3>Easy To Use</h3>
                <p>No Tech Skills? No<br>Problem. It's Built For<br>Simplicity</p>
            </div>

        </div>
    </section>
"""

async def dashboard_love_style():
    return """
        <style>
        /* --- Base & Desktop Styles (Theme-Agnostic) --- */
        /* This section contains all layout, positioning, and sizing rules. */
        
        .features-section {
            width: 100%;
            padding: 5vh 2vw 10vh 2vw;
            text-align: center;
            box-sizing: border-box;
        }

        .section-title {
            font-size: 3.5vw;
            font-weight: 700;
            margin-bottom: 8vh;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }

        .section-title .highlight {
            color: #5FC7FB; /* Blue highlight color works for both themes */
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5vw;
            max-width: 80vw;
            margin: 0 auto;
            justify-items: center;
        }

        .feature-card {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            text-align: left;
            padding: 1.7vw;
            gap: 1vw;
            border-radius: 1vw;
            width: 18vw;
            height: 19vw;
            border: 0.1vw solid; /* Border color will be set by theme */
            border-bottom: none;
            position: relative;
            box-sizing: border-box;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card::after {
            content: '';
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: 0.1vw;
        }

        .icon-container {
            width: 3.5vw;
            height: 3.5vw;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 0.1vw solid; /* Border color will be set by theme */
            border-radius: 0.7vw;
        }

        .icon-container svg {
            width: 1.8vw;
            height: 1.8vw;
        }
        
        .icon-container svg path {
            transition: fill 0.3s ease;
        }

        .feature-card h3 {
            font-size: 1.5vw;
            font-weight: 600;
            line-height: 1.3;
            text-transform: none;
        }

        .feature-card p {
            font-size: 1vw;
            font-weight: 300;
            line-height: 1.4;
            text-transform: none;
            margin-top: 0.5vw;
        }

        /* --- Theming Section --- */
        /* Contains all color and background rules for light and dark modes. */

        /* Light Theme */
        @media (prefers-color-scheme: light) {
            .section-title {
                color: #1A202C; /* Dark text color */
            }
            .feature-card {
                background-color: #29A4EA;
                border-color: transparent;
            }
            .feature-card:hover {
                transform: translateY(-0.5vw);
                box-shadow: 0 0.8vw 1.5vw rgba(41, 164, 234, 0.35);
            }
            .feature-card::after {
                background: none; /* No gradient border in light mode */
            }
            .icon-container {
                border-color: rgba(255, 255, 255, 0.7);
            }
            .icon-container svg path {
                fill: #FFFFFF;
            }
            .feature-card h3 {
                color: #FFFFFF;
            }
            .feature-card p {
                color: rgba(255, 255, 255, 0.9);
            }
        }

        /* Dark Theme */
        @media (prefers-color-scheme: dark) {
            .section-title {
                color: #FFFFFF;
            }
            .feature-card {
                background: transparent;
                border-color: #5FC7FB;
            }
            .feature-card:hover {
                transform: translateY(-0.5vw);
                box-shadow: 0 0.8vw 1.5vw rgba(95, 199, 251, 0.2);
            }
            .feature-card::after {
                background: linear-gradient(to right, transparent, #5FC7FB, transparent);
            }
            .icon-container {
                border-color: #5FC7FB;
            }
            .icon-container svg path {
                fill: #5FC7FB;
            }
            .feature-card h3 {
                color: #FFFFFF;
            }
            .feature-card p {
                color: rgba(254, 254, 254, 0.8);
            }
        }
        

        /* --- Tablet View (Structural) --- */
        @media (max-width: 1024px) {
            .section-title {
                font-size: 5vw;
            }
            .features-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 4vw;
                max-width: 90vw;
            }
            .feature-card {
                width: 40vw;
                height: auto;
                aspect-ratio: 1 / 1;
                padding: 3vw;
                gap: 2vw;
                border-radius: 2vw;
            }
            .icon-container {
                width: 7vw;
                height: 7vw;
                border-radius: 1.5vw;
            }
            .icon-container svg {
                width: 3.5vw;
                height: 3.5vw;
            }
            .feature-card h3 {
                font-size: 2.8vw;
            }
            .feature-card p {
                font-size: 2vw;
            }
        }
        
        /* --- Mobile View (Structural) --- */
        @media (max-width: 767px) {
            .features-section {
                padding: 3vh 5vw;
            }
            .section-title {
                font-size: 9vw;
                margin-bottom: 8vh;
            }
            .features-grid {
                grid-template-columns: 1fr;
                gap: 5vh;
                max-width: 100%;
            }
            .feature-card {
                width: 100%;
                height: auto; /* Changed from fixed rem for flexibility */
                min-height: 19rem;
                padding: 8vw 6vw;
                gap: 3vh;
                border-radius: 4vw;
                align-items: center;
                text-align: center;
            }
            .feature-card:hover {
                 transform: translateY(-1vw);
            }
            /* Mobile-specific box-shadows inside theme queries */
             @media (prefers-color-scheme: light) {
                 .feature-card {
                    box-shadow: 0 0.5vw 1vw rgba(41, 164, 234, 0.2);
                 }
                .feature-card:hover {
                    box-shadow: 0 1vw 2vw rgba(41, 164, 234, 0.3);
                }
            }
             @media (prefers-color-scheme: dark) {
                .feature-card {
                    box-shadow: 0 0.5vw 1vw rgba(95, 199, 251, 0.1);
                }
                .feature-card:hover {
                    box-shadow: 0 1vw 2vw rgba(95, 199, 251, 0.25);
                }
            }

            .icon-container {
                width: 16vw;
                height: 16vw;
                border-radius: 3vw;
            }
            .icon-container svg {
                width: 8vw;
                height: 8vw;
            }
            .feature-card h3 {
                font-size: 6vw;
            }
            .feature-card p {
                font-size: 4vw;
                line-height: 1.5;
            }
        }
    </style>
"""