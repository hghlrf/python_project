import streamlit as st
import numpy as np
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="给梁志清的星空祝福",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 星空主题CSS样式
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');

* {
    font-family: 'Noto Sans SC', sans-serif;
}

/* 星空背景 */
.stApp {
    background: #000428;
    background: linear-gradient(to bottom, #000428, #004e92);
    color: white;
    min-height: 100vh;
}

/* 隐藏Streamlit默认元素 */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 标题样式 */
.main-title {
    font-size: 3.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1.5rem;
    background: linear-gradient(90deg, #a8edea, #fed6e3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(168, 237, 234, 0.3);
    animation: twinkle 3s ease-in-out infinite alternate;
}

@keyframes twinkle {
    0% { opacity: 0.9; }
    100% { opacity: 1; }
}

/* 祝福卡片 */
.blessing-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 30px;
    margin: 20px auto;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    max-width: 800px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* 星星效果 */
.star {
    position: fixed;
    background-color: white;
    border-radius: 50%;
    animation: float 5s infinite ease-in-out;
    z-index: -1;
}

@keyframes float {
    0%, 100% { transform: translateY(0) scale(1); opacity: 0.5; }
    50% { transform: translateY(-20px) scale(1.1); opacity: 0.8; }
}

/* 流星效果 */
.shooting-star {
    position: fixed;
    width: 2px;
    height: 100px;
    background: linear-gradient(to bottom, transparent, white);
    animation: shooting 3s linear infinite;
    z-index: -1;
}

@keyframes shooting {
    0% { transform: translateX(-100px) translateY(-100px) rotate(45deg); opacity: 0; }
    10% { opacity: 1; }
    100% { transform: translateX(100vw) translateY(100vh) rotate(45deg); opacity: 0; }
}

/* 按钮样式 */
.stButton > button {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50px;
    padding: 10px 25px;
    font-size: 1rem;
    transition: all 0.3s;
    backdrop-filter: blur(5px);
}

.stButton > button:hover {
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
}

/* 消息样式 */
.message {
    font-size: 1.2rem;
    line-height: 1.8;
    margin: 15px 0;
    padding-left: 20px;
    border-left: 3px solid #a8edea;
    animation: fadeIn 1s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* 签名样式 */
.signature {
    text-align: right;
    font-style: italic;
    font-size: 1.3rem;
    margin-top: 40px;
    color: #fed6e3;
}
</style>
""", unsafe_allow_html=True)

# 修复的星空背景脚本 - 添加错误处理和兼容性改进
st.markdown("""
<div id="stars-container"></div>
<script>
// 确保DOM完全加载后再初始化
document.addEventListener('DOMContentLoaded', function() {
    try {
        const container = document.getElementById('stars-container');
        if (!container) {
            console.error('Stars container not found');
            return;
        }
        
        // 创建星星
        function createStars() {
            for(let i = 0; i < 150; i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                
                // 随机位置
                const left = Math.random() * 100;
                const top = Math.random() * 100;
                
                // 随机大小
                const size = Math.random() * 3 + 1;
                
                // 随机动画延迟
                const delay = Math.random() * 5;
                
                star.style.left = left + 'vw';
                star.style.top = top + 'vh';
                star.style.width = size + 'px';
                star.style.height = size + 'px';
                star.style.animationDelay = delay + 's';
                
                container.appendChild(star);
            }
        }
        
        // 创建流星
        function createShootingStar() {
            const shootingStar = document.createElement('div');
            shootingStar.classList.add('shooting-star');
            
            // 随机起始位置
            const startY = Math.random() * 50;
            
            shootingStar.style.left = '0';
            shootingStar.style.top = startY + 'vh';
            shootingStar.style.animationDelay = Math.random() * 2 + 's';
            
            container.appendChild(shootingStar);
            
            // 移除流星元素 - 使用兼容性更好的方法
            setTimeout(() => {
                if (container.contains(shootingStar)) {
                    container.removeChild(shootingStar);
                }
            }, 3000);
        }
        
        // 初始化
        createStars();
        
        // 创建流星
        setInterval(createShootingStar, 2000);
        
        // 确保创建初始流星
        setTimeout(createShootingStar, 1000);
        
        // 添加窗口大小变化时的处理
        window.addEventListener('resize', function() {
            console.log('Window resized,星空背景已适应');
        });
        
    } catch (error) {
        console.error('星空效果初始化失败:', error);
        // 创建一个简单的替代背景
        document.body.style.background = 'linear-gradient(to bottom, #000428, #004e92)';
        // 显示错误提示
        const errorDiv = document.createElement('div');
        errorDiv.style.position = 'fixed';
        errorDiv.style.top = '20px';
        errorDiv.style.left = '50%';
        errorDiv.style.transform = 'translateX(-50%)';
        errorDiv.style.backgroundColor = 'rgba(255, 0, 0, 0.7)';
        errorDiv.style.color = 'white';
        errorDiv.style.padding = '10px 20px';
        errorDiv.style.borderRadius = '5px';
        errorDiv.style.zIndex = '1000';
        errorDiv.innerHTML = '星空效果加载失败，已使用替代背景';
        document.body.appendChild(errorDiv);
        
        // 5秒后自动移除错误提示
        setTimeout(() => {
            if (document.body.contains(errorDiv)) {
                document.body.removeChild(errorDiv);
            }
        }, 5000);
    }
</script>
""", unsafe_allow_html=True)

# 主标题
st.markdown('<h1 class="main-title">✨ 给梁志清的星空祝福 ✨</h1>', unsafe_allow_html=True)

# 祝福卡片
st.markdown('<div class="blessing-card">', unsafe_allow_html=True)

st.markdown("## 🌌 亲爱的梁志清：")

# 祝福消息
st.markdown('<div class="message">在这片星空下，我想把最美好的祝福送给你。</div>', unsafe_allow_html=True)
st.markdown('<div class="message">愿你的人生如这星空般广阔，充满无限可能。</div>', unsafe_allow_html=True)
st.markdown('<div class="message">愿你的每一天都如星辰般闪耀，照亮前行的道路。</div>', unsafe_allow_html=True)
st.markdown('<div class="message">愿你的心中永远有一片宁静的星空，可以安放所有的梦想与希望。</div>', unsafe_allow_html=True)
st.markdown('<div class="message">愿你保持好奇心，像探索星空一样探索这个世界。</div>', unsafe_allow_html=True)
st.markdown('<div class="message">愿你的未来，如这夜空中的银河，璀璨而美丽。</div>', unsafe_allow_html=True)

st.markdown("")

# 名言引用
st.markdown("> \"我们都在阴沟里，但仍有人仰望星空。\" —— 奥斯卡·王尔德")

st.markdown("")

# 互动部分
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⭐ 点亮一颗星"):
        st.balloons()
        st.success("为你点亮了一颗特别的星！")

with col2:
    if st.button("🌠 许个愿"):
        st.info("愿你的愿望如流星般实现！")

with col3:
    if st.button("💫 发送祝福"):
        st.success("祝福已发送到宇宙中！")

# 日期信息
today = datetime.now()
st.markdown(f"<p style='text-align: center; margin-top: 30px; opacity: 0.7;'>{today.strftime('%Y年%m月%d日')} • 一个繁星点点的夜晚</p>", unsafe_allow_html=True)

# 签名
st.markdown('<div class="signature">—— 仰望星空的人</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 分隔线
st.markdown("---")

# 底部信息
st.markdown("""
<div style="text-align: center; padding: 20px 0; opacity: 0.7;">
<p>🌌 星空中的每一颗星，都代表着对你的一个美好祝愿 🌌</p>
<p style="font-size: 0.9rem;">愿你在人生的旅程中，总能找到属于自己的那片星空</p>
</div>
""", unsafe_allow_html=True)

# 星空知识小彩蛋
with st.expander("🌙 星空小知识"):
    st.markdown("""
    **你知道吗？**
    
    1. 夜空中肉眼可见的星星大约有6000颗，但同一时间只能看到大约3000颗。
    
    2. 我们看到的星光可能来自数百甚至数千年前，因为它们需要很长时间才能到达地球。
    
    3. 北斗七星是大熊座的一部分，在古代常被用作导航工具。
    
    4. 流星并不是"星星坠落"，而是宇宙尘埃进入地球大气层燃烧产生的现象。
    
    5. 每个人都可以在夜空中找到属于自己的星座故事。
    """)

# 星空主题选择
st.markdown("")
st.markdown("### 🌟 选择你的星空主题")

theme = st.selectbox(
    "选择你喜欢的星空颜色",
    ["经典深蓝星空", "紫色梦幻星空", "绿色极光星空", "粉色浪漫星空"]
)

# 根据选择更新主题
if theme == "紫色梦幻星空":
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e);
    }
    </style>
    """, unsafe_allow_html=True)
elif theme == "绿色极光星空":
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #000000, #0a3d2e, #1a5a4a);
    }
    </style>
    """, unsafe_allow_html=True)
elif theme == "粉色浪漫星空":
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #3a1c71, #d76d77, #ffaf7b);
    }
    </style>
    """, unsafe_allow_html=True)

st.info(f"已切换到：{theme}")
