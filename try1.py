#함수정의
def divide(a,b):
    return a/b

#호출
#예외처리
try:
    result=divide(5,0)
    print("{0} 결과".format(result))
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
else:
    print("결과 {0}".format(result))
finally:
    print("무조건 실행")
print("코드 실행 종료")