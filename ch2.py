#ch2
'''
기본적인 자료형: 문자열, 숫자, 불(boolean)
type(): 자료의 형식을 확인하는 함수
'''
print(type("Hello")) #string
print(type(1234))   #int
print()

#문자열을 만드는 방법은 두 가지가 있음
print("Hello")  #큰따옴표
print('Hello')  #작은따옴표
print()

'''
print(""Hello"뇸뇸")처럼 큰따옴표만 사용하면 Syntex Error가 발생
이스케이프 문자인 \를 사용하면 \다음 문자를 그대로 출력할 수 있음
'''
#이스케이프 문자 활용법
print("\"Hello\"뇸뇸")
print("Hello\n뇸뇸")   #\n=줄바꿈
print("Hello\tHello\tHello")   #\t=탭
print("\\ \\ \\ \\ \\ \\")  #\\=역슬래시
print()

#\n으로 줄바꿈하기
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세")
print()

#""" & '''으로 여러 줄을 문자열로 취급함
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
""")
print()

#위 아래 줄바꿈이 들어감
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세

""")
print()

#\으로 줄바꿈하지 않는다고 알려줌 
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세\
""")
print()


#문자열 연결 연산자 +와 문자열 반복 연산자 *
print("Hello" + "뇸뇸")
print("Hello" * 3)
print()

#문자 선택 연산자: 파이썬은 제로 인덱스 유형
print("영일이삼사오육"[0])
print("영일이삼사오육"[3])
print("영일이삼사오육"[6])
print("영일이삼사오육"[-1])
print("영일이삼사오육"[-3])
print("영일이삼사오육"[-6])
print()

#문자열 범위 선택 연산자: 슬라이싱[:]
print("영일이삼사오육"[1:4])   #뒤의 숫자 -1번까지 선택됨***
print("영일이삼사오육"[1:])    #1번부터 끝까지
print("영일이삼사오육"[:4])    #0번부터 3번까지
print()

'''
슬라이싱해도 원본의 값은 그대로 남아있음
만약 인덱스가 범위를 넘었다면 Index Error가 발생
'''
#문자열의 길이 구하기
print(len("안녕하슈"))
print()

'''
int: 정수, integer
float: 실수, floating point(부동 소수점)
사칙 연산자 +,-,*,/는 기본적으로 사용 가능
//: 정수 나누기 연산자
%: 나머지 연산자
**: 제곱 연산자
연산자 우선 순위: 곱셈&나눗셈 > 덧셈&뺄셈
--> 헷갈린다면 괄호로 묶어서 사용하기!
Type Error: 서로 다른 자료를 연산하려고 할 때 발생
'''
print("3 // 2 =", 3 // 2)
print("5 % 2 =", 5 % 2)
print("2 ** 3 =", 2 ** 3)
print()

'''
변수 사용법
1. 변수 선언
2. 변수에 값 할당
3. 변수 참조
'''
#변수 선언과 할당
pi = 3.14159265
r = 10

#변수 참조
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)
print()

'''
복합 대입 연산자: +=, -=, *=, /=, %=, **=
문자열 복합 대입 연산자: +=, *=
사용자 입력 함수인 input()은 무조건 자료형으로 값을 받음!
--> 따라서 int(), float(), str()로 자료형을 변환해야 함(캐스트)
float("안녕"), int("52.273")처럼 변환할 수 없는 것을 변환하려고 하면 Value Error가 발생
'''
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)   #결과가 문자+문자로 나옴
print("숫자 자료:", int_a + int_b)
print()

'''
문자열의 format() 함수
{} 기호의 개수가 format() 함수의 매개변수 개수보다 많으면 Index Error가 발생
--> {}의 짝꿍이 없으면 절대 안 됨!!
'''
#format() 함수 사용해보기
format_a = "{} {} {}".format(1, "뇸뇸", True)
print(format_a)

#정수를 특정 칸에 출력하기
output_a = "{:d}".format(23)    #기본
output_b = "{:5d}".format(23)   #5칸
output_c = "{:10d}".format(23)  #10칸
output_d = "{:05d}".format(23)  #양수, 빈칸은 0으로 채우기
output_e = "{:05d}".format(-23) #음수, 빈칸은 0으로 채우기
print(output_a, output_b, output_c, output_d, output_e)
print()

#기호와 함께 출력하기
output_f = "{:+d}".format(23)   #양수
output_g = "{:+d}".format(-23)  #음수
output_h = "{: d}".format(23)   #양수: 기호 부분 공백
output_i = "{: d}".format(-23)  #음수: 기호 부분 공백
print(output_f, output_g, output_h, output_i)
print()

#조합하기
output_h = "{:+5d}".format(23)  #기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-23) #기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(23) #기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-23)#기호를 앞으로 밀기: 음수
output_l = "{:+05d}".format(23) #0으로 채우기: 양수
output_m = "{:+05d}".format(-23)#0으로 채우기: 음수
print(output_h, output_i, output_j, output_k, output_l, output_m)
print()

#부동 소수점 출력하기
foutput_a = "{:f}".format(23.234)       #기본
foutput_b = "{:15f}".format(23.234)     #15칸 만들기
foutput_c = "{:+15f}".format(23.234)    #15칸에 부호 추가하기
foutput_d = "{:+015f}".format(23.234)   #15칸에 부호 추가하고 0으로 채우기
foutput_e = "{:15.3f}".format(23.234)   #15칸에 소수점 세자리까지 출력하기
foutput_f = "{:15.1f}".format(23.234)   #15칸에 소수점 한자리까지 출력하기
foutput_g = "{:g}".format(23.0)         #의미 없는 소수점 제거하기
print(foutput_a, foutput_b, foutput_c, foutput_d, foutput_e, foutput_f, foutput_g)
print()

#대소문자 바꾸기, 원본은 바뀌지 않음!
a = "Hello world"
a.upper()   #대문자로
a.lower()   #소문자로
print()

'''
문자열 공백 제거하기
strip(): 양옆 공백 제거
lstrip(): 왼쪽 공백 제거
rstrip(): 오른쪽 공백 제거
'''
sample = """
    안녕안녕
공백을 제거해봅시다.
"""
print(sample.strip())
print()

'''
문자열의 구성 파악하기
isalnum(): 알파벳 또는 숫자인지
isalpha(): 알파벳만 있는지
isidentifier(): 식별자로 사용 가능한지
isdecimal(): 정수 형태인지
isdigit(): 숫자로 인식될 수 있는지
isspace(): 공백인지
islower(): 소문자인지
isupper(): 대문자인지
--> bool로 결과 반환

문자열 찾기
find(): 왼쪽부터 처음 등장하는 위치를 찾음
rfind(): 오른쪽부터 처음 등장하는 위치를 찾음
'''
find_a = "안녕안녕하슈".find("안녕")
print(find_a)
find_b = "안녕안녕하슈".rfind("안녕")
print(find_b)
print()

#문자열과 in 연산자--> bool로 결과 반환
print("안녕"in "안녕하슈")
print("끝!"in "안녕하슈")
print()

#문자열 자르기--> 특정한 문자열을 기준으로 자름, 실행 결과는 리스트임
split_a = "10 2020 303 2".split(" ")
print(split_a)
print()
