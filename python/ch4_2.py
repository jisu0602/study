#ch4-3, 4-4
'''
범위 range 사용하기
range(5): 0부터 4까지
range(3, 5): 3부터 4까지
range(0, 10, 2): 0부터 2씩 증가하면서 10-1까지의 정수 범위

범위가 10까지 임을 강조하려면 range(0, 10+1)이라고 표현하는 것이 더 명료함
범위 매개변수에 나눗셈을 사용하면 TypeError가 발생. range(0, n // 2)처럼 정수 나누기 연산자 이용해야 함
'''
#for 반복문에서 범위 사용하기
for i in range(0, 10, 3):
    print(str(i) + "= 반복 변수")
print()

#리스트와 범위
array = [274, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
'''       
for i in range(len(array)):
    print(i, "번째 반복: ", array[i])
'''
print()

#역반복문
#방법 1. range() 함수 매개변수 세 개를 사용하기
for i in range(4, 0 -1, -1):
    print("현재 반복 변수: {}".format(i))

#방법 2. reversed() 함수 사용하기, * 주의 사항이 많은 함수임
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()

'''
while 불 표현식:
    문장
--> 불 표현식이 참인 동안 문장을 계속 반복함(강제 종료는 ctrl + c)
'''
#while 반복문을 for 반복문처럼 사용하기
i = 0
while i < 4:
    print("{}번째 반복".format(i))
    i += 1
print()

#while 반복문을 상태 기반으로 반복하기
list_test = [1, 2, 1, 2]
value = 2

while value in list_test:    #list_test 내부에 value가 있다면 반복
    list_test.remove(value)

print(list_test)
print()

#while 반복문을 시간을 기반으로 반복하기
#유닉스 타임: 세계 포준시로 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지를 정수로 나타낸 것
import time 
number = 0

target_tick = time.time() + 1
while time.time() < target_tick:
    number += 1

print("1초 동안 {}번 반복함".format(number))
print()

#반복문 내부에서만 사용 가능한 break, continue 키워드
i2 = 0

while True:
    print("{}번째 반복문 임".format(i2))
    i2 += 1

    input_text = input(">종료할까요?(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료함!")
        break

#continue 예제
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:     #number가 10보다 작으면 계속 반복함
        continue
    
    print(number)   #number가 10보다 커야 출력 됨.

#확인문제 2.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)
print()

#확인문제 3.
limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    sum_value = sum_value+i
    i = i+1
    #print(sum_value, i)
    
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))
print()

#확인문제 4.
max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    #최댓값 구하기
    current = i * j
    #print(i, j, current)
    if max_value < current:
        a = i
        b = j
        max_value = current
        
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
print()


'''
파이썬의 고유한 기능을 알아보자
- 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
- 리스트 뒤집기: reversed()
- 현재 인덱스가 몇 번째인지 확인하기: enumerate()
- 딕셔너리로 쉽게 반복문 작성하기: items()
- 리스트 안에 for문 사용하기: 리스트 내포

#min(), max(), sum()
numbers = [103, 52, 273, 23]
>>>max(numbers)
273
>>>min(103, 52, 263)
52
'''
#reversed() 함수로 리스트 뒤집기
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("reversed([1, 2, 3, 4, 5]):", list_reversed)  #이러테이터 값을 출력함(메모리를 효율적으로 관리하는 방법)
print(next(list_reversed))  #next() 함수로 요소를 하나하나 꺼내야 함
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

#반복문 사용
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)
    
#reversed() 함수의 결과는 제너레이터이므로 필요한 시점에 넣어서 사용해야 함
'''
temp = reversed([1, 2, 3, 4, 5, 6])    #두 번째 반복문은 전혀 출력이 안됨

for i in temp:
    print("첫 번째 반복문: {}".format(i))

for i in temp:
    print("두 번째 반복문: {}".format(i))
'''
numbers_a = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers_a):
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers_a):
    print("두 번째 반복문: {}".format(i))
print()

'''
#확장 슬라이싱 사용하기: [::-1]
numbers = [1, 2, 3, 4, 5]
>>>numbers[::-1}
[5, 4, 3, 2, 1]
>>>"안녕하세요"[::-1]
'요세하녕안'
'''

#enumerate() 함수와 반복문 조합하기(리스트에서)
example_list = ["A", "B", "C"]

print(enumerate(example_list))  #이터레이터가 출력됨
print()

print(list(enumerate(example_list)))    #list() 함수로 강제 변환 출력
print()

for i, value in enumerate(example_list):    #반복문과 조합해서 사용하기
    print("{}번째 요소는 {}입니다.".format(i, value))
print()

#딕셔너리의 items() 함수와 반복문 조합하기
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

print("items():", example_dictionary.items())
print()

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print()

#리스트 내포
'''
array = []

for i in range(0, 20, 2):
    array.append(i*I)
를 짧게 표현하면 아래와 같음
'''
array = [i*i for i in range(0, 20, 2)]
print(array)

array_a = [1, 2, 3, 4, 5]
output = [number for number in array_a if number != 3]  #array_a의 요소를 number라고 할 때 3이 아닌 number로 리스트를 재조합해주세요.
print(output)
print()

#괄호로 문자열 연결하기
print(
    "첫 번째 줄. \n"
    "두 번째 줄.")
#join() 함수로 리스트의 요소를 문자열로 연결하기
print("::".join(["1", "2", "3"]))

#확인문제 2.
output = [i for i in range(0, 100+1)
          if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))
