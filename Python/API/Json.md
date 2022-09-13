# How to use API

## JSON (JavaScript Object Notation)
- JavaScript Object Notation이라는 의미의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 DATA 교환 방식**
- JSON은 데이터 포맷일 뿐이며 어떠한 통신 방법도, 프로그래밍 문법도 아닌 단순히 데이터를 표시하는 표현 방법일 뿐이다.

## Json 특징
- 서버와 클라이언트 간의 교류에서 일반적으로 많이 사용된다.
- JSON 문서 형식은 자바 스크립트 객체의 형식을 기반으로 만들었지만 텍스트 형식일 뿐이다.

## JSON 형식
- JSON 형식은 자바스크립트 객체와 마찬가지로 key / value가 존재할 수 있으며 key값이나 문자열은 항상 쌍따옴표를 이용하여 표기
- 객체, 배열 등의 표기를 사용할 수 있따.
- 일반 자바 스크립트의 객체처럼 원하는 만큼 중첩시켜서 사용할 수도 있다.
- JSON 형식에서는 **null, number, string, array, object, boolean**을 사용할 수 있다.
```
{
  "employees": [
    {
      "name": "Surim",
      "lastName": "Son"
    },
    {
      "name": "Someone",
      "lastName": "Huh"
    },
    {
      "name": "Someone else",
      "lastName": "Kim"
    } 
  ]
}
```
1. name-value 형식의 쌍
> {String key : String value}
- 여러가지 언어들에서 object등으로 실현되었다.
- name은 항상 string 타입이기 때문에 ""로 묶인다.
- value 는 string, int, array 전부 다 된다.
```
{
  "firstName": "Kwon",
  "lastName": "YoungJae",
  "email": "kyoje11@gmail.com"
}
```
2. 값들의 순서화된 리스트 형식
> \[value1, value2, ...]
- 여러가지 언어들에서 배열(Array)등으로 실현되었다.
```
{
  "firstName": "Kwon",
  "lastName": "YoungJae",
  "email": "kyoje11@gmail.com",
  "hobby": ["puzzles","swimming"]
}
```

## REST API를 이용해서 받아온 값을 JSON 형태로 이용하기
- http 요청을 통해 가져온 json 파일을 파이썬에서 사용
```
import json, requests
data = requests.get(URL).json()
```
- 가져온 JSON 파일을 Parsing 해서 사용하기!
```
value = data["people"]
# 아까도 말했듯이 name은 
```


## Reference
[Reference](https://qgqg264.tistory.com/49)
[Reference](https://velog.io/@surim014/JSON%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)
