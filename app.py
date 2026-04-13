import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# 2. البيانات والروابط الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
map_location_url = "https://maps.google.com/?q=31.1345,31.7225" # إحداثيات تقريبية لمنية النصر

video_ids = [
    "1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL",
    "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi",
    "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0",
    "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1",
    "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"
]

# 3. إدارة التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        if submit and u_name and u_phone:
            msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}")
            st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)
    
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar) - تعديل العنوان والأرقام
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 أرقام التواصل")
    st.success("📱 01055901090")
    st.success("📱 01055907095")
    
    st.write("---")
    st.markdown("### 📍 العنوان بالتفصيل")
    st.info("الدقهليه - منيه النصر - شارع البحر\n\n(أعلى يونيكورن - الدور الخامس)")
    
    # زرار اللوكيشن بتصميم أوضح
    st.markdown(f'<a href="{map_location_url}" target="_blank" style="background-color: #EA4335; color: white; padding: 10px; text-decoration: none; border-radius: 5px; display: block; text-align: center;">📍 افتح الموقع على الخريطة</a>', unsafe_allow_html=True)
    
    # إطار الخريطة
    map_html = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3410.875225438!2d31.7225!3d31.1345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzHCsDA4JzA0LjIiTiAzMcKwNDMnMjEuMCJF!5e0!3m2!1sar!2seg!4v1620000000000!5m2!1sar!2seg" width="100%" height="200" style="border:0; border-radius:10px;" allowfullscreen="" loading="lazy"></iframe>'
    st.markdown(map_html, unsafe_allow_html=True)
    
    st.write("---")
    st.caption("شكراً لاختياركم بيوتي سنتر يارا ثروت 💕")
