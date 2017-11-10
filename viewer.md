### 개요 
베타테스트 신청 회원 리스트 DB 제공 요청 from 이경환K(해냄)

- 환경: Production Server
- 계정: khlee
- CSRTeacherAdjustmentDecisionWork 에 있는 모든 Actor(Student)에 대하여 
학부모명, 학부모 연락처, 회원명, 생년월일/나이, 주소, 회원구분, 수준진단내용 추출, 약 270명 예상

```python
from account.models import Actor, ActorType 

students = [student for student in Actor.objects.filter(model_type=ActorType.get('Student')) if student.wink_service_issue and student.wink_service_issue.current_work.is_instance_of('CSRTeacherAdjustmentDecisionWork')]

print(p.auth_human_name, p.auth_human_mdn, s.auth_human_name, s.auth.birthday.date(), '{}세'.format(s.age), '{} {}({})'.format(p.auth.human_address, p.auth.human_detail_address, p.auth.human_postal_code), s.status.name, s.data["levels"])
```
