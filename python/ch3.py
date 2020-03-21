#ch3
'''
비교 연산자: ==, !=, <, >
논리 연산자: not, and, or
'''
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20:", not under_20)
print()

'''
if 조건문
조건 분기: 조건을 기반으로 실행의 흐름을 변경하는 것
'''
#입력 받기
number = input("정수 입력> ")
number = int(number)

#양수 조건
if number > 0:
    print("양수!")

#음수 조건
if number < 0:
    print("음수!")

#0 조건
if number == 0:
    print("0임")
print()

#날짜/시간 출력하기
#날짜/시간 관련된 기능 임포트
import datetime

#현재 날짜/시간 가져오기
now = datetime.datetime.now()

#출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

#format() 함수로 출력
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

#오전/오후 구분하기
if now.hour < 12:
    print("지금 시간은 {}시로 오전입니다!".format(now.hour))

if now.hour >= 12:
    print("지금 시간은 {}시로 오후입니다!".format(now.hour))
'''
#계절 구분하기
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
    
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

#elif로 계절 구분하기
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
    
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
'''
#더 간단하게 정리하면
if 3 <= now.month < 6:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
    
elif now.month < 9:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

elif now.month < 12:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

print()

#홀수와 짝수를 구분해보자
'''
#방법 1. 끝자리로 확인하기
number1 = input("홀짝을 구분하기 위한 정수 입력> ")
last_number = int(number1[-1])   #숫자로 변환

#짝수 확인
if last_number == 0 \
   or last_number == 2 \
   or last_number == 4 \
   or last_number == 8:
    print("짝수!")
    
#홀수 확인
if last_number == 1 \
   or last_number == 3 \
   or last_number == 5 \
   or last_number == 7:
    print("홀수!")

#방법 2. in 문자열로 확인하기
number1 = input("홀짝을 구분하기 위한 정수 입력> ")
last_character = number1[-1]

#짝수 확인
if last_character in "02468":
    print("짝수!")
    
#홀수 확인
if last_character in "13579":
    print("홀수!")

#방법 3. 나머지 연산자로 구분하기
number1 = input("홀짝을 구분하기 위한 정수 입력> ")
number1 = int(number)

#짝수 확인
if number1 % 2 ==0:
    print("짝수!")
    
#홀수 확인
if number1 % 2 ==1:
    print("홀수!")
'''

#방법 4. else 활용하기
number1 = input("홀짝을 구분하기 위한 정수 입력> ")
number1 = int(number)

#짝수 확인
if number1 % 2 ==0:
    print("짝수!")
    
#홀수 확인
else :
    print("홀수!")
print()

'''
False로 변환되는 값: None, 숫자 0과 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리)
'''
print("# if 조건문에 0 넣기")
if 0:
    print("0은 Ture로 변환됨")
else:
    print("0은 False로 변환됨")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 Ture로 변환됨")
else:
    print("빈 문자열은 False로 변환됨")
print()

'''
코드 골격을 먼저 만들고 세부 구현을 하려면 나중에 구현할 부분에 pass를 사용함
파이썬에서 if else 구문 아래 아무것도 작성하지 않으면 IndentationaError가 발생하므로 pass 키워드 이용
pass 키워드: 진짜로 아무것도 안함, 곧 개발하겠음을 의미!
구현하지 않은 부분을 까먹을 수도 있으니 raise NotImpelmentedError 이용하면 좋음
'''
number2 = input("pass 예제, 정수 입력> ")
number2 = int(number2)

if number > 0:
    '''pass'''
    raise NotImplementedError
else:
    '''pass'''
    raise NotImplementedError
