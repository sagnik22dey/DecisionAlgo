async def client_feedback_style():
    return """
    <style>
        :root {
            --primary-blue: #5FC7FB;
            --primary-white: #FFFFFF;
            --primary-light-gray: #EBF0F3;
            --background-dark: #141414;
            --card-white: #FFFFFF;
            --card-header-bg: #F3F3F3;
            --text-dark: #1D1D1D;
            --text-muted: #737373;
            --star-color: #F2D645;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html,
        body {
            overflow-x: hidden;
            background-color: var(--background-dark);
            font-family: 'Exo 2', sans-serif;
        }

        .testimonials-section {
            width: 100vw;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vh 2vw;
        }

        .section-header {
            text-align: center;
            margin-bottom: 8vh;
        }

        .section-header h1 {
            font-size: 4vw;
            line-height: 1.2;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: -0.02em;
            color: var(--primary-light-gray);
        }

        .section-header h1 span {
            color: var(--primary-blue);
        }

        .slider-viewport {
            width: 90vw;
            overflow: hidden;
        }

        .slider-track {
            display: flex;
            transition: transform 0.5s ease-in-out;
        }

        .testimonial-card {
            background-color: var(--card-white);
            border-radius: 1.5vw;
            box-shadow: 0px 2vw 8vw rgba(0, 0, 0, 0.08);
            position: relative;
            flex: 0 0 28vw;
            /* 3 cards visible with some spacing */
            margin: 1vw;
            min-height: 55vh;
            display: flex;
            flex-direction: column;
        }

        .card-top {
            background-color: var(--card-header-bg);
            border-radius: 1.5vw 1.5vw 0 0;
            padding: 2vw;
            display: flex;
            align-items: center;
            gap: 1.5vw;
            min-height: 20vh;
        }

        .client-photo {
            width: 9vw;
            height: 9vw;
            border-radius: 1vw;
            object-fit: cover;
        }

        .client-info h3 {
            font-size: 1.8vw;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 0.5vh;
        }

        .client-info p {
            font-size: 1.3vw;
            line-height: 1.3;
            color: var(--text-muted);
        }

        .card-bottom {
            padding: 2vw;
            text-align: center;
            color: var(--text-dark);
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .rating-box {
            background-color: var(--card-white);
            border-radius: 1vw;
            box-shadow: 0px 1.5vw 5vw rgba(0, 0, 0, 0.07);
            padding: 1vh 2vw;
            margin-top: -8vh;
            /* Pulls the rating box up */
            margin-bottom: 4vh;
            display: inline-flex;
            gap: 0.5vw;
            z-index: 2;
        }

        .rating-box svg {
            width: 1.5vw;
            height: 1.5vw;
            fill: var(--star-color);
        }

        .testimonial-quote {
            font-size: 1.2vw;
            line-height: 1.5;
            max-width: 90%;
        }

        .slider-pagination {
            display: flex;
            justify-content: center;
            gap: 1vw;
            margin-top: 5vh;
        }

        .pagination-dot {
            width: 3.5vw;
            height: 0.8vh;
            background-color: var(--primary-blue);
            opacity: 0.3;
            border-radius: 2vw;
            cursor: pointer;
            transition: opacity 0.3s ease;
        }

        .pagination-dot.active {
            opacity: 1;
        }

        /* --- Mobile View --- */
        @media (max-width: 768px) {
            .testimonials-section {
                padding: 10vh 5vw;
            }

            .section-header h1 {
                font-size: 8vw;
            }

            .slider-viewport {
                width: 100%;
            }

            .testimonial-card {
                flex: 0 0 90vw;
                /* 1 card visible */
                margin: 0 5vw;
                /* Center the single card */
                border-radius: 4vw;
                min-height: 60vh;
            }

            .card-top {
                padding: 5vw;
                border-radius: 4vw 4vw 0 0;
                min-height: 25vh;
            }

            .client-photo {
                width: 25vw;
                height: 25vw;
                border-radius: 2.5vw;
            }

            .client-info h3 {
                font-size: 5.5vw;
            }

            .client-info p {
                font-size: 4vw;
            }

            .card-bottom {
                padding: 5vw;
            }

            .rating-box {
                margin-top: -10vh;
                margin-bottom: 5vh;
                padding: 1.5vh 5vw;
                border-radius: 2.5vw;
                gap: 2vw;
            }

            .rating-box svg {
                width: 5vw;
                height: 5vw;
            }

            .testimonial-quote {
                font-size: 4.2vw;
            }

            .slider-pagination {
                gap: 3vw;
            }

            .pagination-dot {
                width: 15vw;
                height: 1vh;
            }
        }
    </style>
"""

