
# Links

https://www.postgresql.org/docs/10/static/index.html

https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

# postgresql10 설치

1. 저장소 추가
```bash
$ sudo vi /etc/apt/sources.list.d/pgdg.list
```

2. pgdg.list 에 아래내용 쓰기
```vi
deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main
```

3. 저장소 키 추가 & 업데이트
```
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
```

4. 설치
```
apt-get install postgresql-10
```

# psql 명령어

- db 프로그램 접속
> sudo -u postgres psql -U <유저명>

- 모든 데이터베이스 목록 나열후 종료
> sudo -u postgres psql -l

- 데이터베이스 목록 조회
> \l 또는 \list

- 데이터베이스 목록 상세조회
> \list+ 또는 \l+

- 데이터베이스 삭제
> DROP DATABASE 데이터베이스명;

- 데이터베이스 생성
> CREATE DATABASE 데이터베이스명;

- 데이터베이스 연결
> \c 데이터베이스명

- 테이블 정의보기
> \d 테이블명

- 모든 테이블의 스키마 나열
> \dt *.* (*.* 생량된 경우 SEARCH_PATH 만 표시)

- 스키마 목록
> \dn

- 함수 목록
> \df

- 목록보기
> \dv

- 색인 목록
> \di

- pretty 쿼리결과로 보기
> \x

- csv로 테이블 빼기
> \copy (select * from account_actor;) to '/home/jinhwan/file.csv' with 
csv;

- 사용자 나열:
> \du

- 데이터베이스 소유주 변경
> alter database DB owner to USER;

- 유저 생성 & DB 생성 후 유저에 권한주기
> CREATE USER DB WITH PASSWORD 'password';

> ALTER ROLE USER SET client_encoding TO 'utf8';

> ALTER ROLE USER SET default_transaction_isolation TO 'read committed';

> ALTER ROLE USER SET TIMEZONE TO 'UTC';

> ALTER ROLE USER WITH SUPERUSER;

> CREATE DATABASE DB;

> GRANT ALL PRIVILEGES ON DATABASE DB TO USER;

- postgresql 서비스 관리 명령어
```
sudo service postgresql stop
sudo service postgresql start
sudo service postgresql restart
```

- postgresql 쿼리 연습 사이트

https://pgexercises.com