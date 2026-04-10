import streamlit as st
import urllib.parse

st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# رابط اللوجو الذهبي
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"

# عرض اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# الجملة الترحيبية
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h3>", unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.image(logo_url, width=150)
    st.title("تواصل معنا")
    st.markdown("---")
    st.write("📞 01055901090")
    st.write("📞 01055907095")
    st.markdown("---")
    st.write("📍 منيه النصر - شارع البحر - مقابل ستار مول - اعلي يونيكورن - الدور الخامس")

# الحالة
if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

# لو لسه ما أكدش البيانات، الفورم لازم تظهر
if not st.session_state.confirmed:
    st.header("برجاء إدخال البيانات التالية للحجز")
    
    # الفورم الأساسية
    with st.form("main_form"):
        name = st.text_input("الاسم بالكامل")
        age = st.number_input("السن", min_value=1, max_value=100, value=20)
        address = st.text_input("العنوان")
        phone = st.text_input("رقم الهاتف")
        email = st.text_input("البريد الإلكتروني")
        
        submit = st.form_submit_button("إرسال البيانات وتأكيد الحجز")
        
        if submit:
            if name and address and phone and email:
                # تجهيز رسالة الواتساب
                msg = f"حجز جديد من موقع يارا ثروت:\n\nالاسم: {name}\nالسن: {age}\nالعنوان: {address}\nالهاتف: {phone}\nالإيميل: {email}"
                msg_encoded = urllib.parse.quote(msg)
                whatsapp_url = f"https://wa.me/201055901090?text={msg_encoded}"
                
                # إظهار رابط التحويل مباشرة
                st.write("---")
                st.success("
