import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة - تنسيق centered ومخصص للتليفونات
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered", initial_sidebar_state="collapsed")

# 2. تعريف رابط صورة الخلفية الرخامية المفضلة
background_image_url = "https://i.postimg.cc/85z1X2t9/image-4.png" # تم الرفع على رابط موثوق

# --- كود CSS و JavaScript مدمج لخلق المقص المتحرك والتنقل الجديد ---
st.markdown(f"""
<style>
/* تعيين الخلفية الرخامية للموقع بالكامل */
.stApp {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #fff !important;
}}

/* تأكيد تنسيق الحاوية الأساسية لتكون فوق الخلفية */
.main {{
    position: relative;
    z-index: 10;
    padding-bottom: 80px; /* مساحة للشريط السفلي */
}}

/* تأثير المقص المتحرك في الخلفية (في الصفحة الرئيسية فقط) */
@keyframes scissors-magic {{
    0% {{ transform: rotate(0deg) scale(1) translate(-50%, -50%); opacity: 0.15; }}
    25% {{ transform: rotate(10deg) scale(1.1) translate(-50%, -50%); opacity: 0.25; }}
    50% {{ transform: rotate(0deg) scale(1) translate(-50%, -50%); opacity: 0.15; }}
    75% {{ transform: rotate(-10deg) scale(0.9) translate(-50%, -50%); opacity: 0.25; }}
    100% {{ transform: rotate(0deg) scale(1) translate(-50%, -50%); opacity: 0.15; }}
}}

.magic-scissors {{
    position: fixed;
    top: 50%;
    left: 50%;
    width: 300px;
    height: 300px;
    /* مقص ذهبي كلاسيكي كبير بلون واضح */
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M128 320c0 35.3 28.7 64 64 64s64-28.7 64-64-28.7-64-64-64-64 28.7-64 64zm64-96c35.3 0 64 28.7 64 64s-28.7 64-64 64-64-28.7-64-64 28.7-64 64-64zM320 128c0 35.3 28.7 64 64 64s64-28.7 64-64-28.7-64-64-64-64 28.7-64 64zm64-96c35.3 0 64 28.7 64 64s-28.7 64-64 64-64-28.7-64-64 28.7-64 64-64z"/></svg>');
    background-size: contain;
    background-repeat: no-repeat;
    pointer-events: none;
    z-index: 5;
    animation: scissors-magic 15s linear infinite;
    opacity: 0.15; /* شفاف جداً في الخلفية */
}}

/* تحسين تنسيق المربعات لتكون بارزة جداً على الموبايل بخلفية سوداء ووردية */
div[data-testid="stMarkdownContainer"] > div > a > div, .stForm {{
    border: 1px solid rgba(212, 175, 55, 0.4) !important;
    background: rgba(0, 0, 0, 0.75) !important; /* خلفية سوداء شفافة فخمة */
    backdrop-filter: blur(5px);
    transition: 0.3s all ease-in-out !important;
    color: #fff !important;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
    margin-bottom: 15px;
}}

/* تنسيق الهيدر واللوجو */
.stImage img {{
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}}

/* تحسين عرض المراجعات والآراء */
.rev-box {{
    padding: 15px;
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 10px;
    margin-bottom: 10px;
    background: rgba(26, 26, 26, 0.8);
    color: #fff;
}}

/* --- شريط التنقل السفلي الذكي للموبايل الهواتف --- */
.bottom-nav-container {{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #1a1a1a;
    border-top: 2px solid #D4AF37;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 10px;
    z-index: 100;
    box-shadow: 0 -4px 15px rgba(212, 175, 55, 0.2);
}}

.nav-item {{
    text-decoration: none;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    transition: 0.3s;
    font-size: 14px;
}}

.nav-item:hover, .nav-item.active {{
    color: #D4AF37;
    transform: scale(1.1);
    text-shadow: 0 0 5px rgba(212, 175, 55, 0.5);
}}

.nav-icon {{
    font-size: 24px;
    margin-bottom: 3px;
    display: block;
}}

/* --- تنسيقات مخصصة للتليفونات والهواتف --- */
@media (max-width: 600px) {{
    .main {{
        padding-left: 10px;
        padding-right: 10px;
    }}
    
    .stImage img {{
        max-width: 100%;
        height: auto;
    }}
    
    h2, h3 {{
        font-size: 20px !important;
        text-align: center !important;
        color: #D4AF37 !important; /* لون ذهبي لامع للعناوين */
    }}
    
    .magic-scissors {{
        width: 250px;
        height: 250px;
    }}
}}
</style>

<div class="magic-scissors"></div>

<div class="bottom-nav-container">
    <a class="nav-item nav-main active" href="./?p=home" target="_self"><span class="nav-icon">🏠</span>الرئيسية</a>
    <a class="nav-item nav-booking" href="./?p=booking" target="_self"><span class="nav-icon">📅</span>الحجز</a>
    <a class="nav-item nav-gallery" href="./?p=gallery" target="_self"><span class="nav-icon">✨</span>شغلنا</a>
    <a class="nav-item nav-reviews" href="./?p=reviews" target="_self"><span class="nav-icon">🌟</span>الآراء</a>
    <a class="nav-item nav-prices" href="./?p=prices" target="_self"><span class="nav-icon">💵</span>الأسعار</a>
</div>

<script>
    // تفعيل التحديد على الشريط السفلي بناءً على الصفحة الحالية
    const params = new URLSearchParams(window.location.search);
    const page = params.get("p") || "home";
    const navItem = document.querySelector(`.nav-${{page}}`);
    if (navItem) {{
        document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
        navItem.classList.add('active');
    }}
</script>
""", unsafe_allow_html=True)

# --- وظيفة حساب حالة العمل (مصر UTC+3) ---
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

# 2. البيانات والروابط الأساسية
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

# 3. إدارة التنقل عبر الرابط
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
            else:
                st.warning("من فضلك ادخلي الاسم ورقم الهاتف ورقم الهاتف")

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
            st.markdown(f'<div class="rev-box">"{t}"<br><small style="color:#D4AF37;">- {n}</small></div>', unsafe_allow_html=True)
            
    with st.expander("🔐 إدارة"):
        pwd = st.text_input("الباسورد", type="password")
        if pwd == ADMIN_PASSWORD:
            for i, rev in enumerate(all_revs):
                if "|" in rev:
                    content, sender = rev.strip().split("|")
                    if st.button(f"🗑️ حذف {sender}", key=f"del_{i}"):
                        handle_reviews("delete_one", i)
                        st.rerun()

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    # الصفحة الرئيسية (الافتراضية)
    # جعل اللوجو في الوسط على الموبايل
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    for title, p in [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]:
        st.markdown(f'<a href="./?p={p}" target="_self" style="text-decoration:none;color:inherit;"><div style="padding:15px; border:1px solid rgba(212, 175, 55, 0.4); border-radius:10px; text-align:center; margin-bottom:12px; font-weight: bold; background: rgba(0,0,0,0.6);">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar (السايدبار)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(212,175,55,0.1); border-radius:5px; background:rgba(0,0,0,0.5); color:#fff;">📞 {phone_1}<br>📞 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\n الدقهليه - منيه النصر - \n شارع البحر - امام استار مول - \n اعلى يونيكورن - الدور الخامس")
