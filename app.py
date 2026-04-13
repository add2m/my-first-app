import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة للموبايل
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. نظام التنقل التلقائي (عشان الصفحة ما تظهرش فاضية)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# 4. القائمة الجانبية (معلومات فقط)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل\n01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان\nمنيه النصر - الدقهلية")

# --- محتوى الصفحات ---

# أ. الصفحة الرئيسية
if st.session_state.page == 'home':
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>بيوتي سنتر يارا ثروت</h2>", unsafe_allow_html=True)
    
    # أزرار موبايل كبيرة
    st.button("📅 حجز موعد", use_container_width=True, on_click=go_to, args=('booking',))
    st.button("💰 قائمة الأسعار", use_container_width=True, on_click=go_to, args=('prices',))
    st.button("✨ معرض الأعمال", use_container_width=True, on_click=go_to, args=('gallery',))

# ب. صفحة الحجز
elif st.session_state.page == 'booking':
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        if submit and u_name and u_phone:
            msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالهاتف: {u_phone}")
            st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)
    
    st.write("---")
    st.button("🏠 العودة للرئيسية", use_container_width=True, on_click=go_to, args=('home',))

# ج. صفحة الأسعار
elif st.session_state.page == 'prices':
    st.markdown("### 💰 الأسعار")
    st.info("سيتم إضافة الصور قريباً")
    st.button("🏠 العودة للرئيسية", use_container_width=True, on_click=go_to, args=('home',))

# د. صفحة المعرض
elif st.session_state.page == 'gallery':
    st.markdown("### ✨ أعمالنا")
    st.success("سيتم إضافة الصور قريباً")
    st.button("🏠 العودة للرئيسية", use_container_width=True, on_click=go_to, args=('home',))

# تذييل الصفحة
st.write("---")
st.caption("مركز يارا ثروت - منيه النصر")
