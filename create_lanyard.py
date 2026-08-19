def create_lanyard():
    with open("avatar_base64.txt", "r") as f:
        avatar_b64 = f.read().strip()
        
    width = 400
    height = 600
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
        <!-- Lanyard Gradient -->
        <linearGradient id="lanyardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ff79c6"/>
            <stop offset="100%" stop-color="#bd93f9"/>
        </linearGradient>
        
        <!-- Glassmorphism Card -->
        <linearGradient id="glassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0.1)"/>
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0.05)"/>
        </linearGradient>
        
        <!-- Hologram Sweep -->
        <linearGradient id="sweepGrad" x1="-100%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="rgba(255, 255, 255, 0)"/>
            <stop offset="50%" stop-color="rgba(255, 255, 255, 0.4)"/>
            <stop offset="100%" stop-color="rgba(255, 255, 255, 0)"/>
        </linearGradient>

        <clipPath id="avatarClip">
            <circle cx="200" cy="220" r="60"/>
        </clipPath>
        
        <clipPath id="cardClip">
            <rect x="75" y="100" width="250" height="400" rx="15"/>
        </clipPath>
    </defs>
    
    <style>
        .text {{ font-family: 'Segoe UI', Ubuntu, sans-serif; fill: #ffffff; text-anchor: middle; }}
        .name {{ font-size: 22px; font-weight: bold; }}
        .role {{ font-size: 14px; fill: #c9d1d9; }}
        .handle {{ font-size: 12px; fill: #ff79c6; font-weight: bold; }}
        
        /* Pendulum physics */
        @keyframes swing {{
            0% {{ transform: rotate(15deg); }}
            25% {{ transform: rotate(-10deg); }}
            50% {{ transform: rotate(5deg); }}
            75% {{ transform: rotate(-2deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        @keyframes swayForever {{
            0% {{ transform: rotate(0deg); }}
            50% {{ transform: rotate(2deg); }}
            100% {{ transform: rotate(0deg); }}
        }}
        .lanyard-group {{
            transform-origin: 200px -200px;
            animation: swing 3s cubic-bezier(0.25, 1, 0.5, 1) forwards, swayForever 4s ease-in-out infinite 3s;
        }}
        
        /* Drop in from top */
        @keyframes dropIn {{
            from {{ transform: translateY(-800px); }}
            to {{ transform: translateY(0); }}
        }}
        .drop-group {{
            animation: dropIn 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }}
        
        /* Holographic sweep */
        @keyframes shineSweep {{
            0% {{ transform: translateX(-300px) translateY(-300px); }}
            100% {{ transform: translateX(300px) translateY(300px); }}
        }}
        .hologram-sweep {{
            animation: shineSweep 4s infinite linear;
        }}
    </style>
    
    <g class="drop-group">
        <g class="lanyard-group">
            
            <!-- Strap -->
            <path d="M 185 -200 L 185 80 L 215 80 L 215 -200" fill="url(#lanyardGrad)"/>
            
            <!-- Strap text (rotated) -->
            <!-- <text transform="rotate(90, 200, 0)" class="text" x="200" y="0" font-size="12">DEVELOPER</text> -->
            
            <!-- Metal Ring & Clasp -->
            <rect x="180" y="80" width="40" height="15" rx="5" fill="#a0a0a0"/>
            <circle cx="200" cy="105" r="12" fill="none" stroke="#d0d0d0" stroke-width="4"/>
            <rect x="195" y="117" width="10" height="20" rx="3" fill="#a0a0a0"/>
            
            <!-- Card -->
            <g clip-path="url(#cardClip)">
                <!-- Card Background -->
                <rect x="75" y="100" width="250" height="400" fill="#161b22" rx="15"/>
                <rect x="75" y="100" width="250" height="400" fill="url(#glassGrad)" rx="15"/>
                <rect x="75" y="100" width="250" height="400" fill="none" stroke="#ff79c6" stroke-width="2" rx="15"/>
                
                <!-- Card Hole -->
                <rect x="180" y="115" width="40" height="10" rx="5" fill="#0d1117"/>
                
                <!-- Avatar Ring Glow -->
                <circle cx="200" cy="220" r="64" fill="none" stroke="url(#lanyardGrad)" stroke-width="4"/>
                
                <!-- Avatar -->
                <image href="{avatar_b64}" x="140" y="160" width="120" height="120" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)"/>
                
                <!-- Texts -->
                <text class="text name" x="200" y="320">Pranav Navghare</text>
                <text class="text role" x="200" y="345">Full-Stack &amp; CyberSec</text>
                
                <rect x="130" y="360" width="140" height="25" rx="12" fill="#21262d"/>
                <text class="text handle" x="200" y="377">@PranavXDragon</text>
                
                <!-- Barcode -->
                <g transform="translate(100, 420)" fill="#ffffff">
                    <rect x="0" y="0" width="4" height="40"/>
                    <rect x="8" y="0" width="2" height="40"/>
                    <rect x="14" y="0" width="8" height="40"/>
                    <rect x="26" y="0" width="2" height="40"/>
                    <rect x="32" y="0" width="4" height="40"/>
                    <rect x="40" y="0" width="10" height="40"/>
                    <rect x="54" y="0" width="4" height="40"/>
                    <rect x="62" y="0" width="2" height="40"/>
                    <rect x="68" y="0" width="6" height="40"/>
                    <rect x="78" y="0" width="8" height="40"/>
                    <rect x="90" y="0" width="4" height="40"/>
                    <rect x="98" y="0" width="10" height="40"/>
                    <rect x="112" y="0" width="2" height="40"/>
                    <rect x="118" y="0" width="6" height="40"/>
                    <rect x="128" y="0" width="4" height="40"/>
                    <rect x="136" y="0" width="8" height="40"/>
                    <rect x="148" y="0" width="2" height="40"/>
                    <rect x="154" y="0" width="6" height="40"/>
                    <rect x="164" y="0" width="10" height="40"/>
                    <rect x="178" y="0" width="4" height="40"/>
                    <rect x="186" y="0" width="2" height="40"/>
                    <rect x="192" y="0" width="8" height="40"/>
                </g>
                <text class="text role" x="200" y="475" font-size="10" font-family="monospace">1 0 1 0 0 1 1 0 1</text>
                
                <!-- Hologram Sweep Overlay -->
                <rect class="hologram-sweep" x="-100" y="-100" width="500" height="800" fill="url(#sweepGrad)" transform="rotate(45, 200, 300)"/>
            </g>
        </g>
    </g>
</svg>"""

    with open("lanyard.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == '__main__':
    create_lanyard()
    print("Created lanyard.svg")
