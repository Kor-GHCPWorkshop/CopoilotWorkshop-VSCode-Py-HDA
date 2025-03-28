# Task 4: Django 웹앱 만들기 (Part 2) 

## Use case: 
- Part 1에서 생성된 Django 웹앱에 Copilot을 활용해 모델을 생성하고, Copilot Edit기능을 사용해 템플릿 뷰에 내용을 신속하게 추가하면서 나머지 기능을 구현하며, 추가적인 컨텍스트를 제공하거나, CLI에서의 Copilot을 활용하는 등등 다양한 기능을 활용합니다.

## 목표: 
- 에러 해결을 위해 Copilot에게 다양한 컨텍스트 추가 방법을 익힙니다. #terminalSelection, #file, #selection

- CLI 명령어 창에서 Copilot을 활용하는 방법을 익힙니다.
- Copilot Edit을 활용해 여러개 템플릿 파일을 동시에 생성하는 방법을 실습합니다.
- prompt 파일을 생성하여, Copilot Edit을 활용해 여러개 템플릿 파일을 동시에 생성하는 방법을 실습합니다. 

## Step 1: User 모델 생성

- `python manage.py runserver` 명령을 통해 개발 서버를 실행 합니다. <br>
  <img src="img/01.png" width="500"> 
  - 만약 아래와 같이 에러가 발생하면, `#terminalLastCommand`를 통해 에러 수정을 요청합니다. <br> 
    <img src="img/02.png" width="500">
    <img src="img/03.png" width="400"> <br>
    <img src="img/04.png" width="500">

- `users/models.py` 파일을 열고, Copilot chat에 요청하여 모델을 정의 합니다. <br>
    <img src="img/18.png" width="200">
    <img src="img/19.png" width="200">

   * 혹, 불필요한 부분이 제안되었다면 삭제합니다. (닉네임, 이미지등)

- `settings.py` 파일에 다음을 추가합니다. <br>
    <img src="img/20.png" width="300">

- 모델 정의 후, Copilot이 제안해 준, 이어지는 과정을 진행하기 위해 별도 CLI터미널을 실행합니다. <br>
    <img src="img/10.png" width="200">

- venv를 실행합니다. <br>
    <img src="img/11.png" width="600">

- `python manage.py makemigrations users` 명령어를 실행합니다. <br>
    <img src="img/21.png" width="700">

- `python manage.py migrate` 명령어를 실행합니다. <br>
    <img src="img/22.png" width="500">

  * Copilot이 제안해준 명령어에 마우스를 위치하면, `'Insert into terminal`'을 통해 실행할 수도 있습니다. <br>
    <img src="img/13.png" width="400">

- Admin페이지에 모델을 등록하기 위해 `admin.py` 파일을 열고, 모델을 등록합니다. <br>
    <img src="img/23.png" width="500"> <br>

## Step 2: 슈퍼 유저 생성하기
- CLI 터미널에서 Ctrl + i를 입력하고, Copilot 창에에 `superuser를 생성` 라고 입력합니다. 
  <img src="img/24.png" width="700">
  <img src="img/25.png" width="500">
   - `Insert into terminal` 혹은 `copy` 버튼을 활용합니다. 

- `python manage.py createsuperuser` 명령어를 통해해 슈퍼 유저를 생성합니다. <br>
  <img src="img/26.png" width="500">


## Step 3: Memos 모델 생성
- 개발 서버는 계속 실행 중인 상태에서 진행합니다. <br>

- `memos/models.py` 파일을 열고, Copilot chat에 요청하여 모델을 정의 합니다. <br>
    <img src="img/05.png" width="400"> <br>
    <img src="img/06.png" width="400"> 
    <img src="img/08.png" width="300">

- `python manage.py makemigrations` 명령어를 실행합니다. <br>
    <img src="img/12.png" width="600">
    
- `python manage.py migrate` 명령어를 실행합니다. <br>
    <img src="img/14.png" width="500">

- 관리자 페이지에 모델을 등록하기 위해 `memos`디렉토리의 `admin.py` 파일을 열고, 모델을 등록합니다. <br>
  <img src="img/15.png" width="100"> 
      <img src="img/09.png" width="500"> 

- localhost:8000/admin/으로 접속하여, 관리자 계정으로 로그인합니다. <br>
    <img src="img/16.png" width="300">

- 등록된 모델을 확인합니다. <br>
    <img src="img/17.png" width="300">

- `Ctrl + Shift + P`를 눌러 명령어 팔레트를 열고, `File: Save All Files`를 선택합니다. <br>


