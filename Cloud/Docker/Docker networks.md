# Docker netowork

- 컨테이너는 외부와의 통신을 위해 2개의 network interface를 함께 생성한다.
  - eth0 : 컨테이너 내부 namespace에 해당되는 인터페이스
  - veth interface : vethxxxxxxx 이름 형식을 따르며, network bridge docker0에 바인딩됨
- docker0 brige 는 veth 가상 interface와 host의 eth0를 이어주는 역할
- 컨테이너 내부의 eth0 interface는 veth 가상 인터페이스를 통해 외부와 통신

![Docker network](https://user-images.githubusercontent.com/105041834/209779314-390369a4-2fa2-460f-a6cc-70ba8b06ffb4.jpg)

## Bridge network
A bridge network is a Link Layer device(Wi-Fi, Ethernet) which forwards traffic between network segments.

In terms of Docker, a bridge network uses a software bridge which allows containers connected to the same bridge network to communicate
While providing isolation from containers which are not connected to that bridge network.

> Docker의 입장에서는 같은 bridge network로 연결을 하여 통신이 가능하게 하고 연결되지 않은 container으로부터 isolation

The Docker bridge driver automatically installs rules in the host machine so that containers on different bridge networks cannot communicate directly with each other.

> Docker bridge는 host machine에 rule을 설치함으로 써 다른 bridge에서 서로 통신 불가능하게 한다.

Bridge networks apply to containers running on the **same** Docker daemon host.
For communication among containers running on different Docker daemon hosts, 
you can either manage routing at the OS level, or you can use an overlay network.

## Docker ports
> Docker는 host service의 어떤 port를 통해서 사용이 되는지 알려줌.

### Options (expose and publish)
Containers connected to the same user-defined bridge network effectively expose all ports to each other.
For a port to be accessible to containers or non-Docker hosts on different networks,
that port must be published using the -p or --publish flag

> 같은 bridge에 연결된 container들은 expose 사용 시 서로 communication이 가능하다.
> network bridge에 연결되지 않은 곳과 연결을 하기 위해서는 publish를 해야 한다.

- Neither specify **EXPOSE** nor -p
  - The service in the container will only be accessible from inside the container itself
> EXPOSE 나 -p를 사용하지 않을 경우에는 container에 있는 service는 container 내부에서만 접근이 가능하다.
- Only specify **EXPOSE**
  - If you **EXPOSE** a port, the service in the container is not accessible from outside Docker
  - But from inside other Docker containers could access (good for inter-container communication)
> EXPOSE만 하게 될 경우 Docker의 밖에서는 access가 불가능하지만 다른 Docker container들은 access가 가능하다. (Network bridge에 연결된 container끼리의 통신)
- **EXPOSE** and -p
  - Container is accessible from anywhere, even outside Docker
- -p but not **EXPOSE**
  - It is automatically also open to other Docker containers
> 어짜피 밖에도 공개되면 내부도 전부 다 공개된다.

### Publish example
- ![port example](https://user-images.githubusercontent.com/105041834/200626548-780889e0-6e4c-4017-8991-1d37e147db51.jpg)


### Features
- EXPOSE instruction does not expose the container's ports to be accessible from the host.
> Host의 경우에는 해당 port에 접근을 할 수가 없다. (inter-container communication)

## Reference
- [Reference](https://www.mend.io/free-developer-tools/blog/docker-expose-port/)
- [Reference](https://stackoverflow.com/questions/22111060/what-is-the-difference-between-expose-and-publish-in-docker)
- [Reference](https://docs.docker.com/network/bridge/)
- [Reference] 학교 ppt 자료