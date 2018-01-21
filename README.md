# MyReference

- Python Ref
    - [파이썬 개발환경 세팅](#python-environment)
    - [파이썬 개발환경 공유](#python-development-dependency-management)
- Django Ref
    - [CookieCutter-Django](#cookie-cutter-django)
- DB Ref
    - [Postgresql Install](#postgresql-install)
    - [Postgresql DB Dump](#postgresql-db-dump)
- Tutorial Ref
    - [Tutorial HTML&CSS](#tutorial-html-and-css)


# Python Environment 
## 파이썬 개발환경 세팅
"Simple Python Version Management"<br/>
로컬에 다양한 파이썬 버전을 설치하고 사용. 파이썬 버전에 대한 의존성 해결.

* pyenv 설치(ubuntu)<br/>

1. 의존성 패키지 설치
```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
```

2. pyenv installer로 설치

```bash
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

3. ".bashrc" 에 하기 내용 추가
```bash
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

* pyenv 사용
```bash
# 파이썬 3.6.2 버전을 pyenv 로 설치
pyenv update
pyenv install 3.6.2

# 지금 사용하고 있는 파이썬 버전확인
pyenv versions

# pyenv 로 설치된 개발환경 리스트 출력
pyenv install --list

# 버전 선택하여 사용
pyenv shell 3.6.2

# 전역 파이썬 버전 설정
pyenv global 3.6.2

# 설치한 버전 삭제
rm -rf ~/.env/versions/{삭제하고싶은 버전}

# virtualenv
로컬에 다양한 파이썬 환경울 구축. pip install 을 통해서 설치하는 패키지들에 대한 의존성을 해결.

# 가상환경 생성
pyenv virtualenv {파이썬 버전} {가상환경 이름}
(example)
  pyenv install 3.6.2
  pyenv virtualenv 3.6.2 django_server

# virtualenv 설치 이후,
# 프로젝트 폴더 엑세스 하면 바로 가상환경에 접속하도록 세팅 방법
cd {프로젝트 폴더}
pyenv local {가상환경 이름} .
(example)
  cd ~/work/dev
  pyenv local django_server .

# 가상환경 접속 및 빠져나오기
pyenv activate {가상환경 이름}  #가상환경 접속.
pyenv deactivate  #가상환경 빠져나오기.
```

# Python Development Dependency Management
## 파이썬 개발환경 공유

* pip<br/>
pip: 파이썬의 패키지 관리 도구<br/>
pip는 Python 2.7.9 또는 Python 3.4 이상 버전을 설치하게 되면 설치되어 있다.
```

* 패키지 의존 리스트 공유

```bash
# 패키지 리스트 내보내기
pip freeze > requirements.txt
# 패키지 리스트 불러오고 설치하기
pip install -r requiremenets.txt
```

* 패키지 환경분리<br/>
local, test, development, production 환경을 분리하여 관리하는 방법
```bash
1. 프로젝트에서 requirements-dev.txt에 "-r requirements.txt"를 추가.
2. development 환경으로 설치: pip install -r requirements-dev.txt
3. production 환경으로 설치: pip install -r requirements.txt 으로 쉘 명령 하나로 환경 설정
```

# Postgresql Install
* 9.6 설치
```bash
# 1.
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
# 2.
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
# 3.
sudo apt-get update
# 4.
sudo apt-get install postgresql-9.6
```

## Cookie Cutter Django
* Cookie Cutter 설치

```
- pyenv virtualenv 3.6.2 global
- pyenv shell global
- pip install 'django<2.0'
- pip install cookiecutter
```
* 쿠키커터 장고로 프로젝트 만들기
```bash
cookiecutter https://github.com/pydanny/cookiecutter-django
```

# Postgresql DB Dump

* pg_dump<br/>
실행중인 트래픽에 영향을 주지 않고 실시간으로 데이터베이스 백업을 얻을 수 있는 도구

    * 문제점
    ```
    1. 테이블 공간, 그룹 또는 사용자를 포함하지 않는다.
    2. 클러스터 / 인스턴스 내 데이터베이스 중 하나만 덤프한다.
    ```
    * 해결책
    ```
    1. pg_dumpall -g 
    : 테이블공간, 그룹, 유저 등 전역오브젝트 덤프
    (users, groups, tablespaces)
    

    2. pg_dumpall
    : 기본적으로 클러스터의 모든 객체를 덤프하여 모든 데이터를 일반 텍스트 모드로 덤프한다.

    3. pg_dump & pg_dumpall 도구 사용 전략
    3-1. 글로벌 오브젝트를 따로 저장 
    >> pg_dumpall -g> globals.sql 
    3-2. 원하는 데이터베이스를 따로 빼낸다. 
    >> pg_dump -d billing -F c -C > billingdb.bak 
    3-3. 복원 시, 원장 테이블이 있을 경우 와 없을 경우를 나눠 복원수행.
    3-4. 여러 클러스터가 있고 이 클러스터에는 여러 DB가 있는 경우, pg_dump는 한 번에 하나의 데이터베이스 에서만 작동한다. 때문에 스크립트를 작성.
    ``` 
```
<예시>
printf "Start: date" >> $backupDir/$dt/backup.log
pg_dumpall -g > /$backupDir/$dt/globals.sql
dbs=psql -t -c "select array_to_string(ARRAY(select datname from pg_database),' ')" | sed -e '/^$/d' | sed -e 's/^[ \t]//g'
for db in $dbs
do
printf "Performing backup of: $db\n"
pg_dump -v -Fp -b -C $db > /$backupDir/$dt/$db.sql 2>> /$backupDir/$dt/backup.log
done
printf "Complete: date" >> $backupDir/$dt/backup.log
```
[출처:"Don't forget the globals - pg_dump"](https://www.openscg.com/2016/10/dont-forget-the-globals/ "dont-forget-the-globals")

* DB의 덤프파일 추출

```
sudo -u postgres pg_dump -h [호스트] -p [포트] -U [DB유저명] -d [DB명] -Fc > [덤프(백업) 파일명]
```
<예시>
```
/usr/lib/postgresql/9.6/bin/pg_dump -h localhost -p 15432 -U danbi_user -d danbi_db -Fc > 20171107.dump
```
-Fc : 압축수행을 지정하는 옵션.<br/>
-Z9 : 압축 레벨을 9레벨로 지정하는 옵션. 레벨은 Z1~9 가 있으며, 숫자가 높을수록 압축률 증가

* 덤프파일로 DB 복원
```
sudo -u postgres pg_restore -h [호스트] -p [포트]  -j [작업 쓰레드 수] -d [DB명] [덤프된 파일]
```
<예시>
```
sudo -u postgres pg_restore -h localhost -p 15432  -j 8 -d danbi_db backup.dump
```
-j: 복원작업을 쓰레드로 돌릴 수 있다. <br/>
(고려해야할 것은 하드웨어의 스펙이고 깊은 내용은 문서 및 하드웨어 지식이 필요. 최적은 8로 추천으로 알려짐)

- 아래 코드는 압축이 안되어 있는 덤프파일 복원방법 
```
sudo -u postgres psql -h localhost -p 15432 -f ~/바탕화면/20171107.dump
```
* 데이터베이스 삭제 & 유저삭제
```
DROP DATABASE db;
DROP USER user;
```
* 데이터베이스 생성 & 유저생성 & 권한설정
```
CREATE USER user WITH PASSWORD 'password';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET TIMEZONE TO 'Asia/Seoul';
ALTER ROLE user WITH SUPERUSER;
CREATE DATABASE db;
GRANT ALL PRIVILEGES ON DATABASE db TO user;
```

- 스크립트로 실행
```
#!/usr/bin/env bash
# 테이블 지우고,
sudo -u postgres psql -h 127.0.0.1 -p 5432 -a -f drop_db.sql

# 테이블스페이스 및 유저 생성
sudo -u postgres psql -h 127.0.0.1 -p 5432 -a -f create_db.sql

# 백업된 데이터 밀어넣기
sudo -u postgres pg_restore -h localhost -p 5432  -j 8 -d db backup.dump 
```
* scp 를 이용하여 서버로부터 파일 가져오기
```
sudo scp -i [aws 접속 키 파일(.pem)] [aws 접속 호스트]:[로컬로 가져올 경로 + 파일이름]
```

* 도커 안의 파일 빼오기 (docker cp)

```
docker cp [container id]:[가져올 파일의 경로 + 파일] [가져와서 저장 될 로컬 경로]
```
* db 예상 사이즈 구하기
```
SELECT pg_size_pretty(pg_database_size('db'));
```
# Tutorial Html and Css
1. 기초부터 쌓자! HTML5, CSS3 정독
    * [기초튜토리얼 블로그 - poiemaweb](http://poiemaweb.com/)
2. 핵심 요소들의 개념과 원리를 빔캠프로 한번 더 쌓기
    * [빔캠프 Youtube](https://www.youtube.com/channel/UCvx57s_ZBt5VG4fvlStiq2g/playlists)
3. 실전에 한발짝
    * [웹페이지실전 - Seoul Wiz](https://www.youtube.com/watch?v=FnZhPxxJtkU&index=14&list=PLieE0qnqO2kRmnv2us27qoCUl2wXJ9-Q0)

4. 이제부터 더 탄탄하게! 기초 + 표준 + 실전<br/>

    3.1 [웹표준 사이트 만들기 - Webstoryboy Webs](https://www.youtube.com/watch?v=i27cyOHfJCw&list=PL4UVBBIc6giKkfYN_2TVPgbMpd87lJEfg)<br/>
    3.2 [하나카드 기업사이트 따라만들기 - Webstoryboy Webs](https://www.youtube.com/watch?v=EYBV2EnQkyQ&list=PL4UVBBIc6giKyLYPtaIUSgKoWa2PeEwLn)<br/>
    3.3 [반응형 사이트 만들기 - Webstoryboy Webs](https://www.youtube.com/watch?v=Br95hhB8xgE&list=PL4UVBBIc6giLZFjhh-UXovCCVlP57YnzA)
  

5. 영감을 주는 웹페이지를 둘러보면서 스스로 프로젝트 하기<br/>
[영감을 웹페이지 저장소]
    * [KoreaWebDesign](http://koreawebdesign.com/site/)
    * [Responsive Web Design - RWDB](http://rwdb.kr/)

6. 디자이너와 협업하기 위해 디자인도 좀 배우기<br/>
[웹디자인 포토샾 Youtube](https://www.youtube.com/channel/UCxRnfrmJAkRLarzeBJETB5g/playlists)