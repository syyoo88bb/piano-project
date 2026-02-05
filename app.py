import streamlit as st

st.write("음악과 기술이 만나는 곳, 저의 피아노 프로젝트에 오신 것을 환영합니다!")
with st.sidebar:
    st.header("Prof. Elsa") # 선생님 이름이나 직함


    # '이력서 보기' 메뉴 만들기 (클릭하면 열림)
    with st.expander("📄 Prof. Elsa 이력서 보기 (Click)"):
        st.markdown("""
        ### 🎓 Education
       *D.M.A.in Piano Performance(UIUC, USA 2005)
       *Dissertation:"A Study of Selected Piano Works of Samuel Adler" 
       *M.M.in Piano Performance(UIUC, USA 2001)
       *B.M.in Piano Performance(SNU, Seoul, Korea, 1997)
        
        ---
        
        ### 💼 Experience
        * **목원대, 전남대, 건국대, 강남대, 숙명여대, 삼육대, 숭실 컨서바토리, 백석 컨서바토리, 계원예중,고 강사 역임
        * **주요 피아노 콩쿨 심사위원** 위촉
        * 국내외 독주회 및 협연 다수
        * 20년 이상 전문 연주자 및 교육자로 활동 중
        
        ---
        
        ### 📧 Contact
        * syyoo88bb@gmail.com
        """)
            
# ==========================================
# [여기까지]
# ==========================================
# 1. 페이지 제목과 아이콘 설정
st.set_page_config(page_title="My Piano World", page_icon="🎹")

# 2. 제목과 소개글
st.title("🎹 [Elsa]의 피아노 이야기")


# 3. 멋진 피아노 사진 (인터넷 주소로 이미지 넣기)
st.image("piano1.png", caption="Music is Life")

# 4. 내용 나누기 (탭 기능)
tab1, tab2 = st.tabs(["🎵 연주 기록", "📝 연구 노트"])

with tab1:
    st.header("나의 연주")
    st.write("제가 연주한 엘가 곡을 감상해보세요.")
    # 유튜브 영상 예시 (나중에 선생님 영상 주소로 바꾸면 돼요!)
    st.video("https://youtu.be/ShyuUs_6Tg4")

with tab2:
    st.header("연구 및 분석")
    st.write("AI와 피아노 연주에 대한 분석 내용을 이곳에 기록합니다.")
    st.info("작성 중인 논문: AI가 해석하는 피아노의 감성")

st.markdown("---") 
note = st.text_area("📝 연구 노트", placeholder="여기에 번뜩이는 아이디어를 자유롭게 적어보세요!")

if st.button("노트 저장하기 💾"):
    if note:
        st.success("Elsa의 아이디어가 화면에 기록됐어! (새로고침하면 사라지니 주의!)")
        st.write(f"**내용:** {note}")
    else:
        st.warning("내용이 비어있어! 😅")
# 👆 여기까지! 👆

# 5. 마무리 버튼
if st.button('응원하기 👏'):
    st.balloons()
    st.success("감사합니다! 더 멋진 연주로 보답할게요!")
