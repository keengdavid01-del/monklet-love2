import streamlit as st
import time
import random

st.set_page_config(page_title="Love for Monklet 💖", page_icon="💌", layout="wide")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 25%, #ffdde1 50%, #ffe6f9 75%, #fff0f5 100%);
    background-attachment: fixed;
    overflow: hidden;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(255, 255, 255, 0);
}
.typing {
    font-size: 32px;
    color: #fff;
    text-align: center;
    text-shadow: 0 0 25px #ff69b4, 0 0 40px #ff1493;
    white-space: pre-wrap;
    min-height: 120px;
    font-weight: bold;
}
.heart {
    font-size: 90px;
    text-align: center;
    animation: pulse 1.2s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); color: #ff66b2; }
    50% { transform: scale(1.3); color: #ff1493; }
    100% { transform: scale(1); color: #ff66b2; }
}
.rainbow {
    text-align: center;
    font-size: 45px;
    background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s infinite alternate;
    font-weight: bold;
}
@keyframes glow {
    0% { text-shadow: 0 0 20px #ff69b4; }
    100% { text-shadow: 0 0 40px #ff1493; }
}
h1 {
    text-align: center;
    color: #fff !important;
    text-shadow: 0 0 25px #ff69b4, 0 0 40px #ff1493;
    font-size: 50px !important;
    margin-top: 30px;
}
.floating-heart {
    position: fixed;
    font-size: 25px;
    animation: floatUp linear infinite;
    opacity: 0.8;
    z-index: 1;
}
@keyframes floatUp {
    0% { transform: translateY(100vh) scale(1); opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
}
.fade-in {
    animation: fadeIn 2s ease-in forwards;
    opacity: 0;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
"""

hearts_html = ""
for i in range(20):
    left = random.randint(0, 100)
    delay = round(random.uniform(0, 10), 1)
    duration = random.randint(8, 18)
    color = random.choice(["#ffb6c1", "#ff69b4", "#ff1493", "#ffc0cb"])
    hearts_html += f"<div class='floating-heart' style='left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s; color:{color};'>💖</div>"

st.markdown(page_bg + hearts_html, unsafe_allow_html=True)
st.markdown("<h1>💖 Love Program for My Monklet 💖</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.5, 2, 1.5])

left_video_url = "https://github.com/keengdavid01-del/monklet-love2/blob/main/left_clip.mp4"
right_video_url = "https://github.com/keengdavid01-del/monklet-love2/blob/main/right_clip.mp4"

left_video_html = f"""
<video autoplay loop playsinline class="fade-in" style="width:100%; border-radius:20px; box-shadow:0 0 25px #ff69b4;" controls>
  <source src="{left_video_url}" type="video/mp4">
</video>
"""

right_video_html = f"""
<video autoplay loop playsinline class="fade-in" style="width:100%; border-radius:20px; box-shadow:0 0 25px #ff69b4;" controls>
  <source src="{right_video_url}" type="video/mp4">
</video>
"""

with col1:
    st.markdown(left_video_html, unsafe_allow_html=True)

with col3:
    st.markdown(right_video_html, unsafe_allow_html=True)

with col2:
    placeholder = st.empty()
    def type_text(text, speed=0.035):
        typed = ""
        for char in text:
            typed += char
            placeholder.markdown(f"<div class='typing'>{typed}</div>", unsafe_allow_html=True)
            time.sleep(speed + random.uniform(0,0.015))
        time.sleep(0.6)

    messages = [
        "Hey Baby 💕",
        "I made this little program because words aren’t enough...",
        "to tell you how much you mean to me 💖",
        "",
        "You make my life beautiful, you make me feel like a child",
        "and every day brighter just by being you 🌷",
        "",
        "So if you ever forget how loved you are...",
        "just open this again 😌",
        "",
        "With all my love,",
        "💞 Your favorite Hubby 💞"
    ]

    for msg in messages:
        type_text(msg)

    time.sleep(1)
    placeholder.markdown("<div class='rainbow'>🌈 Switching to Rainbow Mode 🌈</div>", unsafe_allow_html=True)
    time.sleep(2)

    heart_placeholder = st.empty()
    for _ in range(8):
        heart_placeholder.markdown("<div class='heart'>💗</div>", unsafe_allow_html=True)
        time.sleep(0.4)
        heart_placeholder.markdown("<div class='heart'>💖</div>", unsafe_allow_html=True)
        time.sleep(0.4)

    heart_placeholder.markdown("<div class='rainbow'>I ❤️ My Monklet</div>", unsafe_allow_html=True)
    time.sleep(2)

    st.markdown("<h2 style='text-align:center; color:#fff; text-shadow:0 0 20px #ff1493;'>💌 End of Love Transmission 💌</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#fff; text-shadow:0 0 20px #ff69b4;'>Forever yours — the Hubby who loves his Monklet 💞</h3>", unsafe_allow_html=True)
