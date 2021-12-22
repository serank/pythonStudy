# while 조건식 :
i = 1
while i < 4:
    print("while " + str(i))
    i += 1

# for문
# for 변수 in 문자열(/튜플/리스트):
#   ...명령문...
str = "고양이"
for ch in str:
    print(ch)

'''
range() : 전달된 인수에 따라 연속된 정수들을 반환하는 함수 (마지막 정수 -1 까지 반환함)
1. range(마지막정수)
2. range(시작정수, 마지막정수)
ex) range(5) > 0,1,2,3,4
'''

# for문과 range() 함수로 구구단 출력하기
for col in range(2,10):
    for row in range(1,10):
        if col > 5:
            break # break 이용하여 5단까지만 출력
        print(col,'*',row,'=',col*row)

