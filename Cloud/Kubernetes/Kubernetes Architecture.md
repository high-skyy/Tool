# Kubernetes Architecture

## Namespace
- Kubernetes의 resource들을 논리적으로 분리
- 하나의 클러스터를 여러 개의 팀이나 프로젝트에 걸쳐서 많은 사용자가 있는 환경에서 서로를 분리하기 위한 오브젝트
- Resource들의 이름이 적용되는 범위(scope)를 지정해주는 역할

```
$ kubectl create namespace <namespace 이름>
$ kubectl apply -f namespace.yaml

# namespace.yaml
###########################
apiVersion: v1
kind: Namespace
metadata:
  name : <namespace 이름>
###########################
```