import requests
from bs4 import BeautifulSoup


def moviename():
    url = r"https://movie.naver.com/movie/sdb/rank/rmovie.naver"
    header={
        'Referer': "http://eclass.kpu.ac.kr/ilos/main/main_form.acl",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
        }
    req=requests.get(url, headers=header)
    chart = []
    soup=BeautifulSoup(req.text,'html.parser')
    movielink=soup.find("tbody")
    for href in movielink.find_all("td",{"class":"title"}):
        url2=r"https://movie.naver.com/"+href.find("a")["href"]
        req=requests.get(url2,headers=header)
        soup=BeautifulSoup(req.text,'html.parser')
        movieinfo=soup.find("div",{"class":"mv_info"})
        moviespec=soup.find("dl",{"class","info_spec"})
        moviename=movieinfo.find("a")
        print(moviename.text)
        dd=moviespec.find_all("dd")
        ##영화 개요
        import pprint
        movie11=dd[0].find("p").find("span")
        pprint.pprint(movie11)
        for i in movie11.find_all("a"):
            movie1=i.get_text().strip()
        ###영화 날짜
        try:
            movie22=dd[0].find("p").find_all("span")[3]
            for i in movie22.find_all("a"):
                movie2= i.get_text().strip()
        except Exception:
            movie22=dd[0].find("p").find_all("span")[2]
            for i in movie22.find_all("a"):
                movie2= i.get_text().strip()
        ##감독
        movie3=dd[1].find("a").text
        print(f"{movie1} | {movie2} | {movie3}\n")
moviename()