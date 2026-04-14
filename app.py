import streamlit as st
import urllib.parse
import os
import time
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة المتقدمة (Streamlit Configuration)
# ============================================================
# تم إعداد الصفحة لتناسب العرض على الموبايل والكمبيوتر بشكل احترافي
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. كود الـ CSS الاحترافي (Professional Styling)
# ============================================================
# تم نقل السايدبار لليمين، وتغميق الخلفية، وتعديل المقص ليكون في الجهة المقابلة
st.markdown("""
<style>
    /* تحسين الخطوط والتنسيق العام */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* نقل السايدبار للجهة اليمنى (تعديل الطلب الأول) */
    [data-testid="stSidebar"] {
        position: fixed;
        right: 0 !important;
        left: auto !important;
        background-color: #0f0f0f !important;
        border-right: 2px solid #D4AF37;
        border-left: none !important;
        z-index: 100;
    }
    
    /* ضبط محتوى السايدبار ليدعم العربية من اليمين */
    section[data-testid="stSidebar"] > div {
        direction: rtl;
    }

    /* الخلفية الغامقة الملكية العميقة */
    .stApp {
        background: #050505;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #0a0a0a 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* تأثير المقص الذهبي المتحرك (جهة اليسار الآن) */
    @keyframes scissors-swing {
        0% { transform: rotate(0deg) scale(1); opacity: 0.2; }
        50% { transform: rotate(-20deg) scale(1.15); opacity: 0.4; }
        100% { transform: rotate(0deg) scale(1); opacity: 0.2; }
    }

    .scissors-art {
        position: fixed;
        bottom: 10%;
        left: 5%; 
        width: 300px;
        height: 300px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-swing 10s ease-in-out infinite;
    }

    /* تنسيق الأزرار لتفتح في تاب جديد (الطلب الجديد) */
    .nav-button {
        border: 1px solid #D4AF37 !important;
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 22px;
        text-align: center;
        margin-bottom: 15px;
        transition: all 0.4s ease;
        text-decoration: none !important;
        display: block;
        color: #D4AF37 !important;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .nav-button:hover {
        background: #D4AF37 !important;
        color: #000 !important;
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
    }

    /* تحسين شكل المدخلات (Input Fields) وإلغاء الفواصل الزيادة */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-radius: 8px !important;
    }

    /* إخفاء عناصر Streamlit لزيادة الاحترافية */
    #MainMenu, footer, header { visibility: hidden; }
</style>

<div class="scissors-art">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3. الثوابت والبيانات (System Constants)
# ============================================================
LOGO_IMG = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUMBER = "201055901090"
PHONES = ["01055901090", "01055907095"]
MAP_LINK = "https://maps.google.com/?q=Minyat+al-Nasr"
# العنوان التفصيلي كما هو مطلوب
FULL_ADDRESS = "الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس"

# ============================================================
# 4. وظائف النظام (System Functions)
# ============================================================
def get_current_status():
    """تحديد حالة العمل بناءً على توقيت القاهرة (UTC+3)"""
    now = datetime.utcnow() + timedelta(hours=3)
    if 13 <= now.hour < 22: # من 1 ظهراً لـ 10 مساءً
        return "🟢 نتشرف باستقبالكم الآن", "#28a745"
    return "🔴 السنتر مغلق حالياً", "#dc3545"

def generate_wa_link(msg):
    """توليد رابط واتساب يعمل في نافذة جديدة"""
    return f"https://wa.me/{WA_NUMBER}?text={urllib.parse.quote(msg)}"

# ============================================================
# 5. السايدبار - الجهة اليمنى (Sidebar - Right Side)
# ============================================================
with st.sidebar:
    st.image(LOGO_IMG, use_container_width=True)
    
    # عرض حالة العمل بشكل شيك
    status_text, status_color = get_current_status()
    st.markdown(f"""
        <div style="background:rgba(212,175,55,0.1); color:{status_color}; padding:12px; 
        border-radius:10px; text-align:center; font-weight:bold; border:1px solid {status_color};">
            {status_text}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # أزرار الاتصال واللوكيشن المباشرة (تفتح في تاب جديد)
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" style="text-decoration:none;"><div style="background:#007bff; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصال مباشر</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{MAP_LINK}" target="_blank" style="text-decoration:none;"><div style="background:#6c757d; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 عرض الموقع على الخريطة</div></a>', unsafe_allow_html=True)
    
    # بيانات التواصل التفصيلية
    st.markdown(f"""
        <div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.03);">
            <p style="margin:0; font-size:15px; color:#D4AF37;"><b>📱 أرقامنا:</b></p>
            <p style="margin:0; font-size:14px;">{PHONES[0]}</p>
            <p style="margin:0; font-size:14px;">{PHONES[1]}</p>
            <hr style="border-color:rgba(212,175,55,0.1);">
            <p style="margin:0; font-size:13px; line-height:1.6;"><b>📍 العنوان:</b><br>{FULL_ADDRESS}</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# 6. إدارة الصفحات والمحتوى (Navigation & Content)
# ============================================================
params = st.query_params
current_p = params.get("p", "home")

# --- الصفحة الرئيسية ---
if current_p == "home":
    # إضافة شعار كبير في المنتصف
    st.image(LOGO_IMG, use_container_width=True)
    st.markdown("<h1 style='text-align: center; font-size: 2.2rem;'>✨ Yara Tharwat Beauty Center ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #D4AF37;'>نعتني بجمالكِ بأحدث التقنيات وأفضل الأيادي</p>", unsafe_allow_html=True)
    
    # قائمة الأزرار الرئيسية (كلها تفتح في صفحات جديدة بذكاء)
    main_menu = [
        ("📅 احجزي موعدك الآن", "booking"),
        ("💰 قائمة الأسعار والعروض", "prices"),
        ("📸 معرض أعمالنا", "gallery"),
        ("⭐ آراء الجميلات", "reviews")
    ]
    
    st.write("<br>", unsafe_allow_html=True)
    for title, link_key in main_menu:
        # استخدام target="_blank" للفتح في تاب جديد
        st.markdown(f'<a href="./?p={link_key}" target="_blank" class="nav-button">{title}</a>', unsafe_allow_html=True)

# --- صفحة الحجز (بدون فواصل زيارة وبسيطة) ---
elif current_p == "booking":
    st.markdown("<h2 style='text-align: center;'>🗓️ طلب حجز جديد</h2>", unsafe_allow_html=True)
    st.write("يرجى إدخال البيانات التالية وسيقوم فريقنا بالتواصل معكِ فوراً:")
    
    c1, c2 = st.columns(2)
    with c1:
        u_name = st.text_input("الاسم بالكامل 👤")
        u_age = st.text_input("السن 🎂")
    with c2:
        u_phone = st.text_input("رقم الموبايل 📱")
        u_addr = st.text_input("المنطقة/العنوان 📍")
    
    service = st.selectbox("نوع الخدمة المطلوبة ✨", ["ميك أب", "شعر", "عناية بالبشرة", "أخرى"])
    notes = st.text_area("هل لديكِ أي ملاحظات خاصة؟ 📝")
    
    if st.button("🚀 إرسال الطلب عبر واتساب", use_container_width=True):
        if u_name and u_phone:
            full_msg = f"✨ طلب حجز جديد ✨\n━━━━━━━━━━━━\n👤 الاسم: {u_name}\n📱 الموبايل: {u_phone}\n🎂 السن: {u_age}\n📍 العنوان: {u_addr}\n💄 الخدمة: {service}\n📝 ملاحظات: {notes}"
            wa_url = generate_wa_link(full_msg)
            # فتح الواتساب في تاب جديد
            st.markdown(f'<meta http-equiv="refresh" content="0; url={wa_url}">', unsafe_allow_html=True)
            st.success("جاري توجيهك إلى واتساب لتأكيد الحجز..")
        else:
            st.warning("رجاءً تأكدي من كتابة الاسم ورقم الهاتف.")

# --- الصفحات الأخرى (قوالب جاهزة للتعبئة) ---
elif current_p == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار التفصيلية هنا قريباً.. انتظرو عروضنا القوية!")
    
elif current_p == "gallery":
    st.markdown("### 📸 معرض أعمالنا")
    st.write("نعرض لكِ هنا عينات من شغلنا المتميز:")
    st.warning("جاري تحميل الصور من السيرفر..")

elif current_p == "reviews":
    st.markdown("### ⭐ آراء عملائنا")
    st.success("شغل يارا ملوش حل بجد، تسلم إيدك! 😍")
    st.success("أجمل مكان وأحسن معاملة في منية النصر كلها. ❤️")
