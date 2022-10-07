# index를 postgreSQL 내부에서 구현 및 사용되는 방법

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

## index Types
PostgreSQL provides several index types: B-tree, Hash, GiST, SP-GiST, GIN and BRIN  
By default CREATE INDEX command creates B-tree indexes. (other index types are selected by writing the keyword USING followed by the index type name)
```
// example
# CREATE INDEX [name] ON [table name] USING HASH (column);
```

### B-Tree
B-trees can handle equality and range queries on data that can be sorted into some ordering.
In particular, the PostgreSQL query planner will consider using a B-tree index whenever an indexed column is involved in a comparison using(< <= = >= >)
> B-tree의 경우는 indexed 된 column을 비교하는 query문이 있을 때 항상 고려된다.

### Hash
Hash indexes store a 32-bit hash code derived from the value of the indexed column.
Hence, such indexes can only handle simple equality comparisons.
The query planner will consider using a hash index whenever an indexed column is involved in a comparison using (=)
> Hash index의 경우 index된 column에 대한 32-bit hash code를 저장한다. Query planner의 경우 hash index를 = 으로 비교할 때에만 주로 사용한다.

### GIST
GIST indexes are not a single kind of index, but rather an infrastructure within which many different indexing strategies can be implemented.
Accordingly, the particular operators with which a GiST index can be used vary depending on the indexing strategy.
As an example, the standard distribution of PostgreSQL includes GiST operator classes for several two-dimensional geometric data types
which support indexed queries using (<< &< ...)
> GIST index의 경우 여러 index를 구현하느데 사용된다. 예시 : two-dimensional geometric data

- [Reference](https://www.postgresql.org/docs/current/indexes-types.html) 

[Reference](https://storycode.tistory.com/449)