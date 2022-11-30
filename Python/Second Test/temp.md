# Temporary file for test

## __name__ == __main__
import 만 시켜도 함수가 실행이 됨.
```
testModule.py

def add(x,y) : 
  return x + y

# 이 아래 부분이 없으면 import 시켜도 함수가 실행 됨
# 터미널에서 직접 호출이 되는 경우 사용되고 아니면 동시에 다른 모듈에서 필요한 경우 import 시켜서 사용
# import가 되면 __name__ 변수에는 모듈 이름이 들어가 있음
if __name__ == "__main__":
  print(add(3,4))
```

## JSON object
- response.json()
  - 만약 response가 json 형식이라면 json object를 반환하고 python은 이를 dictionary로 인식한다.

## Shell-script
$을 앞에 붙여서 변수를 나타낸다. 하지만 ${변수}를 해야지만 작동하는 것들이 있음 (ex : echo)

## Reference
- [Reference](https://madplay.github.io/post/python-main-function)