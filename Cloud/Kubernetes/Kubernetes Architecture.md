# Kubernetes Architecture

## Basic objects in Kubernetes
- Cluster, Node -> 쿠버네티스 물리적 구성요소
- Container, Pod -> 배포 대상
- Deployment -> Pod 관리
- Service -> Pod의 노출.

## Kubernetes Cluster
- 1 Master Node (Control Plane)
- 1 ~ Worker Node (Data Plane, Compute Machine)
![Kubernetes](https://user-images.githubusercontent.com/105041834/205571950-40ff5c07-5521-43c3-9ca4-16565b9e5b99.jpg)

### Control Plane Components
![Kube Control Plane](https://user-images.githubusercontent.com/105041834/205577482-6373b320-489d-4fdd-856b-ffae54b1b41e.jpg)
- kube-apiserver (pod)
  - Kubernetes API를 노출하여 Control Plane의 Front-End 역할을 수행
  - kubectl 명령 + REST API를 통해서도 접근 가능
- etcd (pod)
  - 클러스터에 관련된 설정, 상태 데이터를 저장하는 key-value store
  - kube-apiserver를 통해서만 접근 가능
- kube-scheduler (pod)
  - 노드가 할당되지 않은 상태인 파드를 감지하고 어떤 노드로 배포할 지 Scheduling을 담당
  - 여기서 Load balancing이 일어날 것 같다.
- kube-controller-manager (pod)
  - 쿠버네티스 오브젝트들을 관리하는 controller들을 모두 통합한 모듈
  - Node Controller, Replication Controller, Endpoint Controller등이 포함되어 있음.

### Node Components
![Kube Node](https://user-images.githubusercontent.com/105041834/205578418-655608dc-8276-46b0-9097-6c343cc48aba.jpg)
- kublet (linux daemon)
  - 노드마다 하나씩 구동되어서 Control Plane과의 통신을 담당함.
  - Container가 실행되도록 Container Runtime을 제어
  - PodSpec에 따라 파드가 동작하도록 지속적인 관리
- Container Runtime
  - Docker, containerd 등 컨테이너 런타임
- kube-proxy (pod)
  - 네트워크 프록시 역할. 노드의 네트워크 규칙을 유지 및 관리

### Kubernetes Installation
- 관리형 쿠버네티스 서비스 (Managed Kubernetes Services)
  - Google Kubernetes Engine
  - AWS Elastic Kubernetes Services
  - Azure Kubernetes Service
- Self Hosting
  - kubeadm
    - 쿠버네티스에서 공식으로 제공하는 클러스터 설치 및 관리 툴
    - 베어 메탈 서버나 클라우드 인스턴스를 빌려 설치하는데에 적합함
    - (이미 노드들을 갖고 있을 때, 그 위에 쿠버네티스를 설치하는 역할만 담당)
  - kops
    - provisioning(특정 서비스를 제공받기 위하여 서비스 실행부터 시작해 서비를 제공 받기 전 단계까지 처리되는 일련의 절차를 말한다.)까지 수행함.

## Basic Objects

### Pod
![Kube Pod](https://user-images.githubusercontent.com/105041834/205579628-3aa6d0a3-1ebe-4f20-8b77-1cb4b07e40ee.jpg)
- 쿠버네티스에서 생성하고 관리하는 **배포 가능한 가장 작은 컴퓨팅 단위**
- 애플리케이션 별 논리적 호스트를 모델링한 오브젝트이다.
  - Host위에 여러 application(Guest OS)가 올라간다고 생각하면 이해가 된다.
- 하나 이상의 컨테이너의 그룹으로 구성됨.
  - 파드 내의 컨테이너들은 스토리지와 네트워크를 공유함.

![Pod Networking](https://user-images.githubusercontent.com/105041834/205580387-37da08bf-0452-4f75-b05e-314d44265ac9.jpg)
- Networking in Pods
  - 각 파드에는 고유한 IP 주소가 할당되며, 이 네트워크 네임스페이스는 파드 내 모든 컨테이너가 공유함.
  - 즉, 파드 내에 모든 컨테이너가 파드의 고유한 IP를 사용한다.
- 파드는 kubectl run 명령으로 실행할 수 있음 (권장 X)
- yaml 파일에 파드의 원하는 상태(desired state)를 기술하여 yaml파일을 클러스터에 전달하는 방식으로 생성하는 것이 권장됨
```
$ kubectl apply -f filenmae.yaml
```
- Pod Lifecycle
  - Pending : 파드 생성이 승인되었지만 컨테이너가 설정되지 않았고 실행 준비가 되지 않은 상황
    - 컨테이너 이미지 다운로드 시간을 포함하여, **스케줄되기 이전**
    - 마치 프로그램이 아직 CPU를 할당 못 받은 상황이라고 생각하면 되겠다.
  - Running : 파드가 **노드에 바인딩**되었고, 모든 컨테이너가 생성됨.
  - Succeeded : 모든 컨테이너가 **성공적으로 종료**됐고 재시작되지 않을 것임.
  - Failed : 모든 컨테이너가 종료되었지만, **하나 이상의 컨테이너가 실패**로 종료됨.
  - Unknown : 추적이 불가능한 경우
  
> 컨테이너는 근본적으로 프로세스이며, Pod는 컨테이너들을 실행하기 위해 논리적으로 격리된 환경
### ReplicaSet
- 일반적으로 파드를 kubectl run 명령이든, yaml 파일이든 직접 생성하지는 않음.
  - Deployment, ReplicaSet, Job과 같은 **workload resource**를 사용하여 ** 간접적으로 파드를 생성함.

- Pod 집합의 실행을 안정적으로 유지하기 위해, **파드의 개수(Replica)를 일정**하게 유지함.
- ReplicaSet은 파드에 label을 달아서 어떤 파드들이 연결되어 있는지를 파악함.
- 파드의 yaml 파일은 ReplicaSet의 yaml에서 spec.template 아래에 기술함.
  - -> (PodTemplate)

> Pod를 간접적으로 생성하고, Pod의 개수를 일정하게 유지하는 resource


### Deployment
- ReplicaSet은 파드의 replica 개수를 유지하는 역할만 수행함.
- Kubernetes가 application instance를 어떻게 생성하고 업데이트해야 하는지 선언함.
- 파드의 scaling, update, version 추적 등의 역할
- 선언한 스펙에 따라 파드의 개수, 상태 등을 ReplicaSet을 생성해서 유지함.

> ReplicaSet보다 더 상위 개념의 오브젝트로, Pod의 replica 뿐만 아니라 버전 또한 관리 애플리케이션을 배포할 때 일반적으로 사용되는 오브젝트


### Namespace
- Kubernetes의 resource들을 논리적으로 분리
- 하나의 클러스터를 여러 개의 팀이나 프로젝트에 걸쳐서 많은 사용자가 있는 환경에서 서로를 분리하기 위한 오브젝트
- Resource들의 이름이 적용되는 범위(scope)를 지정해주는 역할
  - ex) 파드 이름 "testpod"는 namespace1에도 존재할 수 있고, namespace2에도 존재할 수 있음.

```
$ kubectl create namespace <namespace 이름>       # namespace 설정.
$ kubectl apply -f namespace.yaml                # 

# namespace 내에 파드 검색 (-n : namespace 지정 옵션)
$ kubectl get pods -n <namespace 이름>            
$ kubectl get pods -A                           # namespace 상관 없이 모든 파드를 검색

# namespace.yaml
###########################
apiVersion: v1
kind: Namespace
metadata:
  name : <namespace 이름>
###########################
```

## Reference
- [Reference](학교 자료)
- [Reference](https://www.redhat.com/ko/topics/containers/kubernetes-architecture)
- [Reference](https://platform9.com/blog/kubernetes-enterprise-chapter-2-kubernetes-architecture-concepts/)
- [Reference](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)
- [Reference](https://blog.neuvector.com/article/advanced-kubernetes-networking)