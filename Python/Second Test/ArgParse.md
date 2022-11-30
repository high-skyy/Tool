# ArgParse module

## Argparse 모듈이란?
ru.py라는 파이썬 스크립트가 있을 때 우리는 해당 파일을 명령 프롬프트에서 다음과 같이 실행할 수 있습니다.
```
$ ./run.py
```

만약 어떤 옵션에 따라서 파이썬 스크립트가 다르게 동작하도록 해주려면 명령행을 통해 이러한 인자를 받아야 합니다.

```
$ ./run.py -d 1 -f
```

## Argparse 기초
파싱할 인자를 add_argument method를 통해 추가해줍니다.
- 추가 옵션을 받는 경우 action = "store"를 사용합니다.
- 추가 옵션을 받지 않고 단지 옵션의 유/무만 피요한 경우 action="store_true"를 사용합니다.
- 사용자가 입력한 옵션 값은 dest 인자로 지정한 변수에 저장됩니다.

```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest = "decimal", action = "store")
parser.add_argument("-f", "--fast", dest = "fast", action = "store_true")
```

## Reference
- [Reference](https://wikidocs.net/73785)