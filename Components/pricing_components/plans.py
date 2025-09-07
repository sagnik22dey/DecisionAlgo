async def plans_body():
    return """<section>
    <div class="wrapper">
        <div class="container">
            <h1 class="main-heading">Compare All <span class="highlight">Plans</span></h1>

            <!-- Desktop Table -->
            <table class="comparison" role="table" aria-label="Plan Feature Comparison">
                <thead>
                    <tr>
                        <th scope="col" aria-hidden="true"></th>
                        <th scope="col">Basic Plan</th>
                        <th scope="col">Intermediate Plan</th>
                        <th scope="col">Advanced Plan</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Dedicated Support -->
                    <tr class="feature-row">
                        <th scope="row">Dedicated<br>Support</th>
                        <td data-plan="Basic">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </td>
                    </tr>

                    <!-- Consultation -->
                    <tr class="feature-row">
                        <th scope="row">Consultation</th>
                        <td data-plan="Basic">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Only Business Consultation
                            </div>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Business + Data Consultation
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Only Business Consultation
                            </div>
                        </td>
                    </tr>

                    <!-- Server -->
                    <tr class="feature-row">
                        <th scope="row">Server</th>
                        <td data-plan="Basic">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </td>
                    </tr>

                    <!-- Analytics -->
                    <tr class="feature-row">
                        <th scope="row">Analytics</th>
                        <td data-plan="Basic" class="plan-col--empty">
                            <span class="inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Descriptive Analysis
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Predictive Analysis
                            </div>
                        </td>
                    </tr>

                    <!-- Reports -->
                    <tr class="feature-row">
                        <th scope="row">Reports</th>
                        <td data-plan="Basic" class="plan-col--empty">
                            <span class="inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Monthly Reports
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Daily, Weekly, Monthly Reports
                            </div>
                        </td>
                    </tr>

                    <!-- Dashboard Features -->
                    <tr class="feature-row">
                        <th scope="row">Dashboard<br>Features</th>
                        <td data-plan="Basic">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                KPI Dashboard
                            </div>
                        </td>
                        <td data-plan="Intermediate">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Inquisitive Dashboard
                            </div>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Predictive Dashboard
                            </div>
                        </td>
                    </tr>

                    <!-- AI ChatBots -->
                    <tr class="feature-row">
                        <th scope="row">AI ChatBots</th>
                        <td data-plan="Basic" class="plan-col--empty">
                            <span class="inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </td>
                        <td data-plan="Intermediate" class="plan-col--empty">
                            <span class="inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </td>
                        <td data-plan="Advanced">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Interactive AI Chatbots
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Mobile Tables -->
            <div class="mobile-tables">
                <!-- Basic Plan Table -->
                <div class="mobile-plan-table">
                    <div class="mobile-plan-header">Basic Plan</div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dedicated Support</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Consultation</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Only Business Consultation
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Server</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Analytics</div>
                        <div class="mobile-feature-value empty">
                            <span class="mobile-inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Reports</div>
                        <div class="mobile-feature-value empty">
                            <span class="mobile-inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dashboard Features</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                KPI Dashboard
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">AI ChatBots</div>
                        <div class="mobile-feature-value empty">
                            <span class="mobile-inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </div>
                    </div>
                </div>

                <!-- Intermediate Plan Table -->
                <div class="mobile-plan-table">
                    <div class="mobile-plan-header">Intermediate Plan</div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dedicated Support</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Consultation</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Business + Data Consultation
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Server</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Analytics</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Descriptive Analysis
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Reports</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Monthly Reports
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dashboard Features</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Inquisitive Dashboard
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">AI ChatBots</div>
                        <div class="mobile-feature-value empty">
                            <span class="mobile-inline-dash" aria-hidden="true"></span>
                            <span class="sr-only">Not Included</span>
                        </div>
                    </div>
                </div>

                <!-- Advanced Plan Table -->
                <div class="mobile-plan-table">
                    <div class="mobile-plan-header">Advanced Plan</div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dedicated Support</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24" aria-hidden="true">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Standard Support
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Consultation</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Only Business Consultation
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Server</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Dedicated Server
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Analytics</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Predictive Analysis
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Reports</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Daily, Weekly, Monthly Reports
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">Dashboard Features</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Predictive Dashboard
                            </div>
                        </div>
                    </div>

                    <div class="mobile-feature-row">
                        <div class="mobile-feature-label">AI ChatBots</div>
                        <div class="mobile-feature-value">
                            <div class="check">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M7 12.5l3.1 3L17 8.8" />
                                </svg>
                                Interactive AI Chatbots
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>"""

