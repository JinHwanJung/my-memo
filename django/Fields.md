# Model가 가진 모든 필드를 보는 방법.
```python
for f in Model._meta.fields:
    print(f.name)
```
# JSONField
# UUIDField
# SearchVectorField

### ForeignKey 옵션.
