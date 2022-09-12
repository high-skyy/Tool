# Collections module

## deque
```
from collections import deque
dq = deque()                    # 선언
dq.append()                     # deque의 뒤 (오른쪽)에 값을 추가한다.
dq.appendleft()                 # deque의 앞 (왼쪽)에 값을 추가한다.
dq.extend()                     # deque 뒤(오른쪽)에 iterable 객체를 순환하며 값들을 차례로 추가
dq.extendleft()                 # deque의 앞 (왼쪽)에 iterable 객체를 순환하며 값들을 차례로 추가.
dq.remove( value )              # deque에서 특정 값을 삭제
item = dq.pop()                 # deque 뒤 (오른쪽)의 값 삭제 후 반환
item = dq.popleft()             # deque 앞 (왼쪽)의 값 삭제 후 반환

dq.extend([1,2,3])
dq.rotate()                     # deque 자체를 회전 시킨다. (원소들의 순환)
print(dq)
```

## defaultdict
```
from collections import defaultdict
dict_1 = defaultdict( 자료형 이름 )            # 자료형 이름 int, list, dict ....
print(dict(dict_1))                           # {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 3}
print(list(dict_1.keys()))                    # ['A', 'B', 'C'. 'D']
print(list(dict_1.values()))                  # [1, 2, 3, 3]
print(list(dict_1.items()))                   # [('A', 1), ('B', 2), ('C', 3), ('D', 3)]
if key값 in dict_1                            # dictionary에 key값 존재하면 참

del dict_1['key값']                           # 원소를 삭제 할 수 있지만 키가 없을 시에 파이썬 런타임은 keyError를 던진다.
print(dict_1.pop("E", key가 존재하지 않을 시 반환되는 default 값(설정가능)))     # 있으면 value 반환 없으면 2번째 인자 반환
```
- 특이사항
```
처음에 넣어준 순서가 보장이 된다
from collections import defaultdict
result = defaultdict(int)
from collections import defaultdict
result = defaultdict(int)
result[1] = 1
result[3] = 1
result[2] = 1
print(sorted(result, key = lambda x : result[x], reverse = True))     # [1, 3, 2]
from collections import defaultdict
result = defaultdict(int)
result[1] = 1
result[2] = 1
result[3] = 1
print(sorted(result, key = lambda x : result[x], reverse = True))     # [1, 2, 3]
```

## Counter
```
from collections import Counter
# list, dictionary, 문자열 형태를 받을 수 있음
# 이후 몇 개 있는지 세고 dictionary의 형태로 반환한다.
list_1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
dict_1 = {"A" : 2, "B" : 3, "C" : 4}
print(Counter(list_1))                # Counter({4: 4, 3: 3, 2: 2, 1: 1})
print(Counter(dict_1))                # Counter({'C':4, 'B': 3, 'A' : 2})
print(counter.most_common( 2 )        # 입력된 요소들 중 빈도수 (최빈값)을 n개 반환한다. 결과는 (해당 값, 개수) 인 tuple을 list로 묶어서 반환된다.
print(list(counter.elements())        # Counter객체를 다시 list로 변환 시켜준다.

# Counter 끼리의 연산이 가능하다. (덧셈, 뺄샘, 교집합, 합집합)
```
