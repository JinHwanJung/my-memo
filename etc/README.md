도전과제
Cpython Development 천천히 모두 읽기
python trace_malloc 모듈로 메모리 누수 찾기

개념이해하기
- DB 트랜잭션 격리 수준 완벽한 이해
- key 채굴하는 구조의 장점 단점? id auto increasement 하지 않는 이유는??


* save 포인트 발생(Lock 발생)하면,  다른 수정(save) 요청 pending
 
1. select_for_update() 를 수행하면,
 1) 실제 수정이 없어도 save 포인트를 남긴다.
 2) save 포인트가 존재하는지 먼저 확인한 후, 가져와서 save 포인트를 남긴다.
	즉, select_for_update 로 가져온 객체는 save 에 대한 lock 이 발생되므로, OptimisticLock 에러를 회피할 가능성이 높다.

2. 트랜잭션 내 먼저 된 save() 는 save 포인트를 남기고, 알려진다.

* select_for_update 는 먼저 발생된 save 포인트 조회한 후에 객체를 가져온다.

* 그냥 save() 할 경우는 먼저 수행중인 다른 save 포인트가 있다면, 기다린 후에 수행된다.
    -> 하지만 이때 version 값이 서로 달라지므로, OptimisticLock 이 발생한다.
    -> 결국 save 포인트가 있는지 검사가 됬다면, 쿼리를 날릴 필요없이 OptimisticLock 발생하면 되지 않을까??? 하지만 여기서 말하는 save 포인트는 DB에서 제공하므로... 이 훅을 걸 수 있는지가 의문
    -> OptimisticLock 은 충돌이 많이 발생하면 비용이 많이 발생 되므로 주의 필요함

* savepoint 발생은 DB 수준에서 처리된다.
즉, update 요청시에 해당 row 가 갱신중 이라면 해당 트랜잭션이 커밋되거나 롤백을 기다린 후 update가 수행된다. 
