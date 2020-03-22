#ch4-1

'''
리스트: 자료(요소, element)를 저장할 수 있는 자료
인덱스(index)로 요소 호출 가능

#인덱스 사용법
list = [273, 32, 103, "문자열", [1, 2, 3]]
>>>list[1:3]
32, 103
>>>list[3][0]
문
>>>list[4][2]
3

요소가 존재하지 않는 위치의 요소를 꺼내려고 하면 IndexError 발생
'''
#리스트 연산자: +, *, len()
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print("len(list_a) =", len(list_a))
print()

#리스트에 요소 추가하기: append(), insert(), extend()
list_a.append(4)        #리스트 뒤에 추가
print(list_a)
list_a.insert(0, 10)    #인덱스 위치에 추가
print(list_a)
list_a.extend([7, 8, 9])#리스트 뒤에 여러 요소 추가
print(list_a)
print()

'''
리스트 연산자 +와는 달리 append(), insert(), extend()를 사용하면 list_a에 직접적인 변화가 생김.
비파괴적 vs 파괴적 = +, * vs append(), insert(), extend()
'''
#리스트에서 요소 제거하기
#방법1. 인덱스로 제거하기: del, pop()
del list_a[1]
'''
del list_a[3:6] #인덱스 3부터 6-1까지 제거
del list_a[:3]  #인덱스 0부터 3-1까지 제거
del list_a[3:]  #인덱스 3부터 마지막까지 제거
'''
print("del list_a[1]:", list_a)

list_a.pop(2)   #pop() 함수의 매개변수에 아무 것도 입력하지 않으면 -1이 들어가 마지막 요소가 제거됨
print("list_a.pop(2):", list_a)
print()

#방법2. 값으로 제거하기: remove
list_a.remove(10)   #만약 리스트에 10이 두 개 있더라도 앞쪽에서 발견되는 10 하나만 제거됨
print("list_a.remove(10):", list_a)

#방법3. 모두 제거하기: clear
list_a.clear()
print("list_a.clear():", list_a)
print()

'''
리스트 내부에 특정 값 확인하기: in/not in 연산자
list_b = [11, 22, 33, 44, 55]
>>>11 in list_b
True
>>>100 in list_b
False
>>>44 not in list_b
False
>>>0 not in list_b
True
'''
#for 반복문 사용하기
for i in range(5):
    print("출력")
print()

#for 반복문 리스트와 함께 사용하기: for 반복자 in 반복할 수 있는 것
array = [273, 32, 103, 57, 52]

for element in array:
    print(element)
    
for character in "안녕하세요":
    print("-", character)
print()

#확인문제 3.
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다.") #len()은 string으로 변환해서 사용해야 함
print()

#확인문제 5.
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number2 in numbers2:
    output[(number2 + 2) % 3].append(number2)
    print(output)
print(output)
print()

'''
딕셔너리 선언하기
변수 = {
    키: 값,
    키: 값,
    ...
    키: 값
}
문자열로 키를 사용할 때는 반드시 따옴표를 붙여야 NameError가 발생하지 않음
딕셔너리에 존재하지 않는 키에 접근하면 KeyError가 발생함
'''
dictionary = {
    "name": "망고망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print(dictionary)
dictionary["price"] = 5000  #값 추가하기, 키가 기존에 있는 키라면 값이 대체됨
print(dictionary)
del dictionary["ingredient"]#값 제거하기
print(dictionary)
print()

#딕셔너리 내부에 키가 있는지 확인하기: in, get()
key = input("> 접근하고자 하는 키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근함")
print()

#존재하지 않는 키에 일부러 접근해보기
value = dictionary.get("아무거나")
print("값:", value)

if value == None:   #None 확인 방법
    print("존재하지 않는 키에 접근함")
print()

#for 반복문 사용하기
for key in dictionary:
    print(key, ":", dictionary[key])
print()

#확인문제 3.
numbers = [1,2,6,8,2,5,4,2,1,4,6,7,4,5,7,3,2,8,0,9]
counter= {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number] = 1

print(counter)
print()

#확인문제 4.
character = {
    "name": "기사",
    "level": "12",
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])
print()
