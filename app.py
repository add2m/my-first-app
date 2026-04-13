import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة للموبايل
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. التأكد من فتح الصفحة الرئيسية فوراً
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# 4. الشريط الجانبي الثابت (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول")
    
    # زرار الرجوع يظهر في الجنب "فقط" لو العميل داخل صفحة فرعية
    if st.session_state.page != 'home':
        st.write("---")
        st.button("🏠 العودة للرئيسية", on_click=go_to, args=('home',), use_container_width=True)

# --- محتوى الصفحات ---

# أ. الصفحة الرئيسية
if st.session_state.page == 'home':
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h2>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>اختار القسم الذي تريده:</p>", unsafe_allow_html=True)
    
    # أزرار كبيرة للموبايل بضغطة واحدة
    st.button("📅 حجز موعد", use_container_width=True, on_click=go_to, args=('booking',))
    st.button("💰 قائمة الأسعار", use_container_width=True, on_click=go_to, args=('prices',))
    st.button("✨ معرض الأعمال", use_container_width=True, on_click=go_to, args=('gallery',))

# ب. صفحة الحجز
elif st.session_state.page == 'booking':
    st.markdown("<h2 style='text-align: center;'>بيانات الحجز</h2>", unsafe_allow_html=True)
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان بالتفصيل")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        
        if submit:
            if u_name and u_phone:
                # تنسيق الرسالة لضمان الترتيب الصحيح في واتساب
                msg = f"حجز جديد من الموقع\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}"
                encoded_msg = urllib.parse.quote(msg)
                link = f"https://wa.me/{whatsapp_num}?text={encoded_msg}"
                st.success("تمام! بياناتك جاهزة.")
                st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">تأكيد الحجز عبر واتساب</a>', unsafe_allow_html=True)
            else:
                st.error("يرجى كتابة الاسم ورقم الهاتف على الأقل.")

# ج. صفحة الأسعار (مكان فاضي للصور)
elif st.session_state.page == 'prices':
    st.markdown("<h2 style='text-align: center;'>💰 قائمة الأسعار</h2>", unsafe_allow_html=True)
    st.info("ابعت لي صور المنيو عشان نحطها هنا")

# د. صفحة المعرض (مكان فاضي للصور)
elif st.session_state.page == 'gallery':
    st.markdown("<h2 style='text-align: center;'>✨ معرض أعمالنا</h2>", unsafe_allow_html=True)
    st.success("ابعت لي صور الشغل عشان أرتبها لك هنا")

# تذييل بسيط
st.write("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>مركز يارا ثروت - جمالك هو تخصصنا</p>", unsafe_allow_html=True)
