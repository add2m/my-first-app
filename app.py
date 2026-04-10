import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_number = "201055901090"

# 3. عرض اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# 4. الجملة الترحيبية
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️ اهلا بكم في بيوتي سنتر يارا ثروت ❤️</h3>", unsafe_allow_html=True)

# 5. الشريط الجانبي (Sidebar) - العنوان متقسم عشان يظهر كامل
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    
    st.markdown("### 📍 العنوان")
    # تقسيم العنوان لسطور عشان يبقى شيك وكامل
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")

# 6. عنوان الفورم
st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)

# 7. فورم إدخال البيانات
with st.form("booking_form"):
    name = st.text_input("الاسم بالكامل")
    age = st.text_input("السن")
    address = st.text_input("العنوان بالتفصيل")
    phone = st.text_input("رقم الهاتف")
    email = st.text_input("البريد الإلكتروني (اختياري)")
    
    submit = st.form_submit_button("إرسال البيانات")
    
    if submit:
        if name and address and phone:
            # تجهيز الرسالة بتنسيق يمنع أخطاء الـ Syntax
            booking_msg = f"حجز جديد:\n- الاسم: {name}\n- السن: {age}\n- العنوان: {address}\n- الهاتف: {phone}"
            msg_encoded = urllib.parse.quote(booking_msg)
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text={msg_encoded}"
            
            st.success("بياناتك جاهزة!")
            # زرار الواتساب
            st.markdown(f'<a href="{whatsapp_link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold;
