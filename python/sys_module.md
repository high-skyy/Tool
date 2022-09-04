# import sys

## Brief explanation
sys 모듈은 파이썬 interpreter가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
> 직접적으로 제어를 할 수 있다.

## 명령실행 시 형태
명령 프롬프트 창에 다음과 같이 명령어를 치면.
```
(directory)>python (파일이름).py 변수1 변수2 변수3
```
py까지만 하면 파일의 실행이지만 sys.argv리스트에 그 값이 추가된다.
```
['(파일이름).py', '변수1', '변수2', '변수3']
```
## 사용자 입력 sys.stdin.readline()
> input( )과 같은 역할을 하지만 input( ) 보다 더 빠르게 동작한다.

## (추가사항)
- 강제로 스크립트 종료하기 ( sys.exit() )
```sys.exit()```

- 자신이 만든 모듈을 불러와 사용하기 ( sys.path )
sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다.
> sys.path는 list의 형태를 띠고 list에 경로를 추가해주게 되면 모듈들을 가져와 사용할 수 있다.
```sys.path.append("<경로>")```


## References
[Reference](https://wikidocs.net/33#:~:text=sys%20%EB%AA%A8%EB%93%88%EC%9D%80%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0,%EC%88%98%20%EC%9E%88%EA%B2%8C%20%ED%95%B4%EC%A3%BC%EB%8A%94%20%EB%AA%A8%EB%93%88%EC%9D%B4%EB%8B%A4.&text=%EB%AA%85%EB%A0%B9%20%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8%20%EC%B0%BD%EC%97%90%EC%84%9C%20%EC%9C%84,%EA%B7%B8%20%EA%B0%92%EC%9D%B4%20%EC%B6%94%EA%B0%80%EB%90%9C%EB%8B%A4.)
