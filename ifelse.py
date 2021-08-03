#ifelse.py
score = int(input("Input score:"))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 90:
    grade = "B"
elif 70 <= score <= 80:
    grade = "C"
else:
    grade = "D"
print("Grade is", grade)

#99dan
for x in [2,3,4,5,6]:
	print("==={0}단===".format(x))
	for y in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(x, y, x*y))

#draw*triangle
for i in [1,2,3,4,5,6,7,8,9]:
    print("*"*i)

lst = [1,2,3,4,5,6,7,8,9]
for item in lst:
    if item % 2 == 0:
        continue
    print("item : {0}".format(item))