# Database
- 모든 SQL 파일(.sql)과 데이터베이스 파일들(.db, .sqlite)은 `/db` 디렉토리에 위치
- SQLite는 `/db/dev.db`에 저장
- 모든 ORM모델은 `/db/models` 디렉토리에 위치
- 데이터베이스 테이블은 소문자이며 밑줄을 사용
- 모든 테이브은 `id`를 primary key를 가지며 자동으로 증가
- `users`는 패스워드는 저장하지 않고, 이메일 링크
- 다대다(Many-to-Many) 관계에서는 복합 기본 키(compound primary key)를 사용하며, 단일 ID와 복합 고유 키(compound unique)를 함께 사용하지 않는다.
- `char`, `varchar`, `nvarchar`는 문자열에 사용하지 않고, `text`만 사용
- 모든 connection string들은 로컬에 `.env`파일에 저장

# 테이블 스키마

- users 테이블

    - id: Primary Key, 자동 증가
    - username: 사용자 이름 (고유)
    - email: 이메일 주소 (고유)
    - password: 암호화된 비밀번호

- memos 테이블

    - id: Primary Key, 자동 증가
    - user_id: Foreign Key, users 테이블과 연결
    - title: 메모 제목
    - content: 메모 내용
    - created_at: 메모 생성 날짜
    - updated_at: 메모 수정 날짜
