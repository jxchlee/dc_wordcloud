![image](image.png)


# dc_wordcloud
dcinside 워드클라우드 이미지 생성 파이썬 스크립트

<strong>
이 Repository는 [dc_wordcloud](https://github.com/pdjdev/dc_wordcloud) 를 fork 하여 수정, 보완한 코드입니다.
원본 설명에 대해 수정, 보충한 부분은 굵은 글씨로 설명을 추가하였습니다.
run.py는 원본 코드, run2.py는 수정한 코드입니다. 따라서 run.py는 굵은 글씨 설명을 따르지 않아도 실행이 가능합니다.
</strong>



## 사용법
1. `pip install requests bs4 lxml matplotlib wordcloud` 로 필요한 패키지를 설치합니다

<strong>
    &emsp;
추가적으로 konlpy를 설치해야합니다.
`pip install konlpy`
운영체제마다 명령어에 차이가 있고 윈도우의 경우 konlpy 사용을 위해선 JDK가 설치되어있어야 합니다. 자세한 설치 방법은 [링크](https://konlpy.org/ko/latest/index.html#) 를 참고해주세요.

</strong>

2. 스크립트 폴더 안에 사용할 폰트를 넣고 파일명을 `font.otf`로 설정합니다. (`*.ttf` 형식의 클리어타입일 경우 스크립트 맨 위의 `fontpath='font.otf'` 부분을 변경하시면 됩니다)

3. 스크립트를 실행합니다. 순서대로 갤러리 이름, 검색어, 페이지 범위를 입력합니다.

<strong>

&emsp;
- 검색어의 경우 그냥 아무 입력없이 엔터를 눌러도 '*' 를 입력한 것으로 처리합니다.

- 페이지는 숫자만 입력하면 1페이지부터 숫자페이지까지 조회하고 '3-5'처럼 '-' 기호를 사용하면 3페이지부터 5페이지 같이 시작페이지를 설정할 수 있습니다.

</strong>

4. 처리가 완료되고 생성되는 두 이미지 파일 (title.png, nick.png) 파일을 확인합니다.
