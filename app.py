import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- وظيفة الآراء ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: 
            f.write("شغل ممتاز وتجربة رائعة!|سارة أحمد")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: 
            f.write(f"\n{data}")
    return reviews

# 2. كود الـ CSS (السر كله هنا لظهور الزرار)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown, .stApp {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* السايدبار يسار والمحتوى يمين */
    [data-testid="stAppViewContainer"] {
        flex-direction: row-reverse !important;
    }

    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-right: 2px solid #D4AF37;
    }

    /* --- الزرار الذهبي اللي بتسأل عليه --- */
    [data-testid="stSidebarCollapsedControl"] {
        left: 20px !important; /* مكانه في اليسار */
        right: auto !important;
        background-color: #D4AF37 !important; /* لونه ذهبي */
        border-radius: 10px !important;
        padding: 5px !important;
        z-index: 1000000 !important; /* يظهر فوق أي صورة أو مقص */
        display: flex !important;
    }
    
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: #000 !important; /* السهم لونه أسود عشان يبان */
    }

    .stApp {
        background: #000000;
        background-image: radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
                          linear-gradient(180deg, #000000 0%, #050505 100%);
    }

    .nav-btn {
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background: rgba(255, 255, 255, 0.03) !important;
        border-radius: 15px;
        padding: 22px;
        text-align: center;
        margin-bottom: 15px;
        display: block;
        color: #D4AF37 !important;
        font-weight: bold;
        text-decoration: none !important;
    }

    header, footer, #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 3. البيانات
LOGO = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUM = "201055901090"
PHONES = ["01055901090", "01055907095"]
ADDR = "الدقهلية - منية النصر"
VIDS = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi"]

# 4. السايدبار
with st.sidebar:
    st.image(LOGO)
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" class="nav-btn" style="padding:10px;">📞 اتصلي بنا</a>', unsafe_allow_html=True)

# 5. الصفحات (صلحنا اسم المتغير هنا عشان الـ NameError يختفي)
p = st.query_params.get("p", "home")

if p == "home":
    st.image(LOGO)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    menu = [("📅 للحجز والاستفسار ✨💄", "booking"), ("🎥 صور لشغلنا 🎬", "gallery"), ("⭐ آراء العملاء 💖", "reviews")]
    for text, target in menu:
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-btn">{text}</a>', unsafe_allow_html=True)

elif p == "booking":
    st.markdown("### 📅 حجز موعد جديد")
    with st.form("book"):
        name = st.text_input("الاسم")
        phone = st.text_input("الموبايل")
        notes = st.text_area("ملاحظات")
        if st.form_submit_button("إرسال"):
            msg = f"حجز جديد: {name} - {phone} - {notes}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url=https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}">', unsafe_allow_html=True)

elif p == "gallery":
    st.markdown("### 🎥 معرض الأعمال")
    for v in VIDS:
        st.markdown(f'<iframe src="https://drive.google.com/file/d/{v}/preview" width="100%" height="400"></iframe>', unsafe_allow_html=True)

elif p == "reviews":
    st.markdown("### ⭐ آراء الجميلات")
    revs = handle_reviews()
    for r in reversed(revs):
        if "|" in r:
            t, n = r.strip().split("|")
            st.markdown(f'<div style="border:1px solid #D4AF37; padding:10px; border-radius:10px; margin-bottom:10px;">"{t}"<br>— {n}</div>', unsafe_allow_html=True)
