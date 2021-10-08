마님 튜토리얼 영상 레파지토리 입니다.

README 에 자유롭게 원하는 내용을 작성해주세요~ ㅎㅎ 

방식은 자유입니다.


-----------------------------------------------------------------
2021-10-04 수정내용

VisualCafe 패키지는 firstvisualcafe 하위에 위치했습니다.

이제는 VisualCafe 패키지 위치를 가장 상위 디렉토리에 위치시켰습니다. 

현재 디렉터리 구조
- manim_tutorial
  - VisualCafe           <- 여기로 패키지 위치 옮김
  - tutorial_notebook
  - firstvisualcafe
    - byoungho
    - jinseok
    - seongmin


네이밍 규칙 
1. 패키지폴더 이름은 캐멀케이스 첫번째 문자 대문자 
2. 모든 .py 로 끝나는 파일은 lowercase, 언더바 ( _ ) 생략
3. 모든 scene 을 상속받은 클래스 이름은 "secene_(원하는 이름).py
4. 만드신 클래스 이름은 캐멀케이스 첫번째 문자 대문자


-----------------------------------------------------------------
2021-10-07 새로운 영상 생성시

아마 영상을 하나 만들때 보통 이런방식을 취할것 같습니다.
```python
from manim import *

class 영상이름(Scene):
  construct(self):
    pass
```    
이제는 이런방식으로 만드시면 자동으로 영상앞에 저희 인트로부분이 생길겁니다.

```python
from manim import *
from VisualCafe.scene.visualcafescene2d import *

class 영상이름(VisualCafeScene2D):
  def visualcafe_construct(self):
    pass
```

2d scene과 3d scene 모듈은 다르니 숫자만 바꿔서 사용하시면 됩니다.

-----------------------------------------------------------------






