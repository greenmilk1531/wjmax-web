lastlink = "https://cafe.naver.com/steamindiegame/18334183" #모기형 마지막 패치 링크


#toolbarMode = "minimal"
import streamlit as st
import time
from PIL import Image
from streamlit_modal import Modal

공지 = 0 #공지를 0으로 설정

st.set_page_config(
    page_title="WJMAX",
    page_icon="wjmax.webp"  # 이모지 아이콘 또는 URL을 통해 커스텀 이미지 추가
)

# 헤더 숨기기 위한 스타일 적용
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

@st.dialog("공지사항") # 타이틀
def vote():
    st.info("왁제이맥스 3주 업데이트 선언! 및 콜라보 선언!")
    st.link_button("보러가기", lastlink)
    

if 공지 != 1: #공지를 읽지 않았을때만 보여줌
    vote()
    공지 = 1

title,imgs = st.columns([2,7])
with title:
    st.title("WJMAX")
with imgs:
    wjmax_img = Image.open('wjmax.webp')
    st.image(wjmax_img)
    st.markdown("""
<style>
img {
	max-height: 94px;
}
</style>
""", unsafe_allow_html=True)
b,c,soop = st.columns([3,4,19])
with b:
    st.link_button("카페", "https://cafe.naver.com/moogimogi")
with c:
    st.link_button("다운로드", "https://cafe.naver.com/steamindiegame/12309318")

with soop:
    st.link_button("숲(SOOP)","https://bj.afreecatv.com/doob32")

e,d,ha,se = st.columns([4.5,4,5,15])
with e:
    st.link_button("last patch", lastlink)
with d:
    st.link_button("패치내역", "https://namu.wiki/w/%EC%99%81%EC%A0%9C%EC%9D%B4%EB%A7%A5%EC%8A%A4/%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%20%EB%82%B4%EC%97%AD#toc")
with ha:
    st.link_button("수록곡 보기","https://namu.wiki/w/%EC%99%81%EC%A0%9C%EC%9D%B4%EB%A7%A5%EC%8A%A4/%EC%88%98%EB%A1%9D%EA%B3%A1")
with se:
    st.link_button("검색하기","검색")
st.markdown("""
<iframe width="400" height="225" 
src="https://www.youtube.com/embed/ClCjvkpKJnY" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
""", unsafe_allow_html=True)


st.text("*- 왁맥 공식사이트가 아닙니다")
st.text("원작게임: DJMAX")