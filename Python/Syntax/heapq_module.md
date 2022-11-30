# Heapq module
```
import heapque
heapq.(name of functions)
```
> heap은 기본적으로 완전히 정렬되는 것이 아니다. 최대, 최소만을 반환하는 함수가 필요할 때 사용하는 것이 유용하다
## Functions
```
import heapq
list_1 = []
heapq.heappush(list_1, 3)             # heapq.heappush(list 이름, push하고 싶은 item)
heapq.heappush(list_1, 2)
heapq.heappush(list_1, 1)
print(list_1)                         # [1, 3, 2]
print(heapq.heappop(list_1))          # heapq.heappop(list 이름)
print(heapq.heappop(list_1))
print(heapq.heappop(list_1))
list_2 = [3,2,1,5,0,4]
heapq.heapify(list_2)                 # heapq.heapify(heap으로 만들고 싶은 list)

# 해당 리스트를 직접 heap으로 만들어줌 새로 반환하는 것이 아닌 그 list자체를 변형 시킨다.    
print(list_2)           # [0, 2, 1, 5, 3, 4]

print(heapq.nsmallest(3, list_2)[-1])
# heapq.nsmallest(몇 번째 작은 원소, 리스트의 이름)[-1]
# [-1] 까지 해야 해당 원소를 반환한다. nlargest()도 가능하다.
```

## Heap을 이용한 정렬
> 힙 정렬은 해당 리스트를 heappush를 한 뒤 heappop을 하게 되면 정렬된 list가 나온다.
```
import heapq
list_1 = [5,4,3,2,1]
list_2 = []
list_3 = []
for i in range(len(list_1)):
    heapq.heappush(list_2, list_1[i])

for i in range(len(list_2)):
    list_3.append(heapq.heappop(list_2))
print(list_3)           # [1,2,3,4,5]
```

## min heap이 아닌 max heap을 사용하고 싶을 경우
> heap은 list나 튜플의 앞 index에 따라서 차례로 정렬해주기 때문에 첫 index에 priority를 넣어주면 된다.
```
import heapq
list_1 = [5,4,3,2,1]
list_2 = []
list_3 = []
for i in range(len(list_1)):
    heapq.heappush(list_2, (-list_1[i],list_1[i]))

for i in range(len(list_2)):
    list_3.append(heapq.heappop(list_2)[1])
print(list_3)         # [5, 4, 3, 2, 1]
```
