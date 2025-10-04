async def plans_body():
    return """<section>
    <div class="wrapper">
        <div class="container">
            <h1 class="main-heading">Compare All Plans</h1>

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
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dedicated Support</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M7 12.5l3.1 3L17 8.8" /></svg>Standard Support</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Consultation</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Only Business Consultation</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Server</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Dedicated Server</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Analytics</div><div class="mobile-feature-value empty"><span class="mobile-inline-dash" aria-hidden="true"></span><span class="sr-only">Not Included</span></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Reports</div><div class="mobile-feature-value empty"><span class="mobile-inline-dash" aria-hidden="true"></span><span class="sr-only">Not Included</span></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dashboard Features</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>KPI Dashboard</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">AI ChatBots</div><div class="mobile-feature-value empty"><span class="mobile-inline-dash" aria-hidden="true"></span><span class="sr-only">Not Included</span></div></div>
                </div>

                <!-- Intermediate Plan Table -->
                <div class="mobile-plan-table">
                    <div class="mobile-plan-header">Intermediate Plan</div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dedicated Support</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M7 12.5l3.1 3L17 8.8" /></svg>Standard Support</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Consultation</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Business + Data Consultation</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Server</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Dedicated Server</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Analytics</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Descriptive Analysis</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Reports</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Monthly Reports</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dashboard Features</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Inquisitive Dashboard</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">AI ChatBots</div><div class="mobile-feature-value empty"><span class="mobile-inline-dash" aria-hidden="true"></span><span class="sr-only">Not Included</span></div></div>
                </div>

                <!-- Advanced Plan Table -->
                <div class="mobile-plan-table">
                    <div class="mobile-plan-header">Advanced Plan</div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dedicated Support</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M7 12.5l3.1 3L17 8.8" /></svg>Standard Support</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Consultation</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Only Business Consultation</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Server</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Dedicated Server</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Analytics</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Predictive Analysis</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Reports</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Daily, Weekly, Monthly Reports</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">Dashboard Features</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Predictive Dashboard</div></div></div>
                    <div class="mobile-feature-row"><div class="mobile-feature-label">AI ChatBots</div><div class="mobile-feature-value"><div class="check"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" /><path d="M7 12.5l3.1 3L17 8.8" /></svg>Interactive AI Chatbots</div></div></div>
                </div>
            </div>
        </div>
    </div>
</section>"""

