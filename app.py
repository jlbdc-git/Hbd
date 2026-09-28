
import streamlit as st
import random
import time

st.set_page_config(
    page_title="A Little Birthday Surprise 🎀",
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
        radial-gradient(circle at 10% 10%, rgba(255, 182, 193, .35), transparent 25%),
        radial-gradient(circle at 90% 15%, rgba(173, 216, 230, .30), transparent 25%),
        radial-gradient(circle at 50% 90%, rgba(255, 223, 128, .28), transparent 30%),
        linear-gradient(135deg, #fff4fb 0%, #f5f0ff 45%, #effbff 100%);
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
    color: #c15c91;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-size: 0.9rem;
}

.hero h1 {
    font-family: 'Pacifico', cursive;
    font-size: clamp(3.2rem, 9vw, 7rem);
    line-height: 1.05;
    margin: 10px 0;
    background: linear-gradient(90deg, #ff5f9e, #a56cff, #48b9ff, #ff77bd);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 5s ease infinite;
}

.hero p {
    font-size: 1.3rem;
    color: #715d72;
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
    from { opacity: .45; transform: scale(.96); }
    to { opacity: 1; transform: scale(1.05); }
}

.card {
    background: rgba(255,255,255,.72);
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 18px 45px rgba(111, 79, 120, .13);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 28px;
    margin: 18px 0;
}

.card h2 {
    color: #8b4d83;
    margin-top: 0;
}

.message {
    font-size: 1.15rem;
    line-height: 1.8;
    color: #594b5d;
}

.birthday-cake {
    text-align: center;
    font-size: 7rem;
    filter: drop-shadow(0 15px 20px rgba(255, 100, 170, .2));
    animation: cakeFloat 3s ease-in-out infinite;
}
@keyframes cakeFloat {
    0%,100% { transform: translateY(0) rotate(-1deg); }
    50% { transform: translateY(-12px) rotate(1deg); }
}

.heart {
    display: inline-block;
    animation: heartBeat 1.5s infinite;
}
@keyframes heartBeat {
    0%, 40%, 100% { transform: scale(1); }
    20% { transform: scale(1.22); }
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
    box-shadow: 0 12px 25px rgba(80,60,100,.13);
    transition: transform .25s ease;
}
.memory:hover {
    transform: translateY(-8px) rotate(1deg);
}
.m1 { background: linear-gradient(135deg,#ff80ab,#ffb36b); }
.m2 { background: linear-gradient(135deg,#9b7cff,#d785ff); }
.m3 { background: linear-gradient(135deg,#48c6ef,#6f86d6); }
.m4 { background: linear-gradient(135deg,#52d69a,#49b8b1); }
.m5 { background: linear-gradient(135deg,#ffcf5c,#ff8a8a); }
.m6 { background: linear-gradient(135deg,#f78fb3,#9b59b6); }

.wish {
    text-align:center;
    background: linear-gradient(135deg, rgba(255,227,242,.85), rgba(226,236,255,.85));
    border-radius: 30px;
    padding: 35px 25px;
}

.wish-big {
    font-family: 'Pacifico', cursive;
    font-size: 2.2rem;
    color: #a85a92;
}

.footer {
    text-align:center;
    color:#9a8299;
    padding: 35px 0 10px;
    font-size: .95rem;
}

.floating {
    position: fixed;
    pointer-events: none;
    z-index: 0;
    animation: floatUp linear infinite;
    opacity: .7;
}
@keyframes floatUp {
    0% { transform: translateY(110vh) rotate(0deg); opacity:0; }
    15% { opacity:.75; }
    85% { opacity:.75; }
    100% { transform: translateY(-15vh) rotate(360deg); opacity:0; }
}

@media (max-width: 700px) {
    .memory-grid { grid-template-columns: 1fr; }
    .hero { padding-top: 25px; }
}
</style>
""", unsafe_allow_html=True)

# Floating decorative elements
decorations = ["💖", "✨", "🌸", "🎀", "💗", "🌷", "⭐", "🦋", "💕", "🌈"]
for i, item in enumerate(decorations):
    left = random.randint(3, 95)
    duration = random.randint(9, 18)
    delay = random.randint(0, 8)
    size = random.randint(18, 34)
    st.markdown(
        f'<div class="floating" style="left:{left}%;font-size:{size}px;animation-duration:{duration}s;animation-delay:-{delay}s;">{item}</div>',
        unsafe_allow_html=True
    )

# Hero
st.markdown(f"""
<div class="hero">
    <div class="sparkles">✨ 💕 ✨</div>
    <div class="small-label">A tiny surprise made just for you</div>
    <h1>Happy Birthday,<br>{FRIEND_NAME}! 🎀</h1>
    <p>Today is officially a <b>you deserve all the happiness</b> kind of day.</p>
</div>
""", unsafe_allow_html=True)

# Celebration controls
c1, c2, c3 = st.columns([1, 1.4, 1])
with c2:
    if st.button("🎉 LET'S CELEBRATE! 🎉", use_container_width=True):
        st.balloons()
        st.toast("✨ Birthday magic activated! ✨", icon="🎀")
        time.sleep(0.2)

st.markdown('<div class="birthday-cake">🎂</div>', unsafe_allow_html=True)

# Message
st.markdown(f"""
<div class="card">
    <h2>💌 A Little Birthday Message</h2>
    <div class="message">
        Hey <b>{FRIEND_NAME}</b>! <span class="heart">💗</span><br><br>
        Happy birthday! I hope this new chapter brings you so many reasons
        to smile, laugh until your stomach hurts, discover new things,
        and make memories you'll want to keep forever.
        <br><br>
        You deserve a day filled with good food, great people,
        beautiful surprises, and absolutely <b>zero stress</b>.
        🌷✨
        <br><br>
        Keep being your wonderful self, keep chasing the things that make
        you happy, and don't forget that there are people cheering for you.
        Today, tomorrow, and all the days after. 💕
    </div>
</div>
""", unsafe_allow_html=True)

# Fun facts / memories
st.markdown("""
<div class="card">
    <h2>🌸 The Birthday Vibe</h2>
    <div class="memory-grid">
        <div class="memory m1"><span style="font-size:2rem">😂</span><b>More laughs</b><small>Because life needs more ridiculous moments.</small></div>
        <div class="memory m2"><span style="font-size:2rem">🌟</span><b>More adventures</b><small>New places, new memories, new stories.</small></div>
        <div class="memory m3"><span style="font-size:2rem">🦋</span><b>More growth</b><small>Keep becoming the person you want to be.</small></div>
        <div class="memory m4"><span style="font-size:2rem">🌷</span><b>More happiness</b><small>The kind that appears in tiny everyday moments.</small></div>
        <div class="memory m5"><span style="font-size:2rem">🍰</span><b>More cake</b><small>This one is non-negotiable.</small></div>
        <div class="memory m6"><span style="font-size:2rem">💖</span><b>More love</b><small>From the people who genuinely care about you.</small></div>
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
    "💗 May you have more peaceful days and unforgettable nights.",
    "🦋 May you grow without losing the things that make you, YOU.",
    "🌈 May your next chapter be brighter than you imagined.",
    "🎀 May something you've secretly wished for finally happen.",
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

if st.button("💝 Open the Secret Message", use_container_width=True):
    st.success(
        f"Whatever happens this year, remember: you are more appreciated than you probably realize. "
        f"Happy birthday, {FRIEND_NAME}! 💕🎂✨"
    )
    st.balloons()

st.markdown(f"""
<div class="footer">
    Made with 💗 by {YOUR_NAME} · For one very special birthday girl 🎀
</div>
""", unsafe_allow_html=True)
