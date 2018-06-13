# 기본
- 유닉스 계열 컴퓨터 시스템에서 소프트웨어를 관리하는 프로세스를 단순화 목적
- APT (Advanced Package Tool)는 Debian, Ubuntu 및 기타 Linux 배포판에서 소프트웨어의 설치 및 제거를 처리하기 위해 코어 라이브러리와 함께 작동하는 자유 소프트웨어 사용자 인터페이스
- 사전에 컴파일 된 파일에 대한 소프트웨어 패키지를 검색, 구성 및 설치

## 사용법
### 패키지 검색 업데이트
> apt-get은 인덱스를 가지고 있는데 이 인덱스는 /etc/apt/sources.list 에 있다. 이곳에 저장된 저장소에서 사용할 패키지의 정보를 얻는다.  

- sudo apt-get update

#### 패키지 업그레이드
> 설치되어 있는 패키지를 모두 새버전으로 업그레이드 한다.

- 기본: sudo apt-get upgrade
- 의존성 검사하며 업그레이드하기: sudo apt-get dist-upgrade

#### 패키지 설치
- sudo apt-get install <패키지명>

패키지 재설치

- apt-get --reinstall install <패키지명>

#### 패키지 삭제
- 기본: sudo apt-get remove <패키지명>
- sudo apt-get purge --auto-remove qgit
    - 옵션설명
    - purge: 구성 또는 데이터 파일도 삭제
    - --auto-remove: 우분투관련 종속성 모두제거 

#### 패키지 정보 보기
- sudo apt-cache show <패키지명>

- - - 

# 자주 사용하는 패키지 정리

## qgit
> git 로그 시각화 프로그램
- sudo apt-get install qgit
