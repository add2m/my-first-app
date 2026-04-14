import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- إضافة: خلفية متحركة مكثفة (أيقونات مقص وشعر بلون غامق) ---
st.markdown("""
<style>
.stApp {
    background-color: #0f0f0f;
    overflow: hidden;
}

.beauty-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.beauty-bg span {
    position: absolute;
    display: block;
    width: 35px;
    height: 35px;
    background-repeat: no-repeat;
    background-size: contain;
    opacity: 0.12; /* درجة شفافية هادية */
    animation: moveBeauty 20s linear infinite;
}

@keyframes moveBeauty {
    0% { transform: translateY(110vh) rotate(0deg); }
    100% { transform: translateY(-20vh) rotate(360deg); }
}

/* أيقونة المقص والمشط - لون رمادي غامق فخم */
.icon-style {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23444444"><path d="M442.2 26.3c-10.1-10.1-26.5-10.1-36.5 0L303.5 128.5V112c0-8.8-7.2-16-16-16s-16 7.2-16 16v64c0 8.8 7.2 16 16 16h64c8.8 0 16-7.2 16-16s-7.2-16-16-16H344.5l97.7-97.7c10.1-10.1 10.1-26.5 0-36.5zM153 223c-18.7-18.7-49.1-18.7-67.9 0l-58.8 58.8c-18.7 18.7-18.7 49.1 0 67.9s49.1 18.7 67.9 0L153 290.9c18.7-18.7 18.7-49.1 0-67.9z"/></svg>');
}

/* توزيع 12 أيقونة في الفراغات */
.beauty-bg span:nth-child(1) { left: 5%; animation-delay: 0s; animation-duration: 22s; }
.beauty-bg span:nth-child(2) { left: 15%; animation-delay: 4s; animation-duration: 18s; }
.beauty-bg span:nth-child(3) { left: 25%; animation-delay: 8s; animation-duration: 25s; }
.beauty-bg span:nth-child(4) { left: 35%; animation-delay: 2s; animation-duration: 20s; }
.beauty-bg span:nth-child(5) { left: 45%; animation-delay: 10s; animation-duration: 28s; }
.beauty-bg span:nth-child(6) { left: 55%; animation-delay: 6s; animation-duration: 23s; }
.beauty-bg span:nth-child(7) { left: 65%; animation-delay: 1s; animation-duration: 19s; }
.beauty-bg span:nth-child(8) { left: 75%; animation-delay: 5s; animation-duration: 26s; }
.beauty-bg span:nth-child(9) { left: 85%; animation-delay: 9s; animation-duration: 21s; }
.beauty-bg span:nth-child(10) { left: 92%; animation-delay: 3s; animation-duration: 24s; }
.beauty-bg span:nth-child(11) { left: 10%; animation-delay: 12s; animation-duration: 30s; }
.beauty-bg span:nth-child(12) { left: 80%; animation-delay: 7s; animation-duration: 27s; }

.element-container { z-index: 10; position: relative; }
</style>

<div class="beauty-bg">
    <span class="icon-style"></span><span class="icon-style"></span>
    <span class="icon-style"></span><span class="icon-style"></span>
    <span class="icon-style"></span><span class="icon-style"></span>
    <span class="icon-style"></span><span class="icon-style"></span>
    <span class="icon-style"></span><span class="icon-style"></span>
    <span class="icon-style"></span><span class="icon-style"></span>
</div>
""", unsafe_allow_html=True)

# --- وظيفة حساب حالة العمل ---
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
    elif action == "delete_one" and data is not None:
        if 0 <= data < len(reviews):
            reviews.pop(data)
            with open(file_path, "w", encoding="utf-8") as f: f.writelines(reviews)
    return reviews

# 2. البيانات والروابط
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
ADMIN_PASSWORD = "9811" 
site_url = "https://yara-tharwat.streamlit.app" 
share_msg = urllib.parse.quote(f" شوفت بيوتي سنتر يارا ثروت وشغله عجبني جداً، شوفي موقعهم من هنا: {site_url}")

video_ids = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi", 
             "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1", 
             "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"]

# 3. إدارة التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_phone = st.text_input("رقم الهاتف")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                lines = ["✨ حجز جديد من الموقع ✨", f"👤 الاسم: {u_name}", f"📱 الهاتف: {u_phone}", f"🎂 السن: {u_age}", f"📍 العنوان: {u_address}"]
                full_msg = "\n".join(lines)
                msg = urllib.parse.quote(full_msg)
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">✅ تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💵 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار قريباً")

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    with st.expander("اضف رأيك هنا"):
        with st.form("review_form"):
            r_name = st.text_input("الاسم")
            r_text = st.text_area("رأيك")
            if st.form_submit_button("نشر"):
                if r_name and r_text:
                    handle_reviews("add", f"{r_text}|{r_name}")
                    st.rerun()
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            t, n = rev.strip().split("|")
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(49,51,63,0.2); border-radius:10px; margin-bottom:10px; background: rgba(255,255,255,0.05);">"{t}"<br><small style="color:#D4AF37;">- {n}</small></div>', unsafe_allow_html=True)

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    for title, p in [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]:
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(255, 255, 255, 0.1); border-radius:8px; text-align:center; margin-bottom:12px; background: rgba(255,255,255,0.02);">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(255,255,255,0.1); border-radius:5px;">📞 {phone_1}<br>📞 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\n الدقهليه - منيه النصر - \n شارع البحر - امام استار مول - \n اعلى يونيكورن - الدور الخامس")
