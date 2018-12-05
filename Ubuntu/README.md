- 패키지 매니저
```sh
# 불필요 패키지 제거
sudo apt autoremove

# 패키지가 설치된 경로 찾기
dpkg -L gradle
```
- 환경변수

```sh
# 시스템 단계에서 설정하는 파일
# 모든 유저에게 적용됨
cat /etc/environment

# 각 사용자 마다 개별적으로 가지고있는 스크립트 파일
cat ~/.profile

# 전역 스크립트
# 이게 먼저 실행되고 개별 ~/.profile 이 실행됨
cat /etc/profile
ls /etc/profile.d/

# 현재 터미널에서만 적용하는 방법
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/

# 현재 터미널 환경변수 해제
unset 환경변수명

# 정의된 모든 환경변수 확인
export
env
env | grep JAVA_HOME


# 특정 환경변수 값 확인
echo $환경변수명

# ex) 자바 환경변수를 만들어야 되면
sudo vi /etc/profile.d/java.sh
# 스크립트 파일을 하나 만들고 아래의 내용 추가
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
```

- git tracking list에서 파일 제거하기
```
# tracking list 보기
git ls-files

# tracking list 에서 제거하기 
git rm --cached <file>
```
