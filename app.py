import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Smart Fitness Trainer", page_icon="💪")

# --- كود تنسيق الألوان والأحجام (CSS) ---
st.markdown("""
    <style>
    /* العنوان الرئيسي - كبير وواضح */
    .main-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 55px; /* تكبير الحجم */
        font-weight: 800;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px #d6eaf8;
    }
    /* العنوان الفرعي - أصغر قليلاً من الرئيسي */
    .sub-title {
        color: #5DADE2 !important;
        text-align: center;
        font-size: 28px; /* حجم متوسط */
        font-weight: 500;
        margin-top: 0px;
        margin-bottom: 30px;
    }
    /* تنسيق الزرار */
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: white !important;
        border: none;
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
    }
    h2, h3 {
        color: #5DADE2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض العناوين بالأحجام الجديدة
st.markdown('<p class="main-title">💪 مساعد التدريب الذكي 🌟</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">صمم نظامك التدريبي المخصص بناءً على أهدافك</p>', unsafe_allow_html=True)
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
        st.write("حساب مؤشر كتلة الجسم (BMI)...")
        time.sleep(1.5)
        st.write("تحديد الاحتياج اليومي من السعرات...")
        time.sleep(1.5)
        status.update(label="✅ تم تصميم نظامك التدريبي بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    
    # 4. النتيجة
    st.markdown(f"<h2 style='color: #89CFF0;'>📊 النظام المقترح لـ: {goal}</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📅 جدول التمارين", "🍎 نظام التغذية"])
    
    with tab1:
        st.info("📍 **خطة التدريب الأسبوعية:**")
        st.write("""
        - **السبت:** صدر + بطن.
        - **الأحد:** ظهر + سواعد.
        - **الاثنين:** راحة.
        - **الثلاثاء:** أكتاف + ترايسيبس.
        - **الأربعاء:** أرجل + بايسيبس.
        - **الخميس والجمعة:** كارديو خفيف أو راحة.
        """)
    
    with tab2:
        st.success("💡 **توصيات التغذية:**")
        st.write(f"- الالتزام بوجبات غنية بالبروتين (صدور دجاج، سمك، بيض).")
        st.write("- توزيع الوجبات على 4-5 مرات يومياً.")
        st.write("- الابتعاد عن الوجبات السريعة والمشروبات الغازية.")

    st.markdown("---")
    st.caption("تم تطوير هذا المساعد الذكي لدعم النشاط البدني - مشروع الميدترم 2026")
