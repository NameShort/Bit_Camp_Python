strA = "Python is powerful"
print(len(strA))
print(strA.capitalize)
print(strA.count("p"))
print(strA.count("p", 7))
print("demo.ppt".endswith("ppt"))
strB="<<< Spam and Ham >>>"
result = strB.strip()
print(result)

#앞뒤에 있는 캐릭터 제거
result=strB.strip("<>")
print(result)
result2=result.replace("Spam", "Spam Egg")
print(result2)
#문자열을 리스트로 변환(공백문자 기준)
lst=result2.split()
print(lst)

#문자열 하나로 합치기
print(":)".join(lst))

#정규표횬현식
import re
#패턴을 통한 검색
print(re.match("[0-9]*th", "35th"))
print(re.search("[0-9]*th", "35th"))
result=re.search("[0-9]*th", "35th")
print(result.group())
#약간의함정
print(bool(re.match("[0-9]*th", "  35th")))
print(bool(re.search("[0-9]*th", "   35th")))
print(bool(re.search("apple", "this is apple")))
print("===우변번호===")
print(bool(re.search("\d{5}", "우리 동네는 52300")))
print(bool(re.search("\d{4}", "올해는 2021년입니다")))
#\d{i} 숫자가 i만큼 연속으로 있다