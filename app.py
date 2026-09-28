import random
import time

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Happy Birthday Shaznay! 🎂",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PERSONALIZATION
# ============================================================

FRIEND_NAME = "Shaznay"
YOUR_NAME = "BM"

def render_html(html: str):
    """Render trusted HTML/CSS through Streamlit."""
    st.markdown(html, unsafe_allow_html=True)



# ============================================================
# CUSTOM CSS
# ============================================================

render_html(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Pacifico&display=swap');

    html, body, [class*="css"] {
        font-family: "Baloo 2", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 182, 193, 0.38),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(173, 216, 230, 0.32),
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(255, 223, 128, 0.30),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff4fb 0%,
                #f7f0ff 45%,
                #eefaff 100%
            );

        overflow-x: hidden;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }


    /* HERO */

    .hero {
        text-align: center;
        padding: 55px 20px 30px;
    }

    .small-label {
        color: #c15c91;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-size: 0.9rem;
    }

    .hero h1 {
        font-family: "Pacifico", cursive;
        font-size: clamp(3.2rem, 9vw, 7rem);
        line-height: 1.05;
        margin: 10px 0;

        background:
            linear-gradient(
                90deg,
                #ff5f9e,
                #a56cff,
                #48b9ff,
                #ff77bd
            );

        background-size: 300% 300%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation: gradientMove 5s ease infinite;
    }

    .hero p {
        font-size: 1.3rem;
        color: #715d72;
    }


    /* GRADIENT ANIMATION */

    @keyframes gradientMove {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }

    }


    /* SPARKLES */

    .sparkles {
        font-size: 2rem;
        letter-spacing: 18px;
        animation: sparkle 2s ease-in-out infinite alternate;
    }

    @keyframes sparkle {

        from {
            opacity: 0.45;
            transform: scale(0.96);
        }

        to {
            opacity: 1;
            transform: scale(1.05);
        }

    }


    /* CARDS */

    .card {
        background: rgba(255, 255, 255, 0.74);

        border: 1px solid rgba(255, 255, 255, 0.9);

        box-shadow:
            0 18px 45px rgba(111, 79, 120, 0.13);

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


    /* CAKE */

    .birthday-cake {
        text-align: center;
        font-size: 7rem;

        filter:
            drop-shadow(
                0 15px 20px rgba(255, 100, 170, 0.20)
            );

        animation: cakeFloat 3s ease-in-out infinite;
    }

    @keyframes cakeFloat {

        0%,
        100% {
            transform:
                translateY(0)
                rotate(-1deg);
        }

        50% {
            transform:
                translateY(-12px)
                rotate(1deg);
        }

    }


    /* FLOATING DECORATIONS */

    .floating {
        position: fixed;
        pointer-events: none;
        z-index: 0;

        animation:
            floatUp
            linear
            infinite;

        opacity: 0.7;
    }

    @keyframes floatUp {

        0% {
            transform:
                translateY(110vh)
                rotate(0deg);

            opacity: 0;
        }

        15% {
            opacity: 0.75;
        }

        85% {
            opacity: 0.75;
        }

        100% {
            transform:
                translateY(-15vh)
                rotate(360deg);

            opacity: 0;
        }

    }


    /* BIRTHDAY STATUS */

    .status-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-top: 20px;
    }

    .status {
        padding: 20px;
        border-radius: 20px;

        text-align: center;
        color: white;

        box-shadow:
            0 10px 25px rgba(80, 60, 100, 0.12);

        transition:
            transform 0.25s ease;
    }

    .status:hover {
        transform:
            translateY(-7px)
            rotate(1deg);
    }

    .status-icon {
        font-size: 2rem;
    }

    .status-title {
        font-weight: 800;
        font-size: 1.1rem;
    }

    .status-text {
        font-size: 0.9rem;
    }

    .s1 {
        background:
            linear-gradient(
                135deg,
                #ff80ab,
                #ffb36b
            );
    }

    .s2 {
        background:
            linear-gradient(
                135deg,
                #9b7cff,
                #d785ff
            );
    }

    .s3 {
        background:
            linear-gradient(
                135deg,
                #48c6ef,
                #6f86d6
            );
    }

    .s4 {
        background:
            linear-gradient(
                135deg,
                #52d69a,
                #49b8b1
            );
    }


    /* BIRTHDAY OBJECTIVES */

    .memory-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }

    .memory {
        min-height: 140px;

        border-radius: 22px;

        padding: 20px;

        color: white;

        display: flex;
        flex-direction: column;
        justify-content: flex-end;

        box-shadow:
            0 12px 25px rgba(80, 60, 100, 0.13);

        transition:
            transform 0.25s ease;
    }

    .memory:hover {
        transform:
            translateY(-8px)
            rotate(1deg);
    }

    .memory-icon {
        font-size: 2.2rem;
        margin-bottom: 5px;
    }

    .memory-title {
        font-weight: 800;
        font-size: 1.2rem;
    }

    .memory-text {
        font-size: 0.9rem;
    }

    .m1 {
        background:
            linear-gradient(
                135deg,
                #ff80ab,
                #ffb36b
            );
    }

    .m2 {
        background:
            linear-gradient(
                135deg,
                #9b7cff,
                #d785ff
            );
    }

    .m3 {
        background:
            linear-gradient(
                135deg,
                #48c6ef,
                #6f86d6
            );
    }

    .m4 {
        background:
            linear-gradient(
                135deg,
                #52d69a,
                #49b8b1
            );
    }

    .m5 {
        background:
            linear-gradient(
                135deg,
                #ffcf5c,
                #ff8a8a
            );
    }

    .m6 {
        background:
            linear-gradient(
                135deg,
                #f78fb3,
                #9b59b6
            );
    }


    /* WISH */

    .wish {
        text-align: center;

        background:
            linear-gradient(
                135deg,
                rgba(255, 227, 242, 0.90),
                rgba(226, 236, 255, 0.90)
            );

        border-radius: 30px;

        padding: 35px 25px;

        margin-top: 20px;

        box-shadow:
            0 15px 35px rgba(100, 80, 120, 0.10);
    }

    .wish-big {
        font-family: "Pacifico", cursive;
        font-size: 2.2rem;
        color: #a85a92;
    }


    /* FINAL MESSAGE */

    .final-message {
        text-align: center;

        padding: 45px 25px;

        border-radius: 35px;

        background:
            linear-gradient(
                135deg,
                #ffe3f1,
                #e8e0ff,
                #dff6ff
            );

        box-shadow:
            0 20px 45px rgba(100, 80, 120, 0.12);
    }

    .final-message h2 {
        font-family: "Pacifico", cursive;
        font-size: 2.7rem;
        color: #9b568f;
    }

    .final-message p {
        font-size: 1.15rem;
        color: #66556b;
        line-height: 1.8;
    }


    /* FOOTER */

    .footer {
        text-align: center;
        color: #9a8299;

        padding:
            35px 0 10px;

        font-size: 0.95rem;
    }


    /* MOBILE */

    @media (max-width: 700px) {

        .memory-grid {
            grid-template-columns: 1fr;
        }

        .status-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .hero {
            padding-top: 25px;
        }

    }

    </style>
    """
)


# ============================================================
# FLOATING DECORATIONS
# ============================================================

decorations = [
    "✨",
    "🌸",
    "🎀",
    "⭐",
    "🌷",
    "🦋",
    "🌈",
    "🎈",
    "🍰",
    "🎉",
]

for item in decorations:

    left = random.randint(3, 95)
    duration = random.randint(9, 18)
    delay = random.randint(0, 8)
    size = random.randint(18, 34)

    render_html(
        f"""
        <div
            class="floating"
            style="
                left: {left}%;
                font-size: {size}px;
                animation-duration: {duration}s;
                animation-delay: -{delay}s;
            "
        >
            {item}
        </div>
        """,
            )


# ============================================================
# HERO
# ============================================================

render_html(
    f"""
    <div class="hero">

        <div class="sparkles">
            ✨ 🎀 ✨
        </div>

        <div class="small-label">
            OFFICIAL BIRTHDAY NOTICE
        </div>

        <h1>
            Happy Birthday,<br>
            {FRIEND_NAME}! 🎂
        </h1>

        <p>
            Congratulations on successfully unlocking
            another year of life! 😂🎉
        </p>

    </div>
    """
)


# ============================================================
# CELEBRATION BUTTON
# ============================================================

column_1, column_2, column_3 = st.columns([1, 1.4, 1])

with column_2:

    if st.button(
        "🎉 LET'S CELEBRATE! 🎉",
        use_container_width=True,
    ):

        st.balloons()

        st.toast(
            "🎀 Birthday mode activated!",
            icon="🎉",
        )

        time.sleep(0.2)


# ============================================================
# CAKE
# ============================================================

render_html(
    '<div class="birthday-cake">🎂</div>'
)


# ============================================================
# BIRTHDAY STATUS
# ============================================================

render_html(
    """
    <div class="card">

        <h2>
            🎮 Birthday Status
        </h2>

        <div class="status-grid">

            <div class="status s1">
                <div class="status-icon">🎂</div>
                <div class="status-title">
                    Cake
                </div>
                <div class="status-text">
                    REQUIRED
                </div>
            </div>

            <div class="status s2">
                <div class="status-icon">😂</div>
                <div class="status-title">
                    Laughs
                </div>
                <div class="status-text">
                    MAXIMUM
                </div>
            </div>

            <div class="status s3">
                <div class="status-icon">😎</div>
                <div class="status-title">
                    Stress
                </div>
                <div class="status-text">
                    DISABLED
                </div>
            </div>

            <div class="status s4">
                <div class="status-icon">🎉</div>
                <div class="status-title">
                    Birthday Energy
                </div>
                <div class="status-text">
                    100%
                </div>
            </div>

        </div>

    </div>
    """
)


# ============================================================
# BIRTHDAY MESSAGE
# ============================================================

render_html(
    f"""
    <div class="card">

        <h2>
            🎀 A Message From {YOUR_NAME}
        </h2>

        <div class="message">

            Hey <b>{FRIEND_NAME}</b>! 😂🎂

            <br><br>

            Happy birthday!

            <br><br>

            Since apparently birthdays are important,
            I decided to make an unnecessarily colorful
            website instead of just saying
            "Happy Birthday" like a normal person. 😂

            <br><br>

            Anyway, I hope you have an awesome day,
            eat something really good,
            get plenty of cake,
            and spend the day doing things that
            actually make you happy.

            <br><br>

            Hopefully this next year brings you
            lots of good experiences, funny memories,
            new adventures, and fewer stressful moments.

            <br><br>

            Enjoy your day, birthday girl! 🎉

        </div>

    </div>
    """
)


# ============================================================
# BIRTHDAY OBJECTIVES
# ============================================================

render_html(
    """
    <div class="card">

        <h2>
            🌈 Birthday Objectives
        </h2>

        <div class="memory-grid">

            <div class="memory m1">

                <div class="memory-icon">
                    😂
                </div>

                <div class="memory-title">
                    Laugh A Lot
                </div>

                <div class="memory-text">
                    Collect as many ridiculous moments
                    as possible.
                </div>

            </div>


            <div class="memory m2">

                <div class="memory-icon">
                    🌟
                </div>

                <div class="memory-title">
                    Try Something New
                </div>

                <div class="memory-text">
                    New experiences make the best stories.
                </div>

            </div>


            <div class="memory m3">

                <div class="memory-icon">
                    🦋
                </div>

                <div class="memory-title">
                    Keep Growing
                </div>

                <div class="memory-text">
                    New year, new experiences,
                    same awesome person.
                </div>

            </div>


            <div class="memory m4">

                <div class="memory-icon">
                    🌷
                </div>

                <div class="memory-title">
                    Enjoy The Little Things
                </div>

                <div class="memory-text">
                    Sometimes random moments become
                    the best memories.
                </div>

            </div>


            <div class="memory m5">

                <div class="memory-icon">
                    🍰
                </div>

                <div class="memory-title">
                    Eat More Cake
                </div>

                <div class="memory-text">
                    This objective is mandatory.
                    There are no exceptions.
                </div>

            </div>


            <div class="memory m6">

                <div class="memory-icon">
                    🎉
                </div>

                <div class="memory-title">
                    Have Fun
                </div>

                <div class="memory-text">
                    Today is officially a
                    no-boring-day zone.
                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# RANDOM BIRTHDAY WISH
