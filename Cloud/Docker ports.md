# Docker ports
> Docker는 host service의 어떤 port를 통해서 사용이 되는지 알려줌.

## Options (expose and publish)
- Neither specify **EXPOSE** nor -p
  - The service in the container will only be accessible from inside the container itself
> EXPOSE 나 -p를 사용하지 않을 경우에는 container에 있는 service는 container 내부에서만 접근이 가능하다.
- Only specify **EXPOSE**
  - If you **EXPOSE** a port, the service in the container is not accessible from outside Docker
  - But from inside other Docker containers could access (good for inter-container communication)
> EXPOSE만 하게 될 경우 Docker의 밖에서는 access가 불가능하지만 다른 Docker container들은 access가 가능하다.
- **EXPOSE** and -p
  - Container is accessible from anywhere, even outside Docker
- -p but not **EXPOSE**
  - It is automatically also open to other Docker containers
> 어짜피 밖에도 공개되면 내부도 전부 다 공개된다.

## Publish example
- ![port example](https://user-images.githubusercontent.com/105041834/200626548-780889e0-6e4c-4017-8991-1d37e147db51.jpg)


## Features
- EXPOSE instruction does not expose the container's ports to be accessible from the host.
> Host의 경우에는 해당 port에 접근을 할 수가 없다. (inter-container communication)

## Reference
- [Reference](https://www.mend.io/free-developer-tools/blog/docker-expose-port/)
- [Reference](https://stackoverflow.com/questions/22111060/what-is-the-difference-between-expose-and-publish-in-docker)