# How to handle strings

## Basics
### 문자열은 indexing이 가능하다.

### 문자열의 연산
> 파이썬은 매우 편리하게도 문자열 끼리의 연산이 가능하다. (덧셈과 곱셈만 가능)
```
a = "python"
b = "hello"
print(a*2)          # pythonpython
print(a + b)        # pythonhello
print(b + a)        # hellopython
```

### strip
> **문자열**.lstrip( **삭제할 문자열** ) / **문자열**.rstrip( **삭제할 문자열**)
> 원래 문자열을 변환 시키는 것이 아닌 적용된 값을 반환한다.
> lstrip의 경우는 왼쪽 부터 검사했을 때 해당 문자열이 존재할 경우 삭제 아니면 삭제 안함
> rstrip은 오른쪽에서 부터 검사
> 기본적으로 lstrip, rstrip의 경우는 빈칸을 없앤다.
```
test_string = " Hello | Python "
test_string = test_string.rstrip()        #  Hello | Python
print(test_string)
test_string = test_string.lstrip()        # Hello | Python
print(test_string)
test_string = test_string.lstrip("Hello")
print(test_string)                        #  | Python
test_string = test_string.lstrip("Python")
print(test_string)                        #  | Python
test_string = test_string.rstrip("Python")
print(test_string)                        #  | 
```

### replace
> 문자열.replace( **바꾸고 싶은 문자열**, **새로운 문자열**, **치환 횟수(없으면 전 부다 바꾼다.)**)
> Strip과는 다르게 문자열 중간에 있는 내용들을 바꿀 수 있어서 좋다.
```
test_1 = "Hello python"
test_2 = "Hello Hello python"
test_3 = "Hello Hello python"
test_4 = "Hello Hello python"
test_1 = test_1.replace("Hello", "Bye")
print(test_1)                                 # Bye python
test_2 = test_2.replace("Hello", "Bye")
print(test_2)                                 # Bye Bye python
test_3 = test_3.replace("Hello", "Bye", 1)
print(test_3)                                 # Bye Hello python
test_4 = test_4.replace("Hello", "Bye", 2)
print(test_4)                                 # Bye Bye python
```

### 대소문자
> **문자열**.upper()는 모든 문자열을 대문자로
> **문자열**.lower()는 모든 문자열을 소문자로
> **문자열**.title()는 모든 단어 앞을 대문자로
> **문자열**.capitalize()는 문장의 맨 앞 단어 만을 대문자로
```
test = "Hello Python"
test = test.upper()
print(test)                 # HELLO PYTHON
test = test.lower()
print(test)                 # hello python
test = test.title()
print(test)                 # Hello Python
test = test.capitalize()
print(test)                 # Hello python
```

### Count
> **문자열**.count(**'찾고 싶은 문자'**)
> 특정 문자의 개수를 반환 해준다.
```
test = "AAaaabbccc"
print(test.count('A'))        # 2
print(test.count('c'))        # 3
print(test.count('z'))        # 0
```

### Find
> **문자열**.find(**'찾고 싶은 문자'**, )
> Find 함수는 해당 문자가 처음으로 등장하는 인덱스를 반환해줍니다. (문자가 없으면 -1을 반환)
```
test = "AAaaabbccc"
print(test.find('A'))         # 0
print(test.find('c'))         # 7
print(test.find('z'))         # -1
```

### 문자열 구성 파악
> **문자열**.함수이름()
> isalpha : 문자열 전체가 알파벳(한글)이면 True
> isdigit : 문자열 전체가 숫자이면 True
> isupper : 문자열 전체가 대문자이면 True
> islower : 문자열 전체가 소문자이면 True
> 주의 : lower랑 upper는 상관 없지만 alpha랑 digit는 중간에 공백이 있을 경우에 False가 된다.
```
test_1 = '123'
test_2 = 'abc'
test_3 = 'aBC'
test_4 = 'ABC'
print(test_1.isalpha())       # False
print(test_1.isdigit())       # True
print(test_2.isdigit())       # False
print(test_2.isalpha())       # True
print(test_2.isupper())       # False
print(test_2.islower())       # True
print(test_3.isupper())       # False
print(test_3.islower())       # False
print(test_4.islower())       # False
print(test_4.isupper())       # True
print(test_5.isdigit())       # False
print(test_6.isalpha())       # False
```

### 문자열 쪼개기, 합치기
> **문자열**.join(**list**)
> join의 경우는 list에서 하나 받아와서 앞에 넣고 그 다음에 원래 문자열 넣고 list 다음 원소 넣고 다시 문자열 넣고 다음 원소를 다시 넣는다.
> **문자열**.split(**"기준 문자열" (기본값 : 공백)**
```
# JOIN
test_1 = 'abc'
test_2 = ['d', 'e', 'f']
test_3 = ['ab', 'cd','ef']
print(test_1.join(test_2))        # dabceabcf
test_4 = "".join(test_3)
print(test_4)                     # abcdef
```
```
# Split
test_1 = "My name is 서상현"
test_2 = "Mywnamewisw서상현"
for word in test_1.split():   
    print(word)                   # My / name / is / 서상현
test_list = test_1.split()
print(test_list)                  # ['My', 'name', 'is', '서상현']
test_list_2 = list(test_2.split('w'))
print(test_list_2)                # ['My', 'name', 'is', '서상현']
```

```
# Tip 한 문자 씩 받기
test = "My name is SangHyun"
test_list = list(test)
print(test_list)
# ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'S', 'a', 'n', 'g', 'H', 'y', 'u', 'n']
```

## Reference
- [Reference] (https://snowple.tistory.com/271#:~:text=Python%20%2F%20Python%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%8B%A4%EB%A3%A8%EA%B8%B0,-Technology%2FProgramming&text=%EC%B2%AB%20%EB%AC%B8%EC%9E%90%EB%A5%BC%20%EB%8C%80%EB%AC%B8%EC%9E%90%EB%A1%9C,%EB%A5%BC%20%EC%86%8C%EB%AC%B8%EC%9E%90%EB%A1%9C%20%EB%B0%94%EA%BF%94%EC%A4%80%EB%8B%A4.&text=parameter%EA%B0%80%20%EB%AA%87%20%EB%B2%88%20%ED%8F%AC%ED%95%A8%EB%90%98%EC%96%B4%20%EC%9E%88%EB%8A%94%EC%A7%80%20%EC%95%8C%EB%A0%A4%EC%A4%80%EB%8B%A4.&text=str%20class%EB%8A%94%20%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EB%91%90%20%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C%EC%9D%B4%EB%8B%A4.&text=tab%EC%9D%84%20%EA%B3%B5%EB%B0%B1%EC%9C%BC%EB%A1%9C%20%EC%B9%98%ED%99%98%ED%95%A9%EB%8B%88%EB%8B%A4.)
- [Reference] (https://rebro.kr/123#:~:text=2.-,%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%97%B0%EC%82%B0%ED%95%98%EA%B8%B0,%EC%9D%B4%EC%96%B4%20%EB%B6%99%EC%9D%B8%EB%8B%A4%EB%8A%94%20%EC%9D%98%EB%AF%B8%EC%9D%B4%EB%8B%A4.)
