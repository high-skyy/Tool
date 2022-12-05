# Docker commands

## 자주 쓰는 명령어
```

```

## Docker Run
The **Docker run** command first creates a writeable container layer over the specified image, and then **starts** it using the specified command.
That is, **docker run** is equivalent to the API /containers/create then /containers/(id)/start.
A stopped container can be restarted with all its previous changes using **docker start**.
See **docker ps -a** to view a alist of all containers.

The **docker run** command can be used in combination with **docker commit** to change the command that a container runs.


- [Reference](https://docs.docker.com/engine/reference/commandline/run/)

## Docker Build
The **docker build** commands build Docker images from a Dockerfile and a "context".
A build's context is a set of files located in the specified **PATH** or **URL**.
The build process can refer to any of the files in context.

The **URL** parameter can refere to three kinds of resources: Git repositories, pre-packaged tarball contexts and plain text files.

```
$ docker build [OPTIONS] PATH | URL | -
```


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