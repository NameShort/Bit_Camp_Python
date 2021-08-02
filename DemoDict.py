# DemoDict.py

d=dict(a=1, b=2, c=3)
print(type(d))
print(d)

#실제는 이렇게 초기화
color = {"apple": "red", "kiwi": "green"}
print(len(color))
print(color["apple"])

#입력
color["cherry"]="red"
print(color)
#삭제
del color["apple"]
print(color)

color.clear()
print(color)

#장비를 관리한다.
device = {"아이폰":10, "아이패드":15, "윈도우":20}
print(len(device))
print(type(device))

#반복구문
#디버깅할 떄 중단점(Break Point)
for item in device.items():
    print(item)
for k, y in device.items():
    print(k ,y)
