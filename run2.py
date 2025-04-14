import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests, lxml, os
from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Hannanum
from collections import Counter
import sys

# 글자 필터링
mystop = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다', '그','너','나','테','니','뇨','진짜', '굳이', '뭔가','하고','못하면','안','요즘','자꾸','거임','어떤', '을','있다','아','암','어케','했으면','그나마','쎈','걍','일단','하는디','나는', '보고','할','이런','나','무슨','아니냐','좋은','또','아직','님들','없나','딱','원래','같음','많이','좋겠다','뭐임','뭔','뭐','요즘','하는','못','같은','와','안됨','이거','더','그래도','그냥','이게','혹시','저거','어떻게', '됨']
stopwords = set(STOPWORDS)
for i in mystop:
    stopwords.add(i)


fontpath='C:/Windows/Fonts/malgun.ttf'
#게시글 수, 가장 많은 단어 top 10

tdata = ''
ndata = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

name = input('갤러리 입력:')
keyword = input('검색어 입력(*=전체):')
if keyword == '': keyword = '*'
last_page = input('조회 페이지 범위 입력(최소 1 이상, \'3-5\'로 특정 시점 조회 가능):')
first_page = 1
if '-' in last_page:
    try:
        num = last_page.split('-')
        first_page = int(num[0])
        last_page = int(num[1])
    except:
        sys.exit("숫자 입력 오류.")
else:
    last_page = int(last_page)
print('갤러리 검색중...')
r = requests.get('https://search.dcinside.com/gallery/q/' + name, headers = headers).text

if 'integrate_cont_list' in r:

    bs = BeautifulSoup(r, 'lxml')
    link = bs.find('ul', class_='integrate_cont_list').a['href']

    r = requests.get(link, headers = headers).text

    print('갤러리 형식:', end=' ')
    #마이너 갤러리일 경우
    if 'location.replace' in r:
        link = link.replace('board/','mgallery/board/')
        
        print('마이너')
    else:
        print('정식')
        
    for i in range(first_page, last_page + 1):
        #print('페이지 읽는 중... [{}/{}]'.format(i, last_page), end='\r')
        print(f'페이지 읽는 중... [{i}/{last_page}]')
        r = requests.get(link + '&page=' + str(i), headers = headers).text    
        bs = BeautifulSoup(r, 'lxml')

        tmp1 = bs.find_all('td', class_='gall_tit ub-word')
        tmp2 = bs.find_all("td", {"class", "gall_writer ub-writer"})

        post_data = zip(tmp1, tmp2)
        
        for s in post_data:
             if str(s[0]).find('<b>')==-1 and s[1]['data-nick'].strip() != 'ㅇㅇ': ndata += s[1]['data-nick'].strip() + '\n'

        tmp2 = bs.find_all('td', class_='gall_num')

        post_data = zip(tmp1, tmp2)

        for s in post_data:
            if str(s[0]).find('<b>')==-1 and ((keyword in s[0].find('a').text) or keyword=='*'):
                tdata += s[0].find('a').text + '\n'


    #제목 nlp 사용해서 명사 분리
    hannanum = Hannanum()
    nouns = hannanum.nouns(tdata)

    #한글자 명사 제외
    new_nouns = []
    for n in nouns:
        if len(n)>1: new_nouns.append(n)

    #Counter 사용해서 글자수 세기
    cnt = Counter(new_nouns)

    #워드 클라우드 생성

    print()
    print('워드클라우드 생성 중... [1/2]', end='\r')
    # wc_title = WordCloud(font_path=fontpath, width=1920, height=1080, background_color='white', stopwords=stopwords).generate(tdata)
    wc_title = WordCloud(font_path=fontpath, width=1920, height=1080, background_color='white',
                         stopwords=stopwords).generate_from_frequencies(cnt)
    
    print('워드클라우드 생성 중... [2/2]')
    wc_nick = WordCloud(font_path=fontpath, width=1920, height=1080, background_color='white', stopwords=stopwords).generate(ndata)

    print('이미지 저장 중...')
    wc_title.to_file('title.png')
    wc_nick.to_file('nick.png')

    print('저장 완료')
    print('<분석 결과>')
    print('게시글 수:', format((last_page-first_page+1)*50,','))
    print('-가장 많은 단어-')
    rank = 1
    for v in cnt.most_common(10):
        print(f'{rank}. {v[0]}: {v[1]}')
        rank += 1

else:
    print('해당 명칭의 갤러리가 없습니다.')



