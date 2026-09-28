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


# Initialize session state
if "confetti_clicked" not in st.session_state:
    st.session_state["confetti_clicked"] = 0
if "trivia_score" not in st.session_state:
    st.session_state["trivia_score"] = 0
if "trivia_shown" not in st.session_state:
    st.session_state["trivia_shown"] = False


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
}


.hero p {
    font-size: 1.3rem;
    color: #5a6b7c;
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
    box-shadow: 0 18px 45px rgba(100, 120, 140, .13);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 28px;
    margin: 18px 0;
}


.card h2 {
    color: #4a6fa5;
    margin-top: 0;
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
    box-shadow: 0 12px 25px rgba(80,100,120,.13);
    transition: transform .25s ease;
}
.memory:hover {
    transform: translateY(-8px) rotate(1deg);
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
}


.wish-big {
    font-family: 'Pacifico', cursive;
    font-size: 2.2rem;
    color: #ff8c42;
}


.footer {
    text-align:center;
    color:#6b7280;
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


/* Gallery styles */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
}
.gallery-item {
    background: white;
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0,0,0,.08);
    transition: all .3s ease;
    cursor: pointer;
}
.gallery-item:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 14px 30px rgba(0,0,0,.15);
}
.gallery-emoji {
    font-size: 3rem;
    display: block;
    margin-bottom: 8px;
}
.gallery-text {
    font-size: 0.95rem;
    color: #5a6b7c;
    font-weight: 600;
}


/* Trivia styles */
.trivia-container {
    background: linear-gradient(135deg, #fff5e6, #e6f3ff);
    border-radius: 24px;
    padding: 24px;
    margin: 16px 0;
}
.trivia-question {
    font-size: 1.2rem;
    font-weight: 700;
    color: #4a6fa5;
    margin-bottom: 16px;
}
.trivia-options button {
    margin: 6px 4px;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: 600;
}


/* Time capsule */
.capsule {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border-radius: 26px;
    padding: 32px;
    text-align: center;
}
.capsule-title {
    font-family: 'Pacifico', cursive;
    font-size: 2rem;
    margin-bottom: 16px;
}
.capsule-message {
    font-size: 1.15rem;
    line-height: 1.7;
    opacity: .95;
}


/* Playlist */
.playlist-item {
    background: white;
    border-left: 5px solid #ff6b6b;
    border-radius: 14px;
    padding: 16px 20px;
    margin: 10px 0;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,.06);
}
.playlist-emoji {
    font-size: 2rem;
}
.playlist-info {
    flex: 1;
}
.playlist-title {
    font-weight: 700;
    color: #4a6fa5;
    font-size: 1.05rem;
}
.playlist-artist {
    color: #718096;
    font-size: 0.9rem;
}


@media (max-width: 700px) {
    .memory-grid, .gallery-grid { grid-template-columns: 1fr; }
    .hero { padding-top: 25px; }
    .playlist-item { flex-direction: column; text-align: center; }
}
</style>
""", unsafe_allow_html=True)


# Floating decorative elements
decorations = ["🎉", "✨", "🎈", "🌟", "🎊", "🦄", "⭐", "🌈", "🎁", "🍀"]
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
    <div class="sparkles">✨ 🎉 ✨</div>
    <div class="small-label">A little birthday surprise made for you</div>
    <h1>Happy Birthday,<br>{FRIEND_NAME}! 🎂</h1>
    <p>Today is officially a <b>you deserve all the happiness</b> kind of day.</p>
</div>
""", unsafe_allow_html=True)


# Celebration controls
c1, c2, c3 = st.columns([1, 1.4, 1])
with c2:
    if st.button("🎊 LET'S CELEBRATE! 🎊", use_container_width=True):
        st.session_state["confetti_clicked"] += 1
        st.balloons()
        st.toast(f"✨ Birthday magic activated! ({st.session_state['confetti_clicked']}x) ✨", icon="🎉")
        time.sleep(0.2)


st.markdown('<div class="birthday-cake">🎂</div>', unsafe_allow_html=True)


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


# NEW: Memory Gallery
st.markdown(f"""
<div class="card">
    <h2>📸 Memory Lane</h2>
    <p class="message">Some moments that make you, YOU! Hover over each one.</p>
</div>
""", unsafe_allow_html=True)

gallery_items = [
    ("🎮", "That time we laughed way too hard"),
    ("🍕", "Food adventures together"),
    ("🎵", "Sing-it-out-loud moments"),
    ("✈️", "Adventure awaits"),
    ("📚", "Learning something new"),
    ("🌙", "Late night conversations"),
]

