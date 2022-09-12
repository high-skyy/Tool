# Basic Functions

## 형 변환
syntax : int( 변환해야 할 변수 ) 
```
int(<variable>)
float(<variable>)
list (<variable>)
tuple(<variable>)
```

## range function
syntax : range( start, end, step )
> start에서 시작하여 end까지 step만큼 씩 증가 시킨다.
```
print(list(range(5))              # [0, 1, 2, 3, 4]
print(list(range(1, 10))          # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 100, 11))     # [1, 12, 23, 34, 45, 56, 67, 78, 89]
```

## list methods
### list의 길이
syntax : len(list)
```
len( list_name )
```

### 리스트 삭제(index)
syntax : del 리스트명[인덱스], 리스트명.pop(인덱스)
```del list1[0]
list1.pop(0)
# 삭제가 될 경우 다시 리스트의 앞 부터 채워준다. 해당 값에 default값이 들어가는 것이 아니다.
```

### 리스트 삭제(value)
syntax : 리스트명.remove(값)
```list1.remove(value)
# 주의 사항 : 가장 먼저 발견한 값 만을 삭제해준다. 전부 다 삭제하고 싶을 경우 for문을 이용하자.
# 해당 value가 list 내부에 존재하지 않을 경우에 오류가 발생한다.
```
### insert
> **리스트 이름**.insert(**index**, **object**)
해당 자리에 오브젝트가 들어가며 자동적으로 list가 이에 맞춰 배열됨 (사이에 들어갈 때만)
```
a = [1,2,3]
a.insert(0,'4')
print(a)                # ['4', 1, 2, 3]

list_1 = []
list_1.insert(4, 0)
print(list_1)               # [0]
```

### index
첫 번째 일치 항목의 인덱스를 반환
> **리스트 이름**.index(**value**)
```
a = [1,2,3,1]
print(a.index(1))               # 0
```

### count
인수로 전달 된 항목 수의 개수를 반환한다.
> **리스트 이름**.count(**value**)
```
a = [1,2,3,1]
print(a.count(1))               # 2
```

### reverse
목록의 항목 순서를 반대로 바꿉니다.
> **리스트 이름**.reverse()
```
a = [1,2,3]
a.reverse()
print(a)                    # [3, 2, 1]
```

### 특이점 
python의 경우 list의 비교시 == 으로 직접 비교가 가능하다.
```
x, y = [[1,2], [3, 4]], y = [[1,2], [3,4]]
x == y                  # True가 된다.
```

## print 함수들
```
print("a + b :", a+b)       # a + b = 15
print('a', end = ' ')       # end가 없을 경우 \n이 발생함
print("a", "b", "c", "d", sep = '*')    #a*b*c*d (끝에는 *이 없음)
```

## Sorted 함수
syntax : 리스트명.sort( )
```
list1 = [2, 1]
list1.sort()
print(list1)          # [1, 2]
# 원래 list 자체가 변형된다.
```
syntax : sorted ( 리스트명, reverse = True/False, key = 해당 파라미터 )
```
list1 = [3, 5, 2, 1, 4]
list2 = [[1,2], [2,1], [1,3], [3,1]]
print(sorted(list1))                      # [1, 2, 3, 4, 5]
print(sorted(list1, reverse = True))      # [5, 4, 3, 2, 1]
print(sorted(list2, key = lambda x : x[1]))   # [[2, 1], [3, 1], [1, 2], [1, 3]]
```

##  lambda 함수
syntax : lambda 매개변수 : 결과
```
def 함수이름(매개변수):
    return 결과
```
와 같은 역할을 한다.
```
list_1 = [1,2]
c = lambda x : x[1]
print(c(list_1))            # 2
print((lambda x : x[1])(list_1))      # 2

list_2 = [[1,2], [3,4], [1,3], [5,1]]
print(sorted(list_2, key = lambda x : x[1]))      # [[5,1], [1,2], [1,3], [3,4]]
```

## Set 함수
- 집합을 나타낸다.
```
list_1 = [1,1,2,2,2,3,4,4]
p = set(list_1)
print(p)                    # {1,2,3,4} 
```
- 데이터 추가
* syntax : 집합이름.add(추가 하고 싶은 것)
* syntax : 집합이름.update(추가하고 싶은 list)
```
p.add(5)                 # {1,2,3,4,5}
p.update([5,6,7])        # {1,2,3,4,5,6,7}
```
- 데이터 삭제
* syntax : 집합이름.remove(제거 하고 싶은 것)
* syntax : 집합이름.discard(제거하고 싶은 것)
```
p.remove(3)             # {1,2,4,5}
p.discard(5)            # {1,2,5}
# remove 같은 경우에는 원소가 존재하지 않을 시 오류가 발생하지만 discard의 경우에는 원소가 존재 하지 않아도 에러가 발생하지 않는다.)
```
- 연산자 이용 가능 (| : 합집합, & 교집합, - : 차집합, ^ : 합집합 - 교집합
```a | b     a & b      a - b       a ^ b```

## python 만의 list 쉽게 사용 하는 방법
```
list_1 = [x * y for x in range(1,10) if x is 3 or x is 7 for y in range(1,10)]

for x in range(1,10):
    if x is 3 or 7:
        for y in range(1,10):
            list_1.append(x*y)
# 위와 아래의 식들이 동일하다.
```
```
print([[1] * 5])         # [[1, 1, 1, 1, 1]]
print([[1] * 3 for i in range(3)])    # [[1,1,1], [1,1,1], [1,1,1]]
```

## if의 인자에 따른 특별한 결과
- None을 주면 거짓 None이 아닌 값을 주면 참
```
if None : print("Yes")        # 
if not None : print("Yes")    # Yes
```
- 숫자의 경우는 0이면 거짓이고 아닌 경우에는 전부 참이 된다.
- 문자열의 경우는 내용이 있으면 참이고 아니면 거짓이 된다.
- 리스트, 튜플인 경우 내용이 있으면 참 아니면 거짓이다.

## sum 함수
Syntax : sum(iterable한 변수, (시작 값 : sum에 포함되는 값 index가 아니다.)start = 0)
```
list_1 = [2,3,4]
print(sum(list_1, start = 0))       # 9
print(sum(list_1, start = 1))       # 10
```

## zip 함수
syntax : zip(iterable한 변수, iterable한 변수, iterable한 변수)
짝을 지어준다.
```
list_1 = [2,3,4]
list_2 = [1,2,3]
for _ in zip(list_1, list_2):
    print(_)                          # (2,1)\n (3,2)\n (4,3)
```
```
dict_1 = {"A" : 1, "B" : 2, "C" : 3}
dict_2 = {"1" : "A", "2" : "B", "3" : "C"}
for _ in zip(dict_2, dict_2):
    print(_)                        # ('a', '1') \n('b', '2') \n('c', '3')
# 사전은 key값 끼리만 pair가 이루어진다.
# 각자 끼리 하고 싶으면 tuple(key, value)가 나타나는 형태로 바꾸어서 해야 할 것 같다.)
```

## Reference
[Reference] (https://sinaworld.co.kr/39)
