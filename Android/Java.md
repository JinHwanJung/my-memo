# JAVA 환경변수 지정

```sh
sudo vi /etc/environment
```

# JAVA 설치

```
# JRE 만 설치
sudo apt-get install default-jre
# JDK 설치
sudo apt-get install default-jdk
```

## Open JAVA

```
sudo apt-get install openjdk-8-jdk
sudo apt-get install openjdk-8-jre
```

# JAVA 관리

- 오라클 공식 사이트에서 tar.gz 형태의 파일을 내려 받은 뒤 직접 설치하는 방법

```
1. /usr/lib/jvm 아래에 압축해제된 jdk 폴더를 이동

$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-10.0.1/bin/java 1
$ sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-10.0.1/bin/javac 1
$ sudo update-alternatives --install /usr/bin/javaws javaws /usr/lib/jvm/jdk-10.0.1/bin/javaws 1

2. 사용하는 것으로 선택

$ sudo update-alternatives --config java
$ sudo update-alternatives --config javac
$ sudo update-alternatives --config javaws
```