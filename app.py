import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# روابط الصور والبيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_number = "201055901090"

# عرض اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# الجملة الترحيبية
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h3>", unsafe_allow_html=True)

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.title("تواصل معنا")
    st.write("📞 01055901090")
    st.write("📞 01055907095")
    st.write("📍 منيه النصر - شارع البحر")

# فورم إدخال البيانات - دي اللي كانت بتختفي
st.header("برجاء إدخال البيانات للحجز")

with st.form("booking_form"):
    name = st.text_input("الاسم بالكامل")
    age = st.text_input("السن")
    address = st.text_input("العنوان")
    phone = st.text_input("رقم الهاتف")
    email = st.text_input("البريد الإلكتروني")
    
    submit = st.form_
