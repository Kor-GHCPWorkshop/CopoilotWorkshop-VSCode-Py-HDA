# Task 5: Django 웹앱 만들기 (Part 1) 

## Use case: 
- Copilot에게 Test code를 제안 받습니다.

## 목표:
 - Copilot Edit을 활용하여, 여러개의 테스트 파일을 동시에 생성하는 방법을 실습합니다.
 - Commit message 자동 생성 기능을 사용해 보고, Custom instruction을 제공하여, 원하는 형태로 commit message를 제안받아 봅니다.

## Step 1: Coiplot Edit을 활용하여 테스트 코드 작성
 - Task 3에서 생성한 TestCustom instructions를 확인합니다. (`test-style.md`) <br>
   (원하는 내용이 있을 경우 추가 삭제) <br>
   <img src="img/01.png" width="800">

 - Copilot Edit을 열고, 'Add Files' 버튼에서 프로젝트 디렉토리를 선택한 뒤, 챗 창에 `이 프로젝트의 테스트 코드를 작성해 줘` 등으로 요청합니다. <br>
   <img src="img/02.png" width="600">

 - 제안되는 테스트 내용들을 확인합니다. <br>
   <img src="img/03.png" width="600">

 - Chat 창에 '생성된 테스트를 실행해 줘'라고 입력합니다. <br>
   <img src="img/04.png" width="600"> 

 - 테스트 실행 방법에 대해 확인합니다. <br>
   <img src="img/05.png" width="700"> <br>
   <img src="img/06.png" width="700"> <br>

 - 전체 프로젝트에 대한 테스트 코드를 실행 합니다. <br>
   <img src="img/07.png" width="800"> <br>

 - 특정 앱만의 테스트도 실행해 봅니다. <br>
   <img src="img/08.png" width="800"> <br>


## Step 2: Commit message 자동 생성 (Custom instruction으로 원하는 형태로 제안받기)
 - .vscode/settings.json 파일을 열고 아래와 같이 입력합니다.  <br>
    ```json
    - "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text" : "커밋 메시지는 한글로 작성하며, 현재 시제로 작성합니다. 커밋 메시지는 변경 내용을 자세히 요약해서, 항목마다 문장 앞에 '-'를 붙여서 작성해주세요. 이모지들을 포함합니다."
        }
    ]
    ```
    <img src="img/09.png" width="800">

    - 파일 변경내용을 저장합니다. <br>
 
 - 왼편의 Git 아이콘을 클릭하고, 'Changes' 우측의 '+' 아이콘을 클릭하여, 변경된 파일을 staging area에 추가합니다. <br>
   <img src="img/10.png" width="400"> <br>

   ** Git이 초기화되지 않은 경우, 'initialize repository'를 클릭하여 Git을 초기화합니다. <br>
   <img src="img/13.png" width="400"> <br>


 - Message 입력란 우측에 'sparkle' 아이콘을 클릭합니다다. <br>
   <img src="img/11.png" width="500"> <br>
 
  - 제안되는 commit message 내용들을 확인합니다. <br>
   <img src="img/12.png" width="600">

## 추가자료
- [GitHub Copilot을 활용한 Unit test생성 사용예](https://github.blog/ai-and-ml/github-copilot/how-to-generate-unit-tests-with-github-copilot-tips-and-examples/)