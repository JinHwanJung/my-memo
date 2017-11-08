
# POSTGRES DB DUMP


+ pg_dump 
: 실행중인 트래픽에 영향을 주지 않고 실시간으로 데이터베이스 백업을 얻을 수 있는 도구.
 + 문제점
  + 1. 테이블 공간, 그룹 또는 사용자를 포함하지 않는다.
  + 2. 클러스터 / 인스턴스 내 데이터베이스 중 하나만 덤프한다.  
 + 해결
  + 1. 테이블공간, 그룹, 유저에 대한 해결책 : pg_dump -g # dump only global objects (users, groups, tablespaces)

+ pg_dumpall
 + : 기본적으로 클러스터의 모든 객체를 덤프하여 모든 데이터를 일반 텍스트 모드로 덤프한다.
  + pg_dump -g : **전역 오브젝트**만 덤프한다.

+ pg_dump & pg_dumpall 도구 사용 전략
 + 1. pg_dumpall -g> globals.sql # 글로벌 오브젝트를 따로 저장하고,
 + 2. pg_dump -d billing -F c -C> billingdb.bak # 원하는 데이터베이스를 따로 빼낸다.
 + 3. 복원 시, 원장 테이블이 있을 경우 또는 없을 경우를 나눠 복원수행.
 + 4. 여러 클러스터가 있고 이 클러스터에는 여러 DB가 있는 경우. 
  + : pg_dump는 한 번에 하나의 데이터베이스 에서만 작동한다. 때문에 스크립트를 작성함.
   + ```
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
[출처](https://www.openscg.com/2016/10/dont-forget-the-globals/ "dont-forget-the-globals")

1. DB의 덤프파일 추출
**sudo -u postgres pg_dump -h [호스트] -p [포트] -U [DB유저명] -d [DB명] -Fc > [덤프(백업) 파일명]**
```
/usr/lib/postgresql/9.6/bin/pg_dump -h localhost -p 15432 -U danbi_user -d danbi_db -Fc > 20171107.dump
```
- Fc : 압축수행을 지정하는 옵션.
- -Z9 : 압축 레벨을 9레벨로 지정하는 옵션. 레벨은 Z1~9 가 있으며, 숫자가 높을수록 압축률 증가

2. DB 덤프파일로 복원
**sudo -u postgres pg_restore -h [호스트] -p [포트]  -j [작업 쓰레드 수] -d [DB명] [덤프된 파일]**
```
sudo -u postgres pg_restore -h localhost -p 15432  -j 8 -d danbi_db backup.dump
```
- j 옵션을 사용하면 복원작업을 쓰레드로 돌릴 수 있다. (고려해야할 것은 하드웨어의 스펙이고 깊은 내용은 문서 및 하드웨어 지식이 필요함. **최적은 8로 추천한다고 함. 출처링크참조***.)

- 아래 코드는 압축이 안되어 있는 덤프파일 복원방법 
```
sudo -u postgres psql -h localhost -p 15432 -f ~/바탕화면/20171107.dump
```

3. local postgresql 에서 작업 DROP DB & CREATE DB
 + drop db 
 + ```
 sudo -u postgres psql -h localhost -p 15432
 DROP DATABASE danbi_db;
 DROP DATABASE test_danbi_db;
 DROP DATABASE test_danbi_db_gw0;
 DROP DATABASE test_danbi_db_gw1;
 DROP DATABASE test_danbi_db_gw2;
 DROP DATABASE test_danbi_db_gw3;
 DROP USER danbi_user;
 ```

 + create db
 + ```
 CREATE USER danbi_user WITH PASSWORD 'abcdefg';
 ALTER ROLE danbi_user SET client_encoding TO 'utf8';
 ALTER ROLE danbi_user SET default_transaction_isolation TO 'read committed';
 ALTER ROLE danbi_user SET TIMEZONE TO 'Asia/Seoul';
 ALTER ROLE danbi_user WITH SUPERUSER;
 CREATE DATABASE danbi_db;
 GRANT ALL PRIVILEGES ON DATABASE danbi_db TO danbi_user;
 ```

4. 스크립트로 실행
```
#!/usr/bin/env bash
sudo -u postgres psql -h 127.0.0.1 -p 15432 -a -f myscript/drop_db.sql # 테이블 지우고,
sudo -u postgres psql -h 127.0.0.1 -p 15432 -a -f myscript/create_db.sql # 테이블스페이스 및 유저 생성하고,
sudo -u postgres pg_restore -h localhost -p 15432  -j 8 -d danbi_db backup.dump # 백업된 데이터 밀어넣기
```

5. aws 서버에서 scp을 이용하여 외부로 파일 가져오기(dump파일을 빼내오기)
**sudo scp -i [aws 접속 키 파일(.pem)] [aws 접속 호스트]:[로컬로 가져올 경로 + 파일이름]**
```
sudo scp -i danbi-key.pem ubuntud~~~.com:/home/ubuntu/docs.../1107.dump
```

6. 도커 안의 파일 빼오기(docker cp)
**docker cp [container id]:[가져올 파일의 경로 + 파일] [가져와서 저장 될 로컬 경로]**
```
docker cp e9b43642246e:/tmp/20171107.dump .
```

7. 리눅스 용량확인
df -h 

8. db 예상 사이즈??
```
SELECT pg_size_pretty(pg_database_size('danbi_db'));
```
