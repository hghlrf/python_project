import streamlit as st
import time
import random

# 页面配置
st.set_page_config(
    page_title="给梁志清的特别礼物",
    page_icon="🎁",
    layout="centered"
)

# 自定义CSS样式 - 包含更多动效和移动端适配
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&display=swap');

body {
    font-family: 'Noto Serif SC', serif;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

.main-title {
    font-size: 2.5rem;
    text-align: center;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: bold;
    margin: 1rem 0;
    animation: title-pulse 2s infinite alternate;
}

@keyframes title-pulse {
    0% { transform: scale(1); }
    100% { transform: scale(1.05); }
}

.friend-title {
    font-size: 1.2rem;
    text-align: center;
    color: #555;
    margin-bottom: 2rem;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.gift-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 60vh;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    padding: 1rem;
}

.gift-box {
    width: 180px;
    height: 140px;
    background: linear-gradient(45deg, #ff6b6b, #ffa5a5, #ff6b6b, #ffa5a5);
    background-size: 400% 400%;
    animation: gradient 4s ease infinite;
    border: 5px solid #d4af37;
    border-radius: 10px;
    position: relative;
    cursor: pointer;
    transition: all 0.5s ease;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    transform-style: preserve-3d;
    perspective: 1000px;
    margin: 2rem 0;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.gift-box:hover {
    transform: scale(1.1) rotateY(10deg);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    animation: shake 0.5s ease infinite alternate;
}

@keyframes shake {
    0% { transform: scale(1.1) rotateY(0deg); }
    100% { transform: scale(1.15) rotateY(5deg); }
}

.ribbon {
    position: absolute;
    top: -5px;
    left: 50%;
    transform: translateX(-50%);
    width: 25px;
    height: 90px;
    background: #d4af37;
    animation: ribbon-wave 2s infinite ease-in-out;
}

@keyframes ribbon-wave {
    0% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(-5px); }
    100% { transform: translateX(-50%) translateY(0); }
}

.ribbon::before,
.ribbon::after {
    content: "";
    position: absolute;
    top: 0;
    width: 25px;
    height: 25px;
    background: #d4af37;
    border-radius: 50% 50% 0 0;
}

.ribbon::before {
    left: -15px;
    transform: rotate(-45deg);
}

.ribbon::after {
    right: -15px;
    transform: rotate(45deg);
}

.message-container {
    margin: 2rem auto;
    padding: 1.5rem;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    max-width: 90%;
    text-align: center;
    animation: fadeInUp 1s ease-out;
    position: relative;
    overflow: hidden;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.message {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #333;
    animation: color-change-text 10s infinite alternate;
}

@keyframes color-change-text {
    0% { color: #333; }
    25% { color: #ff6b6b; }
    50% { color: #4ecdc4; }
    75% { color: #45b7d1; }
    100% { color: #96ceb4; }
}

.friend-message {
    font-style: italic;
    color: #666;
    margin-top: 1rem;
    font-size: 0.9rem;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.opened-gift {
    animation: open 0.8s forwards;
}

@keyframes open {
    0% { transform: translateY(0) rotate(0); }
    100% { transform: translateY(-100px) rotate(10deg); }
}

.confetti {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: #f00;
    animation: fall 5s linear infinite;
}

@keyframes fall {
    0% { transform: translateY(-100px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}

.surprise-text {
    font-size: 1.8rem;
    font-weight: bold;
    text-align: center;
    margin: 2rem 0;
    color: #d4af37;
    animation: bounce 1s infinite alternate, color-cycle 3s infinite;
}

@keyframes bounce {
    from { transform: translateY(0); }
    to { transform: translateY(-15px); }
}

@keyframes color-cycle {
    0% { color: #d4af37; }
    25% { color: #ff6b6b; }
    50% { color: #4ecdc4; }
    75% { color: #45b7d1; }
    100% { color: #96ceb4; }
}

.floating-element {
    position: absolute;
    font-size: 1.5rem;
    opacity: 0.7;
    animation: float-element 6s ease-in-out infinite;
    z-index: -1;
}

@keyframes float-element {
    0% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
    100% { transform: translateY(0) rotate(360deg); }
}

.button-anim {
    animation: button-pulse 2s infinite;
}

@keyframes button-pulse {
    0% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7); }
    70% { box-shadow: 0 0 0 15px rgba(212, 175, 55, 0); }
    100% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0); }
}

.sparkle {
    position: absolute;
    width: 6px;
    height: 6px;
    background-color: #fff;
    border-radius: 50%;
    animation: sparkle-anim 1.5s ease-out forwards;
    z-index: 10;
}

@keyframes sparkle-anim {
    0% { transform: scale(0); opacity: 1; }
    50% { opacity: 1; }
    100% { transform: scale(1.5); opacity: 0; }
}

.heart {
    position: absolute;
    font-size: 1.2rem;
    animation: float-heart 4s linear infinite;
    color: #ff6b6b;
    z-index: 5;
}

@keyframes float-heart {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
}

.star {
    position: absolute;
    font-size: 1rem;
    animation: twinkle 3s ease-in-out infinite;
    color: #ffd700;
    z-index: 5;
}

@keyframes twinkle {
    0% { opacity: 0.3; transform: scale(0.5); }
    50% { opacity: 1; transform: scale(1.2); }
    100% { opacity: 0.3; transform: scale(0.5); }
}

.content-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* 移动端适配 */
@media (max-width: 768px) {
    .main-title {
        font-size: 2rem;
    }
    
    .friend-title {
        font-size: 1rem;
    }
    
    .gift-box {
        width: 150px;
        height: 120px;
    }
    
    .ribbon {
        width: 20px;
        height: 70px;
    }
    
    .ribbon::before,
    .ribbon::after {
        width: 20px;
        height: 20px;
    }
    
    .ribbon::before {
        left: -12px;
    }
    
    .ribbon::after {
        right: -12px;
    }
    
    .message {
        font-size: 1rem;
    }
    
    .surprise-text {
        font-size: 1.5rem;
    }
    
    .gift-container {
        min-height: 50vh;
    }
    
    .message-container {
        padding: 1rem;
        max-width: 95%;
    }
}

/* 特殊动画效果 */
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes pulse-grow {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.7; }
    100% { transform: scale(1); opacity: 1; }
}

.special-effect {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
}

.circle {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
    animation: pulse-grow 4s infinite ease-in-out;
}

.circle:nth-child(1) {
    width: 200px;
    height: 200px;
    top: 10%;
    left: 10%;
    animation-delay: 0s;
}

.circle:nth-child(2) {
    width: 150px;
    height: 150px;
    top: 60%;
    left: 70%;
    animation-delay: 1s;
}

.circle:nth-child(3) {
    width: 180px;
    height: 180px;
    top: 30%;
    left: 80%;
    animation-delay: 2s;
}

.circle:nth-child(4) {
    width: 120px;
    height: 120px;
    top: 70%;
    left: 20%;
    animation-delay: 3s;
}

@keyframes drift {
    0% { transform: translate(0, 0) rotate(0deg); }
    25% { transform: translate(10px, 10px) rotate(5deg); }
    50% { transform: translate(0, 20px) rotate(0deg); }
    75% { transform: translate(-10px, 10px) rotate(-5deg); }
    100% { transform: translate(0, 0) rotate(0deg); }
}

.drift-element {
    position: absolute;
    animation: drift 8s infinite linear;
    z-index: -1;
    opacity: 0.3;
}

.drift-element:nth-child(5) { top: 20%; left: 5%; animation-duration: 10s; }
.drift-element:nth-child(6) { top: 40%; left: 90%; animation-duration: 8s; }
.drift-element:nth-child(7) { top: 75%; left: 15%; animation-duration: 12s; }
.drift-element:nth-child(8) { top: 85%; left: 85%; animation-duration: 9s; }

/* 额外的惊喜效果 */
@keyframes float-up {
    0% { transform: translateY(0) scale(0.5); opacity: 0; }
    50% { transform: translateY(-100px) scale(1); opacity: 1; }
    100% { transform: translateY(-200px) scale(0.5); opacity: 0; }
}

.float-up {
    position: absolute;
    animation: float-up 3s forwards;
    font-size: 1.5rem;
    z-index: 10;
}
</style>
""", unsafe_allow_html=True)

# 创建背景特效
st.markdown('<div class="special-effect">', unsafe_allow_html=True)
for i in range(4):
    st.markdown(f'<div class="circle"></div>', unsafe_allow_html=True)

for i in range(4):
    elements = ["🎉", "🎁", "✨", "🎈", "🎊", "💝", "🌟", "💫"]
    st.markdown(f'''
    <div class="drift-element" style="
        top: {random.randint(10, 90)}%; 
        left: {random.randint(10, 90)}%;
        font-size: {random.randint(20, 40)}px;
        animation-delay: {random.uniform(0, 5)}s;
    ">{random.choice(elements)}</div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 创建内容包装器
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# 添加浮动元素
for i in range(5):
    st.markdown(f"""
    <div class="floating-element" style="
        top: {random.randint(10, 90)}%; 
        left: {random.randint(10, 90)}%; 
        animation-delay: {random.uniform(0, 3)}s;
    ">🎁</div>
    """, unsafe_allow_html=True)

# 主标题
st.markdown('<div class="main-title">给梁志清的特别礼物 🎁</div>', unsafe_allow_html=True)
st.markdown('<div class="friend-title">来自朋友的心意</div>', unsafe_allow_html=True)

# 礼物盒子
st.markdown('<div class="gift-container">', unsafe_allow_html=True)

# 礼物盒
gift_opened = st.button("🎁 点击打开礼物 🎁", key="gift_button", 
                        help="点击打开你的特别礼物", 
                        type="primary")

if gift_opened:
    # 创建惊喜效果
    for i in range(15):
        st.markdown(f"""
        <div class="sparkle" style="
            top: {random.randint(10, 90)}%; 
            left: {random.randint(10, 90)}%;
            background-color: #{random.choice(['ff6b6b', '4ecdc4', '45b7d1', '96ceb4', 'ffeaa7', 'ffd700'])};
            animation-delay: {random.uniform(0, 1)}s;
        "></div>
        """, unsafe_allow_html=True)
    
    # 添加飘动的心形
    for i in range(10):
        st.markdown(f"""
        <div class="heart" style="
            left: {random.randint(5, 95)}%;
            animation-delay: {random.uniform(0, 2)}s;
        ">❤️</div>
        """, unsafe_allow_html=True)
    
    # 添加闪烁的星星
    for i in range(8):
        st.markdown(f"""
        <div class="star" style="
            top: {random.randint(10, 80)}%; 
            left: {random.randint(10, 90)}%;
            animation-delay: {random.uniform(0, 2)}s;
        ">✨</div>
        """, unsafe_allow_html=True)
    
    # 浮动元素
    for i in range(5):
        elements = ["🎉", "🎊", "✨", "🎈", "💝", "🌟", "💫", "💖"]
        st.markdown(f"""
        <div class="float-up" style="
            top: {random.randint(30, 70)}vh; 
            left: {random.randint(20, 80)}vw;
            animation-delay: {random.uniform(0, 1)}s;
        ">{random.choice(elements)}</div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="surprise-text">🎉 惊喜展开 🎉</div>', unsafe_allow_html=True)
    
    # 随机生成一些祝福语
    messages = [
        "感谢你一直以来的友谊！",
        "愿你每天都有好心情！",
        "希望你所有的梦想都能实现！",
        "愿你健康快乐每一天！",
        "友谊万岁！",
        "愿你前程似锦！",
        "祝你工作顺利，生活美满！",
        "愿你永远保持微笑！",
        "你是最棒的朋友！",
        "愿你的未来充满光明！"
    ]
    
    # 显示随机祝福
    selected_message = random.choice(messages)
    
    st.markdown(f"""
    <div class="message-container">
        <div class="message">
            亲爱的梁志清：<br><br>
            {selected_message}<br><br>
            作为你的朋友，我很高兴认识你。<br>
            你是一个很棒的人，值得拥有世界上所有的美好。<br><br>
            这份特别的礼物虽然简单，但承载着我对你深深的友谊和祝福。<br>
            愿我们的友谊天长地久！
        </div>
        <div class="friend-message">
            - 你真诚的朋友
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # 未打开时显示礼物盒
    st.markdown("""
    <div class="gift-box">
        <div class="ribbon"></div>
    </div>
    <p style="text-align: center; margin-top: 1rem; font-size: 1.1rem; color: #666; animation: pulse 2s infinite;">
        点击上面的按钮打开你的特别礼物
    </p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 添加一些动态效果
if gift_opened:
    st.balloons()
    st.success("礼物已打开！希望你喜欢这份特别的心意！")

st.markdown('</div>', unsafe_allow_html=True)
