## DB덤프파일 추출
> /usr/lib/postgresql/9.6/bin/pg_dump -h localhost -p 15432 -U danbi_user -d danbi_db -Fc > 20171107.dump
- Fc 옵션은 압축.
-Z1~9 옵션을 추가하여 압축률 증가시킬 수 있음.

> /usr/lib/postgresql/9.6/bin/pg_dumpall -h localhost -p 15432 -U danbi_user > 20171107.dump

## DB 덤프파일로 복원
> sudo -u postgres pg_restore -h localhost -p 15432  -j 8 -d danbi_db backup.dump
- j 옵션을 사용하면 복원작업을 쓰레드로 돌릴 수 있음. 고려해야할 것은 하드웨어의 스펙이고 깊은 내용은 문서 및 하드웨어 지식이 필요함. 최적은 8로 추천한다고 함.
> 또는, sudo -u postgres psql -h localhost -p 15432 -f ~/바탕화면/20171107.dump 
> sudo -u postgres pg_restore -Fc ~/바탕화면/20171107.dump -h localhost -p 15432

## local postgresql 에서 작업 DROP DB & CREATE DB
#### drop db 
> sudo -u postgres psql -h localhost -p 15432
DROP DATABASE danbi_db;
DROP DATABASE test_danbi_db;
DROP DATABASE test_danbi_db_gw0;
DROP DATABASE test_danbi_db_gw1;
DROP DATABASE test_danbi_db_gw2;
DROP DATABASE test_danbi_db_gw3;
DROP USER danbi_user;

#### create db
> CREATE USER danbi_user WITH PASSWORD 'Eksql12#$';
ALTER ROLE danbi_user SET client_encoding TO 'utf8';
ALTER ROLE danbi_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE danbi_user SET TIMEZONE TO 'Asia/Seoul';
ALTER ROLE danbi_user WITH SUPERUSER;
CREATE DATABASE danbi_db;
GRANT ALL PRIVILEGES ON DATABASE danbi_db TO danbi_user;

#### 스크립트로 실행
<code>
#!/usr/bin/env bash
sudo -u postgres psql -h 127.0.0.1 -p 15432 -a -f myscript/drop_db.sql
sudo -u postgres psql -h 127.0.0.1 -p 15432 -a -f myscript/create_db.sql
sudo -u postgres pg_restore -h localhost -p 15432  -j 8 -d danbi_db backup.dump
</code>


- scp로 파일 옮기기
> sudo scp -i danbi-key.pem ubuntud~~~.com:/home/ubuntu/docs.../1107.dump

- 도커 cp
docker cp e9b43642246e:/tmp/20171107.dump .

- 용량확인
df -h 

- db 예상 사이즈??
SELECT pg_size_pretty(pg_database_size('danbi_db'));