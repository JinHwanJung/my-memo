# == 과 is 비교.
<code>is</code> : 같은 객체를 가리키고 있는 두 변수에 대해서 비교하여 같으면 True를 반환한다.<br/>
<code>==</code> : 변수가 참조하고 있는 값에 대해 비교하여 같으면 True를 반환한다.<br/><br/>
파이썬은 small integer objects에 대해서만 캐쉬 데이터를 가지고 있기 때문에 다음과 같이 예제가 동작함.<br/><br/>
```python
>> 1000 is 10**3
False

>> 1000 is 10**3
False

>> [] is []
False

>> [] == []
True

>>  "a" is "a"
True

>> "aa" is "a" * 2
True

>> x = "a"
>> "aa" is x * 2
False

>> "aa" is intern(x*2)
True

```
---
# if not v and v != 0
- v 변수는 메모리에 있으나 타입은 None 타입 또는 ""(즉, 빈 문자열) 일 경우를 검사한다.

---
# @property
- get, set에 대한 액션을 변수에 직접 접근하지 않고 메서드(getter, setter)로 호출되도록 하려면 @property를 사용하면 된다.
- getter함수에 @property 데코레이터. 
- setter함수에 @메서드이름.setter 데코레이터.
- 이렇게 하면 .color="red" 경우 color(clr)메서드 실행되고
- .color 이렇게 쓰면 __color이 반환된다.

```python
class Test:

    def __init__(self):
        self.__color = "red"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,clr):
        self.__color = clr

if __name__ == '__main__':

    t = Test()
    t.color = "blue"

    print(t.color)
```
---
# with 구문
- with 구문 body 코드 실행의 전과 후의 실행되는 코드를 정의할 수 있다.
- 파이썬의 context_manager에 의해 실행된다.
- context_manager는 with 구문의 body 전에 실행되어야 할 함수 \__enter()__ 와 body 후에 실행되어야 할 함수 \__exit()__를 찾아 실행해준다.
- try/finally를 대신하여 더 간편하며 쉽게 사용할 수 있는 이점이 있음.
```python
class controlled_execution:
    def __enter__(self):
        set things up
        return thing
    def __exit__(self, type, value, traceback):
        tear things down

with controlled_execution() as thing:
     some code using thing
```
- 코드에서 context_manager에 의해 \__enter__가 실행되고 반환되는 값은 <code>as</code>의 thing으로 전달 된다.
- 이후 body code가 실행되고 코드가 무슨 일이 있더라도 \__exit__ 함수 호출이 보장된다.
---
# 파이썬의 다중상속
- 파이썬에서 다중상속의 경우, [class D(B,C)] => 왼쪽에서 오른쪽 순서로 메서드를 찾는다.
- 복잡한 다중상속의 경우, overwrite에 대한 순서를 추적할 때는 mro() 함수를 사용하여 클래스가 파생된 순서의 목록을 얻어서 확인.
- 메서드 탐색 순서(Method Resolution Order, MRO)
---

# 시스템 환경변수 PYTHONPATH
모듈 import 를 위한 파이썬 환경변수 PYTHONPATH 설정하기
1. 프로젝트 루트에서 "export PYTHONPATH=${PWD}" 를 실행하여 환경변수 세팅 그때그때 해준다?
2. virtualenv 를 사용하고 pip 또는 setup.py 를 작성하여 이용한다.
