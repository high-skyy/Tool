# re module
```
import re
```
> 사용하는 이유는 regular expression을 사용하여 포괄적인 단어들을 찾기 위함이다.

## regular expression 사용법
1. 컴파일 후 매칭
- pattern = re.compile(**"패턴"**)
- x = pattern.search("I like apple!")
- pattern 객체를 생성한다!
```
import re
pattern = re.compile("apple")
print(pattern.search("I like apple!").group())        # apple
```
2. 축약형
- 그냥 패턴 직접 입력
- x = re.search(**"패턴"**, **"문자열"**)

## Meta characters
### []
- []사이의 문자들 중 하나와 매치(or과 역할 비슷)
- 하이픈(-) 으로 연결 가능 ([0-9], [a-z])
- [^ ]으로 시작할 경우 반대 의미(해당 문자가 아니면 매치)
```
import re
test = "1ajgdlfkjg3skdlfj4"
pattern_1 = re.compile("[0-9]")
pattern_2 = re.compile("[^0-9]")
print(re.findall(pattern_1, test))    # ['1', '3', '4']
print(re.findall(pattern_2,test))     # ['a', 'j', 'g', 'd', 'l', 'f', 'k', 'j', 'g', 's', 'k', 'd', 'l', 'f', 'j']
```

### .(점)
- \n을 제외한 모든 문자와 매치
- 단, 문자클래스 안의 .([.])은 말 그대로 '.'을 의미함
- 또 한 가지 방법은 .앞에 \를 붙이면 된다. '\.'이면 '.' 그대로를 의미함
```
import re
test = "ab1abcabiabjab."
pattern_1 = re.compile("ab.")       # ['ab1', 'abc', 'abi', 'abj', 'ab.']
pattern_2 = re.compile("ab\.")      # ['ab.']
pattern_3 = re.compile("ab[.]")     # ['ab.']
print(re.findall(pattern_1, test))
print(re.findall(pattern_2, test))
print(re.findall(pattern_3, test))
```
### 여러 문자 (표현)
- (별)은 0회 이상 반복
- +는 1회 이상 반복
- ?는 0회 또는 1회 (있어도 되고 없어도 됨)
- ^은 문자열의 시작 ([]안에 없어야 함)
- $은 문자열의 끝
- \은 이스케이프 문자, 메타문자를 일반 문자로 인식하게 함
- ()은 그룹핑, 추출할 패턴을 지정 (그룹핑 메타 문자 있어야 함)
```
import re
test = "ab1abca biabja b."
pattern_1 = re.compile("[\w]*")
pattern_2 = re.compile("[\w]?")
pattern_3 = re.compile("[\w]+")
print(re.findall(pattern_1, test))    # ['ab1abca', '', 'biabja', '', 'b', '', '']
print(re.findall(pattern_2, test))    # ['a', 'b', '1', 'a', 'b', 'c', 'a', '', 'b'...
print(re.findall(pattern_3, test))    # ['ab1abca', 'biabja', 'b']

re.findall(f"[^a-z]({word})[^a-z]", page)
# page에서 앞과 뒤에 문자가 아닌 것이 오면 
```


### 축약 표현
- \d : 숫자
- \D : 숫자가 아닌 것(텍스트, 특수문자, white space)
- \s : white space (space, tap, new line)
- \S : white space가 아닌 것 (텍스트, 특수문자, 숫자)
- \w : 문자 (텍스트 & 숫자)
- \W : 문자(텍스트&숫자)가 아닌 것 (특문, white space)
```
import re
test = "ab1abcabiabjab."
pattern_1 = re.compile("\w")
pattern_2 = re.compile("[\w]")
pattern_3 = re.compile("\d")
pattern_4 = re.compile("\s")
pattern_5 = re.compile("[^\w]")
print(re.findall(pattern_1, test))    # ['a', 'b', '1', 'a', 'b', 'c', 'a', 'b', 'i'...
print(re.findall(pattern_2, test))    # ['a', 'b', '1', 'a', 'b', 'c', 'a', 'b', 'i'...
print(re.findall(pattern_3, test))    # ['1']
print(re.findall(pattern_4, test))    # [' ', ' ']
print(re.findall(pattern_5, test))    # [' ', ' ', '.']
```

## findall
- re.findall(**패턴 문자열**, **찾는 대상의 문자열**, **플래그(없어도 됨)**
- 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환합니다.
```
import re
test = "aaaaaa"
test_2 = 'aaaaa'
result = re.findall('aaa', test)
result_2 = re.findall('aaa', test_2)
print(result)                           # ['aaa', 'aaa']
print(result_2)                         # ['aaa']
```

## split
- re.split(**패턴**, **찾고자 하는 문자열**, **최대 split수**, **플래그**)
- 문자열에서 패턴이 맞으면 이를 기점으로 리스트로 쪼개는 함수이다.
- 수를 지정하면 지정한 수 만큼 쪼개고 그 수가 도달하면 쪼개지 않습니다.
```
import re
test = "my name is 서상현"
test_list = re.split(" ", test, 1)
test_list_2 = re.split(' ',test )
print(test_list)                      # ['my', 'name is 서상현']
print(test_list_2)                    # ['my', 'name', 'is', '서상현']
```

## sub
- re.sub(**패턴**, **찾아서 교체할 문자열**, **대상 문자열**, **최대 교체 수**, **플래그**)
- sub는 문자열에 맞는 패턴을 2번째 인자로 교체합니다. 교체수 이상이 되면 교체하지 않는다.
```
import re
test = "Hello Hello Hello Python"
test_1 = re.sub("Hello", "Bye", test)         
print(test_1)                                 # Bye Bye Bye Python
test_2 = re.sub("Hello", "Bye", test, 2)
print(test_2)                                 # Bye Bye Hello Python
```

## search와 그 외 함수들
- re.search(**패턴**, **문자열**, **플래그**).함수이름()
- group : 패턴에 맞는 문자열을 추출
- start : 문자열의 어디서부터 패턴이 시작되는지 index 반환
- end   : 문자열의 어디서 패턴이 끝나는지
- span  : 문자열의 어디서부터 어디까지 패턴이 있는지 index 반환
> 주의 : 해당 문자열을 찾을 수 없을 경우 search 함수에서 None이 반환된다. (None일 때, group등의 함수를 같이 한번에 사용하면 오류 발생함)
```
import re
print(re.search('aa', 'baab').group())        # aa
print(re.search('aa', 'baab').start())        # 1
print(re.search('aa', 'baab').end())          # 3
print(re.search('aa', 'baab').span())         # (1, 3)
```

## Reference
- [Reference](https://velog.io/@dosilv/python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9Dregular-expression-%EC%82%AC%EC%9A%A9%EB%B2%95)

