import streamlit as st


# ==========================================
# [여기서부터 복사하세요] 왼쪽 사이드바 C.V. 설정
# ==========================================
with st.sidebar:
    st.header("Prof. Elsa") # 선생님 이름이나 직함
    
    # 1단계에서 올린 파일 이름이 'cv.pdf'라고 가정할게요!
    # 만약 이름이 다르면 "cv.pdf" 부분을 그 파일 이름으로 고쳐주세요.
    with open("cv.pdf", "rb") as file:
        btn = st.download_button(
            label="📥 Download cv.",  # 버튼에 적힐 글자
            data=file,
            file_name="Elsa_cv.pdf",   # 다운로드될 때 저장될 이름
            mime="application/pdf"
        )
# ==========================================
# [여기까지]
# ==========================================
# 1. 페이지 제목과 아이콘 설정
st.set_page_config(page_title="My Piano World", page_icon="🎹")

# 2. 제목과 소개글
st.title("🎹 [Elsa]의 피아노 이야기")
st.write("음악과 기술이 만나는 곳, 저의 피아노 프로젝트에 오신 것을 환영합니다!")

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
