# Postgresql basic commands

## personal command $
```
# \d                            // database 내 relation 정보 확인
# SELECT* FROM pg_indexes WHERE tablename = [TABLE 이름];  // 해당 table의 index들을 조회
# \di                           // index 조회
```



## Basic Manipulation
```
UPDATE [테이블 이름] SET [컬럼 이름] = [값], , , WHERE [조건];
```

## index
```
CREATE INDEX [인덱스 이름] ON [테이블 이름] (컬럼 이름)       # 일반적으로
DROP INDEX [인덱스 이름]
```

## analyzing command
```
# explain analyze [Query 문]         // query plan 과 execution time을 알려준다.
```

## basic commands
```
# \h                            // sql에 대한 명령어 정보
# \l                            // 서버에 접속된 database 목록을 확인
# \d                            // database 내 relation 정보 확인
# \dt                           // database 내 table 조회
# \d+                           // relation 상세 조회
# \dS                           // system table 조회
# \dv                           // view 조회
# \dl                           // large object 조회
# \di                           // index 조회
# \df                           // function 조회
# \dn                           // schema 조회
# \c [DB 이름]                   // 다른 데이터 베이스 접속
# \q                            // psql 종료
# \set [name] [value]           // 변수 선언 및 초기화
# \echo [name]                  // 변수를 호출하여 변수에 저장된 값이 출력
# SELECT* FROM pg_indexes WHERE tablename = [TABLE 이름];
```
- [Reference](https://kwomy.tistory.com/8)