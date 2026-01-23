import streamlit as st

# 1. 페이지 제목과 아이콘 설정
st.set_page_config(page_title="My Piano World", page_icon="🎹")

# 2. 제목과 소개글
st.title("🎹 [Elsa]의 피아노 이야기")
st.write("음악과 기술이 만나는 곳, 저의 피아노 프로젝트에 오신 것을 환영합니다!")

# 3. 멋진 피아노 사진 (인터넷 주소로 이미지 넣기)
st.image("https://https://www.canva.com/design/DAG_P4hxUFw/CGgTMBjX0Pzk3IvX6F7n8g/edit?ui=eyJEIjp7IkoiOnsiRCI6eyJBPyI6IkMifX19LCJBIjp7IkEiOiJkb3dubG9hZF9wbmciLCJGIjp0cnVlfSwiRyI6eyJEIjp7IkQiOnsiQT8iOiJBIiwiQSI6IkIifX19fQ", caption="Music is Life")

# 4. 내용 나누기 (탭 기능)
tab1, tab2 = st.tabs(["🎵 연주 기록", "📝 연구 노트"])

with tab1:
    st.header("나의 연주")
    st.write("제가 연주한 베버 곡을 감상해보세요.")
    # 유튜브 영상 예시 (나중에 선생님 영상 주소로 바꾸면 돼요!)
    st.video("https://youtu.be/Nu70WEsjz88?si=2Pr4585N-BqBCt7")

with tab2:
    st.header("연구 및 분석")
    st.write("AI와 피아노 연주에 대한 분석 내용을 이곳에 기록합니다.")
    st.info("작성 중인 논문: AI가 해석하는 피아노의 감성")

# 5. 마무리 버튼
if st.button('응원하기 👏'):
    st.balloons()
    st.success("감사합니다! 더 멋진 연주로 보답할게요!")
