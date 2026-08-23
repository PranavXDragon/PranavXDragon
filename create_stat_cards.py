def create_stat_cards():

    # ── Exact same design pattern as example/megha-*.svg ─────────────────
    # bg: #170e28    border: animated gradient #ff7eb6 ↔ #c084fc
    # font: SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace
    # Animations: <animate> SMIL (not CSS transforms) for bar widths
    # Shine sweep across card, fadeSlide per row, rankPulse for rank text
    # ─────────────────────────────────────────────────────────────────────

    # 1. stats.svg  (mirrors megha-stats.svg)
    stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 232" width="500" height="232" role="img" aria-label="Pranav Navghare's GitHub stats">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeSlide{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rankPulse{0%,100%{opacity:.85}50%{opacity:1}}
@keyframes shineX{0%{transform:translateX(-160px) skewX(-15deg)}60%,100%{transform:translateX(560px) skewX(-15deg)}}
.row{opacity:0;animation:fadeSlide .5s ease forwards}
.rk{animation:rankPulse 2.4s ease-in-out infinite}
.sh{animation:shineX 4.5s ease-in-out 2.4s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff7eb6;#c084fc;#ff7eb6" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#c084fc;#ff7eb6;#c084fc" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#ff7eb6"/><stop offset="100%" stop-color="#8b5cf6"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="498" height="230" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="1" y="1" width="498" height="230" rx="14" fill="#170e28" stroke="url(#tg)" stroke-width="1.5"/>
<text x="24" y="38" font-size="16" font-weight="bold" fill="url(#tg)">&#128202; Pranav Navghare's GitHub Stats</text>

  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="74" font-size="14">&#11088;</text>
    <text x="52" y="74" font-size="13.5" fill="#c9d1d9">Total Stars Earned:</text>
    <text x="316" y="74" text-anchor="end" font-size="14" font-weight="bold" fill="#fde047">4,000+</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="105" font-size="14">&#128187;</text>
    <text x="52" y="105" font-size="13.5" fill="#c9d1d9">Total Commits:</text>
    <text x="316" y="105" text-anchor="end" font-size="14" font-weight="bold" fill="#7dd3fc">1,000+</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="136" font-size="14">&#128230;</text>
    <text x="52" y="136" font-size="13.5" fill="#c9d1d9">Public Repos:</text>
    <text x="316" y="136" text-anchor="end" font-size="14" font-weight="bold" fill="#4ade80">42+</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="167" font-size="14">&#128101;</text>
    <text x="52" y="167" font-size="13.5" fill="#c9d1d9">Followers:</text>
    <text x="316" y="167" text-anchor="end" font-size="14" font-weight="bold" fill="#c084fc">250+</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="198" font-size="14">&#128737;&#65039;</text>
    <text x="52" y="198" font-size="13.5" fill="#c9d1d9">Cyber Projects:</text>
    <text x="316" y="198" text-anchor="end" font-size="14" font-weight="bold" fill="#ff7eb6">10+</text>
  </g>

<!-- Rank ring -->
<g transform="translate(408,138)">
  <circle r="52" fill="none" stroke="#241740" stroke-width="9"/>
  <circle r="52" fill="none" stroke="url(#ringg)" stroke-width="9" stroke-linecap="round"
    stroke-dasharray="326.7 326.7" stroke-dashoffset="326.7" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="326.7" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk" y="14" text-anchor="middle" font-size="32" font-weight="bold" fill="#ff7eb6" filter="url(#g)">S+</text>
  <text y="76" text-anchor="middle" font-size="10.5" fill="#8b949e" opacity="0" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>

<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="120" height="232" fill="url(#shg)"/></g>
</svg>"""
    
    with open("stats.svg", "w", encoding="utf-8") as f:
        f.write(stats_svg)

    # 2. langs.svg  (mirrors megha-langs.svg)
    langs_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 282" width="420" height="282" role="img" aria-label="Top languages">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes shineX{0%{transform:translateX(-140px)}60%,100%{transform:translateX(460px)}}
.row{opacity:0;animation:fadeUp .5s ease forwards}
.sh{animation:shineX 4s ease-in-out 2.2s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff7eb6;#c084fc;#ff7eb6" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#c084fc;#ff7eb6;#c084fc" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".08"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cardc"><rect x="1" y="1" width="418" height="280" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="58" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="380" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
</defs>
<rect x="1" y="1" width="418" height="280" rx="14" fill="#170e28" stroke="url(#tg)" stroke-width="1.5"/>
<text x="20" y="34" font-size="16" font-weight="bold" fill="url(#tg)">&#128202; Top Languages</text>
<g clip-path="url(#stackc)"><rect x="20.0" y="58" width="171.6" height="11" fill="#3572A5"/><rect x="191.6" y="58" width="114.4" height="11" fill="#3178c6"/><rect x="306.0" y="58" width="58.9" height="11" fill="#f1e05a"/><rect x="364.9" y="58" width="35.1" height="11" fill="#e34c26"/></g>

  <g class="row" style="animation-delay:0.90s">
    <circle cx="26" cy="91" r="5" fill="#3572A5"/>
    <text x="40" y="96" font-size="13" fill="#e6edf3" font-weight="bold">Python</text>
    <text x="396" y="96" text-anchor="end" font-size="13" fill="#3572A5" font-weight="bold">45.2%</text>
    <rect x="40" y="104" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect x="40" y="104" width="0" height="9" rx="4.5" fill="#3572A5">
      <animate attributeName="width" from="0" to="121.1" dur="1.1s" begin="1.05s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.25s">
    <circle cx="26" cy="133" r="5" fill="#3178c6"/>
    <text x="40" y="138" font-size="13" fill="#e6edf3" font-weight="bold">TypeScript</text>
    <text x="396" y="138" text-anchor="end" font-size="13" fill="#3178c6" font-weight="bold">30.1%</text>
    <rect x="40" y="146" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect x="40" y="146" width="0" height="9" rx="4.5" fill="#3178c6">
      <animate attributeName="width" from="0" to="80.7" dur="1.1s" begin="1.40s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.60s">
    <circle cx="26" cy="175" r="5" fill="#f1e05a"/>
    <text x="40" y="180" font-size="13" fill="#e6edf3" font-weight="bold">JavaScript</text>
    <text x="396" y="180" text-anchor="end" font-size="13" fill="#f1e05a" font-weight="bold">15.5%</text>
    <rect x="40" y="188" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect x="40" y="188" width="0" height="9" rx="4.5" fill="#f1e05a">
      <animate attributeName="width" from="0" to="41.5" dur="1.1s" begin="1.75s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.95s">
    <circle cx="26" cy="217" r="5" fill="#e34c26"/>
    <text x="40" y="222" font-size="13" fill="#e6edf3" font-weight="bold">HTML/CSS</text>
    <text x="396" y="222" text-anchor="end" font-size="13" fill="#e34c26" font-weight="bold">9.2%</text>
    <rect x="40" y="230" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect x="40" y="230" width="0" height="9" rx="4.5" fill="#e34c26">
      <animate attributeName="width" from="0" to="24.7" dur="1.1s" begin="2.10s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="100" height="282" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>"""
    with open("langs.svg", "w", encoding="utf-8") as f:
        f.write(langs_svg)

    # 3. trophies.svg  (mirrors megha-trophies.svg)
    trophies_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes popCell{0%{opacity:0;transform:translateY(16px) scale(.85)}70%{opacity:1;transform:translateY(-3px) scale(1.03)}100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes rankGlow{0%,100%{opacity:.75}50%{opacity:1}}
@keyframes shineX2{0%{transform:translateX(-200px) skewX(-15deg)}60%,100%{transform:translateX(1172px) skewX(-15deg)}}
.cell{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}
.rk{animation:rankGlow 2.2s ease-in-out infinite}
.sh2{animation:shineX2 5s ease-in-out 2s infinite}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="tg2" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff7eb6;#c084fc;#ff7eb6" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#c084fc;#ff7eb6;#c084fc" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
</defs>
<rect x="0" y="0" width="1092" height="168" rx="14" fill="#170e28" stroke="url(#tg2)" stroke-width="1.5"/>

  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff7eb6" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="82" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z" fill="#ff7eb6"/></svg>
    <text class="rk" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#ff7eb6" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Multi-Language</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Python+JS+TS+more</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#ff7eb6">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#fde047" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="262" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21 12 17.27z" fill="#fde047"/></svg>
    <text class="rk" x="344" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#fde047" style="animation-delay:0.88s">S+</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Star Gazer</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Stars 4,000+</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#fde047">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#e879f9" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="442" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M11.73 3.12c-.22.56-.12 1.35.33 2.1 1.09 1.83 2.5 3.32 2.5 5.78 0 2.4-1.55 4.58-3.76 5.54-1.89.82-4.04.57-5.61-.71-.87-.71-1.37-1.78-1.42-2.93-.05-1.12.35-2.26 1.1-3.13 1.05-1.22 2.82-1.92 2.82-3.32 0-1.41-1.16-2.5-2.52-2.5-1.31 0-2.47 1-2.53 2.31 0 .28 0 .58.07.87C1.49 8.44 1 10.15 1 12.01c0 2.57 1.04 4.88 2.72 6.55C5.41 20.24 7.73 21 10 21c4.85 0 9-3.93 9-8.79 0-3.66-2-6.52-4.32-8.35-.41-.33-.87-.63-1.35-.91.24.62.33 1.34.4 2.17z" fill="#e879f9"/></svg>
    <text class="rk" x="524" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#e879f9" style="animation-delay:1.06s">S</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Deep Commits</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Commits 1,000+</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#e879f9">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#c084fc" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="622" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z" fill="#c084fc"/></svg>
    <text class="rk" x="704" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#c084fc" style="animation-delay:1.24s">S</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Cyber Defender</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Security Projects</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#c084fc">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#7dd3fc" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="802" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M19 10V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S8 3.34 8 5H5c-1.1 0-2 .9-2 2v3H1v2h2v5c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-5h2v-2h-2zm-9 6H6v-2h4v2zm6 0h-4v-2h4v2z" fill="#7dd3fc"/></svg>
    <text class="rk" x="884" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#7dd3fc" style="animation-delay:1.42s">S</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">AI Artisan</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">AI Agents Builder</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#7dd3fc">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#4ade80" stroke-opacity=".55" stroke-width="1.3"/>
    <svg x="982" y="24" width="28" height="28" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zm0 12l-10-5v5l10 5 10-5v-5l-10 5z" fill="#4ade80"/></svg>
    <text class="rk" x="1064" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#4ade80" style="animation-delay:1.60s">A</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Pull Shark</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">PRs 250+</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#241740"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#4ade80">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="140" height="168" fill="url(#shg2)"/></g>
</svg>"""
    with open("trophies.svg", "w", encoding="utf-8") as f:
        f.write(trophies_svg)

if __name__ == '__main__':
    create_stat_cards()
    print("Created stat cards.")
