# django orm
쿼리셋(QuerySet) : 전달받은 모델의 객체 목록,
데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬을 할 수 있다.

## Select

### Get
> Model.objects.get()
- 단일행 "모델타입"으로 반환된다.
- 만약 조회결과가 존재하지 않을 경우 Model.DoesNotExist Exception으로 처리된다.
- get() 안에 조건을 제시할 수 있음. 
- get()은 단일행을 반환하므로 다른 method들을 get다음에 연결 할 수 없음.

### All
> Model.objects.all()
- 전체 자료를 불러오며 "QuerySet 타입"으로 반환된다.
- 조회결과가 존재하지 않으면 빈값으로 처리된다.

### Create
> Model.objects.create(username='test', name='정진환', pass='1234')


### Filter
> Model.objects.filter() (=Model.objects.all().filter()와 동일한 기능)
> value = key = Model.objects.filter(name='jung')
> print(key[0]['name'])
- get과 다르게 filter는 조건에 맞는 여러 행을 출력하며 "QuerySet 타입"으로 반환된다.


### 조건 키워드

#### __lt / __gt
- 보다 작다 / 보다 크다
- id가 1보다 큰 자료 검색
> Model.objects.filter(id__gt=1)


#### __lte / __gte
- 같거나 보다 작다 / 같거나 보다 크다
> Model.objects.filter(value__gte=3)


#### __in
- 주어진 리스트안에 존재하는 자료 검색
- id가 2,3,5 인 자료 검색
> Model.objects.filter(id__[2,3,5])


#### __year / __month / __day
- 해당 년도, 월, 일 자료 검색
> Model.objects.filter(pub_date__year=2005)


#### __isnull
- 해당 열의 값이 null인 자료 검색
> Model.objects.filter(name__isnull=True)


#### __contains / __icontains
- 해당 열의 값이 지정된 문자열을 포함하는 자료 검색 /  icontains는 대소문자를 구별하지 않음.
> Model.objects.filter(title__icontains='movie')


#### __startswith / __istartswith
- 해당 열의 값이 지정한 문자열로 시작하는 자료 검색 / istartwith는 대소문자를 구별하지 않음.
> Model.objects.filter(title__startwith='Movie')


#### __endswith / __iendswith
- 해당 열의 값이 지정한 문자열로 끝나는 자료 검색 / iendswith는 대소문자 구별 하지 않음.
> Model.objects.filter(name__iendswith='test')


#### __range
- 문자, 숫자, 날짜의 범위를 지정한다. SQL의 between에 해당.
> Model.objects.filter(id__range(2,10))

### Order by
> Model.objects.order_by()
- 기본 정렬순서는 오름차순. 내림차순일 경우 컬럼명에 -를 붙여서 사용.
> value = Model.objects.order_by('-pk') # 내림차순 정렬
> value = Model.objects.order_by('pk') # 오름차순 정렬


### Values
> Model.objects.values() 
- SQL에서 select에 해당한다.
- value를 사용하지 않으면 sql의 select * 와 같이 전체를 출력한다
> value = Model.objects.values('pk') # query set 타입으로 pk만 출력.

### Aggregate
- sql에서 max, min, count과 같은 기능. 단일행을 출력해줌.
- 단일행을 반환하므로, 다른 method와 같이 사용 못함.
> from django.db.models import Max
> value = Model.objects.aggregate(temp_name=Max('pk'))
> print(value['temp_name'])
,
> from django.db.models import Max
> from django.db.models.functions import Coalesce
> value = Model.objects.aggregate(temp_name=Coalesce(Max('pk'),10000))
> print(value['temp_name'])

## Insert

### save()
> instance.name = temp_name
> instance.save()

### objects.create()
> Model.objects.create(name='temp')
- objects.create()를 사용할 경우 .save()를 할 필요 없이 바로 저장된다.

### DRF에서 insert
> serializer = CommonTaxInSerializer(data=json_format_data, partial=True)
> if serializer.is_valid()
> serializer.save()
- partial은 테이블 내의 일부분만 insert할 때, 
- partial을 제외하고 serializer에 명시한 값 중 일부분만 insert하려고 하면 에러
- .save() 하기 위해선 validation을 한 다음 진행


## Update

### 단일 업데이트
> data = Model.objects.get(pk=pk)
> data.name = 'test'
> data.save()

### 다중 업데이트
> Model.objects.filter(name='test', age='20').update(**update_dic)


# DRF에서 사용

## 단일 업데이트
> instance = Model.objects.get(pk=pk)
> serializer = Model(instance, data = json_data)
> if serializer.is_valid():
>   serializer.save()
- 업데이트 할 단일행을 구한 후, data에 변경할 값의 json 값을 넣어서 업데이트.

## 다중 업데이트
> queryset = Model.objects.all()
> serializer = BookSerializer(queryset, many=True)
> if serializer.is_valid():
>    serializer.save()

## Delete(장고, DRF 둘다 같은 방식)
### 단일 삭제
> instance = Model.objects.get(pk=pk)
> instance.delete()

### 다죽삭제
> Model.objects.filter(name='test', age='20').delete()

---
OR 연산자 사용하여 쿼리
```python
from django.db.models import Q
Model.objects.filter(Q(first_name='jung') | Q(first_name='test'))
```