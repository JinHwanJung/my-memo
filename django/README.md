- 아래와 같은 코드 동작 살펴보기
```python
Articles.objects.get(id=1).values(’title’, ’author’, ‘body', alias={"title": "my_custom_title"}, nested=True)
```