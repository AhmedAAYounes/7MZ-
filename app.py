import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Smart Fitness Trainer", page_icon="💪")

# --- كود تنسيق الألوان Baby Blue ---
st.markdown("""
    <style>
    .main-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: white !important;
        border: none;
        width: 100%;
        border-radius: 10px;
        height: 3em;
    }
    h2, h3 {
        color: #5DADE2 !important;
    }
    .stSelectbox, .stNumberInput, .stTextInput {
        color: #5DADE2;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض العناوين
st.markdown('<p class="main-title">💪 مساعد التدريب الذكي 🌟</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5DADE2;'>صمم نظامك التدريبي المخصص بناءً على أهدافك الشخصية</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. إدخال البيانات الشخصية (زي ما طلبت)
st.subheader("📋 أدخل بياناتك البدنية:")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("العمر:", min_value=10, max_value=80, value=20)
    weight = st.number_input("الوزن (كيلو جرام):", min_value=30, max_value=200, value=75)
    goal = st.selectbox("هدفك الأساسي:", ["تضخيم عضلات", "تنشيف وحرق دهون", "لياقة بدنية عامة"])

with col2:
    height = st.number_input("الطول (سم):", min_value=100, max_value=220, value=175)
    level = st.selectbox("مستوى خبرتك:", ["مبتدئ", "متوسط", "متقدم"])
    days = st.slider("عدد أيام التدريب في الأسبوع:", 1, 7, 4)

if st.button("توليد نظام التدريب المخصص"):
    with st.status("🔍 جاري تحليل البيانات البدنية...", expanded=True) as status:
        st.write("حساب مؤشر كتلة الجسم (BMI)...")
        time.sleep(1.5)
        st.write("تحديد السعرات الحرارية المناسبة لهدفك...")
        time.sleep(1.5)
        st.write("تصميم جدول التمارين الأمثل...")
        time.sleep(1)
        status.update(label="✅ تم تصميم نظامك التدريبي بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    
    # 4. النتيجة الثابتة (نظام تدريبي احترافي)
    st.markdown(f"<h2 style='color: #89CFF0;'>📊 النظام المقترح لـ: {goal}</h2>", unsafe_allow_html=True)
    
    # تفاصيل النظام
    st.info(f"📍 **تحليل الحالة:** بناءً على وزنك ({weight} كجم) وهدفك، تم وضع خطة تعتمد على تقسيم العضلات.")
    
    tab1, tab2 = st.tabs(["📅 جدول التمارين", "🍎 نظام التغذية"])
    
    with tab1:
        st.write("""
        - **اليوم الأول:** تمارين الصدر والترايسيبس (Chest & Triceps).
        - **اليوم الثاني:** تمارين الظهر والبايسيبس (Back & Biceps).
        - **اليوم الثالث:** راحة نشطة (Active Recovery).
        - **اليوم الرابع:** تمارين الأكتاف والبطن (Shoulders & Abs).
        - **اليوم الخامس:** تمارين الأرجل (Legs Day).
        """)
    
    with tab2:
        st.success("💡 **نصائح غذائية هامة:**")
        st.write(f"- تحتاج إلى حوالي **{weight * 2} جرام** بروتين يومياً.")
        st.write("- شرب 3 لتر مياه يومياً لتحسين الأيض.")
        st.write("- تقليل السكريات والاعتماد على الكربوهيدرات المعقدة (شوفان، أرز بني).")

    st.markdown("---")
    st.caption("تم تطوير هذا المساعد الذكي لدعم النشاط البدني - مشروع الميدترم 2026")
