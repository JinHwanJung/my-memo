---
marp: true
---
# 도커
  - 도커는 2013년 3월 Docker Inc 에서 출시
  - 오픈소스 컨테이너 프로젝트
  - AWS, GCP, AZURE 등 클라우드 서비스에서 공식지원
---
# 도커가 인기를 끌게된 이유
  - 복잡한 **리눅스 기반** 애플리케이션을 묶어서 관리
    - 개발, 테스트, 서비스 환경을 통일
  - 컨테이너(이미지)를 전 세계 사람들과 공유
    - Docker Hub : https://hub.docker.com/
---
# 도커의 핵심 기술
  - 리눅스 **커널**(리눅스 OS의 Core)에서 제공하는 **컨테이너** 기술을 이용
  - **컨테이너**는 **가상화**보다 훨씬 가벼운 기술!
---
# 컨테이너 vs 가상화
---

![](vm-vs-docker.png)

---
# 가상머신의 문제점
  - 가상 머신은 완전한 컴퓨터
    - **항상 Guest OS 를 설치 해야만 함**
  - 이미지 안에 OS가 포함되기 때문에 이미지 용량이 큼
    - **네트워크로 가상화 이미지를 주고 받는 건 부담**
  - 가상화 소프트웨어는 OS 가상화에 만 주력
    - **배포와 관리 기능 부족**
---
# 가상머신의 문제점을 보완하는 "리눅스 컨테이너"
  - 컨테이너 안에 **격리된 가상 공간**을 만들지만 애플리케이션(ex. 서버)을 **호스트에서 직접 실행**
  - 이건 리눅스 커널의 **cgroups** 와 **namespaces**가 제공하는 기술
  - 즉 가상화가 아닌 **격리** 
---

![](libcontainer.png)

---
# Docker(container)의 작동 원리
- https://tech.ssut.me/what-even-is-a-container/
---
# 정리하자면, 도커는 Guest OS 를 설치하지 않음
### 도커는 하드웨어 가상화 계층이 없음
따라서,
  - 이미지에 서버 운영을 위한 프로그램과 라이브러리만 격리해서 설치
  - 이미지 용량이 크게 줄어듦
  - 호스트와 OS 자원(시스템콜)을 공유
---
# 도커에 대한 설명은 이쯤하고 도커를 사용 해 봅시다!
  - 도커 이미지 만들고 배포하기
    - https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html
  - 도커를 사용해 장고 서버를 배포
    - Dockerfile 작성 > 빌드(이미지) > 실행(컨테이너)
    - 자동화를 위한 스크립트 작성 
---
# 추천 레퍼런스
1. 공식문서 : https://docs.docker.com/ 
2. 가장 빨리 만나는 Docker 위키 : http://pyrasis.com/docker.html
3. [토크ON세미나] 컨테이너 오케스트레이션 : https://www.youtube.com/watch?v=WxzWXqTNdlw
