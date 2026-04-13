import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. نظام التنقل التلقائي (Session State)
# ده بيضمن إن الموقع يفتح على الرئيسية وميبقاش فاضي
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# 4. الشريط الجانبي (ثابت فيه التليفون والعنوان)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")
    
    # زرار العودة بيظهر "فقط" لو إنت مش في الصفحة الرئيسية
    if st.session_state.page != 'home':
        st.write("---")
        st.button("🏠 القائمة الرئيسية", on_click=go_to, args=('home',), use_container_width=True)

# --- محتوى الصفحات ---

# الصفحة الرئيسية
if st.session_state.page == 'home':
    col_logo = st.columns([1, 2, 1])
    with col_logo[1]:
        st.image(logo_url, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>اختار القسم الذي تريده:</p>", unsafe_
