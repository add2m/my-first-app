import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- خلفية الرخام الملكي والمقص المتحرك (بدون شريط سفلي) ---
st.markdown("""
<style>
/* الخلفية الرخامية الملكية */
.stApp {
    background: #f8f9fa;
    background-image: 
        radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.08) 0, transparent 50%), 
        radial-gradient(at 100% 100%, rgba(0, 0, 0, 0.03) 0, transparent 50%),
        linear-gradient(135deg, #ffffff 0%, #f4f4f4 100%);
    background-attachment: fixed;
}

/* المقص الذهبي المتحرك - ملفت للنظر جداً */
@keyframes scissors-cut {
    0% { transform: rotate(0deg) scale(1); opacity: 0.15; }
    50% { transform: rotate(15deg) scale(1.1); opacity: 0.25; }
    100% { transform: rotate(0deg) scale(1); opacity: 0.15; }
}
.scissors-bg {
    position: fixed;
    top: 20%;
    right: 5%;
    width: 200px;
    height: 200px;
    z-index: 0;
    pointer-events: none;
    animation: scissors-cut 6s ease-in-out infinite;
}

/* تنسيق المربعات الأصلية */
div[data-testid="stMarkdownContainer"] > div > a > div {
    border: 1px solid rgba(212, 175, 55, 0.5) !important;
    background: rgba(26, 26, 26, 0.9) !important;
    color: #ffffff !important;
    border-radius: 10px;
    padding: 15px !important;
    text-align: center;
    margin-bottom: 12px;
}
</style>

<div class="scissors-bg">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# --- الوظائف والبيانات الأصلية ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    if 13 <= current_hour < 22:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    return "🔴 السنتر مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
location_url = "https://maps.app.goo.gl/YV9Z6X2u3vL1X8T87" # رابط اللوكيشن الافتراضي

query_params = st.query_params
current_page = query_params.get("p", "home")

# --- محتوى الصفحات ---
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_phone = st.text_input("رقم الهاتف")
        if st.form_submit_button("إرسال البيانات"):
            if u_name and u_phone:
                full_msg = f"✨ حجز جديد ✨\n👤 الاسم: {u_name}\n📱 الهاتف: {u_phone}"
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={urllib.parse.quote(full_msg)}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">✅ تأكيد عبر واتساب</a>', unsafe_allow_html=True)

else:
    # الصفحة الرئيسية الأصلية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    btns = [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]
    for title, p in btns:
        st.markdown(f'<a href="./?p={p}" target="_self" style="text-decoration:none;"><div style="font-weight: bold;">{title}</div></a>', unsafe_allow_html=True)

# --- السايدبار الأصلي (فيه كل الزراير اللي طلبتها) ---
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    
    # زرار الاتصال الأزرق الأصلي
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:12px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    
    # زرار اللوكيشن الأصلي
    st.markdown(f'<a href="{location_url}" target="_blank" style="text-decoration:none;"><div style="background-color:#6c757d; color:white; padding:12px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 موقع السنتر (الخريطة)</div></a>', unsafe_allow_html=True)
    
    # أرقام التليفونات الأصلية
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(212,175,55,0.2); border-radius:5px; background:rgba(0,0,0,0.05);">📱 {phone_1}<br>📱 {phone_2}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📍 العنوان الكامل\n الدقهليه - منيه النصر - \n شارع البحر - امام استار مول - \n اعلى يونيكورن - الدور الخامس")