# ============================================================

render_html(
    """
    <div class="card">

        <h2>
            🔮 Random Birthday Wish Generator
        </h2>

        <p class="message">
            Click the button and let the completely
            scientifically accurate birthday universe
            choose a wish. 😂
        </p>

    </div>
    """
)


wishes = [
    "🌸 May this year bring you lots of good surprises.",
    "✨ May you discover something that makes you really happy.",
    "🌈 May you have more fun days and fewer stressful ones.",
    "🦋 May you get opportunities that take you somewhere new.",
    "🎀 May your next chapter be full of great memories.",
    "⭐ May something you've been hoping for finally happen.",
    "🎂 May your cake be delicious and your problems be small.",
    "😂 May you have enough funny stories to tell for years.",
    "🎉 May this birthday be the beginning of a really good year.",
]


if st.button(
    "🎁 REVEAL A RANDOM BIRTHDAY WISH",
    use_container_width=True,
):

    st.session_state["wish"] = random.choice(wishes)

    st.balloons()


if "wish" in st.session_state:

    render_html(
        f"""
        <div class="wish">

            <div class="wish-big">
                {st.session_state["wish"]}
            </div>

        </div>
        """,
            )


# ============================================================
# SECRET MESSAGE
# ============================================================

render_html(
    """
    <div class="card">

        <h2>
            🤫 Psst... One More Thing
        </h2>

        <p class="message">
            There may or may not be a completely unnecessary
            secret message hidden behind this button.
        </p>

    </div>
    """
)


if st.button(
    "🎁 OPEN THE SECRET MESSAGE",
    use_container_width=True,
):

    st.success(
        f"""
        🎉 Happy Birthday, {FRIEND_NAME}!

        Hope you have an amazing day,
        enjoy the cake, enjoy the celebrations,
        and have a really good year ahead!

        — {YOUR_NAME} 🎂
        """
    )

    st.balloons()


# ============================================================
# FINAL MESSAGE
# ============================================================

render_html(
    f"""
    <div class="final-message">

        <h2>
            🎀 That's All, {FRIEND_NAME}!
        </h2>

        <p>

            Hopefully this little website
            made your birthday a little more fun. 😂

            <br><br>

            Have an awesome birthday,
            enjoy every bit of it,
            and make some great memories!

            <br><br>

            <b>
                Happy Birthday! 🎂🎉✨
            </b>

        </p>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_html(
    f"""
    <div class="footer">

        Because saying “Happy Birthday” wasn't dramatic enough. 😂🎂

        <br><br>

        For <b>{FRIEND_NAME}</b>'s birthday 🎀

    </div>
    """
)