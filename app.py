import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered", initial_sidebar_state="collapsed")

# --- كود CSS احترافي: خلفية رخامية مبرمجة + تنسيق الهواتف ---
st.markdown("""
<style>
/* إنشاء خلفية رخامية (Marble) باستخدام الألوان المفضلة بدون صور خارجية */
.stApp {
    background: #fdf2f4; /* لون أساسي وردي فاتح جداً */
    background-image: 
        radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.05) 0, transparent 50%), 
        radial-gradient(at 50% 0%, rgba(0, 0, 0, 0.05) 0, transparent 50%), 
        radial-gradient(at 100% 0%, rgba(212, 175, 55, 0.05) 0, transparent 50%),
        linear-gradient(135deg, rgba(255,255,255,1) 0%, rgba(253,242,244,1) 100%);
    background-attachment: fixed;
}

/* تحسين المربعات لتكون بارزة جداً على الموبايل */
div[data-testid="stMarkdownContainer"] > div > a > div, .stForm {
    border: 2px solid #D4AF37 !important; /* إطار ذهبي صريح */
    background: #1a1a1a !important; /* أسود فخم */
    color: #ffffff !important;
    border-radius: 15px;
    padding: 20px !important;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    transition: 0.3s;
}

/* تأثير عند الضغط أو اللمس */
div[data-testid="stMarkdownContainer"] > div > a > div:active {
    transform: scale(0.95);
    background: #D4AF37 !important;
    color: #000 !important;
}

/* تنسيق النصوص والقوائم */
h2, h3 {
    color: #000 !important;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(212,175,55,0.3);
}

/* إخفاء القوائم غير الضرورية لزيادة المساحة على الموبايل */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* تنسيق مخصص للشاشات الصغيرة جداً */
@media (max-width: 600px) {
    .stImage img {
        width: 100% !important;
        border: 3px solid #D4AF37;
        border-radius: 20px;
    }
    div[data-testid="stMarkdownContainer"] > div > a > div {
        font-size: 18px !important;
        padding: 25px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# --- وظيفة حساب حالة العمل (مصر) ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    start_hour = 13
    end_hour = 22
    if start_hour <= current_hour < end_hour:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 السنتر مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

# --- وظيفة الآراء ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: f.write("شغل ممتاز وتسلم إيديكم!|سارة")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: f.write(f"\n{data}")
    return reviews

# البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
site_url = "https://yara-tharwat.streamlit.app" 
share_msg = urllib.parse.quote(f"شوفت بيوتي سنتر يارا ثروت وشغله عجبني، شوفي موقعهم: {site_url}")

# التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_phone = st.text_input("رقم الهاتف")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        if st.form_submit_button("إرسال البيانات"):
            if u_name and u_phone:
                full_msg = f"✨ حجز جديد من الموقع ✨\n👤 الاسم: {u_name}\n📱 الهاتف: {u_phone}\n🎂 السن: {u_age}\n📍 العنوان: {u_address}"
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={urllib.parse.quote(full_msg)}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">✅ تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💵 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار قريباً")

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            t, n = rev.strip().split("|")
            st.markdown(f'<div style="background:white; padding:15px; border-radius:10px; border-right: 5px solid #D4AF37; margin-bottom:10px; color: black;"><b>{n}:</b><br>{t}</div>', unsafe_allow_html=True)

elif current_page == "gallery":
    st.markdown("### ✨ صور لشغلنا")
    st.write("سيتم إضافة الصور قريباً")

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    # أزرار التنقل بشكل جذاب جداً للموبايل
    btns = [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]
    for title, p in btns:
        st.markdown(f'<a href="./?p={p}" target="_self" style="text-decoration:none;"><div style="font-size: 20px;">{title}</div></a>', unsafe_allow_html=True)

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:12px; border-radius:8px; text-align:center; margin-top:10px;">📞 اتصل بنا</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:12px; border-radius:8px; text-align:center; margin-top:10px;">🔗 مشاركة الموقع</div></a>', unsafe_allow_html=True)
