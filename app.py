import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered", initial_sidebar_state="collapsed")

# --- كود CSS و JavaScript لخلق الخلفية والمقص المتحرك بدون صور خارجية ---
st.markdown("""
<style>
/* إنشاء الخلفية الرخامية (بناءً على ذوقك في الصورة) */
.stApp {
    background: #fdf2f4;
    background-image: 
        radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
        radial-gradient(at 100% 100%, rgba(0, 0, 0, 0.05) 0, transparent 50%),
        linear-gradient(135deg, #ffffff 0%, #fdf2f4 100%);
    background-attachment: fixed;
}

/* --- المقص الذهبي المتحرك (ملفت جداً وواضح) --- */
@keyframes scissors-cut {
    0% { transform: rotate(0deg) scale(1); opacity: 0.1; }
    25% { transform: rotate(15deg) scale(1.1); opacity: 0.2; }
    50% { transform: rotate(0deg) scale(1); opacity: 0.1; }
    75% { transform: rotate(-15deg) scale(0.9); opacity: 0.2; }
    100% { transform: rotate(0deg) scale(1); opacity: 0.1; }
}

.scissors-bg {
    position: fixed;
    top: 30%;
    left: 10%;
    width: 250px;
    height: 250px;
    z-index: 1;
    pointer-events: none;
    animation: scissors-cut 8s ease-in-out infinite;
}

/* تنسيق المربعات والأزرار لتكون واضحة وفخمة */
div[data-testid="stMarkdownContainer"] > div > a > div, .stForm {
    border: 2px solid #D4AF37 !important; /* إطار ذهبي واضح */
    background: #1a1a1a !important; /* أسود فخم للتباين */
    color: #ffffff !important;
    border-radius: 15px;
    padding: 20px !important;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
    position: relative;
    z-index: 10;
}

/* شريط التنقل السفلي الاحترافي للموبايل */
.nav-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #1a1a1a;
    border-top: 2px solid #D4AF37;
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
    z-index: 1000;
}

.nav-item {
    text-decoration: none;
    color: #D4AF37;
    font-size: 12px;
    text-align: center;
}
</style>

<div class="scissors-bg">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>

<div class="nav-bar">
    <a href="./?p=home" class="nav-item">🏠<br>الرئيسية</a>
    <a href="./?p=booking" class="nav-item">📅<br>الحجز</a>
    <a href="./?p=gallery" class="nav-item">✨<br>شغلنا</a>
    <a href="./?p=reviews" class="nav-item">🌟<br>الآراء</a>
    <a href="./?p=prices" class="nav-item">💵<br>الأسعار</a>
</div>
""", unsafe_allow_html=True)

# --- الوظائف البرمجية (الحالة، الآراء) ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    if 13 <= current_hour < 22:
        return "🟢 نحن متاحون الآن", "#28a745"
    return "🔴 السنتر مغلق حالياً", "#dc3545"

status_msg, text_color = get_business_status()

# البيانات والروابط
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
query_params = st.query_params
current_page = query_params.get("p", "home")

# --- محتوى الصفحات ---
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_phone = st.text_input("رقم الهاتف")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        if st.form_submit_button("إرسال البيانات"):
            if u_name and u_phone:
                full_msg = f"✨ حجز جديد ✨\n👤 الاسم: {u_name}\n📱 الهاتف: {u_phone}"
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={urllib.parse.quote(full_msg)}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">✅ تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    st.info("سيتم عرض الآراء هنا")

elif current_page == "gallery":
    st.markdown("### ✨ معرض الصور")
    st.info("سيتم إضافة الصور قريباً")

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #1a1a1a;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    # أزرار الصفحة الرئيسية
    menu = [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]
    for title, p in menu:
        st.markdown(f'<a href="./?p={p}" target="_self" style="text-decoration:none;"><div style="font-size: 18px; font-weight: bold;">{title}</div></a>', unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="color: {text_color}; text-align: center; font-weight: bold;">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\n منية النصر - الدقهلية")
