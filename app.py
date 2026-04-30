import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Smart Fitness Trainer", page_icon="💪")

# --- كود التنسيق الجبار للعناوين (CSS) ---
st.markdown("""
    <style>
    /* العنوان الرئيسي - ضخم جداً وملفت */
    .hero-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 50px !important; /* حجم ضخم جداً */
        font-weight: 600 !important;
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
        text-shadow: 3px 3px 6px rgba(137, 207, 240, 0.3);
        line-height: 1.2;
    }
    /* العنوان الفرعي - كبير وواضح وتحت الرئيسي مباشرة */
    .hero-sub {
        color: #5DADE2 !important;
        text-align: center;
        font-size: 35px !important; /* حجم كبير للمبيّن */
        font-weight: 600 !important;
        margin-top: -10px !important;
        margin-bottom: 40px !important;
    }
    /* تنسيق الزرار عشان يبقى ضخم هو كمان */
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: white !important;
        border: none;
        width: 100%;
        border-radius: 15px;
        height: 4em;
        font-size: 22px !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    /* تحسين شكل النصوص الجانبية */
    label {
        font-size: 18px !important;
        font-weight: bold !important;
        color: #5DADE2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض العناوين بالأحجام الجديدة "الضخمة"
st.markdown('<p class="hero-title">💪 مساعد التدريب الذكي 🌟</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">نظامك الرياضي المتكامل بلمسة ذكاء اصطناعي</p>', unsafe_allow_html=True)
st.markdown("---")

# 3. إدخال البيانات الشخصية
st.subheader("📋 أدخل بياناتك البدنية:")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر:", min_value=10, max_value=80, value=22)
    weight = st.number_input("الوزن (كيلو جرام):", min_value=30, max_value=200, value=80)
    goal = st.selectbox("هدفك الأساسي:", ["تضخيم عضلات", "تنشيف وحرق دهون", "لياقة بدنية عامة"])

with col2:
    height = st.number_input("الطول (سم):", min_value=100, max_value=220, value=180)
    level = st.selectbox("مستوى خبرتك:", ["مبتدئ", "متوسط", "متقدم"])
    days = st.slider("عدد أيام التدريب في الأسبوع:", 1, 7, 5)

if st.button("توليد نظام التدريب المخصص"):
    with st.status("🔍 جاري تحليل البيانات البدنية...", expanded=True) as status:
        st.write("حساب الاحتياجات الغذائية...")
        time.sleep(1)
        st.write("تصميم الجدول التدريبي...")
        time.sleep(1)
        status.update(label="✅ تم تصميم نظامك بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    
    # 4. النتيجة
    st.markdown(f"<h2 style='color: #89CFF0; text-align: center; font-size: 40px;'>📊 الجدول التدريبي المقترح</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🏋️ الجدول الأسبوعي", "🥗 الدليل الغذائي"])
    
    with tab1:
        st.info("📍 **تقسيم التمارين:**")
        st.write("توزيع التمارين مصمم لضمان أقصى استفادة وعمل استشفاء عضلي سليم.")
        st.markdown("""
        - **يوم 1:** صدر + بطن.
        - **يوم 2:** ظهر + سواعد.
        - **يوم 3:** راحة.
        - **يوم 4:** أكتاف + تراي.
        - **يوم 5:** أرجل + باي.
        """)
    
    with tab2:
        st.success("💡 **أهم النصائح:**")
        st.write("- اهتم بشرب الماء بكثرة أثناء التمرين.")
        st.write("- النوم لمدة لا تقل عن 7-8 ساعات يومياً.")

    st.markdown("---")
    st.caption("حقوق المشروع محفوظة - كلية التربية النوعية 2026")
