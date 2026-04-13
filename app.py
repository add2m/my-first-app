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
    st.markdown("<h
