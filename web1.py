from bs4 import BeautifulSoup

page = open("D:\\Python\\Bit_Camp_Python\\test01.html", "rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

#<p> 전체를 가져오기
# print(soup.find_all("p"))

#첫번째 <p> 검색
# print(soup.find("p"))

#조건이 있는경우 <p class="outer-text">
# print(soup.find_all("p", class_="outer-text"))

#태그를 검색해서 컨텐츠만 가져오기
# for item in soup.find_all("p"):
#     print(item.text.strip())

for item in soup.find_all("p"):
    title = item.text.strip().replace("\n", "")
    title2 = title.replace("\t", "")
    print(title2)