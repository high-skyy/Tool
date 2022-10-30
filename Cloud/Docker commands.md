# Docker commands

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
