# Brief information

## JSON (Java Script Object Notation)
> 일반적으로 protocol이라고 생각

- name-value 형식 (name은 항상 string type 이기 때문에 ""로 묶는다.)
```
{
    "key1" : "value"
    "key2" : 100
}
import json, requests
data = requests.get(URL).json()
```

## HTTP 메소드에 따른 요청
- GET, POST, PUT등의 방식을 지정하여 웹 요청을 해야할 때 다음처럼 코드를 작성하면 된다.
- POST와 PUT의 경우는 보통 데이터 생성과 수정을 일으키는 HTTP method
```
import requests
response = requests.get('https://api.github.com/events')
response = requests.post('https://httpbin.org/post', data = {'key' : 'value'}
```

## 웹 요청시 매개변수 전달 방법 (GET)
- GET 요청 기준으로 URL은 HOST + PATH ? Parameter1=value1&Parameter2=value2... 형식
```
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

# 아이스크림을 검색하는 url
# https://search.naver.com/search.naver?query=아이스크림
host = 'https://search.naver.com'
path = '/search.naver'
params = {'query': '아이스크림'}

url = host + path
response = requests.get(url, params=params)
```

## 응답 데이터(response)의 속성들
```
response.status_code        # 응답 상태 코드
response.url                # 요청했던 url

# 응답데이터(str) - 주로 웹 페이지 소스코드나 문자 데이터 or json을 확인할 때
response.text

# 응답데이터(byte) - 주로 음악, 비디오 등 byte 자체를 받아 저장시킬 때 사용
response.content

response.encoding           # 응답데이터의 인코딩 방식
response.headers            # 응답데이터의 헤더

# 응답 데이터가 json일 경우에는 굳이 import json의 dumps 함수를 쓰지 않아도 바로 변환이 가능하다.
data = response.json()
```

## POST 방식으로 요청
POST 방식으로 요청할 때 대부분 클라이언트 측에서 데이터를 전송한다. 그 데이터가 단순 객체 (변수 값 등)
이 될수도, 파일이 될 수도 있다.

- 단순 객체를 보낼 때에는 data 매개 변수를 사용한다.
```
data = {'key' : 'value'}
r = requests.post('https://httpbin.org/popst', data=data)
```
- 특정 파일을 보낼 경우에는 open 함수를 통해 해당 파일을 binary 형태로 데이터를 불러온 뒤, 실질적 웹 요청 때 files 매개변수에 넣어준다.
```
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
response = requests.post(url, files=files)
```
- 딕셔너리(dict)형 데이터를 전달해야할 때 json으로 변환하여 전달해야 한다.
```
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some' : 'data'}
r = requests.post(url, data=json.dumps(payload))
```

- 최근에는 json 매개변수가 따로 생김
```
url = 'https://api.github.com/some/endpoint'
payload = {'some' : 'data'}
r = requests.post(url, json=payload)
```

## curl 읽는 법
> REST api 문서들을 보면 curl 방식으로 가이드가 되어 있다.

-d : data 함께 전달할 파라미터 값 설정하기
-f : files
-j : json
-H : headers
-A : 헤더의 user-agent가 안내
-G : 전송할 사이트 url 및 ip 주소
-i : 사이트의 Header 정보만 가져오기
-l : 사이트의 Header와 바디 정보를 함께 가져오기
-u : 사용자 정보

### examples
```
curl -v -X POST "http://kapi.kakao.com/v1/vision/face/detect" \
-d "image_rul=https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/01.jpg" \
-H "Authorization: KakaoAK kkkkkkkkkkkkkkkkkkkkkkkkk"

import requests

url = "https://kapi.kakao.com/v1/vision/face/detect"
data = {'image_url' : 'https://t1.daumcdn.net/alvolo/\_vision/openapi/r2/images/01.jpg'}
header = {'Authorization':'KakaoAK kkkkkkkkkkkkkkkkk'}

res = requests.post(url, data=data, headers=header)
print(res.status_code)
```

```
curl -v -X POST "https://kapi.kakao.com/v1/vision/face/detect" \
-F "file=@sample_face.jpg" \
-H "Authorization: KakaoAK kkkkkkkkkkkkkkkkkkkkkk"

url = "https://kapi.kakao.com/v1/vision/face/detect"
files = {'file' : open('sample_face.jpg', 'rb').read()}
header = {'Authorization' : 'KakaoAK kkkkkkkkkkkkkkkkkk}

res = requests.post(url, files = files, headers = header)
print(res.status_code)
```

## Reference
- [Reference](https://qgqg264.tistory.com/49?category=797264)
- [Reference](https://gosmcom.tistory.com/130)