async def plans_style():
    return """<style>
        /* --- THEME VARIABLES --- */
        :root {
            /* Dark Theme (Default) */
            --bg-body: radial-gradient(circle at 0% 0%, #1b1b1b 0%, #090909 55%, #000 110%);
            --col-header-bg: #2f2f2f;
            --feature-col-bg: #070707;
            --cell-bg: #1d1d1d;
            --cell-bg-alt: #222222;
            --border-color: #343434;
            --vertical-border-color: #0f0f0f;
            --text-primary: #ffffff;
            --text-secondary: #ffffff;
            --text-muted: #d9d9d9;
            --accent: #00a3dc;
            --dash-color: #e5e5e5;
            --heading-gradient: linear-gradient(180deg, #FFFFFF 50%, #B0B0B0 100%);
            --check-shadow: drop-shadow(0 0 0.29vh rgba(0, 163, 220, .35));
        }

        @media (prefers-color-scheme: light) {
            :root {
                /* Light Theme */
                --bg-body: #FFFFFF;
                --col-header-bg: #E5E7EB;
                --feature-col-bg: #FFFFFF;
                --cell-bg: #2596F4;
                --cell-bg-alt: #2596F4;
                --border-color: #111111;
                --vertical-border-color: #FFFFFF;
                --text-primary: #1F2937;
                --text-secondary: #1F2937;
                --text-muted: #FFFFFF;
                --accent: #FFFFFF;
                --dash-color: #FFFFFF;
                --heading-gradient: none;
                --check-shadow: none;
            }
        }

        /* --- STRUCTURAL & THEME-AGNOSTIC STYLES --- */
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: 'Exo-2', system-ui, sans-serif;
            background: var(--bg-body);
            color: var(--text-primary);
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
        }

        .wrapper {
            width: 100%;
            display: flex;
            justify-content: center;
            padding: 8.88vh 2.96vw;
        }
        .container { width: 116.48vw; max-width: 100%; }

        /* Main Heading */
        .main-heading {
            text-align: center;
            margin: 0 0 7.4vh;
            font-size: clamp(4.44vh, 8vw, 8.88vh);
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1;
            color: var(--text-primary);
            background: var(--heading-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        /* Unset gradient text fill for light mode */
        @media (prefers-color-scheme: light) {
            .main-heading { -webkit-text-fill-color: initial; }
        }
        
        /* Desktop Table */
        .comparison {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            font-size: 2.22vh;
            line-height: 1.25;
        }

        .comparison thead th {
            font-weight: 600;
            text-align: left;
            padding: 3.25vh 4.14vw;
            font-size: 2.96vh;
            letter-spacing: .04vh;
            background: var(--col-header-bg);
            border-right: 0.59vh solid var(--vertical-border-color);
            border-left: 0.59vh solid var(--vertical-border-color);
            position: sticky; top: 0; z-index: 2;
            color: var(--text-secondary);
        }
        .comparison thead th:first-child { background: transparent; border: none; }
        .comparison th, .comparison td { vertical-align: middle; }

        .comparison tbody th {
            width: 18.35vw;
            background: var(--feature-col-bg);
            padding: 2.96vh 2.66vw 2.96vh 1.48vw;
            font-weight: 600;
            font-size: 2.66vh;
            letter-spacing: .03vh;
            line-height: 1.15;
            border-top: 0.14vh solid var(--border-color);
            border-bottom: 0.14vh solid var(--border-color);
            color: var(--text-primary);
        }
        .comparison tbody tr:first-child th { border-top: none; }

        .comparison tbody td {
            width: 28.12vw;
            background: var(--cell-bg);
            padding: 2.96vh 3.85vw;
            border-top: 0.14vh solid var(--border-color);
            border-bottom: 0.14vh solid var(--border-color);
            border-left: 0.59vh solid var(--vertical-border-color);
            border-right: 0.59vh solid var(--vertical-border-color);
            font-weight: 400;
            color: var(--text-muted);
        }
        .comparison tbody tr:nth-child(even) td { background: var(--cell-bg-alt); }
        .comparison tbody td.plan-col--empty { text-align: center; }

        .check {
            display: inline-flex;
            align-items: center;
            gap: 1.48vh;
            color: var(--text-muted);
            font-weight: 400;
        }
        .check svg {
            width: 2.66vh; height: 2.66vh;
            stroke: var(--accent);
            fill: none; stroke-width: 2.4;
            stroke-linecap: round; stroke-linejoin: round;
            flex-shrink: 0;
            filter: var(--check-shadow);
        }
        .inline-dash {
            display: inline-block;
            width: 11.85vh; height: 0.44vh;
            background: var(--dash-color);
            border-radius: 0.29vh; margin: 0.88vh 0 0.59vh;
        }

        /* Mobile Layout */
        .mobile-tables { display: none; }
        .mobile-plan-table { margin-bottom: 5.92vh; border-radius: 1.77vh; overflow: hidden; border: 0.14vh solid var(--border-color); background: var(--cell-bg); }
        .mobile-plan-header { background: var(--col-header-bg); padding: 2.96vh 3.55vw; font-size: 2.96vh; font-weight: 600; text-align: center; border-bottom: 0.14vh solid var(--border-color); color: var(--text-secondary); }
        .mobile-feature-row { display: flex; border-bottom: 0.14vh solid var(--border-color); }
        .mobile-feature-row:last-child { border-bottom: none; }
        .mobile-feature-label { flex: 0 0 45%; background: var(--feature-col-bg); padding: 2.96vh 2.37vw; font-weight: 600; font-size: 2.37vh; line-height: 1.2; border-right: 0.14vh solid var(--border-color); display: flex; align-items: center; color: var(--text-primary); }
        .mobile-feature-value { flex: 1; background: var(--cell-bg); padding: 2.96vh 2.96vw; display: flex; align-items: center; justify-content: center; }
        .mobile-feature-row:nth-child(even) .mobile-feature-value { background: var(--cell-bg-alt); }
        .mobile-feature-value.empty { justify-content: center; }
        .mobile-inline-dash { width: 8.88vh; height: 0.44vh; background: var(--dash-color); border-radius: 0.29vh; }

        /* Responsive Breakpoints */
        @media (max-width: 1200px) and (min-width: 769px) { /* Tablet */
            .comparison tbody th { width: 15.62vw; }
            .comparison tbody td { width: 21.87vw; }
        }
        @media (max-width: 768px) { /* Mobile */
            .wrapper { padding: 4.44vw 2.37vw; }
            .main-heading { font-size: clamp(3.7vh, 10vw, 5.92vh); margin-bottom: 4.44vh; }
            .comparison { display: none; }
            .mobile-tables { display: block; }
            .check { gap: 1.18vh; font-size: 2.07vh; }
            .check svg { width: 2.37vh; height: 2.37vh; }
        }
        
        .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); border: 0; }
    </style>"""