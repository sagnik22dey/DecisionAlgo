async def get_in_touch_body():
    return """
    <section class="wrap" role="main" aria-label="Contact section">
        <h1>Get In Touch</h1>
        <section class="stage" aria-label="Contact layout">

            <div class="map-container" aria-hidden="true">
                <img src="../../Resources/Images/ContactUs/world_map.png" alt="Stylized world map with location pins">
            </div>

            <form class="contact-form" action="#" method="post" autocomplete="on" aria-label="Contact form">
                <input class="field" id="name" name="name" type="text" placeholder="Name*" aria-label="Name" required>
                <input class="field" id="email" name="email" type="email" placeholder="Email*" aria-label="Email" required>
                <input class="field" id="subject" name="subject" type="text" placeholder="Subject*" aria-label="Subject" required>
                <textarea class="field textarea" id="comments" name="comments" placeholder="Comments" aria-label="Comments"></textarea>
                <button class="button" type="submit">Send Message</button>
            </form>
        </section>
    </section>
"""


async def get_in_touch_style():
    return """
<style>
        :root {
            --bg: #111111;
            --field-bg: #EFEFEF;
            --placeholder-text: #888888;
            --field-text: #333333;
            --white: #ffffff;
        }

        /* base */
        * {
            box-sizing: border-box
        }

        html,
        body {
            min-height: 100vh
        }

        body {
            margin: 0;
            background-color: var(--bg);
            color: var(--white);
            font-size: max(1.2vh, 1.1vw);
            line-height: 1.3;
        }

        /* layout */
        .wrap {
            min-height: 100vh;
            width: 100%;
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
            /* Metallic gradient effect */
            background: linear-gradient(180deg, #FFFFFF 50%, #B0B0B0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
        }

        .stage {
            width: 90vw;
            max-width: 1400px;
            /* Max width for large screens */
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 5vw;
        }

        /* left visual (world map image) */
        .map-container {
            flex: 1 1 55%;
            /* Allow shrinking but prefer 55% width */
        }

        .map-container img {
            width: 100%;
            height: auto;
            object-fit: contain;
        }


        /* right form */
        .contact-form {
            flex: 1 1 40%;
            /* Allow shrinking but prefer 40% width */
            display: flex;
            flex-direction: column;
            gap: 2.5vh;
        }

        /* fields */
        .field {
            width: 100%;
            height: 7vh;
            display: block;
            color: var(--field-text);
            background: var(--field-bg);
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

        /* placeholder */
        .field::placeholder {
            color: var(--placeholder-text);
            opacity: 1;
        }

        .field:focus {
            box-shadow: 0 0 0 0.3vw rgba(255, 255, 255, 0.2);
        }

        /* button */
        .button {
            height: 6.5vh;
            width: auto;
            /* let padding define width */
            padding: 0 2.5vw;
            background: var(--white);
            color: var(--bg);
            font-weight: 700;
            font-size: 1.2vw;
            border: none;
            border-radius: 3vw;
            /* Pill shape */
            letter-spacing: .05vw;
            cursor: pointer;
            align-self: flex-start;
            /* Align to the left */
            transition: transform .1s ease, filter .2s ease;
        }

        .button:hover {
            transform: translateY(-.3vh);
            filter: brightness(1.05)
        }

        .button:active {
            transform: translateY(.2vh);
        }

        /* responsive */
        @media (max-width: 768px) {
            .stage {
                flex-direction: column;
                align-items: center;
                gap: 6vh
            }

            .map-container,
            .contact-form {
                flex-basis: auto;
                width: 90%;
            }

            .field {
                height: 8vh;
                border-radius: 3vw;
                font-size: 4vw;
            }

            .button {
                align-self: center;
                width: 70%;
                height: 8vh;
                font-size: 4vw;
                border-radius: 8vw;
            }
        }
        </style>
"""
