# itertools module
```
from itertools import 함수이름
```
> 모든 원소들은 tuple로 반환된다.

## combinations
> combinations 함수는 오브젝트를 만든다.
```
from itertools import combinations      # 조합

list_1 = [1,2,3,4]
for comb in combinations(list_1, 2):          # combinations(list이름, 원소 갯수)
    print(comb)
# (1, 2)(1, 3)(1, 4)(2, 3)(2, 4)(3, 4)
print(combinations(list_1, 3))          # object
```

## combinations_with_replacement
```
from itertools import combinations_with_replacement     # 중복 조합

list_1 = [1,2,3,4]
for comb in combinations_with_replacement(list_1, 2):
    print(comb)

# (1, 1)(1, 2)(1, 3)(1, 4)(2, 2)(2, 3)(2, 4)(3, 3)(3, 4)(4, 4)
```

## permutations
```
from itertools import permutations

list_1 = [1,2,3]
for perm in permutations(list_1, 3):
    print(perm)

# (1, 2, 3)(1, 3, 2)(2, 1, 3)(2, 3, 1)(3, 1, 2)(3, 2, 1)
```

## product
> 주어진 input에 대해서 repeat번 조합하는 모든 경우의 수를 튜플로 출력을 해준다.
```
from itertools import product

list_1 = [1,2,3]
list_2 = [4,5,6]
for prod in product(list_1, list_2, repeat = 1):  # 서로 다른 두 list에서 
    print(prod)
# (1, 4)(1, 5)(1, 6)(2, 4)(2, 5)(2, 6)(3, 4)(3, 5)(3, 6)

for prod in product('abc', repeat = 3):           # 자기 자신을 반복해서 만들기
    print(prod)
# ('a', 'a', 'a')('a', 'a', 'b')('a', 'a', 'c')('a', 'b', 'a')('a', 'b', 'b')('a', 'b', 'c')...
```

