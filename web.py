from urllib.request import urlopen
# 내장함수
import requests as req
# requests => 요청하는거 웹에ㅔ 요청한 결과값을 얻어올수있는 모듈
from bs4 import BeautifulSoup
# 웹에 요청한 결과를 조작해주는 모듈, 셀레니움도 같은역활함


def main():
    search = input("어떤 이미지를 저장하시겠습니까?\n")
    #입력 값 search로 저장
    #https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch
    url_info = "https://www.google.co.kr/search?"


    params = {
        "q" : search,
        #입력값을 parmas로 날림
        "tbm":"isch"
    }
    #딕셔너리

    html_object = req.get(url_info,params)
    #GET이라는 함수에 url, params 두변수를 넣음
    #html_object에 파싱한 값 들어있음(html 소스)


    if html_object.status_code == 200:
        #html_object가 상태코드 200 이면 실행 (200은 정상실행)
        bs_object = BeautifulSoup(html_object.text,"html.parser")
        #인스턴스 만드는것, html_object 텍스트로 변경해서 parser로 지정
        img_data = bs_object.find_all("img")
        #리턴값 img 인것들 변수에 넣음, img 태그 뽑기

        for i in enumerate(img_data[1:]):
            #enumerate 함수 써서 반복문 이미지(img)태그 전체 돌림
            t = urlopen(i[1].attrs['src']).read()
            #이미지 소스 즉 src 만 뽑아서 읽고 t에 저장
            filename = search+str(i[0]+1)+'.jpg'
            #파일이름 +순서+,jpg로 저장
            with open(filename,"wb") as f:
                #파일 생성 with가 알아서 close 해줌
                f.write(t)
            print(str(i[0]+1)+"번째 이미지 저장")


if __name__=="__main__":
    main()
