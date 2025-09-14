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

        .testimonials-section {
            width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10vw 2vw;
        }

        .section-header {
            text-align: center;
            margin-bottom: 8vw;
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
            width: 90%;
            overflow: hidden;
        }

        .slider-track {
            display: flex;
            cursor: grab;
            user-select: none;
        }

        .slider-track:active {
            cursor: grabbing;
        }

        .testimonial-card {
            background-color: var(--card-white);
            border-radius: 1.5vw;
            box-shadow: 0px 2vw 8vw rgba(0, 0, 0, 0.08);
            position: relative;
            flex: 0 0 calc(80vw / 3);
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
            margin-bottom: 0.5vw;
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
            padding: 1vw 2vw;
            margin-top: -3.7vw;
            /* Pulls the rating box up */
            margin-bottom: 4vw;
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
            margin-top: 5vw;
        }

        .pagination-dot {
            width: 3.5vw;
            height: 0.8vw;
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
                padding: 5vh 5vw;
                justify-content: flex-start;
                min-height: 100vh;
                height: auto;
            }

            .section-header {
                margin-bottom: 8vh;
            }

            .section-header h1 {
                font-size: 7vw;
                line-height: 1.3;
            }

            .slider-viewport {
                width: 100%;
            }

            .testimonial-card {
                flex: 0 0 100%;
                margin: 0;
                border-radius: 6vw;
                min-height: 65vh;
                height: auto;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
            }

            .card-top {
                flex-direction: column;
                text-align: center;
                padding: 8vw 6vw 6vw;
                gap: 3vw;
                border-radius: 6vw 6vw 0 0;
                min-height: 30vh;
                flex-shrink: 0;
            }

            .client-photo {
                width: 28vw;
                height: 28vw;
                border-radius: 4vw;
            }

            .client-info h3 {
                font-size: 5.5vw;
                line-height: 1.2;
            }

            .client-info p {
                font-size: 3.8vw;
                line-height: 1.4;
            }

            .card-bottom {
                padding: 0 6vw 8vw;
                flex-grow: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .rating-box {
                margin-top: -12vh;
                margin-bottom: 4vh;
                padding: 2.5vh 6vw;
                border-radius: 10vw;
                gap: 2vw;
            }

            .rating-box svg {
                width: 4.5vw;
                height: 4.5vw;
            }

            .testimonial-quote {
                font-size: 4vw;
                line-height: 1.6;
                max-width: 100%;
            }

            .slider-pagination {
                margin-top: 6vh;
                gap: 3vw;
            }

            .pagination-dot {
                width: 12vw;
                height: 1.2vh;
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
            if (!track) return;

            let slides = Array.from(track.children);
            const slideCount = slides.length;
            if (slideCount === 0) return;

            // Clone all slides for a seamless infinite loop with multiple visible cards
            slides.forEach(slide => {
                const clone = slide.cloneNode(true);
                track.appendChild(clone);
            });
            for (let i = slideCount - 1; i >= 0; i--) {
                const clone = slides[i].cloneNode(true);
                track.insertBefore(clone, slides[0]);
            }

            slides = Array.from(track.children); // update slides array

            let isDragging = false,
                startPos = 0,
                currentTranslate = 0,
                prevTranslate = 0,
                animationID,
                currentIndex = slideCount; // Start at the first real slide

            const getSlideWidth = () => {
                const viewport = document.querySelector('.slider-viewport');
                if (!viewport || slides.length === 0) return 0;

                const slidesPerView = window.innerWidth > 768 ? 3 : 1;
                return viewport.clientWidth / slidesPerView;
            };

            function setSliderPosition() {
                track.style.transform = 'translateX(' + currentTranslate + 'px)';
            }

            function setPositionByIndex(withTransition = true) {
                const slideWidth = getSlideWidth();
                currentTranslate = -currentIndex * slideWidth;
                prevTranslate = currentTranslate;
                if (withTransition) {
                    track.style.transition = 'transform 0.5s ease-out';
                } else {
                    track.style.transition = 'none';
                }
                setSliderPosition();
            }
            
            // Set initial position
            setPositionByIndex(false);

            function dragStart(event) {
                isDragging = true;
                startPos = getPositionX(event);
                animationID = requestAnimationFrame(animation);
                track.style.transition = 'none';

                document.addEventListener('mousemove', dragMove);
                document.addEventListener('touchmove', dragMove, { passive: true });

                document.addEventListener('mouseup', dragEnd);
                document.addEventListener('touchend', dragEnd);
            }

            function dragMove(event) {
                if (isDragging) {
                    const currentPosition = getPositionX(event);
                    currentTranslate = prevTranslate + currentPosition - startPos;
                }
            }

            function dragEnd() {
                if (!isDragging) return;
                cancelAnimationFrame(animationID);
                isDragging = false;

                document.removeEventListener('mousemove', dragMove);
                document.removeEventListener('touchmove', dragMove);
                document.removeEventListener('mouseup', dragEnd);
                document.removeEventListener('touchend', dragEnd);

                const movedBy = currentTranslate - prevTranslate;
                const slideWidth = getSlideWidth();

                const threshold = slideWidth * 0.35;
                if (movedBy < -threshold) {
                    currentIndex++;
                } else if (movedBy > threshold) {
                    currentIndex--;
                }

                setPositionByIndex();
                
                track.addEventListener('transitionend', () => {
                    checkIndex();
                    updatePagination();
                }, { once: true });
            }

            function getPositionX(event) {
                return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
            }

            function animation() {
                setSliderPosition();
                if (isDragging) requestAnimationFrame(animation);
            }
            
            function checkIndex() {
                // If we are at the prepended clones, jump to the corresponding real slides
                if (currentIndex < slideCount) {
                    currentIndex += slideCount;
                    track.style.transition = 'none';
                    setPositionByIndex(false);
                }
                // If we are at the appended clones, jump to the corresponding real slides
                else if (currentIndex >= slideCount * 2) {
                    currentIndex -= slideCount;
                    track.style.transition = 'none';
                    setPositionByIndex(false);
                }
            }

            // Event Listeners
            track.addEventListener('mousedown', dragStart);
            track.addEventListener('touchstart', dragStart, { passive: true });

            window.addEventListener('resize', () => {
                setPositionByIndex(false);
            });
            
            // --- Pagination ---
            const paginationContainer = document.querySelector('.slider-pagination');
            if (paginationContainer) {
                // Create dots
                for (let i = 0; i < slideCount; i++) {
                    const dot = document.createElement('button');
                    dot.classList.add('pagination-dot');
                    dot.addEventListener('click', () => {
                        currentIndex = i + slideCount;
                        setPositionByIndex();
                        track.addEventListener('transitionend', () => {
                            checkIndex();
                            updatePagination();
                        }, { once: true });
                    });
                    paginationContainer.appendChild(dot);
                }
            }

            function updatePagination() {
                const dots = paginationContainer ? paginationContainer.children : [];
                if (dots.length > 0) {
                    const activeDotIndex = (currentIndex % slideCount);
                    for (let i = 0; i < dots.length; i++) {
                        dots[i].classList.toggle('active', i === activeDotIndex);
                    }
                }
            }

            updatePagination();
        });
    </script>
"""