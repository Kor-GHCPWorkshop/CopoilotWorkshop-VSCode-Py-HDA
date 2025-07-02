<!-- ---
applyTo: "**"
--- -->

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


- 디렉토리 구조
  - .github/
  - docs/
  - memojjang/                  # 메인 Django 프로젝트
  - apps/                     # Django 앱들
    - __init__.py
    - __pycache__/
    - memos/                  # 메모 앱
      - __init__.py
      - admin.py              # 관리자 설정
      - apps.py               # 앱 설정
      - models.py             # 데이터 모델
      - views.py              # 뷰 로직
      - tests.py              # 테스트
      - migrations/           # 데이터베이스 마이그레이션
      - __pycache__/
    - users/                  # 사용자 앱
      - __init__.py
      - admin.py              # 관리자 설정
      - apps.py               # 앱 설정
      - models.py             # 데이터 모델
      - views.py              # 뷰 로직
      - tests.py              # 테스트
      - migrations/           # 데이터베이스 마이그레이션
      - __pycache__/
  - db/                       # 데이터베이스 관련 파일
  - static/                   # 정적 파일
    - css/                    # CSS 파일
    - js/                     # JavaScript 파일
  - templates/                # Django 템플릿
    - base.html               # 기본 템플릿
    - home.html               # 홈페이지 템플릿
    - memos/                  # 메모 관련 템플릿
      - memo_confirm_delete.html
      - memo_detail.html
      - memo_form.html
      - memo_list.html
    - users/                  # 사용자 관련 템플릿
      - login.html
      - register.html

	
# 일반 코딩 지침

1. API 통신 시 에러 처리 및 로딩 상태를 반드시 구현할 것
2. 모든 외부 API URL, 시크릿 등은 환경 변수(.env)로 관리할 것
3. 한글 주석은 필요한 경우에만 간결하게 작성할 것
4. 컴포넌트/함수/파일명은 프로젝트 목적에 맞게 명확하게 작성할 것
5. 불필요한 콘솔 로그는 커밋 전에 반드시 제거할 것
6. 코드 내 하드코딩된 값은 상수로 분리하여 관리할 것
7. 공통 유틸 함수는 별도 utils 폴더에 분리할 것
8. 불변성(immutability)을 지키는 코드를 작성할 것
9. PR(풀리퀘스트)에는 변경 요약 및 테스트 방법을 반드시 포함할 것
10. 코드 리뷰에서 발견된 개선점은 즉시 반영할 것


# 보안 점검 지침
- 코드의 보안 취약점을 점검하고 개선 방안을 제안합니다.
- 입력값 검증, 하드코딩된 비밀번호/시크릿, 취약한 암호화/해시 알고리즘 사용, 인증/인가 누락, 민감 정보 로그 출력, 외부 라이브러리 취약점 등을 점검합니다.
- 발견된 취약점에 대해 상세 설명과 구체적인 개선 방법을 제안합니다.
- 모든 답변은 한국어로 작성합니다.
