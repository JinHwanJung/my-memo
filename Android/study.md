# px, dip, dp, sp

1. dpi: dot per inch, 1인치에 들어가는 픽셀의 수
2. 밀도 독립적 픽셀인 dp
    - 디바이스에 따라 크기가 조정되는 부분은 px이 아니라 dp로 부르도록 한다
3. dp 와 px 계산 수식: dp = px * (160/dpi)
    - 160이라는 값은, 안드로이드가 mdpi 폰의 기준(baseline)을 160dpi로 잡아 두었기 때문
    - 따라서, 160 dpi 인 휴대폰에서는 dp = px 이다.
4. 안드로이드 픽셀 변환기
    - http://angrytools.com/android/pixelcalc/
5. sp 는 글꼴에 대한 dp 와 비슷한 개념...?
6. 요약: 레아이웃 등의 UI적 요소는 dp(dip)을 사용하는 것이 좋고, 글자 크기에는 sp를 사용하는 것이 좋다. (px이나 pt는 사용)

# primitive type (기본형)
- 총 8개
- Boolean, char, byte, short, int, long, float, double

# 상수와 리터럴
- 리터럴 ex: 1, 100, 44
- 상수 ex: final MAX = 100;  // 여기에서 MAX 는 상수, 100 은 리터럴

