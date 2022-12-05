# Basics for Kubernetes

## Introduction
- Container Orchestration
  - 컨테이너의 배포, 관리, 확장, 네트워킹을 자동화

- Container의 이점
  - Portability
    - 컨테이너는 Application과 의존성까지 래핑한 단위로 배포 되기 때문에, 어떤 환경에서든 컨테이너를 쉽게 사용하게 함.
    - ex) Python에 관련된 Application은 python 3 interpereter를 같이 가지고 다닌다.
  - Application deployment
    - 컨테이너를 이용한 애플리케이션 개발은 기존 환경에 비해 빠른 개발 및 배포 주기를 가질 수 있음.
  - Resource utilization and optimization
    - 컨테이너는 lightweight, ephemeral(짧은 시간 동안 존재)

- Container Orchestration의 이점
  - Simplified operations
    - 많은 컨테이너 종류와 수로 이루어진 복잡한 서비스를 관리할 때, 간단한 조작으로 달성할 수 있음.
  - Resilience
    - 서비스에 fail이 발생한 경우, 자동으로 컨테이너를 재시작하거나 스케일 함.
  - Added security
    - 역할 기반 접근 제어 (R BAC, Roll-Based Access Control)
    - 자동화된 시스템으로 Human error의 발생을 줄임.

## Kubernetes의 역할
- Service Discovery and Load Balancing
  - DNS Name이나 자체 IP 주소를 이용해서 컨테이너를 노출할 수 있음.
  - 네트워크 트래픽에 대한 로드 밸런싱을 통해 안정적인 서비스 운영을 달성
- Storage Orchestration
  - Local storage, public cloud storage등 원하는 스토리지를 자동으로 마운트
- Automated Tollouts and Rollbacks
  - Container의 배포에 대해 원하는 상태(desired state)를 미리 작성해 둘 수 있음
  - 쿠버네티스는 원하는 상태를 달성하기 위해 자동으로 rollout/rollback을 시도함.
- Automatic Bin Packing
  - 각 컨테이너가 resource(CPU, RAM등)을 얼마나 필요로 하는지 설정 가능
  - Resource file의 사용률을 자동으로 최적화함.
- Self-Healing
  - 컨테이너에 fail이 발생하면 다시 시작하고, 교체
  - user-defined health check에 응답하지 않는 컨테이너들은 강제 종료
  - 이러한 모든 과정을 클라이언트에게서 감춤.
- Secret and Configuration Management
  - OAuth Token, SSH Key 등과 같은 정보들을 저장하고 관리




## Reference
- [Reference](학교 자료)