async def plans_style():
    return """<style>
        :root {
            --bg-gradient-left: #090909;
            --bg-gradient-right: #1b1b1b;
            --col-divider: #131313;
            --col-header-bg: #2f2f2f;
            --feature-col-bg: #070707;
            --cell-bg: #1d1d1d;
            --cell-bg-alt: #222222;
            --border-color: #343434;
            --text-primary: #ffffff;
            --text-muted: #d9d9d9;
            --accent: #00a3dc;
            --gap: 0;
            --row-height: 108px;
            --feature-col-width: 235px;
            --plan-col-width: 360px;
            --container-width: 1491px;
            --dash-color: #e5e5e5;
            --font-stack: 'Exo 2', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Arial, sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: var(--font-stack);
            background: radial-gradient(circle at 0% 0%, var(--bg-gradient-right) 0%, var(--bg-gradient-left) 55%, #000 110%);
            color: var(--text-primary);
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
        }

        .wrapper {
            width: 100%;
            display: flex;
            justify-content: center;
            padding: 60px 20px;
        }

        .container {
            width: var(--container-width);
            max-width: 100%;
        }

        /* Main Heading */
        .main-heading {
            text-align: center;
            margin: 0 0 50px;
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1;
            color: var(--text-primary);
            position: relative;
        }

        .main-heading .highlight {
            color: var(--accent);
        }

        .caption {
            margin: 10px 0 40px;
            font-size: 14px;
            color: #9d9d9d;
            text-align: left;
            line-height: 1.4;
        }

        /* Desktop Layout */
        .comparison {
            width: 100%;
            position: relative;
            border-collapse: separate;
            border-spacing: 0;
            font-size: 15px;
            line-height: 1.25;
            background:
                linear-gradient(to right, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0) 9%) left top / 100% 64px no-repeat;
        }

        .comparison thead th {
            font-weight: 600;
            text-align: left;
            padding: 22px 28px;
            font-size: 20px;
            letter-spacing: .3px;
            background: var(--col-header-bg);
            border-right: 4px solid #0f0f0f;
            border-left: 4px solid #0f0f0f;
            position: sticky;
            top: 0;
            z-index: 2;
        }

        .comparison thead th:first-child {
            background: transparent;
            border: none;
            font-size: 18px;
            font-weight: 600;
        }

        .comparison th,
        .comparison td {
            vertical-align: middle;
        }

        .comparison tbody th {
            width: var(--feature-col-width);
            background: var(--feature-col-bg);
            padding: 20px 18px 20px 10px;
            font-weight: 600;
            font-size: 18px;
            letter-spacing: .25px;
            line-height: 1.15;
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }

        .comparison tbody tr:first-child th {
            border-top: none;
        }

        .comparison tbody td {
            width: var(--plan-col-width);
            background: var(--cell-bg);
            padding: 20px 26px;
            border-top: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
            border-left: 4px solid #0f0f0f;
            border-right: 4px solid #0f0f0f;
            font-weight: 400;
            color: var(--text-muted);
            position: relative;
        }

        .comparison tbody tr:nth-child(even) td {
            background: var(--cell-bg-alt);
        }

        .comparison tbody td.plan-col--empty {
            text-align: center;
        }

        .check {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            color: var(--text-muted);
            font-weight: 400;
        }

        .check svg {
            width: 18px;
            height: 18px;
            stroke: var(--accent);
            fill: none;
            stroke-width: 2.4;
            stroke-linecap: round;
            stroke-linejoin: round;
            flex-shrink: 0;
            filter: drop-shadow(0 0 2px rgba(0, 163, 220, .35));
        }

        .inline-dash {
            display: inline-block;
            width: 80px;
            height: 3px;
            background: var(--dash-color);
            border-radius: 2px;
            margin: 6px 0 4px;
        }

        /* Mobile Layout - Split into separate tables */
        .mobile-tables {
            display: none;
        }

        .mobile-plan-table {
            margin-bottom: 40px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: var(--cell-bg);
        }

        .mobile-plan-header {
            background: var(--col-header-bg);
            padding: 20px 24px;
            font-size: 20px;
            font-weight: 600;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
        }

        .mobile-feature-row {
            display: flex;
            border-bottom: 1px solid var(--border-color);
        }

        .mobile-feature-row:last-child {
            border-bottom: none;
        }

        .mobile-feature-label {
            flex: 0 0 45%;
            background: var(--feature-col-bg);
            padding: 20px 16px;
            font-weight: 600;
            font-size: 16px;
            letter-spacing: .2px;
            line-height: 1.2;
            border-right: 1px solid var(--border-color);
            display: flex;
            align-items: center;
        }

        .mobile-feature-value {
            flex: 1;
            background: var(--cell-bg);
            padding: 20px 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .mobile-feature-row:nth-child(even) .mobile-feature-value {
            background: var(--cell-bg-alt);
        }

        .mobile-feature-value.empty {
            justify-content: center;
        }

        .mobile-inline-dash {
            width: 60px;
            height: 3px;
            background: var(--dash-color);
            border-radius: 2px;
        }

        /* Tablet responsive adjustments */
        @media (max-width: 1200px) and (min-width: 769px) {
            :root {
                --feature-col-width: 200px;
                --plan-col-width: 280px;
            }

            .comparison thead th {
                padding: 18px 20px;
                font-size: 18px;
            }

            .comparison tbody th {
                padding: 18px 14px 18px 8px;
                font-size: 16px;
            }

            .comparison tbody td {
                padding: 18px 20px;
                font-size: 14px;
            }
        }

        /* Mobile Layout */
        @media (max-width: 768px) {
            .wrapper {
                padding: 30px 16px;
            }

            .main-heading {
                font-size: clamp(2.5rem, 10vw, 4rem);
                margin: 0 0 30px;
            }

            .caption {
                font-size: 13px;
                margin: 0 0 30px;
            }

            .comparison {
                display: none;
            }

            .mobile-tables {
                display: block;
            }

            .check {
                gap: 8px;
                font-size: 14px;
            }

            .check svg {
                width: 16px;
                height: 16px;
            }
        }

        /* Very small screens */
        @media (max-width: 480px) {
            .wrapper {
                padding: 20px 12px;
            }

            .main-heading {
                font-size: clamp(2rem, 12vw, 3rem);
            }

            .mobile-plan-header {
                padding: 16px 20px;
                font-size: 18px;
            }

            .mobile-feature-label {
                flex: 0 0 40%;
                padding: 16px 12px;
                font-size: 15px;
            }

            .mobile-feature-value {
                padding: 16px 16px;
            }

            .check {
                font-size: 13px;
                gap: 6px;
            }

            .check svg {
                width: 14px;
                height: 14px;
            }

            .mobile-inline-dash {
                width: 50px;
                height: 2px;
            }
        }

        /* Screen reader utility */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0 0 0 0);
            border: 0;
        }
    </style>"""