# PUT & POST

## POST
### POST의 정의
- Request(요청)에 포함된 Entity(Http body에 해당)을 Request-URI에 정의된 resource의
하위(Suboridiate) Enitity로 새롭게 생성하는 요청을 서버에 보낼때 사용되는 Http method
- 따라서 Request-URI는 resource의 Entity를 나타내는 Collections URI여야 한다.
> 예를 들어, 신발들의 정보를 저장하는 shoes가 있다.
> shoes라는 큰 카테고리 밑에 하위 item으로 등록되고 저장될 것이다.
> URI는 신발 정보의 Collection-URI는 /shoes가 된다.

## PUT
### PUT의 정의
- Request-URI에 있는 Resource가 존재한다면, Request에 있는 Entity에 값으로 resource를
Update(갱신 한다.)
- 만약 Resource가 존재하지 않고, Request-URI와 Resource-URI가 올바르다면 

## Reference
- [Reference](https://kingjakeu.github.io/study/2020/07/15/http-post-put/)