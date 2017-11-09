### 요청 : 무료체험신청기간을 늘려주세요.
1. 해당 학생을 조회한다. 
```
from account.models import Actor
student = Actor.objects.filter(auth_human_name='시율').first()
```


2. 학생의 서비스 만료 기간을 조회한다.
```
student.service_limit_date # 확인.
```

3. 서비스 기간을 늘린다. 
```
student.extend_service(is_for_test=True) # 학생 인스턴스의 기간 +7일씩 연장.(스케줄링 포함)
```

4. 서비스 기간 및 서비스 이슈 work 확인
```
student.service_limit_date
student.wink_service_issue.current_work
```


5. 스케줄링 정상세팅 확인
```
for sche in student.my_schedules.order_by('start_date').all():
    print(sche.item.name, sche.start_date)
```
