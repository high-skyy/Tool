# Docker compoese
multi-container application을 정의하고 구동하는 툴
> 앱에 대한 구성은 docker-compose.yaml에 YAML 포맷으로 기술함.

## 특징
- docker-compose에서는 기본적으로 bridge network를 생성함.
  - (프로젝트 이름)_default 라는 네트워크를 생성하며, 특별히 지정해주지 않으면 컨테이너들이 이 네트워크에 연결 되어 있어 서로 통신이 가능함.

## 3-Tier Architecture
- Presentation Tier
  - 일반 사용자가 애플리케이션과 상호 작용하는 인터페이스 통신 계층 (Front-end)
- Application Tier
  - Presentation Tier에서 수집된 정보 처리
- Database Tier
  - 데이터의 저장 및 관리 계층 (RDBMS, NoSQL 등의 데이터베이스)

- 각 계층(tier)은 논리적 역할로 분리 구성한 디자인이지만, 실제로 구동되는 **물리적 위치** 에 따라 구분되어 있다.
  - 각 계층이 자체 인프라에서 실행될 수 있음 (별도의 개발 사이클을 가지고 개발되며), 계층 간 영향을 끼치지 않고 배포, 확장 등이 가능함

## 명령어
```
$ docker-compose up
$ docker-compose down
```

### Options
- -d : 옵션 적용 시 백그라운드 실행

## Yaml file
- version : docker-compose file 버전
- depends_on : **서비스 간 의존성**을 표시할 때 사용함. 여기서는 db 서비스가 생성된 후 wordpress가 생성됨.

## Reference
- [Reference](학교 자료)