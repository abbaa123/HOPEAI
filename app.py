import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# 1. إعدادات الهوية البصرية لـ Hope AI (الأزرق والأبيض)
# ==========================================
st.set_page_config(
    page_title="Hope AI - ذكاء الأمل",
    page_icon="✨",
    layout="wide"
)

# تصميم واجهة احترافية تعبر عن الأمل والمستقبل
st.markdown("""
    <style>
    /* تغيير الخلفية العامة */
    .stApp {
        background-color: #f0f4f8;
    }
    /* تنسيق العناوين باللون الأزرق الملكي */
    h1, h2, h3 {
        color: #004aad !important;
        font-family: 'Segoe UI', sans-serif;
    }
    /* تنسيق الأزرار */
    .stButton>button {
        background-color: #004aad;
        color: white !important;
        border-radius: 20px;
        border: none;
        padding: 0.6rem 2rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #003580;
        box-shadow: 0px 4px 15px rgba(0, 74, 173, 0.3);
    }
    /* شريط الجانب */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #e1e8ed;
    }
    /* صندوق التعليمات */
    .info-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-right: 6px solid #004aad;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. القائمة الجانبية (Sidebar) - بوابة المستخدمين
# ==========================================
with st.sidebar:
    # الشعار الجديد (أيقونة تعبر عن الأمل والذكاء)
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>✨</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Hope AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>نزرع الأمل بالمعرفة</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔑 تفعيل المنصة")
    # بما أن الاستخدام عام، كل مستخدم يضع مفتاحه الخاص لضمان الخصوصية والتشغيل المجاني
    user_key = st.text_input("أدخل مفتاح Gemini API Key الخاص بك:", type="password", help="مفتاحك الشخصي يبقى مشفراً ولا نطلع عليه.")
    
    st.markdown("---")
    st.markdown("### عن المبادرة 🇮🇶")
    st.write("منصة Hope AI هي مشروع عراقي طموح يهدف لتمكين الشباب والطلبة عبر أدوات الذكاء الاصطناعي الأكثر تطوراً في العالم.")
    st.info("الاستخدام عام ومفتوح لجميع أبناء الشعب العراقي.")

# ==========================================
# 3. الواجهة الرئيسية
# ==========================================
col1, col2 = st.columns([3, 1])

with col1:
    st.title("مرحباً بك في Hope AI ✨")
    st.markdown("#### بوابتك الذكية لمستقبل أفضل.. كيف يمكن لـ 'الأمل' مساعدتك اليوم؟")

st.write("---")

# هندسة شخصية Hope AI (إيجابية، ملهمة، وداعمة بالهوية العراقية)
hope_instruction = """
أنت الآن ذكاء اصطناعي عراقي متطور اسمك "Hope AI" (ذكاء الأمل).
رسالتك: تقديم المساعدة، نشر التفاؤل، وتبسيط العلم والعمل لكل العراقيين.

قواعدك:
1. الشخصية: أنت ملهم، محفز، ذكي جداً، وودود للغاية.
2. اللغة: تتحدث بالعربية الفصحى البسيطة والجميلة، وتفهم وتتفاعل ببراعة مع اللهجة العراقية.
3. التفاعل العراقي: استخدم كلمات عراقية دافئة (مثل: "عيوني"، "منور"، "تدلل"، "عاش بيتكم") لتجعل المستخدم يشعر أنه يتحدث مع أخ أو صديق عراقي ذكي.
4. المهمة: ركز على تحويل المشاكل إلى حلول، وقدم الإجابات بأسلوب منظم جداً (نقاط، جداول، خطوات).
5. الهدف: كن شعلة أمل في كل جواب، شجع المستخدم على الدراسة، العمل، وبناء مستقبله.
"""

# ==========================================
# 4. محرك الدردشة والمعالجة
# ==========================================
if not user_key:
    # عرض خطوات واضحة للجمهور العراقي حول كيفية البدء
    st.markdown("""
    <div class="info-box">
        <h4>💡 كيف تبدأ باستخدام Hope AI مجاناً؟</h4>
        <ol>
            <li>احصل على مفتاحك المجاني من موقع جوجل الرسمي: <b><a href="https://aistudio.google.com/" target="_blank">Google AI Studio</a></b></li><li>اضغط على <b>Create API Key</b> وانسخ الكود الذي يظهر لك.</li>
            <li>الصق الكود في خانة <b>"تفعيل المنصة"</b> على اليسار وابدأ بسؤال Hope AI عن أي شيء!</li>
        </ol>
        <i>* خصوصيتك مقدسة؛ محادثاتك ومفتاحك لا يتم حفظها في أي قاعدة بيانات.</i>
    </div>
    """, unsafe_allow_html=True)
else:
    try:
        # ربط المحرك بمفتاح المستخدم
        client = genai.Client(api_key=user_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # عرض المحادثة
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # استقبال سؤال المستخدم
        if prompt := st.chat_input("اسأل Hope AI.."):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant", avatar="✨"):
                message_placeholder = st.empty()
                
                # إرسال الطلب لنموذج Gemini 2.5 Flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=hope_instruction,
                        temperature=0.7,
                    )
                )
                
                full_response = response.text
                message_placeholder.markdown(full_response)
                
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error("⚠️ المفتاح الذي أدخلته غير صحيح أو أن الخدمة مشغولة حالياً. يرجى التأكد من الـ API Key الخاص بك.")