async def get_in_touch_body():
    return """
    <section class="wrap" role="main" aria-label="Contact section">
        <!-- Eclipse Glow Background -->
        <div class="eclipse-glow"></div>
        <h1>Get In Touch</h1>
        <section class="stage" aria-label="Contact layout">

            <form class="contact-form" action="#" method="post" autocomplete="on" aria-label="Contact form">
                <input class="field" id="name" name="name" type="text" placeholder="Name*" aria-label="Name" required>
                <input class="field" id="email" name="email" type="email" placeholder="Email*" aria-label="Email" required>
                <input class="field" id="subject" name="subject" type="text" placeholder="Subject*" aria-label="Subject" required>
                <textarea class="field textarea" id="comments" name="comments" placeholder="Comments" aria-label="Comments"></textarea>
                <button class="button" type="submit">Send Message</button>
            </form>
            <div class="map-container" aria-hidden="true">
                <img src="../../Resources/Images/Pricing/india_map.png" alt="Stylized world map with location pins">
            </div>
        </section>
    </section>
"""


async def get_in_touch_style():
    return """
<style>
        /* --- Base & Structural Styles (Theme-Agnostic) --- */
        * {
            box-sizing: border-box;
        }


        .wrap {
            width: 100%;
            height:120vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8vh;
            padding-top: 8vh;
            padding-bottom: 8vh;
            overflow-x: hidden;
        }

        h1 {
            margin: 0;
            font-weight: 700;
            font-size: min(8vw, 10vh);
            letter-spacing: .1vw;
        }

        .stage {
            width: 90vw;
            max-width: 109.37vw;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 5vw;
        }

        .contact-form {
            flex: 1 1 50%;
            display: flex;
            flex-direction: column;
            gap: 4.5vh;
        }
        
        .map-container {
            flex: 1 1 30%;
        }

        .map-container img {
            width: 100%;
            height: auto;
            object-fit: contain;
            border-radius: 1.5vw; /* Added for a softer look */
        }

        .field {
            width: 100%;
            height: 7vh;
            display: block;
            border: none;
            border-radius: 1.2vw;
            padding: 0 1.8vw;
            font-size: 1.2vw;
            outline: none;
        }

        .textarea {
            height: 20vh;
            padding-top: 2vh;
            resize: vertical;
        }

        .button {
            height: 6.5vh;
            width: auto;
            padding: 0 2.5vw;
            font-weight: 700;
            font-size: 1.2vw;
            border: none;
            border-radius: 3vw;
            letter-spacing: .05vw;
            cursor: pointer;
            align-self: flex-start;
            transition: transform .1s ease, filter .2s ease, background-color .2s ease;
        }

        .button:hover {
            transform: translateY(-.3vh);
            filter: brightness(1.05);
        }

        .button:active {
            transform: translateY(.2vh);
        }

        /* --- Theming Section --- */
        
        /* Light Theme */
        @media (prefers-color-scheme: light) {
            .wrap { background-color: #FFFFFF; }
            h1 {
                background: none;
                -webkit-background-clip: initial;
                -webkit-text-fill-color: initial;
                color: #111111;
            }
            .field {
                background-color: #F0F2F5;
                color: #1A202C;
            }
            .field::placeholder { color: #6B7280; opacity: 1; }
            .field:focus { box-shadow: 0 0 0 0.3vw rgba(37, 150, 244, 0.3); }
            .button {
                background-color: #2596F4;
                color: #FFFFFF;
            }
        }

        

        /* Dark Theme */
        @media (prefers-color-scheme: dark) {
            .wrap { 
                background-color: transparent;
                position: relative;
            }
            h1 {
                background: linear-gradient(180deg, #FFFFFF 50%, #B0B0B0 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-fill-color: transparent;
            }
            .field {
                background-color: #EFEFEF;
                color: #333333;
            }
            .field::placeholder { color: #888888; opacity: 1; }
            .field:focus { box-shadow: 0 0 0 0.3vw rgba(255, 255, 255, 0.2); }
            .button {
                background-color: #FFFFFF;
                color: #111111;
            }
            /* Eclipse Glow Effect - Dark Mode Only */
            .eclipse-glow {
                position: absolute;
                width: 60vw;
                height: 60vw;
                right: -10vw;
                top: -12vh;
                background-image: url('../../Resources/Images/Dashboard/ecliplse_glow.png');
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                z-index: -1;
                opacity: 0.6;
                pointer-events: none;
                transition: opacity 0.3s ease;
            }
        }

        /* --- Responsive Structural Adjustments --- */
        @media (max-width: 768px) {
            .stage {
                flex-direction: column;
                align-items: center;
                gap: 6vw;
            }

            .map-container,
            .contact-form {
                flex-basis: auto;
                width: 90%;
            }
            
            /* On mobile, map comes after the form */
            .contact-form { order: 1; }
            .map-container { order: 2; }


            .field {
                height: 8vh;
                border-radius: 3vw;
                font-size: 4vw;
            }

            .button {
                align-self: center;
                width: 70%;
                height: 5vh;
                font-size: 4vw;
                border-radius: 8vw;
            }

            .wrap {
                margin-top: -22vw;
            }
        }
</style>
"""
