import os

def create_banners():
    # Read base64 avatar
    with open("avatar_base64.txt", "r") as f:
        avatar_b64 = f.read().strip()
        
    # Read name SVG paths
    with open("name_paths_individual.svg", "r") as f:
        name_paths = f.read().strip()
        
    width = 1280
    height = 740

    def get_svg_content(is_light):
        return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Pranav Navghare - Full-Stack Developer &amp; Cybersecurity Specialist">
    <title>Pranav Navghare — Full-Stack Developer &amp; Cybersecurity Specialist</title>
    <defs>
        <style type="text/css"><![CDATA[
        text {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        @keyframes popIn {{ 0% {{ opacity: 0; transform: translateY(14px) scale(.7); }} 70% {{ opacity: 1; transform: translateY(-3px) scale(1.06); }} 100% {{ opacity: 1; transform: translateY(0) scale(1); }} }}
        @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
        @keyframes floaty {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-9px); }} }}
        @keyframes floaty2 {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-12px) rotate(6deg); }} }}
        @keyframes heartBeat {{ 0%, 100% {{ transform: scale(1); }} 12% {{ transform: scale(1.25); }} 24% {{ transform: scale(1); }} 36% {{ transform: scale(1.18); }} 48% {{ transform: scale(1); }} }}
        @keyframes neonFlicker {{ 0% {{ opacity: 0; }} 5% {{ opacity: .7; }} 7% {{ opacity: .1; }} 10% {{ opacity: .9; }} 12% {{ opacity: .3; }} 16%, 100% {{ opacity: 1; }} }}
        @keyframes neonPulse {{ 0%, 100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
        @keyframes twinkle {{ 0%, 100% {{ opacity: 0; transform: scale(.4); }} 50% {{ opacity: 1; transform: scale(1); }} }}
        @keyframes rise {{ 0% {{ transform: translateY(0); opacity: 0; }} 12% {{ opacity: .55; }} 88% {{ opacity: .55; }} 100% {{ transform: translateY(-46px); opacity: 0; }} }}
        
        .name-char {{ opacity: 0; animation: popIn .5s cubic-bezier(.2,.8,.3,1.3) forwards; transform-box: fill-box; transform-origin: center bottom; }}
        .ii, .pill, .soc, .st, .cl {{ opacity: 0; }}
        .pill {{ transition: transform .2s ease, filter .2s ease; transform-box: fill-box; transform-origin: center; cursor: pointer; }}
        .pill:hover {{ transform: scale(1.08); filter: brightness(1.35); }}
        .cur {{ animation: blink 1s step-end infinite; }}
        .tw {{ transform-box: fill-box; transform-origin: center; animation: twinkle 2.6s ease-in-out infinite; }}
        .hb {{ transform-box: fill-box; transform-origin: center; animation: heartBeat 2.2s ease-in-out infinite; }}
        .fl {{ animation: floaty 5s ease-in-out infinite; }}
        .fl2 {{ transform-box: fill-box; transform-origin: center; animation: floaty2 4.2s ease-in-out infinite; }}
        .neon-on {{ animation: neonFlicker 2.4s ease 3.2s backwards; }}
        .np {{ animation: neonPulse 2.6s ease-in-out infinite; }}
        .rp {{ animation: rise linear infinite; }}
        .sep {{ stroke: #2a1f3d; stroke-width: 1; opacity: .7; }}
        
        .neon-text-main {{ fill: #ff7eb6; font-size: 18px; font-weight: 900; letter-spacing: 3px; filter: url(#glow); animation: neonPulse 2.6s ease-in-out infinite; text-anchor: middle; }}
        .neon-text-sub {{ fill: #c084fc; font-size: 15px; font-weight: 900; letter-spacing: 2px; filter: url(#glow); text-anchor: middle; }}
        .neon-border {{ fill: rgba(28, 18, 48, 0.6); stroke: #c084fc; stroke-width: 1.5px; stroke-dasharray: 6 3; rx: 12px; }}
        
        .editor-bg {{ fill: #1c1230; stroke: #3b2a5c; stroke-width: 1px; rx: 10px; }}
        .editor-top {{ fill: #2a1f3d; }}
        .editor-title {{ fill: #9aa4b2; font-size: 11px; text-anchor: middle; font-family: monospace; }}
        ]]></style>

        <!-- Gradients -->
        <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#120b20"/><stop offset="55%" stop-color="#170e28"/><stop offset="100%" stop-color="#0e0918"/>
        </linearGradient>
        <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%"><animate attributeName="stop-color" values="#ff7eb6;#c084fc;#8b5cf6;#ff7eb6" dur="7s" repeatCount="indefinite"/></stop>
            <stop offset="55%"><animate attributeName="stop-color" values="#e879f9;#a78bfa;#ff7eb6;#e879f9" dur="7s" repeatCount="indefinite"/></stop>
            <stop offset="100%"><animate attributeName="stop-color" values="#8b5cf6;#ff7eb6;#c084fc;#8b5cf6" dur="7s" repeatCount="indefinite"/></stop>
        </linearGradient>
        <linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ff7eb6" stop-opacity=".35"/>
            <stop offset="50%" stop-color="#c084fc" stop-opacity=".3"/>
            <stop offset="100%" stop-color="#8b5cf6" stop-opacity=".35"/>
        </linearGradient>
        <radialGradient id="orbP"><stop offset="0%" stop-color="#ff7eb6" stop-opacity=".10"/><stop offset="100%" stop-color="#ff7eb6" stop-opacity="0"/></radialGradient>
        <radialGradient id="orbV"><stop offset="0%" stop-color="#8b5cf6" stop-opacity=".12"/><stop offset="100%" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient>
        <radialGradient id="orbB"><stop offset="0%" stop-color="#38bdf8" stop-opacity=".07"/><stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
        <radialGradient id="avatarGlow"><stop offset="0%" stop-color="#c084fc" stop-opacity=".25"/><stop offset="100%" stop-color="#c084fc" stop-opacity="0"/></radialGradient>
        
        <filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        <filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        <pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".6" fill="rgba(192,132,252,.10)"/></pattern>

        <!-- Animations and Clips -->
        <clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="480" dur="1s" begin=".3s" fill="freeze"/></rect></clipPath>
        <clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="200" dur=".5s" begin="1.2s" fill="freeze"/></rect></clipPath>
        <clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="350" dur=".7s" begin="3.4s" fill="freeze"/></rect></clipPath>
        <clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="350" dur=".6s" begin="4.2s" fill="freeze"/></rect></clipPath>
        
        <!-- 4 Cycling Roles across 24s -->
        <clipPath id="r1"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;400;400;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
        <clipPath id="r2"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;400;400;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
        <clipPath id="r3"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;400;400;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
        <clipPath id="r4"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;400;400;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>

        <linearGradient id="scanEdge" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#ff7eb6" stop-opacity="0"/><stop offset="18%" stop-color="#ff7eb6"/>
            <stop offset="50%" stop-color="#e879f9"/><stop offset="82%" stop-color="#c084fc"/>
            <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
        </linearGradient>
        <linearGradient id="scanTrail" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ff7eb6" stop-opacity="0"/><stop offset="100%" stop-color="#ff7eb6" stop-opacity=".18"/>
        </linearGradient>
        <clipPath id="bannerBox"><rect x="1" y="1" width="1278" height="738" rx="22"/></clipPath>
        <clipPath id="avatarReveal"><rect x="680" y="180" width="600" height="0">
          <animate attributeName="height" from="0" to="560" dur="1.8s" begin=".5s" fill="freeze"/>
        </rect></clipPath>
        <clipPath id="avatarBox"><rect x="680" y="180" width="600" height="560"/></clipPath>
    </defs>

    <!-- ================= BACKGROUND & ORBS ================= -->
    <rect width="1280" height="740" rx="22" fill="url(#bg)"/>
    <rect width="1280" height="740" rx="22" fill="url(#dots)"/>
    <circle cx="230" cy="220" r="260" fill="url(#orbP)"><animate attributeName="r" values="260;290;260" dur="6s" repeatCount="indefinite"/></circle>
    <circle cx="1000" cy="520" r="300" fill="url(#orbV)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
    <circle cx="700" cy="120" r="200" fill="url(#orbB)"><animate attributeName="r" values="200;225;200" dur="5.5s" repeatCount="indefinite"/></circle>
    <rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

    <!-- Rising particles -->
    <circle class="rp" cx="140" cy="620" r="1.4" fill="#ff7eb6" style="animation-duration:5s"/>
    <circle class="rp" cx="420" cy="700" r="1.1" fill="#c084fc" style="animation-duration:6s;animation-delay:1s"/>
    <circle class="rp" cx="620" cy="660" r="1.3" fill="#8b5cf6" style="animation-duration:4.6s;animation-delay:2s"/>
    <circle class="rp" cx="1180" cy="690" r="1.2" fill="#ff7eb6" style="animation-duration:5.4s;animation-delay:.6s"/>
    <circle class="rp" cx="1240" cy="360" r="1" fill="#c084fc" style="animation-duration:6.4s;animation-delay:1.6s"/>
    <circle class="rp" cx="70" cy="420" r="1" fill="#e879f9" style="animation-duration:5.8s;animation-delay:2.4s"/>

    <!-- Sparkles -->
    <g class="tw" style="animation-delay:.4s"><path d="M470 120l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#f0abfc"/></g>
    <g class="tw" style="animation-delay:1.5s"><path d="M880 120l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#ff7eb6"/></g>
    <g class="tw" style="animation-delay:2.6s"><path d="M1245 250l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#c084fc"/></g>

    <!-- ================= LEFT COLUMN ================= -->
    <!-- Terminal prompt -->
    <text clip-path="url(#cPrompt)" x="48" y="69" font-size="14">
        <tspan fill="#4ade80" font-weight="bold">pranav@cyber-dragon</tspan><tspan fill="#8b949e">:~$ </tspan><tspan fill="#e6edf3">cat </tspan><tspan fill="#e879f9">README.md</tspan>
    </text>
    <rect x="360" y="56" width="8" height="16" fill="#4ade80" opacity="0"><animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" begin="1.35s"/></rect>

    <!-- Hi, I'm -->
    <text clip-path="url(#cHi)" x="48" y="114" font-size="24" font-weight="bold" fill="#e6edf3">Hi, I'm 👋</text>

    <!-- Name SVG (Smooth Pacifico outline, popIn animation, vibrant animated gradient) -->
    <g transform="translate(48, 120) scale(0.76)" filter="url(#glow)">
        {name_paths}
    </g>
    <!-- Beating Heart / Sparkle after Name -->
    <g class="hb" style="animation-delay:3s">
        <path d="M508 166 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#ff7eb6" opacity=".95" filter="url(#glow)"/>
    </g>

    <!-- Cycling roles -->
    <text clip-path="url(#r1)" x="48" y="241" font-size="17" fill="#e879f9" filter="url(#glow)">&lt; Full-Stack Developer /&gt;</text>
    <text clip-path="url(#r2)" x="48" y="241" font-size="17" fill="#e879f9" filter="url(#glow)">&lt; Cybersecurity Specialist /&gt;</text>
    <text clip-path="url(#r3)" x="48" y="241" font-size="17" fill="#e879f9" filter="url(#glow)">&lt; AI &amp; Agent Architect /&gt;</text>
    <text clip-path="url(#r4)" x="48" y="241" font-size="17" fill="#e879f9" filter="url(#glow)">&lt; Python &amp; React Builder /&gt;</text>
    <rect x="48" y="228" width="2.5" height="16" fill="#e879f9" opacity="0"><animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="2.9s"/></rect>

    <!-- Quote box -->
    <g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
        <rect x="48" y="262" width="390" height="72" rx="8" fill="#1c1230" stroke="#3b2a5c" stroke-width="1"/>
        <rect x="48" y="266" width="3.5" height="64" rx="1.5" fill="#ff7eb6"/>
    </g>
    <text clip-path="url(#q1)" x="76" y="292" font-size="15" fill="#e6edf3">Building things, breaking things,</text>
    <text clip-path="url(#q2)" x="76" y="318" font-size="15"><tspan fill="#e6edf3">and learning </tspan><tspan fill="#ff7eb6" font-weight="bold">how</tspan><tspan fill="#e6edf3"> they work.</tspan></text>
    <g class="tw" style="animation-delay:.9s"><path d="M410 288l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#f0abfc"/></g>

    <!-- Tech I Know -->
    <text class="ii" x="48" y="374" font-size="15" fill="#c084fc" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">🧩 Tech I Know</text>
    <g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="388" width="80" height="26" rx="13" fill="rgba(255,223,30,.10)" stroke="#f7df1e" stroke-width="1"/><text x="88" y="405" text-anchor="middle" font-size="12" fill="#fde047" font-weight="bold">Python</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="136" y="388" width="100" height="26" rx="13" fill="rgba(247,223,30,.10)" stroke="#f7df1e" stroke-width="1"/><text x="186" y="405" text-anchor="middle" font-size="12" fill="#fde047" font-weight="bold">JavaScript</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5s forwards"><rect x="244" y="388" width="100" height="26" rx="13" fill="rgba(49,120,198,.15)" stroke="#3178c6" stroke-width="1"/><text x="294" y="405" text-anchor="middle" font-size="12" fill="#93c5fd" font-weight="bold">TypeScript</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="352" y="388" width="76" height="26" rx="13" fill="rgba(97,218,251,.10)" stroke="#61dafb" stroke-width="1"/><text x="390" y="405" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">React</text></g>
    
    <g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="48" y="422" width="64" height="26" rx="13" fill="rgba(139,92,246,.14)" stroke="#8b5cf6" stroke-width="1"/><text x="80" y="439" text-anchor="middle" font-size="12" fill="#c4b5fd" font-weight="bold">SQL</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="120" y="422" width="76" height="26" rx="13" fill="rgba(255,126,182,.10)" stroke="#ff7eb6" stroke-width="1"/><text x="158" y="439" text-anchor="middle" font-size="12" fill="#f9a8d4" font-weight="bold">AI/ML</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="204" y="422" width="94" height="26" rx="13" fill="rgba(16,185,129,.15)" stroke="#10b981" stroke-width="1"/><text x="251" y="439" text-anchor="middle" font-size="12" fill="#6ee7b7" font-weight="bold">AI Agents</text></g>
    <g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="306" y="422" width="124" height="26" rx="13" fill="rgba(239,68,68,.15)" stroke="#ef4444" stroke-width="1"/><text x="368" y="439" text-anchor="middle" font-size="12" fill="#fca5a5" font-weight="bold">Cybersecurity</text></g>

    <!-- About Me -->
    <text class="ii" x="48" y="490" font-size="15" fill="#ff7eb6" font-weight="bold" style="animation:fadeIn .4s ease 5.6s forwards">💖 About Me</text>
    <text class="ii" x="48" y="516" font-size="13.5" style="animation:fadeIn .4s ease 5.8s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">I build secure, scalable and impactful web architectures.</tspan></text>
    <text class="ii" x="48" y="540" font-size="13.5" style="animation:fadeIn .4s ease 6s forwards"><tspan fill="#fde047">💡 </tspan><tspan fill="#cdd3dd">Always learning, always building.</tspan></text>
    <text class="ii" x="48" y="564" font-size="13.5" style="animation:fadeIn .4s ease 6.2s forwards"><tspan fill="#ff7eb6">🚀 </tspan><tspan fill="#cdd3dd">Turning complex problems into elegant solutions.</tspan></text>

    <!-- Stats card -->
    <g class="st" style="animation:fadeIn .5s ease 6.4s forwards">
        <rect x="48" y="586" width="560" height="66" rx="12" fill="#1c1230" stroke="#3b2a5c" stroke-width="1"/>
        <line x1="188" y1="598" x2="188" y2="640" class="sep"/>
        <line x1="328" y1="598" x2="328" y2="640" class="sep"/>
        <line x1="468" y1="598" x2="468" y2="640" class="sep"/>
        <text x="118" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">📦 Repos</text>
        <text x="258" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">💻 Commits</text>
        <text x="398" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">⭐ Stars</text>
        <text x="538" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">👥 Followers</text>
    </g>
    <text class="st" x="118" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#ff7eb6" filter="url(#glow)" style="animation:fadeIn .4s ease 6.6s forwards">42+</text>
    <text class="st" x="258" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#e879f9" filter="url(#glow)" style="animation:fadeIn .4s ease 6.75s forwards">1000+</text>
    <text class="st" x="398" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#fde047" filter="url(#glow)" style="animation:fadeIn .4s ease 6.9s forwards">4000+</text>
    <text class="st" x="538" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#c084fc" filter="url(#glow)" style="animation:fadeIn .4s ease 7.05s forwards">250+</text>

    <!-- Pixel Heart in Center -->
    <g transform="translate(580,310)" opacity="0">
        <animate attributeName="opacity" from="0" to=".95" dur=".6s" begin="4.4s" fill="freeze"/>
        <g fill="#a855f7">
            <rect x="6" y="0" width="6" height="6"/><rect x="18" y="0" width="6" height="6"/>
            <rect x="0" y="6" width="30" height="6"/><rect x="3" y="12" width="24" height="6"/>
            <rect x="9" y="18" width="12" height="6"/><rect x="12" y="24" width="6" height="4"/>
        </g>
    </g>

    <!-- ================= RIGHT: AVATAR & GLOW ================= -->
    <circle cx="1000" cy="410" r="300" fill="url(#avatarGlow)"><animate attributeName="r" values="300;325;300" dur="5s" repeatCount="indefinite"/></circle>
    <g class="fl">
        <g clip-path="url(#avatarReveal)">
            <image x="680" y="180" width="600" height="560" href="{avatar_b64}" preserveAspectRatio="xMaxYMax meet" />
        </g>
    </g>

    <!-- Floating Heart at Top Right -->
    <g class="hb" style="animation-delay:1.4s"><path d="M1240 280 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#ff7eb6" opacity=".85" filter="url(#glow)"/></g>

    <!-- buildDreams() code card -->
    <g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
        <rect x="552" y="40" width="286" height="212" rx="12" fill="#160f26" fill-opacity=".94" stroke="#3b2a5c" stroke-width="1.2"/>
        <rect x="552" y="40" width="286" height="28" rx="12" fill="#211538"/>
        <rect x="552" y="56" width="286" height="12" fill="#211538"/>
        <circle cx="572" cy="54" r="4.5" fill="#ff5f57"/><circle cx="588" cy="54" r="4.5" fill="#febc2e"/><circle cx="604" cy="54" r="4.5" fill="#28c840"/>
        <text x="695" y="58" text-anchor="middle" font-size="11" fill="#8b949e">dreams.jsx</text>
    </g>
    <g font-size="12.5">
        <text class="cl" x="568" y="90" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#e879f9">function</tspan><tspan fill="#7dd3fc"> buildDreams</tspan><tspan fill="#e6edf3">() {{</tspan></text>
        <text class="cl" x="582" y="110" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#e879f9">return</tspan><tspan fill="#e6edf3"> (</tspan></text>
        <text class="cl" x="596" y="130" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#8b949e">&lt;</tspan><tspan fill="#4ade80">div</tspan><tspan fill="#c084fc"> className</tspan><tspan fill="#e6edf3">=</tspan><tspan fill="#fde047">"dreams"</tspan><tspan fill="#8b949e">&gt;</tspan></text>
        <text class="cl" x="610" y="150" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#8b949e">&lt;</tspan><tspan fill="#ff7eb6">Code</tspan><tspan fill="#8b949e"> /&gt;</tspan></text>
        <text class="cl" x="610" y="168" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#8b949e">&lt;</tspan><tspan fill="#fde047">Coffee</tspan><tspan fill="#8b949e"> /&gt;</tspan></text>
        <text class="cl" x="610" y="186" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#8b949e">&lt;</tspan><tspan fill="#7dd3fc">Repeat</tspan><tspan fill="#8b949e"> /&gt;</tspan></text>
        <text class="cl" x="610" y="204" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#8b949e">&lt;</tspan><tspan fill="#4ade80">Success</tspan><tspan fill="#8b949e"> /&gt;</tspan></text>
        <text class="cl" x="596" y="222" style="animation:fadeIn .3s ease 3.65s forwards"><tspan fill="#8b949e">&lt;/</tspan><tspan fill="#4ade80">div</tspan><tspan fill="#8b949e">&gt;</tspan><tspan fill="#e6edf3">);</tspan></text>
        <text class="cl" x="568" y="242" style="animation:fadeIn .3s ease 3.85s forwards"><tspan fill="#e6edf3">}}</tspan><tspan fill="#8b949e"> // export default</tspan></text>
    </g>
    
    <!-- Neon Sign -->
    <g class="neon-on">
        <rect x="1012" y="42" width="238" height="128" rx="14" fill="none" stroke="#e879f9" stroke-width="1.5" opacity=".5" filter="url(#glow)"/>
        <text class="np" x="1131" y="86" text-anchor="middle" font-size="30" font-weight="bold" fill="#ff7eb6" filter="url(#glowBig)" style="animation-delay:.2s">&lt;/&gt;</text>
        <text class="np" x="1131" y="118" text-anchor="middle" font-size="19" font-weight="bold" fill="#e879f9" filter="url(#glow)" letter-spacing="2">KEEP CODING</text>
        <text class="np" x="1131" y="146" text-anchor="middle" font-size="19" font-weight="bold" fill="#c084fc" filter="url(#glow)" letter-spacing="1.5" style="animation-delay:1.3s">KEEP GROWING</text>
    </g>

    <!-- Pixel Heart in Center -->
    <g class="fl2" style="animation-delay:.7s">
        <g transform="translate(600,300)" opacity="0">
            <animate attributeName="opacity" from="0" to=".95" dur=".6s" begin="4.4s" fill="freeze"/>
            <g fill="#a855f7">
                <rect x="6" y="0" width="6" height="6"/><rect x="18" y="0" width="6" height="6"/>
                <rect x="0" y="6" width="30" height="6"/><rect x="3" y="12" width="24" height="6"/>
                <rect x="9" y="18" width="12" height="6"/><rect x="12" y="24" width="6" height="4"/>
            </g>
        </g>
    </g>

    <!-- ================= FOOTER ================= -->
    <line x1="48" y1="676" x2="1232" y2="676" class="sep" stroke-dasharray="1184" stroke-dashoffset="1184">
        <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.2s" fill="freeze"/>
    </line>
    
    <g class="soc" style="animation:fadeIn .5s ease 7.4s forwards">
        <!-- GitHub Vector Icon -->
        <g transform="translate(48,693) scale(.75)"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#c9d1d9"/></g>
        <text x="72" y="707" font-size="12" fill="#c9d1d9">PranavXDragon</text>
        
        <!-- Mail Vector Icon -->
        <g transform="translate(195,694) scale(.75)"><rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#ff7eb6" stroke-width="2"/><path d="M2.5 5.5 12 13l9.5-7.5" fill="none" stroke="#ff7eb6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
        <text x="219" y="707" font-size="12" fill="#c9d1d9">Pranavnavghare46@gmail.com</text>
        
        <!-- Instagram Vector Icon -->
        <g transform="translate(438,693) scale(.75)"><rect width="24" height="24" rx="6" fill="none" stroke="#e879f9" stroke-width="2"/><circle cx="12" cy="12" r="4.6" fill="none" stroke="#e879f9" stroke-width="2"/><circle cx="18.2" cy="5.8" r="1.5" fill="#e879f9"/></g>
        <text x="462" y="707" font-size="12" fill="#c9d1d9">sudo.void.pranav</text>
        
        <!-- Open to Collaborate with Green Pulse -->
        <text x="615" y="707" font-size="11.5"><tspan fill="#28c840">●</tspan><tspan fill="#8b949e"> open to collaborate</tspan></text>
        
        <!-- Tagline on the Right -->
        <!-- Removed to prevent overlap with the avatar -->
    </g>

    <!-- Full Banner Vertical Laser Scanner -->
    <g clip-path="url(#bannerBox)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,-40;0,780" dur="4s" begin="3s" repeatCount="indefinite"/>
            <rect x="0" y="-34" width="1280" height="34" fill="url(#scanTrail)"/>
            <rect x="0" y="0" width="1280" height="2.2" fill="url(#scanEdge)" opacity=".6" filter="url(#glow)"/>
        </g>
    </g>
</svg>"""

    # Write Dark Mode
    with open("banner.svg", "w", encoding="utf-8") as f:
        f.write(get_svg_content(is_light=False))
        
    with open("banner-light.svg", "w", encoding="utf-8") as f:
        f.write(get_svg_content(is_light=True))

if __name__ == '__main__':
    create_banners()
    print("Created banners with 100% pixel perfect reference quality!")
