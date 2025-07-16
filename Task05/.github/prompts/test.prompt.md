---
mode: 'agent'
model: Claude Sonnet 4
tools: ['changes', 'codebase', 'githubRepo', 'runTests', 'testFailure']
description: "테스트 코드를 작성합니다."
---

테스트 코드를 작성하고 테스트 통과 여부를 확인해 줘.
테스트 코드에 대한 지침은 [test.instructions.md](../instructions/test.instructions.md) 파일을 참조한다.

- 기능이나 함수가 정상적으로 동작하는지 확인할 수 있는 단위 테스트 코드를 작성해 줘.
- 입력값이 유효하지 않을 때 예외가 발생하는지 테스트해 줘.
- 여러 입력 케이스(정상, 경계, 오류)를 포함한 테스트 코드를 작성해 줘.
- 테스트 결과가 기대한 출력과 일치하는지 검증해 줘.
