import streamlit as st
import random
import time


st.set_page_config(
    page_title="Happy Birthday! 🎉",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# -----------------------------
# Personalization
# -----------------------------
FRIEND_NAME = "Shaznay"
YOUR_NAME = "BM"


# -----------------------------
# CSS / animations
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Pacifico&display=swap');


html, body, [class*="css"] {
    font-family: 'Baloo 2', sans-serif;
}


.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 215, 100, .35), transparent 25%),
        radial-gradient(circle at 90% 15%, rgba(100, 200, 255, .30), transparent 25%),
        radial-gradient(circle at 50% 90%, rgba(150, 255, 200, .28), transparent 30%),
        linear-gradient(135deg, #fffef5 0%, #f5f8ff 45%, #f0fff5 100%);
    overflow-x: hidden;
}


.block-container {
    max-width: 1100px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}


.hero {
    text-align: center;
    padding: 55px 20px 35px;
    position: relative;
}


.small-label {
    color: #ff8c42;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-size: 0.9rem;
    animation: labelPulse 2s ease-in-out infinite;
}
@keyframes labelPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.85; transform: scale(1.05); }
}


.hero h1 {
    font-family: 'Pacifico', cursive;
    font-size: clamp(3.2rem, 9vw, 7rem);
    line-height: 1.05;
    margin: 10px 0;
    background: linear-gradient(90deg, #ff6b6b, #ffa502, #4ecdc4, #45b7d1);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 5s ease infinite;
    filter: drop-shadow(0 4px 12px rgba(255, 165, 2, 0.3));
}


.hero p {
    font-size: 1.3rem;
    color: #5a6b7c;
    animation: textFade 3s ease-in-out infinite;
}
@keyframes textFade {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.85; }
}


@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}


.sparkles {
    font-size: 2rem;
    letter-spacing: 18px;
    animation: sparkle 2s ease-in-out infinite alternate;
}
@keyframes sparkle {
    from { opacity: .45; transform: scale(.96) rotate(-5deg); }
    to { opacity: 1; transform: scale(1.05) rotate(5deg); }
}


.card {
    background: rgba(255,255,255,.72);
    border: 2px solid rgba(255,255,255,.9);
    box-shadow: 0 18px 45px rgba(100, 120, 140, .13), 0 0 0 4px rgba(255, 215, 100, 0.1);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 28px;
    margin: 18px 0;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, transparent, rgba(255, 215, 100, 0.1), transparent);
    transform: rotate(45deg);
    animation: shimmer 3s infinite;
}
@keyframes shimmer {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(100%) rotate(45deg); }
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 24px 60px rgba(100, 120, 140, .18), 0 0 0 4px rgba(255, 215, 100, 0.2);
}


.card h2 {
    color: #4a6fa5;
    margin-top: 0;
    animation: titleBounce 2s ease-in-out infinite;
}
@keyframes titleBounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-3px); }
}


.message {
    font-size: 1.15rem;
    line-height: 1.8;
    color: #4a5568;
}


.birthday-cake {
    text-align: center;
    font-size: 7rem;
    filter: drop-shadow(0 15px 20px rgba(255, 165, 2, .2));
    animation: cakeFloat 3s ease-in-out infinite;
}
@keyframes cakeFloat {
    0%,100% { transform: translateY(0) rotate(-1deg); }
    50% { transform: translateY(-12px) rotate(1deg); }
}


.star {
    display: inline-block;
    animation: starPulse 1.5s infinite;
}
@keyframes starPulse {
    0%, 40%, 100% { transform: scale(1) rotate(0deg); }
    20% { transform: scale(1.22) rotate(10deg); }
}


