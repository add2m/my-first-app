import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط الصور والبيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_number = "201055901090"

# 3. عرض اللوجو في منتصف الصفحة
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# 4. الجملة الترحيبية اللي طلبتها
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h3>", unsafe_allow_html=True)

# 5. الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.title("تواصل معنا")
    st.write("📞 01055901090")
    st.write("📞 01055907095")
    st.write("📍 منيه النصر - شارع البحر")

# 6. عنوان فورم الحجز
st.markdown("<h2 style='text-align: right;'>برجاء إدخال البيانات للحجز</h2>", unsafe_allow_html=True)

# 7. فورم إدخال البيانات
with st.form("booking_form"):
    name = st.text_input("الاسم بالكامل")
    age = st.text_input("السن")
    address = st.text_input("العنوان")
    phone = st.text_input("رقم الهاتف")
    email = st.text_input("البريد الإلكتروني")
    
    submit = st.form_submit_button("إرسال البيانات")
    
    if submit:
        if name and address and phone:
            # تجهيز الرسالة للواتساب
            msg = f"حجز جديد من الموقع:\nالاسم: {name}\nالسن: {age}\nالعنوان: {address}\nالهاتف: {phone}"
            msg_encoded = urllib.parse.quote(msg)
            link = f"https://wa.me/{whatsapp_number}?text={msg_encoded}"
            
            st.success("تم تجهيز بياناتك بنجاح!")
            # زرار الواتساب الأخضر
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">اضغط هنا لإرسال الحجز عبر واتساب</a>', unsafe_allow_html=True)
        else:
            st.error("يا آدم، لازم تملأ الاسم والعنوان والتليفون عشان الحجز يكمل.")

#
