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

-f : files
-j : json

-G : 전송할 사이트 url 및 ip 주소
-u : 사용자 정보

-i(--include) : 응답에 Content만 출력하지 않고 서버의 Response도 포함해서 출력
-A(--user-agent) : 서버에 User-Agent <name> 보내기
-k(--insecure) : https protocol에서 SSL인증서에 대한 검증없이 연결
-l(--head) : HTTP 헤더만 보여주고 컨텐츠는 표시하지 않음
-D(--dump-header<file>) : HTTP 헤더를 file에 기록 (덤프)
-L(--location) : HTTP 301, 302 응답을 받은 경우 리디렉션 URL로 따라간다.
-d(--data) : HTTP POST 요청 데이터 입력
-v(--verbose) : 동작하면서 세세한 내용을 출력
-J(--remote-header-name) : 헤더에 있는 파일 이름으로 다운로드 파일을 저장
-o(--output FILE) : curl로 받아온 내용을 FILE 이라는 이름의 파일로 저장.
-O(--remote-name) : 파일 저장시 리모트에 저장되어 있는 이름을 그대로 가져와서 로컬에 저장
-s(--silent) : 진행 내용이나 메세지들을 출력하지 않음
-X(--request) : 요청시 사용할 메소드의 종류 (GET, POST, PUT, PATCH, DELETE)
-H(--header) : 헤더를 보낸다. (헤더가 여러 개일 경우, 파라미터를 여러 개 붙인다.)


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