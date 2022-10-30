# Cloud Computing

원격지의 컴퓨터 resource(CPU, Memory, Disk, Network)를 대여하여 사용하는것

## Features
- Pay-as-you-go(사용한 만큼 지불, 초기 설비 투자 비용이 없음으로 인해 경제적으로 좋다.)
- 확장성 및 탄력성 (필요한 만큼 resource를 증가/감소시킬 수 있음, 자동화 기능)
  - 새로운 resource의 allocation과 release가 편하다.(scalability, elasticity)
- 서비스 제공자(Cloud provider)가 책임지고 관리한다.

## 가상화 기술(Virtualization technique)
- VM(Virtual Machine)
![VM](https://user-images.githubusercontent.com/105041834/198866155-12da1982-95f4-4fe4-9c01-e19a486ab2fe.jpg)
- Container
![Container](https://user-images.githubusercontent.com/105041834/198866153-7af3c4a8-0996-4c04-bdcf-821d8962ae3b.jpg)

- 가상화 기술 (Virtual machine, Container)의 이점을 클라우드 컴퓨팅 서비스 구축에 활용
  - VM의 높은 격리 수준을 통한 사용자간 인스턴스 격리
  - Container는 경량의 가상화 기술이다.
    - VM과는 다르게 OS code가 새로 HOST OS 위에 있지 않기 때문에 편리하다.

## Xaas
- 서비스 제공자의 관리 범위에 따라 (Iaas, Paas, Saas)가 나뉜다.

- ![Xaas](https://user-images.githubusercontent.com/105041834/198866270-6fe97db0-a88b-4abd-bf99-a45f2397d768.jpg)

## SLA(Service Level Agreement)
- 제공하는 서비스에 대해 무엇을 보장하는지 명시 (위반시 보상)

## VPC(Virtual Private Cloud)
- VPC는 자체 데이터 센터에서 운영하는 기존 네트워크와 유사한 가상 네트워크
- VPC를 생성한 후 서브넷을 추가할 수 있음
- 서브넷은 VPC의 IP주소 범위

## Image
- A virtual machine image is a **single file that contains a virtual disk that contains a bootable operating system**
- [Reference](https://docs.rackspace.com/docs/user-guides/infrastructure/cloud-config/compute/cloud-images-product-concepts/)

## 설치를 위한 Configurations (Tencent Cloud 기준)
- Billing mode
- Region + Availability zone
- Instance Configuration (제공하는 model)
- Image (Ubuntu, Window ....)
- Storage
- Snapshot
  - Backup : 파일 전체를 복사.
  - Snapshot : Backup check-point를 설정하는 것과 동일하다.
- Network and bandwidth
- Security group (막아야하는 port 등등)
- Login methods (SSH or 그냥 passwd)

## Reference
- [Reference](학교 ppt)
- [Reference](https://docs.rackspace.com/docs/user-guides/infrastructure/cloud-config/compute/cloud-images-product-concepts/)
