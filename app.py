import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. نظام التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# 4. الشريط الجانبي (ثابت فيه التليفون والعنوان فقط)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول")

# --- محتوى الصفحات ---

# أ. الصفحة الرئيسية
if st.session_state.page == 'home':
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h2>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>اختار القسم الذي تريده:</p>", unsafe_allow_html=True)
    
    # أزرار الأقسام بضغطة واحدة
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
                msg = f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}"
                encoded_msg = urllib.parse.quote(msg)
                link = f"https://wa.me/{whatsapp_num}?text={encoded_msg}"
                st.success("تمام! بياناتك جاهزة.")
                st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">تأكيد الحجز عبر واتساب</a>', unsafe_allow_html=True)
    
    # زرار العودة للقائمة الرئيسية (جوه الصفحة من تحت)
    st.write("---")
    st.button("🏠 العودة للقائمة الرئيسية", use_container_width=True, on_click=go_to, args=('home',))

# ج. صفحة الأسعار
elif st.session_state.page == 'prices':
    st.markdown("<h2 style='text-align: center;'>💰 قائمة الأسعار</h2>", unsafe_allow_html=True)
    st.info("سيتم إضافة صور المنيو هنا قريباً...")
    
    # زرار العودة للقائمة الرئيسية (جوه الصفحة من تحت)
    st.write("---")
    st.button("🏠 العودة للقائمة الرئيسية", use_container_width=True, on_click=go_to, args=('home',))

# د. صفحة المعرض
elif st.session_state.page == 'gallery':
    st.markdown("<h2 style='text-align: center;'>✨ معرض أعمالنا</h2>", unsafe_allow_
