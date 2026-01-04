import streamlit as st

# 页面配置
st.set_page_config(
    page_title="梁志清",
    page_icon="🌟",
    layout="centered"
)

# 自定义CSS样式 - 添加动画效果
st.markdown("""
<style>
.name-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.name {
    font-size: 6rem;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: 
        color-change 3s infinite alternate,
        bounce 2s infinite alternate,
        scale-pulse 4s infinite;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
}

@keyframes color-change {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
}

@keyframes bounce {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}

@keyframes scale-pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stParticles {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}
</style>
""", unsafe_allow_html=True)

# 背景
st.markdown('<div class="background"></div>', unsafe_allow_html=True)

# 动画名字展示
st.markdown('<div class="name-container"><div class="name">梁志清</div></div>', unsafe_allow_html=True)
