# Repository:
https://github.com/JinHwanJung/phone-book-android.git

# 용어정리
 - 라이브러리 : 자주 사용하는 부분 프로그램 집합
 - 모듈 : 프로그램을 구성하는 독립적인 부품 프로그램
 - API : 앱을 개발하기 위한 규칙, 제공하는 기능을 제어할 수 있게 만든 인터페이스

# 메니페스트

```xml
# 카메라 권한
<uses-permission android:name="android.permission.CAMERA"/>
# 저장하기 위한 권한 설정
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
# 읽기 위한 권한 설정
# 카메라 사용을 사용자에게 알림
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-feature android:name="android.hardware.camera2"/>
```

# MainActivity.kt <TODO>
## permissionCheck() 함수 구현부에서 사용한 라이브러리 정리

1. Manifest
```kotlin
import android.Manifest

# 사용
Manifest.permission.READ_EXTERNAL_STORAGE
Manifest.permission.WRITE_EXTERNAL_STORAGE
Manifest.permission.CAMERA
```

2. AppCompatActivity
```kotlin
import android.support.v7.app.AppCompatActivity

# 사용
class MainActivity : AppCompatActivity() { ... }
```

3. Bundle
```kotlin
import android.os.Bundle

# 사용
override fun onCreate(savedInstanceState: Bundle?) { ... }
```

4. PackageManager
```kotlin
import android.content.pm.PackageManager

# 사용
PackageManager.PERMISSION_GRANTED
```

5. ActivityCompat
```kotlin
import android.support.v4.app.ActivityCompat

# 사용
ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE), 100)
``` 

6. ContextCompat
```kotlin
import android.support.v4.content.ContextCompat

# 사용
ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE)
```
