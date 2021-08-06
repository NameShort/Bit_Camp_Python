import sqlite3

#연결객체 생성(일단 메모리에 임시로 저장)
#con = sqlite3.connect(":memory:")
con=sqlite3.connect("D:\\Python\\Bit_Camp_Python\\sample.db")
#구문을 수행할 커서 객체를 생성
cur = con.cursor()
#데이터를 담을 테이블을 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

#입력 하라메터 처리
name = "gildong"
phoneNum = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
#다중의 레코드(데이터를 입력하는 경우)
datalist = (("tom", "010-333"), ("dsp", "010-444"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#결과를 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#정상적으로 작업 완료
#con.commit()

#결과를 검색
cur.execute("select * from PhoneBook;")
print("===fetchone===")
print(cur.fetchone())
print("===fetchmany===")
print(cur.fetchmany(2))
print("===fetchall===")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#정상적으로 작업을 완료
con.commit()