# Bridge networks
A bridge network is a Link Layer device which forwards traffic between network segmetns.

In terms of Docker, a bridge network uses a software bridge which allows containers connected to the same bridge network to communicate
While providing isolation from containers which are not connected to that bridge network.

The Docker bridge driver automatically installs rules in the host machine so that containers on different bridge networks cannot communicate directly with each other.


## Reference
- [Reference](https://docs.docker.com/network/bridge/)