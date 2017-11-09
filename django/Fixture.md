
# django에서 fixture를 이용하여 DB의 테이블을 백업 및 로드
1. Model작성
2. Model 덤프 혹은 입력을 통해서 json 형태로 저장
3. 명령어를 통해 DB에 입력.

+ 현재 db에 있는 data들을 json 형식으로 dump하는 방법
```
python manage.py dumpdata [app_name].[model.name] --indent [INDENT] > [fixture_name].json
```
+ 명령어를 통해 db를 입력하기
```
python manage.py loaddata [app_name]/fixtures/[fixture_name].json
```
+ 기본적으로 dumpdata는 JSON 출력 형식.

## dumpdata
---
### 전체 데이터베이스를 덤프
```
./manage.py dumpdata > db.json
```

### 특정 앱에 대한 덤프 데이터([app_name].[model.name])
```
./manage.py dumpdata admin > admin.json
```
### 특정 테이블 덤프 데이터
```
./manage.py dumpdata account.Actor > Actor.json
./manage.py dumpdata auth.user > user.json  # django 테이블의 내용 덤프
```
### 앱 또는 테이블 제외하고 덤프(--exclude)
```
./manage.py dumpdata --exclude auth.permission > db.json  # auth.permission 제외하고 전체 데이터베이스 복사
```
### 읽기 쉽도록 indent 생성하여 덤프(--indent)
```
./manage.py dumpdata auth.user --indent 2 > user.json
```
### 출력 형식 지정하여 덤프(--format)
```
./manage.py dumpdata auth.user --indent 2 --format xml > user.xml  # format을 xml로 지정함.
지정할 수 있는 format : json, xml, yaml
```

## loaddata
---
### 데이터베이스에 로드하기
```
./manage.py loaddata user.json
```

## 새 데이터베이스 복원
- dumpdata명령을 사용하여 전체 데이터베이스 백업을 하면 데이터베이스의 테이블이 백업된다.
- 이 데이터를 다른 장고 프로젝트에 로드하면 IntegrityError를발생한다.(동일한 데이터베이스가 아니므로)
- 이 문제를 해결 하려면 contenttypes와 auth.permissions를 제외하고 데이터베이스를 백업해야 한다.
```
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```
- 이후 데이터베이스로 로드하여 사용할 수 있다.
```
./manage.py loaddata db.json
```

[출처](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)