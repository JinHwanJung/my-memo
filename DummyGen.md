# 더미데이터 생성 스크립트 실행 방법

1. 로컬 단비서버 접속(서버 도커이미지)
```bash
./myscript/connect_danbi_server.sh
```

2. 파이썬 콘솔 실행
```bash
python manage.py shell
```
3. 스크립트 복사
4. 파이썬 콘솔에 붙여넣기(<code>Ctrl</code>+<code>Shift</code>+<code>v</code>)
5. 콘솔 줄 바꿈
6. 함수 호출하여 더미 생성
```python
start(10) # 해당 스크립트 더미 10개 생성
```
```python
setUp() #선생님, 선생님팀, 책, 동글, 디바이스, 회수송장번호 등 로컬서버에 
```