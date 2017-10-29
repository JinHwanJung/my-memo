- 데이터베이스 url로 연결 형식
<code>
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://유저명:패스워드@a@호스트:포트/데이터베이스명'),
}
</code>

