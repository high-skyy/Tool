# Container 사용

## 기본적인 것
```
$ sudo apt update
```

## GPG key 및 저장소 추가
```
$ sudo mkdir –p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
$ echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

- GPG key
GPG is the Gnu Privacy Guard and it is an implementation of OpenPGP (Open Pretty Good Privacy).

OpenPGP is a hybrid of the two-key cryptography approach where the message to be exchanged is first compressed and then a session key is created as a one-time use secret key.
The session key is then encrypted with the destination's public key and bundled with the encrypted message.
The destination can decrpy the session key with their private key then decompress it to recover the original plaintext.

## Docker engine 설치
- Docker engine is the underlying client-server technology that builds and runs containers using Docker's components and services.
  - Docker daemon, a REST API and the CLI that talks to the Docker daemon through the API
  - Docker Engine supports the tasks and workflows involved to build, ship and run container-based applications
  - **The engine creates a server-side daemon process that hosts images, containers, networks and storage volumes**.
  - Engine also provides a client-side Command-line interface (CLI) that enables users to interact with the daemon through the Docker Engine API.
> Host OS 위에 올려서 Container화가 가능하게 해준다.

- [Reference](https://www.techtarget.com/searchitoperations/definition/Docker-Engine)
```
$ sudo apt install docker-ce docker-ce-cli containerd.io
$ sudo docker version           # 도커 버전 확인
```

## Container 실행
```
$ sudo docker run --rm hello-world
$ sudo docker run -d -pp 81:80 nginx
```
### run 명령어
![Docker run](https://user-images.githubusercontent.com/105041834/198867394-65b2ff96-9f29-4ea1-96ed-daee8935e760.jpg)

- docker run = (이미지가 없을 때) docker pull + docker create, docker start + docker attach