# Docker


## Docker architecture
![Docker architecture](https://user-images.githubusercontent.com/105041834/198867936-5055c749-77e0-4079-9f20-6719ddd9c7df.jpg)

Docker uses a client-server architecture.
The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.
The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon.
> Docker client와 daemon은 같은 시스템에서 실행 될 수도 있고 docker client를 원격의 docker daemon과 연결 할 수 있다.


The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.
> Docker client와 daemon은 REST API, UNIX socket, network interface를 통해서 대화할 수 있따.

Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

-[Reference](https://docs.docker.com/get-started/overview/)

### The Docker daemon
The Docker daemon **dockerd** listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes.
A deamon can also communicate with other daemons to manage Docker services.

### The Docker client
The docker client **docker** is the primary way that many Docker users interact with Docker.
When you use commands such as **docker run**, the client sends these commands to **dockerd**, which arries them out.
The **docker** command uses the Docker API.
The Docker client can communicate with more than one daemon.

### Docker registries
A Docker registry stores Docker images.
Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default.
You can even run your own private registry.
> Docker registry는 Docker image등을 저장하고 Docker(Client)는 image가 없을 시 Docker Hub에 가서 image를 찾는 것이 default로 설정 되어 있다.

When you use the **docker pull** or **docker run** commands, the required images are pulled from your configured registry.
When you use the **docker push** command, your image is pushed to your configured registry.

### Docker objects
When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects.

#### Images
An **image** is a read-only template with instructions for creating a Docker container.
> Image라는 것은 (read-only) Docker container를 생성하는 instruction들이다.

Often, an image is based on another image, with some additional customization.

To build your own image, you create a **Dockerfile** with a simple syntax for defining the steps needed to create the image and run it.
Each instruction in a Dockerfile creates a layer in the image.
When you change the Dockerfile and rebuild the image, only those layers which have changed are reqbuilt.
This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.

#### Containers
A container is a runnable instance of an image.
You can create, start, stop, move, or delete a container using the Docker API or CLI.
You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.

By default, a container is relatively well isolated from other containers and its host machine.
You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine

A container is defined by its image as well as any configuration options you provide to it when you create or start it.
When a container is removed, any changes to its state that are not stored in persistent storage disappear.
