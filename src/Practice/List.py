'''
[List]
파이썬에서 리스트의 특징
1. 리스트에 저장되는 요소가 모두 같은 타입일 필요 없음
2. 다른 프로그래밍 언어에서는 배열(array)라고도 부르지만, 파이썬에서는 리스트(list)라는 용어만을 사용함
3. 리스트는 그 값을 변경할 수 있음 (mutable type)
4. 리스트는 순서대로 저장되며, 각 요소는 0부터 시작하는 인덱스를 가지고 접근할 수 있음
'''

list = [1,2,3,'엥']
for i in list:
    print(i)

# len() : 리스트의 길이, 즉 리스트에 저장된 요소의 개수를 반환
print(len(list))

# 리스트 복사하기
list1 = [1,2,3]
listCopy = list1
listCopy.append(4)

print(listCopy) #[1,2,3,4]
print(list1)    #[1,2,3,4] >> 4 요소가 listCopy 뿐만 아니라 원본 배열 list1 에도 추가됨
                #          >> 단순히 리스트명을 변수에 대입하는 것은 리스트 복사가 아닌 원본 리스트 메모리 주소만을 넘겨주는것이기 때문
                #          >> 따라서 list1과 listCopy는 같은 리스트를 가리키게 됨

# 리스트 복사하고 싶다면 슬라이싱을 이용해 복사해야함
list2 = [3,2,1]
listCopy = list2[:] # > 리스트2의 모든 요소를 선택하여 자르기
listCopy.append(0)

print(list2)       # [3,2,1]
print(listCopy)    # [3,2,1,0]  >> list2와 listCopy는 별도의 리스트이기 때문에 추가된 요소는 listCopy에만 적용됨

# 리스트 붙이기
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)
print(list1.extend(list2))
