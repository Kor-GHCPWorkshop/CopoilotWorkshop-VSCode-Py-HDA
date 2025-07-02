---
applyTo: "**/*.sqlite3"
---

# Database
- 데이터베이스 테이블은 소문자이며 밑줄을 사용
- 모든 테이브은 `id`를 primary key를 가지며 자동으로 증가
- 다대다(Many-to-Many) 관계에서는 복합 기본 키(compound primary key)를 사용하며, 단일 ID와 복합 고유 키(compound unique)를 함께 사용하지 않는다.
- `char`, `varchar`, `nvarchar`는 문자열에 사용하지 않고, `text`만 사용
- 모든 connection string들은 로컬에 `.env`파일에 저장

# 테이블 스키마

- memos 테이블

    - id: Primary Key, 자동 증가
    - user_id: Foreign Key, users 테이블과 연결
    - title: 메모 제목
    - content: 메모 내용
    - created_at: 메모 생성 날짜
    - updated_at: 메모 수정 날짜

- users 테이블

    - id: Primary Key, 자동 증가
    - username: 사용자 이름
    - email: 사용자 이메일
    - password: 사용자 비밀번호
    - created_at: 사용자 생성 날짜
    - updated_at: 사용자 수정 날짜