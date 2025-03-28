# 메모짱
Django 기반의 메모장 웹 애플리케이션

주요 기능
- 사용자 로그인 및 회원가입.
- 메모 작성, 수정, 삭제.
- 메모 목록 조회.



# 구성요소 Stack

- 프론트엔드
   - Django 템플릿 엔진: HTML, CSS, JavaScript를 사용하여 간단한 UI 구현.
   - Bootstrap (선택 사항): 빠르고 반응형 UI를 위해 사용.

- 백엔드
   - Django Framework: 웹 애플리케이션의 핵심 로직과 API 제공.
   - Django Forms: 메모 작성 및 수정 폼 처리.

- 데이터베이스
   - SQLite: 개발 단계에서 간단히 사용할 수 있는 기본 데이터베이스.

- 사용자 인증
   - Django 내장 인증 시스템: 사용자 로그인, 로그아웃, 회원가입 기능 제공.

- 세션 관리
    - Django의 기본 세션 관리 기능 사용.

- 배포
    - 개발 단계: Django의 내장 개발 서버 사용.
    - 프로덕션: Gunicorn + Nginx (선택 사항).

- 추가 라이브러리
    - django-crispy-forms (선택 사항): 폼 스타일링을 간편하게 하기 위해 사용.



