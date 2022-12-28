# Docker commands

## 자주 쓰는 명령어
```
$ docker inspect        # docker layer 확인
$ docker ps -a
$ docker build -t example:v1          # <name>:<name> 형식의 태그
$ docker run -it example:v1 /example.py    
```

## Docker Run
The **Docker run** command first creates a writeable container layer over the specified image, and then **starts** it using the specified command.
That is, **docker run** is equivalent to the API /containers/create then /containers/(id)/start.
A stopped container can be restarted with all its previous changes using **docker start**.
See **docker ps -a** to view a a list of all containers.

> Docker run의 경우 해당 image위에 쓰기 가능한 layer를 만들고 start 시킨다. (API /containers/create + /containers/(id)/start 와 동일하다.)

The **docker run** command can be used in combination with **docker commit** to change the command that a container runs.

- [Reference](https://docs.docker.com/engine/reference/commandline/run/)

![Docker run](https://user-images.githubusercontent.com/105041834/209769082-f31c424f-c943-45ae-a941-d0f750ce6895.jpg)

Dockerfile을 이용해 docker image를 build하고 이를 이용하여 container를 실행시킨다. 만약 해당 image가 존재하지 않을 경우 docker 
hub에서 가져다가 사용한다.

> docker run = (이미지가 없을 때) docker pull + docker create + docker start + docker attach

## Docker Build
The **docker build** commands build Docker images from a Dockerfile and a "context".
A build's context is a set of files located in the specified **PATH** or **URL**.
The build process can refer to any of the files in context.

The **URL** parameter can refere to three kinds of resources: Git repositories, pre-packaged tarball contexts and plain text files.

```
$ docker build [OPTIONS] PATH | URL | -
```
```
# example for ENTRYPOINT and CMD (docker file)
ENTRYPOINT ["<command>", "<parameter1>", "<parameter2>", ...]
CMD ["<command>", "<parameter1>", "<parameter2>", ...]

ENTRYPOINT ["python"]
CMD ["code1.py"]

$ docker run "<컨테이너 이미지 이름>"
$ docker run "<컨테이너 이미지 이름>" code2.py
```
```
# Dockerfile에 여러 개의 RUN 명령문 선언 가능 이미지 빌드 시 항상 실행됨
# 보통 이미지 내부에 특정 소프트웨어를 설치하기 위해 사용됨
RUN ["<command>", "<parameter1>", "<parameter2>", ...]
```
<details>
  <summary>Command details inside dockerfile (yaml)</summary>
  <ol>
    <li>FROM : base 이미지 설정</li>
    <li>WORKDIR : 작업 디렉터리 설정 </li>
    <li>RUN : 이미지 시 command 실행</li>
    <li>ENTRYPOINT : 이미지 실행 시 항상 실행되어야 하는 command 설정</li>
    <li>CMD : 이미지 실행 시 default command 또는 parameter 설정</li>
    <li>EXPOSE : 컨테이너가 listening 할 port 및 protocol 설정</li>
    <li>COPY/ADD : 이미지의 파일 시스템으로 파일 또는 디렉토리 복사</li>
    <li>ENV : 환경 변수 설정</li>
    <li>ARG : 빌드 시 넘겨받을 argument 설정</li>
  </ol>
</details>

- [Reference](https://docs.docker.com/engine/reference/commandline/build/)

## Docker exec
The **docker exec** command runs a new command in a running container.
The command started using **docker exec** only runs while the container's primary process (**PID 1**) is running, and it is not restarted if the container is restarted.

COMMAND will run in the default directory of the container.
If the underlying image has a custom directory specified with the WORKDIR directive in ints Dockerfile, this will be used instead.

COMMAND should be an executable, a chained or a quoted command will not work.

```
$ docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
ex)
$ docker exec -ti my_container sh-c "echo a && echo b"
```

- [Reference](https://docs.docker.com/engine/reference/commandline/exec/)

## Docker network
```
 docker network create [OPTIONS] NETWORK
```
Creates a new network. The **DRIVER** accepts **bridge** or **overlay** which are the built-in network drivers.
If you have installed a third party or your own custom network driver you can specify that **DRIVER** here also.
If you don't specify the **--driver** option, the command automatically creates a **bridge** network
corresponds to the **docker0** bridge that Engine has traditionally relied on.
When you launch a new container with **docker run** it automatically connects to this bridge network.
You cannot remove this default bridge network, but you can create new ones using the **network create** command.

```
docker network create -d bridge my-bridge-network.

ex)
$ docker run -itd --network=mynet busybox

$ docker network create --driver=bridge --subnet=192.168.0.0/16 br0
```

- [Reference](https://docs.docker.com/engine/reference/commandline/network_create/0)