## Step 4 : 이후 과정 질문하기

- `@workspace`를 활용해, Copilot에게 이후 프로젝트를 완성하기 위해 어떤 과정이 남았는지 확인합니다. <br>
    <img src="img/27.png" width="500">
    <img src="img/28.png" width="400">

## Step 5: Prompt파일 생성 - Copilot Edit을 통해 URL 패턴, 뷰, 템플릿 동시에 생성하기

- **[Prompt 파일 이란?](https://code.visualstudio.com/docs/copilot/copilot-customization#_reusable-prompt-files-experimental)**
  - Prompt 파일은 재사용 가능한 프롬프트 지시문을 Markdown 형식으로 저장해, Copilot에 손쉽게 추가 맥락을 제공할 수 있도록 도와줍니다. 예컨대 특정 아키텍처 요건, 코드 스타일 등을 이 파일에 정리해두면, 반복적인 지시사항 없이도 채팅 창에서 손쉽게 불러와 의도된 코드를 빠르게 생성할 수 있습니다.
  - Use cases:
    - 코드 생성(Code generation): 컴포넌트, 테스트, 마이그레이션 등을 재사용 가능한 프롬프트로 만들어, 예를 들어 React 폼이나 API 목업을 간편히 생성.
    - 도메인 전문 지식(Domain expertise): 보안 정책이나 컴플라이언스 확인처럼 특화된 지식을 프롬프트로 공유.
    - 팀 협업(Team collaboration): 문서나 사양을 참조해 패턴과 가이드라인을 기록.
    - 온보딩(Onboarding): 복잡한 프로세스나 프로젝트별 패턴을 단계별로 안내하는 가이드를 생성.

- VS Code의 설정에서 Prompt Files 부분을 확인합니다. <br>
    <img src="img/29.png" width="500">

- default 위치인 .github/prompts 디렉토리를 생성합니다. <br>
    <img src="img/30.png" width="300">

- 위 디렉토리내에 template.prompt.md 파일을 생성하고, 예시로 주어진 `promptExample/` 디렉토리의 `template.prompt.md` 파일의 내용을 붙여 넣습니다다. <br>
    <img src="img/31.png" width="300">


- Copilot Edit으로 이동합니다. <br>
    <img src="img/32.png" width="300">
- 하단에 채팅창에서 클립 모양의 아이콘 'Add Files..'을 클릭합니다. <br>
    <img src="img/33.png" width="300">
- Prompt를 선택합니다. <br>
    <img src="img/34.png" width="500">
- `template.prompt.md` 파일을 선택합니다. <br>
    <img src="img/35.png" width="500"> 
- template 프롬프트가 선택된 것을 확인합니다. <br>
    <img src="img/36.png" width="400">
- 다시 클립 모양 아이콘을 클릭하고 Folder를 선택합니다. <br>
    <img src="img/42.png" width="400">

- Chat에 아래와 같이 입력합니다. <br> 
   - `이 프로젝트를 완성하기 위해, URL패턴, 뷰, 템플릿을 구성해줘`
    <img src="img/43.png" width="500">    

- Copilot Edit이 파일들을 완성합니다. <br>
    <img src="img/38.png" width="600">

- **Keep**을 클릭하여 생성된 내용을 유지합니다. <br>

- 추가로 필요한 내용들을 요청하여 구성합니다. <br>
    <img src="img/39.png" width="400">
- 생성된 파일들을 확인하고, Keep 하여 유지합니다. 그리고 파일들을 저장합니다. <br>
    <img src="img/40.png" width="600">
    <img src="img/41.png" width="500">

- CLI터미널에서 `Ctrl + i`를 입력하고, Copilot 창에 '`django bootstrap 5 설치`' 명령어를 요구합니다. <br>
    <img src="img/44.png" width="600"> <br>
    <img src="img/45.png" width="500">

    - run을 실행하여 bootstrap 5를 설치하고, settings.py에 내용을 추가합니다 . <br>
    <img src="img/46.png" width="300">

- 터미널에서 python manage.py migrate 명령어를 실행합니다. <br>
    <img src="img/47.png" width="600">
    - 만약 아래와 같이 에러가 발생하면, `#terminalLastCommand`를 통해 에러 수정을 요청합니다. <br>

- localhost:8000 으로 접속하여 프로젝트를 확인합니다. <br>
    <img src="img/48.png" width="700">


## 지식 확인
- 다양한 컨텍스트 추가 방법 
- CLI 명령어 창에서 Copilot을 활용
- Copilot Edit의 동작 방식식
- prompt 파일 