async def client_feedback_body():
    return """
    <section class="testimonials-section">
        <div class="section-header">
            <h1>What <span>Our Clients</span> Have <br>To Say</h1>
        </div>
        <div class="slider-viewport">
            <div class="slider-track">
                <!-- Testimonial 1 -->
                <div class="testimonial-card">
                    <div class="card-top">
                        <img src="../../Resources/Images/CaseStudies/customer/emmi.png" alt="Emily Jeff" class="client-photo">
                        <div class="client-info">
                            <h3>Emily Jeff</h3>
                            <p>Product Development Lead</p>
                        </div>
                    </div>
                    <div class="card-bottom">
                        <div class="rating-box">
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                        </div>
                        <p class="testimonial-quote">In the fast-paced world of CPG, understanding consumer trends is crucial. DecisionAlgo guided us to create products that truly resonate with our target audience.</p>
                    </div>
                </div>
                <!-- Testimonial 2 -->
                <div class="testimonial-card">
                    <div class="card-top">
                        <img src="../../Resources/Images/CaseStudies/customer/hamza.png" alt="Hamza Malik" class="client-photo">
                        <div class="client-info">
                            <h3>Hamza Malik</h3>
                            <p>Retail Executive</p>
                        </div>
                    </div>
                    <div class="card-bottom">
                        <div class="rating-box">
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                        </div>
                        <p class="testimonial-quote">A game-changer for our retail operations! DecisionAlgo transformed our supply chain efficiency, increasing sales and customer satisfaction. Highly recommended.</p>
                    </div>
                </div>
                <!-- Testimonial 3 -->
                <div class="testimonial-card">
                    <div class="card-top">
                        <img src="../../Resources/Images/CaseStudies/customer/elizabeth.png" alt="Elizabeth Rai" class="client-photo">
                        <div class="client-info">
                            <h3>Elizabeth Rai</h3>
                            <p>Supply Chain Manager</p>
                        </div>
                    </div>
                    <div class="card-bottom">
                        <div class="rating-box">
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                            <svg viewBox="0 0 24 24">
                                <path d="M12,17.27L18.18,21L17,14.64L22,9.24L15.36,8.27L12,2L8.64,8.27L2,9.24L7,14.64L5.82,21L12,17.27Z" />
                            </svg>
                        </div>
                        <p class="testimonial-quote">Significantly improved our supply chain operations. DecisionAlgo allowed us to reduce costs and optimize inventory management. Can't imagine our success without them.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="slider-pagination"></div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const track = document.querySelector('.slider-track');
            let slides = Array.from(track.children);
            const paginationContainer = document.querySelector('.slider-pagination');
            const originalSlideCount = slides.length;
            let currentIndex = 0;
            let slideInterval;

            if (originalSlideCount === 0) return;

            // Clone slides for infinite loop
            slides.forEach(slide => {
                const clone = slide.cloneNode(true);
                track.appendChild(clone);
            });
            slides = Array.from(track.children);

            // Create pagination dots for original slides
            for (let i = 0; i < originalSlideCount; i++) {
                const dot = document.createElement('button');
                dot.classList.add('pagination-dot');
                dot.addEventListener('click', () => {
                    moveToSlide(i);
                    resetInterval();
                });
                paginationContainer.appendChild(dot);
            }
            const dots = Array.from(paginationContainer.children);

            const updateDots = () => {
                dots.forEach(dot => dot.classList.remove('active'));
                if (dots.length > 0) {
                    dots[currentIndex % originalSlideCount].classList.add('active');
                }
            };

            const getSlideWidth = () => {
                const slideStyle = window.getComputedStyle(slides[0]);
                const slideMargin = parseFloat(slideStyle.marginLeft) + parseFloat(slideStyle.marginRight);
                return slides[0].offsetWidth + slideMargin;
            };

            const moveToSlide = (index, withTransition = true) => {
                const slideWidth = getSlideWidth();
                if (withTransition) {
                    track.style.transition = 'transform 0.5s ease-in-out';
                } else {
                    track.style.transition = 'none';
                }
                track.style.transform = 'translateX(-' + slideWidth * index + 'px)';
                currentIndex = index;
                updateDots();
            };

            const nextSlide = () => {
                moveToSlide(currentIndex + 1);
            };

            track.addEventListener('transitionend', () => {
                if (currentIndex >= originalSlideCount) {
                    moveToSlide(currentIndex % originalSlideCount, false);
                }
            });

            const startInterval = () => {
                slideInterval = setInterval(nextSlide, 5000);
            };

            const resetInterval = () => {
                clearInterval(slideInterval);
                startInterval();
            };

            moveToSlide(0);
            startInterval();

            window.addEventListener('resize', () => {
                moveToSlide(currentIndex, false)
            });
        });
    </script>
"""
