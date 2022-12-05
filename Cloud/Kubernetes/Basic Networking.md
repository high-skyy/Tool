# Kubernetes Basic Networking

## Introduction
![Kube network](https://user-images.githubusercontent.com/105041834/205608482-93fee1fa-ea75-4f29-9edf-b81a1cf627ef.jpg)
- Kubernetes 네트워크에서 파드는 기본적으로 서로 격리되어 있음.
  - 다만, 대부분 application은 외부의 요청에 대해 결과값을 반환하기를 원하고, 네트워크를 통해 파드끼리 통신해야하는 상황이 있다.
- 각 파드에 IP가 할당되므로 파드가 다른 IP에 직접 요청을 하게 되면
  - Cloud 친화적인 방법이 아니다.
    - 파드는 **언제든지 생성되고 소멸**될 수 있다.
    - Kubernetes system이 파드에 IP를 할당할 때, 파드가 배포될 노드가 선택된 후 실제 파드 시작 전에 IP가 할당된다.
      - Client가 타겟 파드의 IP주소를 알기 어렵다.
    - Scale-out 수행 시 파드의 수가 늘어나는데, 이때마다 **새로 할당되는 IP를 매번 클라이언트가 알기는 어렵다.**

## Service
![Kube pod networking](https://user-images.githubusercontent.com/105041834/205610388-80f7b4b3-c379-4f5f-b546-deaca91ba5d3.jpg)

- 같은 application을 구동하는 파드들에 대해서, **변하지 않는 하나의 접근 포인트를 제공**함.
  - Proxy -> 여기를 통해서 Pod로 전부 접근을 해라. (약간 router? NAT랑 비슷하다.)
- 직접 변경하지 않는 한, 서비스가 노출하는 IP 주소와 포트는 변하지 않음.
  - 서비스는 파드의 논리적 집합과, 그 파드들에 접근할 수 있는 정책을 정의하는 추상적인 개념

> 파드 집합에서 실행 중인 application을 네트워크 서비스로 노출하는 추상화 하는 방법

### Example
![Service Example](https://user-images.githubusercontent.com/105041834/205610734-1f3e7553-47eb-4d0d-8cba-9d13f92798d1.jpg)

### ClusterIP Service
- ClusterIP 타입의 서비스 -> 가장 기본적인 타입의 서비스
  - 파드를 Cluster 내부에서 접속 가능하록 노출하는 역할
  - Cluster 외부와는 격리되어 있으며 접속이 불가능함.

> DB 등의 서비스는 같은 Cluster에 배포된 프론트엔드 application에서는 접속이 가능해야 하지만.
> cluster 외부의 유저의 접속은 막아야 한다.

- ClusterIP 생성 (via kubectl)
```
$ kubectl apply -f deployment.yaml
$ kubectl expose deployment nginx-deployment -n lab06 --name=nginx-service
$ kubectl get services -n lab06
```

- ClusterIP 생성 (via .yaml)
```
$ kubectl apply -f deployment.yaml
$ kubectl apply -f service.yaml

# port : 서비스가 노출할 포트
# targetPort : 파드가 노출한 포트
{서비스IP}:port -> {파드IP}:targetPort
```

### NodePort Service
- NodePort 타입의 서비스 -> 클러스터 내 모든 노드들의 같은 포트에 서비스를 노출
  - ClusterIP 타입 서비스를 기반으로 구현됨
  - Cluster 외부에서도 접속 가능
  - Cluster를 구성하는 임의의 노드에 접속해도 서비스 연결됨.
    - ex) nodePort를 30123으로 설정하면, {노드1_IP}:30123 이나 {노드2_IP}:30123 모두 접속이 가능함.
  - 외부에 서비스를 노출하기 위한 가장 간단한 방법.

- yaml
  - port : 서비스가 노출할 포트
  - targetPort : 파드가 노출한 포트
  - nodePort : 클러스터 외부로 노출할 포트
  - {노드IP}:nodePort -> {서비스IP}:port -> {파드IP}:targetPort

### LoadBalancer Service
![Kube Loadbalancer](https://user-images.githubusercontent.com/105041834/205612972-b2db9242-c963-4e1e-8bce-ca70f38b81c7.jpg)

- LoadBalancer 타입의 서비스
  - **NodePort 타입 서비스를 기반**으로 구현됨
  - **Cluster 외부에서도 접속 가능**
  - 상용 클라우드 플랫폼에서 제공하는 load balancer와 연동
    - 상용 클라우드 서비스를 사용하지 않는 경우 연동이 어려움
  - LoadBalancing 기능 제공

## Reference
- [Reference](학교 ppt 자료)