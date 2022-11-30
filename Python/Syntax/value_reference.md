# Call-by-value vs call-by-reference
Python의 자료형에는 크게 immutable(불변)과 mutable(가변)이 있다. Int, str 같은 타입이 불변이고,
list, dictionary, tuple 같은 타입이 mutable이다. Immutable 타입의 객체를 넘기면 call by value가 되고
가변 타입의 객체를 넘기면 call by reference가 된다.
> 함수의 인자로 mutable한 객체를 넘기고 그 객체를 수정하게 되면 수정사항들이 전부 다 반영이 된다.
> 따라서 dfs등에서 visited등을 다시 사용하고 싶을 때에는 반드시 복사 후 사용해야 한다. 가장 빠른 방법은 아래와 같다.

## 얕은 복사
```
list1 = list2[:]
list1 = list(list1) # 얕은 복사에서 그 다음으로 빠른 방법
``` 

## 깊은 복사
```
import copy
A = [1, 2, 3, 4]
B = copy.deepcopy(a)
B[1] = 0                # A가 바뀌지 않음
```
