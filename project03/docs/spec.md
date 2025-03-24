# BLOG Zzilla
블로그 싸이트로 사용자가 로그인하여, 자신의 개인적인 블로그를 만든다. 
- `user` : name, password, email, mobile phone, address
- `post` : userId, title, content, createdAt, updatedAt
- `comments` : postId, userId, content, createdAt
- `likes` : postId, userId, createAt



# 구성요소 Stack

- 프론트엔드: React
    - React Router를 사용하여 페이지 라우팅.
    - 상태 관리를 위해 React Context 사용.
- 백엔드: Node.js + Express
    - SQLite 데이터베이스와 통신하는 API 엔드포인트 제공.
    
- 세션 관리: Passport
- 데이터베이스 
  - 개발상태 : SQLite
  - 상용: PostgreSQL
    - 게시글 데이터를 저장.
- Sequelize
- 서버 모니터링, 관리 : 베스트 프랙티스 적용