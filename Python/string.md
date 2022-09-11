# How to handle strings

## Basics
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
> 문자열.lstrip( 삭제할 문자열 ) / 문자열.rstrip( 삭제할 문자열)
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



## Reference
[Reference] (https://snowple.tistory.com/271#:~:text=Python%20%2F%20Python%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%8B%A4%EB%A3%A8%EA%B8%B0,-Technology%2FProgramming&text=%EC%B2%AB%20%EB%AC%B8%EC%9E%90%EB%A5%BC%20%EB%8C%80%EB%AC%B8%EC%9E%90%EB%A1%9C,%EB%A5%BC%20%EC%86%8C%EB%AC%B8%EC%9E%90%EB%A1%9C%20%EB%B0%94%EA%BF%94%EC%A4%80%EB%8B%A4.&text=parameter%EA%B0%80%20%EB%AA%87%20%EB%B2%88%20%ED%8F%AC%ED%95%A8%EB%90%98%EC%96%B4%20%EC%9E%88%EB%8A%94%EC%A7%80%20%EC%95%8C%EB%A0%A4%EC%A4%80%EB%8B%A4.&text=str%20class%EB%8A%94%20%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EB%91%90%20%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C%EC%9D%B4%EB%8B%A4.&text=tab%EC%9D%84%20%EA%B3%B5%EB%B0%B1%EC%9C%BC%EB%A1%9C%20%EC%B9%98%ED%99%98%ED%95%A9%EB%8B%88%EB%8B%A4.)
[Reference] (https://rebro.kr/123#:~:text=2.-,%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%97%B0%EC%82%B0%ED%95%98%EA%B8%B0,%EC%9D%B4%EC%96%B4%20%EB%B6%99%EC%9D%B8%EB%8B%A4%EB%8A%94%20%EC%9D%98%EB%AF%B8%EC%9D%B4%EB%8B%A4.)
