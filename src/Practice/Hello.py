# C, JAVA와 달리 파이썬은 변수를 선언할 때 타입을 명시할 필요가 없음
a = 7
b = "문자"
c = 1.2

# type() : 데이터/변수 타입을 반환하는 함수
print(type(a)) # > <class 'int'>
print(type(b)) # > <class 'str'>
print(type(c)) # > <class 'float'>

# 한줄 주석
'''
여러줄 주석(작은따음표 3개)
! 파이썬 주석 주의점 : 파이썬은 들여쓰기로 코드의 끝 인식하기 때문에 주석도 들여쓰기 주의할것
'''
print('''
    여러 줄로
    출력도 되지롱
''')

# 불리언 타입 : bool
# True, Flase 가 예약어로 지정되어 있기 때문에 첫 문자를 항상 대문자로 사용하기
# bool() : 데이터의 참/거짓 판단하여 반환
print(bool(1))        # True
print(bool(0))        # False
print(bool(None))     # False
print(bool([]))       # False
print(bool(()))       # False
print(bool({}))       # False
print(bool([1,2,3]))  # True
print(bool(""))       # False
print(bool("python")) # True

# 문자끼리 연산
str1 = "파이썬"
str2 = "배우기"
print(str1 + str2) # > 파이썬배우기
print(str1 * 3)    # > 파이썬파이썬파이썬

# 문자열을 배열로 다룰 수 있음
py = "파이썬 공부 시작"
print(py[0])  #파
print(py[1])  #이
print(py[2])  #썬
print(py[-1]) #작
print(len(py)) #9

# 문자열 자르기 > 파이썬에서는 문자열 슬라이싱을 지원
# [:] > 클론 앞 인덱스부터 콜론 뒤 인덱스 바로 앞 문자까지를 반환
py = "고양이 귀여워"
print(py[0:3]) #고양이
print(py[:4])  #고양이
print(py[4:])  #귀여워

# 조건문 if-else > if 조건식: else:
con = "sweet"
if con == "sweet":
    print("삼키다")
else:
    print("뱉다")

# elif > else if의 줄임말.
# (파이썬 들여쓰기 때문에 if: else: if > 중첩되면 보기 힘들다, elif를 이용해 한줄쓰기 가능)
# 파이썬에는 switch-case문이 제공되지 않는다.
season = "겨울"
if season == "봄":
    print("따뜻하다")
elif season == "여름":
    print("덥다")
elif season == "겨울":
    print("춥다")

# pass 키워드
# 조건문 쓸 때, 아무 명령어도 수행하지 않아야 할 경우 다른 프로그래밍 언어는 명령문을 명시하지 않으면 되지만
# 파이썬은 조건문 내부에 명령문이 무조건 하나 이상 존재해야 함
# 이런 경우 사용할 수 있도록, pass 키워드를 별도로 제공
temp = 18
if temp < 26:
    pass
else:
    print("에어컨 키기")


