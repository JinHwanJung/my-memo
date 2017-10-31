# @property
- get, set에 대한 액션을 변수에 직접 접근하지 않고 메서드(getter, setter)로 호출되도록 하려면 @property를 사용하면 된다.
- getter함수에 @property 데코레이터. 
- setter함수에 @메서드이름.setter 데코레이터.
- 이렇게 하면 .color="red" 경우 color(clr)메서드 실행되고
- .color 이렇게 쓰면 __color이 반환된다.

<code>
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


출처: http://hamait.tistory.com/827 [HAMA 블로그]
</code>