--- Database 생성
CREATE DATABASE django_study_db;

--- User 생성
CREATE USER django_study_user WITH PASSWORD 'db_password';

--- User 설정
ALTER ROLE django_study_user SET client_encoding TO 'utf8';
ALTER ROLE django_study_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_study_user WITH SUPERUSER;

--- DB 에 대한 권한을 User 에게 부여하기
GRANT ALL PRIVILEGES ON DATABASE django_study_db TO django_study_user;
