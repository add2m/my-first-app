import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة والوظائف
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# وظيفة التعليقات (التي أرسلتها سابقاً)
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: 
            f.write("شغل ممتاز وتسلم إيديكم!|سارة")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: f.write(f"\n{data}")
    elif action == "delete_one" and data is not None:
        if 0 <= data < len(reviews):
            reviews.pop(data)
            with open(file_path, "w", encoding="utf-8") as f: f.writelines(reviews)
    return reviews

# ============================================================
# 2. كود الـ CSS (تصحيح الألوان والتنسيق)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* السايدبار جهة اليمين */
    [data-testid="stSidebar"] {
        position: fixed;
        right: 0 !important;
        left: auto !important;
        background-color: #0d0d0d !important;
        border-right: 2px solid #D4AF37;
    }

    /* خلفية فخمة تمزج بين الأسود واللمسات الرقيقة */
    .stApp {
        background: #000000;
        background-image: 
            linear-gradient(rgba(255, 192, 203, 0.05), rgba(0, 0, 0, 0.95)),
            url('https://www.transparenttextures.com/patterns/marble-white.png');
        color: #ffffff !important;
    }

    /* تنسيق الأزرار الذهبية */
    .nav-btn {
        border: 1px solid #D4AF37 !important;
        background: rgba(212, 175, 55, 0.05) !important;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 12px;
        display: block;
        text-decoration: none !important;
        color: #D4AF37 !important;
        font-weight: bold;
        transition: 0.3s;
    }
    .nav-btn:hover {
        background: #D4AF37 !important;
        color: #000 !important;
    }

    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. الثوابت والبيانات
# ============================================================
LOGO = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUM = "201055901090"
ADMIN_PWD = "9811"
# قائمة الفيديوهات
VIDS = [
    "1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi",
    "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1",
    "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"
]

# ============================================================
# 4. السايدبار (Sidebar)
# ============================================================
with st.sidebar:
    st.image(LOGO, use_container_width=True)
    st.markdown("📍 **العنوان:**<br>منية النصر - شارع البحر - أمام ستار مول", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"📞 {WA_NUM}")

# ============================================================
# 5. الصفحات (التصحيح البرمجي هنا)
# ============================================================
p = st.query_params.get("p", "home")

if p == "home":
    st.image(LOGO, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>أهلاً بكم في بيوتي سنتر يارا ثروت</h2>", unsafe_allow_html=True)
    btns = [("📅 للحجز والاستفسار", "booking"), ("🎥 معرض فيديوهاتنا", "gallery"), ("⭐ آراء الجميلات", "reviews")]
    for txt, target in btns:
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-btn">{txt}</a>', unsafe_allow_html=True)

elif p == "gallery":
    st.markdown("### 🎥 معرض الفيديوهات")
    for v_id in VIDS:
        # استخدام iframe لضمان التشغيل المباشر من جوجل درايف
        st.markdown(f'<iframe src="https://drive.google.com/file/d/{v_id}/preview" width="100%" height="450"></iframe>', unsafe_allow_html=True)
        st.write("---")

elif p == "booking":
    st.markdown("### 🗓️ طلب حجز")
    name = st.text_input("الاسم")
    phone = st.text_input("الموبايل")
    service = st.selectbox("الخدمة", ["شعر", "بشرة", "حمام مغربي", "أخرى"])
    notes = st.text_area("ملاحظات")
    if st.button("إرسال عبر واتساب"):
        if name and phone:
            msg = f"حجز جديد: {name}\nخدمة: {service}\nملاحظات: {notes}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url=https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}">', unsafe_allow_html=True)

elif p == "reviews":
    st.markdown("### ⭐ آراء الجميلات")
    with st.expander("أضف رأيك"):
        with st.form("rev"):
            n = st.text_input("الاسم")
            t = st.text_area("الرأي")
            if st.form_submit_button("نشر"):
                handle_reviews("add", f"{t}|{n}")
                st.rerun()
    
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            txt, sender = rev.strip().split("|")
            st.info(f"{txt} - **{sender}**")
