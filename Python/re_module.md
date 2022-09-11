# re module
```
import re
```
> 사용하는 이유는 regular expression을 사용하여 포괄적인 단어들을 찾기 위함이다.

## findall
> re.findall(**패턴 문자열**, **찾는 대상의 문자열**, **플래그(없어도 됨)**
> 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환합니다.
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
> re.split(**패턴**, **찾고자 하는 문자열**, **최대 split수**, **플래그**)
> 문자열에서 패턴이 맞으면 이를 기점으로 리스트로 쪼개는 함수이다.
> 수를 지정하면 지정한 수 만큼 쪼개고 그 수가 도달하면 쪼개지 않습니다.
```
import re
test = "my name is 서상현"
test_list = re.split(" ", test, 1)
test_list_2 = re.split(' ',test )
print(test_list)                      # ['my', 'name is 서상현']
print(test_list_2)                    # ['my', 'name', 'is', '서상현']
```

## sub
> re.sub(**패턴**, **찾아서 교체할 문자열**, **대상 문자열**, **최대 교체 수**, **플래그**)
> sub는 문자열에 맞는 패턴을 2번째 인자로 교체합니다. 교체수 이상이 되면 교체하지 않는다.
```
import re
test = "Hello Hello Hello Python"
test_1 = re.sub("Hello", "Bye", test)         
print(test_1)                                 # Bye Bye Bye Python
test_2 = re.sub("Hello", "Bye", test, 2)
print(test_2)                                 # Bye Bye Hello Python
```

## search와 그 외 함수들
> re.search(**패턴**, **문자열**, **플래그**).함수이름()
> group : 패턴에 맞는 문자열을 추출
> start : 문자열의 어디서부터 패턴이 시작되는지 index 반환
> end   : 문자열의 어디서 패턴이 끝나는지
> span  : 문자열의 어디서부터 어디까지 패턴이 있는지 index 반환
```
import re
print(re.search('aa', 'baab').group())        # aa
print(re.search('aa', 'baab').start())        # 1
print(re.search('aa', 'baab').end())          # 3
print(re.search('aa', 'baab').span())         # (1, 3)
```






