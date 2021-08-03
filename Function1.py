#리턴을 하지 않는 함수

def setValue(newValue):
    #지역변수
    x=newValue
    print("지역변수:",x)

#호출
result =setValue(5)
print(result)

def swap(x, y):
    return x, y

#호출
result = swap(3, 4)
print(result)

#디버깅연습
def intersect(prelist, postlist):
    #지역변수
    result=[]
    #H(0)| A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))

#불변형식과 가변형식
a = 1.2
print(id(a))
a = 2.3
print(id(a))

#객체는 참조를 통해 입출력이 된다
wordlist=["J", "A", "M"]
#함수정의
def change(x):
    x1 = x[:]
    x1[0]="H"
    print("함수내부:", x1)

#함수호출
change(wordlist)
print("함수 호출후 :", wordlist)