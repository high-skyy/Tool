# 내용들을 여러 파일로 분류하기 전 모아 temp file

## Post

## Basic commands

## Scan 방식
- Seq Scan 방식
  - Seq Scan은 table을 Full scan 하면서 레코드를 읽는 방식이다.
  - Index가 존재하지 않거나, 인덱스가 존재하더라도 읽어야 할 범위가 넓은 경우에 선택한다.
- Index Scan 방식
  - Index Scan은 Index Leaf block에 저장된 키를 이용해서 table record를 access하는 방식이다.
  - Index key 순서대로 출력된다.
  - Record가 정렬 상태에 따라서 테이블 블록 액세스 횟수가 크게 차이 난다.
- Index-Only Scans
  - Postgres 특징상 Index-Only Scan을 지원하는 원리

All indexes in PostgreSQL are secondary indexes, meaning that each index is stored separately from the table's main data area
(which is called the table's heap in PostgreSQL terminology)  
This means that in an ordinary index scan, each row retrieval requires fetching data from both the index and the heap.
Furthermore, while the index entries that match a given indexable WHERE condition are usually close together in the index, the table rows they 
reference might be anywhere in the heap. The heap-access portion of an index scan thus involves a lot of random access into the heap, which can be slow.
> PostgreSQL에서는 모든 index가 secondary index(non-cluster index)로 구현이 된다. 즉, Table의 main data area와 다른 곳에서 저장이 된다.
> (PostgreSQL에서는 table의 main data area를 table's heap)이라고 부른다.
> 
> 따라서 index scan이 이루어질 경우 index와 heap 두 곳에서 모두 data를 fetching해야 한다. (컴퓨터 paging 기법에서 page table에서 주소 가져오는 것과 해당 주소를 이용해 진짜 정보 가져오는 것이랑 같은 개념)
> 
> PostgreSQL에서는 모든 index가 secondary index로 저장이 되기 때문에  index file내에서는 index에 해당하는 search key가 서로 가까운 곳에 위치할 수 있지만 heap(main data area)에서는 이들의 정보가 가깝지 않을 수 있다.

To solve this performance problem, PostgreSQL supports index-only scans, which can answer queries from an index alone without any heap access.
The basic idea is to return values directly out of each index entry instead of consulting the associated heap entry.
There are two fundamental restrictions on when this method can be used.
1. The index type must support index-only scans(B-tree indexes always do)
2. The query must reference only columns stored in the index

> 해당 문제를 해결하기 위해서 PostgreSQL은 index-only scan을 제공한다. (heap access 이용하지 않고 index entry 만을 이용해 query에 답을 한다.)
> 
> 가능하기 위해서는 (index type이 index-only scan을 support 해야 한다. + query가 오직 index에 저장된 column 즉 index의 바탕이 되는 attribute만을 reference 해야 한다.)


- [Reference](https://www.postgresql.org/docs/current/indexes-index-only-scans.html)

## Cluster-Index
> 일반적으로 PostgreSQL은 table의 attribute들의 distribution을 확인하여 index를 만들면 자동적으로 cluster 또는 non-cluster index를 만들어준다.

**CLUSTER** instructs PostgreSQL to cluster the table specified by **table_name** based on the index specified by **index_name**.
The index must already have been defined on **table_name**.
> **CLUSTER** 라는 명령어롤 통해서 PostgreSQL은 table을 cluster 시킬 수 있다.
```
CLUSTER table_name [ USING index_name ]
```

When a table is clustered, it is physically reordered based on the index information.
Clustering is a one-time operation: when the table is subsequently updated, the changes are not clustered.
That is, no attempt is made to store new or updated rows according to their index order.
(If one wishes, one can periodically recluster by issuing the command again.)
> Table에게 Clustered 명령어가 실행이 되면 index 정보들을 가지고 table들이 reordered된다. 하지만 PostgreSQL에서는 새로운 attribute
> 의 추가나 update가 된 tuple들에 대해서는 다시 clustering 시켜주지 않는다. 따라서 cluster를 유지하고 싶을 경우에는 다시 명령어를 통해
> 본래 Table을 다시 정렬 시켜주어야 한다.


When a table is clustered, PostgreSQL remembers which index it was clustered by.
The form **CLUSTER table_name** reclusteres the table using the same index as before.
> Table이 clustered될 경우 PostgreSQL은 해당 cluster의 기준이 되는 index를 기억하고 아래 명령어를 통해 같은 index로 recluster가 가능하다.
```
CLUSTER table_name
```

- [Reference](https://www.postgresql.org/docs/current/sql-cluster.html)

[Reference](https://storycode.tistory.com/449)