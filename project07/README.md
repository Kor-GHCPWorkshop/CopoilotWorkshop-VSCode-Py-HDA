# Project 7: 안드로이드 앱 개발 관련 실습

### Use case: 
- Android Studio에서 GitHub Copilot을 사용해 안드로이드 앱을 개발하는 방법을 학습합니다.

### 목표:
- GitHub Copilot을 사용해 리팩토링, 코드 작성, 테스트 코드 작성 등 안드로이드 앱 개발에 활용할 수 있습니다.

### Steps:
- GitHub Copilot과 함께 퀴즈 앱을 Compose로 만들어보세요. 
  - 사용자에게 5개문제를 제시하고, 정답을 입력받는 간단한 퀴즈 앱을 만들어보세요.
    - 퀴즈와 객관식 예시를 표시하는 텍스트, 사용자가 정답을 입력 하는 텍스트 필드, 그리고 이전/다음 문제로 가는 버튼을 포함합니다.
    - 퀴즈가 완료되면 피드백을 받기 위한 survery로 진행합니다. 
  - Quiz클래스의 데이터 클래스를 생성합니다. 
    - 문제는 questions.txt 파일의 내용을 사용하며, 이것을 resource manager에 xml파일로 변환해 주도록 Copilot에 요청합니다. 
  - 사용자에게 퀴즈가 끝난뒤 설문조사를 위한 Survey클래스를 생성합니다. 
    - 설문조사는 survey.txt 파일의 내용을 사용하며, 이것을 resource manager에 xml파일로 변환해 주도록 Copilot에 요청합니다.
  - 진행 현황을 보여주는 (ProgressPrintable) Interface 생성하고 Quiz와 Survey 클래스에 적용합니다.

- 테스트 코드 작성을 Copilot에 요청합니다. 

### 추가 실습:
- 작성된 코드에 대해 /simplify를 요청해 보세요.
- 사용자가 입력한 정답이 틀릴 경우, 정답을 알려주는 피드백을 제안받아 추가해보세요.


