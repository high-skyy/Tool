# Temporary info

## root directory
On linux, every process has its own root directory.
For most processes, this is /.
However, **chroot** can change that.
This information is exposed via /proc.

## Namespaces
**Namespaces are a feature of the Linux kernel that partitions
kernel resources such that one set of processes sees one set of 
resources while another set of processes sees a different set of resources**

> DB에서 transaction의 isolation의 개념이랑 비슷 각 프로세스는 서로 다른 resource partition을 본다.

The key feature of namespaces is that they isolate processes from each other.
이렇게 되면 변화에 대한 영향력이 작다. Mostly though, isolating services meets the 
architectural style of microservices.

### Types of namespaces
Look at Reference link

## cgroups
A control group is a Linux kernel feature that limits, accounts for, and isolates 
the resource usage (CPU, memory, disk I/O, network) of a collection of processes.

## Reference
[Reference](https://www.nginx.com/blog/what-are-namespaces-cgroups-how-do-they-work/)