import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# 2. الروابط الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"

# --- ستايل الأزرار لتظهر بشكل احترافي وتفتح في صفحة جديدة ---
st.markdown("""
    <style>
    .google-btn {
        display: block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        background-color: #D4AF37; /* لون ذهبي */
        color: white !important;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        border: none;
    }
    .google-btn:hover {
        background-color: #B8860B; /* لون أغمق عند اللمس */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل\n01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان\nالدقهليه - منيه النصر - شارع البحر\nمقابل استار مول - اعلى يونيكورن الدور الخامس")

# --- محتوى الصفحة الرئيسية ---
st.image(logo_url, use_container_width=True)
st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)

st.write("<p style='text-align: center;'>اختار القسم الذي تريده (سيفتح في صفحة جديدة):</p>", unsafe_allow_html=True)

# 4. الأزرار التي تفتح صفحات خارجية على جوجل
# ملحوظة: يمكنك تغيير الروابط بالأسفل لأي روابط تريدها
st.markdown('<a href="https://www.google.com" target="_blank" class="google-btn">📅 للحجز</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.google.com/search?q=أسعار+بيوتي+سنتر" target="_blank" class="google-btn">💰 قائمة الأسعار</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.google.com/search?q=صور+تجميل" target="_blank" class="google-btn">✨ صور لشغلنا</a>', unsafe_allow_html=True)

# تذييل الصفحة
st.write("---")
st.caption("شكرا لاختياركم بيوتي سنتر يارا ثروت💕")
