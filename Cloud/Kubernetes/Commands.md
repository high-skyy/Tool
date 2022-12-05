# Commands for Kubernetes

## Commands
```
############ Namespace
$ kubectl create namespace <namespace 이름>       # 추가 (via kubectl)
$ kubectl apply -f <namespace 파일이름>.yaml       # 추가 (via .yaml)
$ kubectl delete namespace <namespace 이름>       # 삭제
$ kubectl get namespace                          # 조회
 

############
$ kubectl apply -f filenmae.yaml    # 권장된 실행 방법
$ kubectl get pods                  # 파드 받기
```

## yaml file
- Deployment
```
apiVersion:apps/v1

```