.memory-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}
.memory {
    min-height: 130px;
    border-radius: 22px;
    padding: 20px;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-shadow: 0 12px 25px rgba(80,100,120,.13);
    transition: all .3s ease;
    position: relative;
    overflow: hidden;
}
.memory::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.2), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.memory:hover::after {
    opacity: 1;
}
.memory:hover {
    transform: translateY(-8px) rotate(1deg) scale(1.03);
    box-shadow: 0 20px 40px rgba(80,100,120,.25);
}
.m1 { background: linear-gradient(135deg,#ff9966,#ff5e62); }
.m2 { background: linear-gradient(135deg,#56ab2f,#a8e063); }
.m3 { background: linear-gradient(135deg,#4facfe,#00f2fe); }
.m4 { background: linear-gradient(135deg,#f093fb,#f5576c); }
.m5 { background: linear-gradient(135deg,#fa709a,#fee140); }
.m6 { background: linear-gradient(135deg,#30cfd0,#330867); }


.wish {
    text-align:center;
    background: linear-gradient(135deg, rgba(255,240,200,.85), rgba(200,240,255,.85));
    border-radius: 30px;
    padding: 35px 25px;
    animation: wishGlow 2s ease-in-out infinite;
    box-shadow: 0 10px 40px rgba(255, 165, 2, 0.2);
}
@keyframes wishGlow {
    0%, 100% { box-shadow: 0 10px 40px rgba(255, 165, 2, 0.2); }
    50% { box-shadow: 0 10px 60px rgba(255, 165, 2, 0.35); }
}


.wish-big {
    font-family: 'Pacifico', cursive;
    font-size: 2.2rem;
    color: #ff8c42;
    animation: wishText 3s ease-in-out infinite;
}
@keyframes wishText {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}


.footer {
    text-align:center;
    color:#6b7280;
    padding: 35px 0 10px;
    font-size: .95rem;
    animation: footerFade 4s ease-in-out infinite;
}
@keyframes footerFade {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}


.floating {
    position: fixed;
    pointer-events: none;
    z-index: 0;
    animation: floatUp linear infinite;
    opacity: .7;
}
@keyframes floatUp {
    0% { transform: translateY(110vh) rotate(0deg) scale(0.8); opacity:0; }
    15% { opacity:.75; }
    85% { opacity:.75; }
    100% { transform: translateY(-15vh) rotate(720deg) scale(1.2); opacity:0; }
}


/* Twinkling stars */
.twinkle {
    position: fixed;
    pointer-events: none;
    z-index: 0;
    animation: twinkle 2s ease-in-out infinite;
}
@keyframes twinkle {
    0%, 100% { opacity: 0.3; transform: scale(0.8); }
    50% { opacity: 1; transform: scale(1.2); }
}


/* Corner decorations */
.corner-decoration {
    position: fixed;
    font-size: 3rem;
    z-index: 0;
    opacity: 0.6;
    animation: cornerFloat 4s ease-in-out infinite;
}
@keyframes cornerFloat {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(10deg); }
}


/* Confetti burst */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    background: #ff6b6b;
    animation: confettiFall 3s linear infinite;
}
@keyframes confettiFall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
}


/* Bouncing elements */
.bounce {
    animation: bounce 2s ease-in-out infinite;
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}


/* Spin animation */
.spin {
    animation: spin 8s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}


/* Pulse glow */
.pulse-glow {
    animation: pulseGlow 2s ease-in-out infinite;
}
@keyframes pulseGlow {
    0%, 100% { filter: drop-shadow(0 0 10px rgba(255, 165, 2, 0.5)); }
    50% { filter: drop-shadow(0 0 25px rgba(255, 165, 2, 0.8)); }
}


/* Button styling for better visibility */
.stButton > button {
    background: linear-gradient(135deg, #ff6b6b, #ffa502) !important;
    color: white !important;
    font-weight: 700 !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #ff8787, #ffb84d) !important;
    box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6) !important;
    transform: translateY(-2px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}


@media (max-width: 700px) {
    .memory-grid { grid-template-columns: 1fr; }
    .hero { padding-top: 25px; }
}
</style>
""", unsafe_allow_html=True)


# Corner decorations
corner_items = ["🎈", "🎊", "🌟", "✨"]
corner_positions = [
    {"top": "20px", "left": "20px"},
    {"top": "20px", "right": "20px"},
    {"bottom": "80px", "left": "20px"},
    {"bottom": "80px", "right": "20px"},
]
for item, pos in zip(corner_items, corner_positions):
    style = ";".join([f"{k}:{v}" for k, v in pos.items()])
    st.markdown(f'<div class="corner-decoration" style="{style};">{item}</div>', unsafe_allow_html=True)


# Floating decorative elements (increased quantity)
decorations = ["🎉", "✨", "🎈", "🌟", "🎊", "🦄", "⭐", "🌈", "🎁", "🍀", "🎂", "🧁", "🎪", "🎯", "🎨"]
for i, item in enumerate(decorations):
    left = random.randint(3, 95)
    duration = random.randint(9, 18)
    delay = random.randint(0, 8)
    size = random.randint(18, 34)
    st.markdown(
        f'<div class="floating" style="left:{left}%;font-size:{size}px;animation-duration:{duration}s;animation-delay:-{delay}s;">{item}</div>',
        unsafe_allow_html=True
    )


# Twinkling stars
stars = ["⭐", "✨", "🌟"]
for i, star in enumerate(stars):
    left = random.randint(10, 90)
    top = random.randint(10, 80)
    delay = random.randint(0, 2)
    size = random.randint(14, 22)
    st.markdown(
        f'<div class="twinkle" style="left:{left}%;top:{top}%;font-size:{size}px;animation-delay:-{delay}s;">{star}</div>',
        unsafe_allow_html=True
    )


# Hero
st.markdown(f"""
<div class="hero">
    <div class="sparkles bounce">✨ 🎉 ✨</div>
    <div class="small-label">A little birthday surprise made for you</div>
    <h1>Happy Birthday,<br>{FRIEND_NAME}! 🎂</h1>
    <p>Today is officially a <b>you deserve all the happiness</b> kind of day.</p>
</div>
""", unsafe_allow_html=True)


# Celebration controls
c1, c2, c3 = st.columns([1, 1.4, 1])
with c2:
    if st.button("🎊 LET'S CELEBRATE! 🎊", use_container_width=True):
        st.balloons()
        st.toast("✨ Birthday magic activated! ✨", icon="🎉")
        time.sleep(0.2)


st.markdown('<div class="birthday-cake pulse-glow">🎂</div>', unsafe_allow_html=True)


# Message
st.markdown(f"""
<div class="card">
    <h2>📝 A Birthday Message</h2>
    <div class="message">
        Hey <b>{FRIEND_NAME}</b>! <span class="star">🌟</span><br><br>
        Happy birthday! I hope this new chapter brings you so many reasons
        to smile, laugh until your stomach hurts, discover new things,
        and make memories you'll want to keep forever.
        <br><br>
        You deserve a day filled with good food, great people,
        beautiful surprises, and absolutely <b>zero stress</b>.
        🌈✨
        <br><br>
        Keep being your wonderful self, keep chasing the things that make
        you happy, and don't forget that there are people cheering for you.
        Today, tomorrow, and all the days after. 🎉
    </div>
</div>
""", unsafe_allow_html=True)


# Fun facts / memories
st.markdown("""
<div class="card">
    <h2>🌟 The Birthday Vibe</h2>
    <div class="memory-grid">
        <div class="memory m1"><span style="font-size:2rem">😂</span><b>More laughs</b><small>Because life needs more ridiculous moments.</small></div>
        <div class="memory m2"><span style="font-size:2rem">🌍</span><b>More adventures</b><small>New places, new memories, new stories.</small></div>
        <div class="memory m3"><span style="font-size:2rem">📈</span><b>More growth</b><small>Keep becoming the person you want to be.</small></div>
        <div class="memory m4"><span style="font-size:2rem">☀️</span><b>More happiness</b><small>The kind that appears in tiny everyday moments.</small></div>
        <div class="memory m5"><span style="font-size:2rem">🍰</span><b>More cake</b><small>This one is non-negotiable.</small></div>
        <div class="memory m6"><span style="font-size:2rem">🎉</span><b>More good times</b><small>With the people who care about you.</small></div>
    </div>
</div>
""", unsafe_allow_html=True)


# Interactive wish generator
st.markdown("""
<div class="card">
    <h2>🔮 Pick Your Birthday Wish</h2>
    <p class="message">Click the button and let the birthday universe choose one for you.</p>
</div>
""", unsafe_allow_html=True)


wishes = [
    "🌸 May this year surprise you in the best possible ways.",
    "✨ May you meet opportunities that feel like they were made for you.",
    "🎉 May you have more peaceful days and unforgettable nights.",
    "🦋 May you grow without losing the things that make you, YOU.",
    "🌈 May your next chapter be brighter than you imagined.",
    "🎂 May something you've secretly wished for finally happen.",
    "⭐ May you always have a reason to look forward to tomorrow.",
]


if st.button("🎁 Reveal My Birthday Wish", use_container_width=True):
    st.session_state["wish"] = random.choice(wishes)
    st.balloons()


if "wish" in st.session_state:
    st.markdown(
        f'<div class="wish"><div class="wish-big">{st.session_state["wish"]}</div></div>',
        unsafe_allow_html=True
    )


# Secret button
st.markdown("""
<div class="card">
    <h2>🤫 Psst... There's One More Thing</h2>
</div>
""", unsafe_allow_html=True)


if st.button("💫 Open the Secret Message", use_container_width=True):
    st.success(
        f"Whatever happens this year, remember: you are more appreciated than you probably realize. "
        f"Happy birthday, {FRIEND_NAME}! 🎉🎂✨"
    )
    st.balloons()


st.markdown(f"""
<div class="footer">
    Made with 🎉 by {YOUR_NAME} · Hope you have an awesome birthday! 🎂
</div>
""", unsafe_allow_html=True)