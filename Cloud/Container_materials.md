# Container

## Docker Container
- 가상화된 공간을 linux 자체 기능인 chroot, namespace, cgroup를 사용함으로써 프로세스 단위의 격리 환경을 만드는 기술
![VM   Container](https://user-images.githubusercontent.com/105041834/198866617-14896b03-1aeb-4d25-b69b-5cb212e34cfe.jpg)

### Features
- 성능 손실이 거의 없다.
- Container에 필요한 kernel은 Host의 kernerl과 공유하여 사용한다.
- 경량 이미지(lightweight)
  - Container 안에는 어플리케이션 구동에 필요한 라이브러리 및 실행 파일만 존재함
  - Kernel에 필요한 code가 필요 없음

### Container technique의 장점
- Application 개발 및 배포의 편리화

- 특징
  - Docker container는 HOST OS 위에서 실행되는 격리된 공간
  - Container 내부에는 각종 SW 설치하고 설정 파일을 수정해도 HOST OS에 영향이 없다.
  - 독립된 개발 환경을 보장받을 수 있음
  - Container 내부에서 작업을 마치고 운영 환경에 배포하려면 Container 'Docker image' 라는 package로 만들어서 운영 server에 전달하면 됨
    - 운영 서버에서 새롭게 패키지를 설치할 필요 x
    - 라이브러리 설치 의존성 문제도 필요가 없다.

- Application의 독립성 및 확장성이 높아짐

- 특징
  - Container는 몇 초 안에 생성, 시작이 가능하고 여러 모듈에 독립된 환경을 동시 제공할 수 있기 때문에 MSA(Microservice Architecture)에서 가장 많이 사용되는 가상화 기술임

#### MSA(MicroService Architecture)
소프트웨어의 여러 모듈이 상호 작용하는 로직을 각각 독립된 형태로 구성하여 구동하는 방식 (구조)

- 특징
  - 대비 -> Monolithic 구조 : SW의 여러 모듈이 상호 작용하는 로직을 하나의 프로그램 내에서 구동시키는 방식.
  - MSA는 여러 모듈을 독립된 형태로 구성하므로 언어에 종속되지 않고, 변화에 빠르게 대응할 수 있으며, 각 모듈의 관리가 쉬워짐
  - 작고, 독립적으로 배포 가능한 각각의 기능을 수행하는 서비스로 구성된 Framework
  - 완전히 독립적으로 배포가 가능하고, 다른 기술 스택이 사용 가능한 단일 사업 영역에 초점을 둔다.
  - 독립된 서비스는 API를 통해서만 상호작용한다.

## Reference
- [Reference](학교 ppt)