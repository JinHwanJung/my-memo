# EventDrivenable Class
- base/models.py
## 클래스 메서드의 시그니처

```python
def prepare_write(self) # EventDrivenable에서 사용하는 변수 초기화
def compute_self_old(self)
@property
def is_creating(self)
def pre_create(self)
def pre_update(self)
def pre_clean(self)
def pre_remove(self)

def on_open(self)
def on_close(self)
def post_clean(self)

def post_save(self)
def post_create(self)
def post_update(self)
def clean_others(self)
def task_clean_others(self)

def clean_heavy(self)
def is_field_modified(self, field_name)
def is_fields_modified(self, *args)
def is_data_field_modified(self, key_name)
@classmethod
def generate_md5(cls, name)
@property
def model_class_name(self)
@property
def relational_fields(self)
def save(self, *args, **kwargs)
def delete(self, using=None, keep_parents=False)
```
### def save(self, *args, **kwargs)
```python
def save(self, *args, **kwargs):
    if self.is_deleting:
    # -> 삭제에 대한 플래그가 있다면, save는 실행되지 않는다.
        return

    self.prepare_write() # -> 자체 사용변수 초기화를 진행한다

    # clean_only 플래그 확인
    # denormalized 필드 갱신 포함, 오직 validation 처리만 하는 경우에 이 플래그가 넘어온다
    # 재진입 문제가 있기 때문에 save() 내에서는 반드시 local 변수로 저장하여 사용해야 함
    clean_only = kwargs.pop('clean_only', False)

    # For Timestampable and HistoricalRecords
    self.clean_only = clean_only

    # 생성인지 수정인지 구분하기 위한 플래그 계산
    is_create = self.is_creating
    if clean_only and is_create:
        raise AssertionError('생성 시에는 clean_only 를 지정할 수 없습니다.')

    # denormalized 필드 최적의 갱신을 위해 현재 DB 에 저장된 상태 그대로 로드
    # self_old 와 self 를 비교하여 정확히 어떠한 값이 변경되었는지 확인할 수 있다.
    self.compute_self_old()
    if self.self_old:
        if self.self_old.status_id == 1 and self.status_id != 1:
            is_create = True

    if not clean_only:
        # clean() 호출 전에 미리 처리되어야만 하는 로직 수행
        # 예를 들면 model_type 이 None 인 경우 default model_type 으로 처리하는 등
        if is_create:
            self.pre_create()
        else:
            self.pre_update()

    # self.clean() 호출을 통해 self 의 상태를 valid 하게 만든다 (denormalized 필드 포함)
    self.pre_clean()
    self.clean_fields(exclude=self.relational_fields)
    self.clean()
    if not clean_only:
        if self.is_field_modified('status'):
            if self.status_id in (0, 5):
                self.on_open()
            elif self.status_id in (1, 2, 4):
                self.on_close()
    self.post_clean()

    # 실제 DB 저장
    if self.is_deleting:
        return
    super().save(*args, **kwargs)
    self.just_created = is_create
    self.post_save()

    if not clean_only:
        # assert ModelStatus.get('Removed').id == 1
        if self.status_id == 1:
            if self.is_field_modified('status'):
                self.pre_remove()
                self.just_removed = True

        # DB 저장 완료 후 반드시 같은 트랜잭션 내에서 진행해야 하는 후속 처리 로직 수행
        # CAUTION!!! : 절대 자기자신을 다시 수정해서는 안됨. 무한루프에 빠지게 됨.
        if is_create:
            self.post_create()
        else:
            self.post_update()

        # self 를 제외한, 다른 instance 들에 대한 clean 처리
        self.task_clean_others()
```
```python
def prepare_write(self):
    self.self_old = None
    self.clean_only = False
    self.just_created = False
    self.just_removed = False
    self.is_deleting = False
    self.just_deleted = False
```