cols = st.columns(3)
for idx, item in enumerate(gallery_items):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="gallery-item">
            <span class="gallery-emoji">{item[0]}</span>
            <span class="gallery-text">{item[1]}</span>
        </div>
        """, unsafe_allow_html=True)


# NEW: Birthday Trivia Quiz
st.markdown(f"""
<div class="card">
    <h2>🧠 How Well Do You Know {FRIEND_NAME}?</h2>
    <p class="message">Let's test your birthday knowledge! (Just for fun!)</p>
</div>
""", unsafe_allow_html=True)

trivia_questions = [
    {
        "question": "What's {FRIEND_NAME}'s favorite way to spend a weekend?".replace("{FRIEND_NAME}", FRIEND_NAME),
        "options": ["Sleeping in", "Going on adventures", "Binge-watching shows", "All of the above"],
        "answer": 3
    },
    {
        "question": "If {FRIEND_NAME} could eat one food forever, it would be:".replace("{FRIEND_NAME}", FRIEND_NAME),
        "options": ["Pizza", "Tacos", "Sushi", "Something sweet"],
        "answer": 0
    },
    {
        "question": "{FRIEND_NAME}'s superpower is:".replace("{FRIEND_NAME}", FRIEND_NAME),
        "options": ["Making people laugh", "Being ridiculously kind", "Finding the best snacks", "All of the above"],
        "answer": 3
    },
]

if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0
    st.session_state["trivia_score"] = 0
    st.session_state["trivia_complete"] = False

if not st.session_state.get("trivia_complete", False):
    q = trivia_questions[st.session_state["current_question"]]
    
    st.markdown(f"""
    <div class="trivia-container">
        <div class="trivia-question">Question {st.session_state["current_question"] + 1}: {q["question"]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(4)
    for idx, option in enumerate(q["options"]):
        with cols[idx]:
            if st.button(option, key=f"q{st.session_state['current_question']}_opt{idx}", use_container_width=True):
                if idx == q["answer"]:
                    st.session_state["trivia_score"] += 1
                    st.success("🎉 Correct!")
                else:
                    st.info(f"Nice try! The answer was: {q['options'][q['answer']]}")
                
                st.session_state["current_question"] += 1
                if st.session_state["current_question"] >= len(trivia_questions):
                    st.session_state["trivia_complete"] = True
                    st.balloons()
                st.rerun()
else:
    score = st.session_state["trivia_score"]
    total = len(trivia_questions)
    
    if score == total:
        message = f"🏆 Perfect score! You really know {FRIEND_NAME}!"
    elif score >= total // 2:
        message = f"🎉 Not bad! You know {FRIEND_NAME} pretty well!"
    else:
        message = f"😄 Time to hang out with {FRIEND_NAME} more!"
    
    st.success(f"{message} Score: {score}/{total}")
    
    if st.button("🔄 Play Again"):
        st.session_state["current_question"] = 0
        st.session_state["trivia_score"] = 0
        st.session_state["trivia_complete"] = False
        st.rerun()


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


# NEW: Time Capsule Message
st.markdown(f"""
<div class="card">
    <h2>⏰ Your Birthday Time Capsule</h2>
    <p class="message">A message from the future... open when you're ready!</p>
</div>
""", unsafe_allow_html=True)

if st.button("📦 Open Time Capsule", use_container_width=True):
    st.markdown(f"""
    <div class="capsule">
        <div class="capsule-title">Dear {FRIEND_NAME},</div>
        <div class="capsule-message">
            Hey! It's future-you checking in. Just wanted to remind you that:<br><br>
            ✨ You're doing better than you think<br>
            🌟 The things you're working on now will pay off<br>
            💫 You have people who believe in you (like me!)<br>
            🎉 Keep going - great things are coming your way<br><br>
            P.S. Don't forget to enjoy the little moments along the journey. 💕
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()


# NEW: Birthday Playlist
st.markdown(f"""
<div class="card">
    <h2>🎵 Birthday Vibes Playlist</h2>
    <p class="message">Some songs to get you in the birthday mood!</p>
</div>
""", unsafe_allow_html=True)

playlist = [
    ("🎉", "Happy", "Pharrell Williams", "Because it's YOUR day!"),
    ("✨", "Good as Hell", "Lizzo", "You're doing amazing!"),
    ("🌟", "Unwritten", "Natasha Bedingfield", "Your story is just beginning"),
    ("🦋", "Brave", "Sara Bareilles", "Keep being your authentic self"),
    ("🌈", "Here Comes the Sun", "The Beatles", "Brighter days ahead"),
]

for emoji, title, artist, note in playlist:
    st.markdown(f"""
    <div class="playlist-item">
        <span class="playlist-emoji">{emoji}</span>
        <div class="playlist-info">
            <div class="playlist-title">{title}</div>
            <div class="playlist-artist">{artist} · {note}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


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