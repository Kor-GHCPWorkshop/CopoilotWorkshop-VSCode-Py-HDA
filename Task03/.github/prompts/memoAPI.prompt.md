---
mode: 'agent'
description: '곡 메모 API 사용법 및 React 예제 안내'
---

아래 API설명과 같이 곡에 메모를 추가, 조회, 수정, 삭제하는 API(`/v1/songs/:id/memo`)를 리액트(React) 클라이언트에서 활용해 코드를 작성하세요.

## 주요 기능

- **메모 조회**: 기존 메모가 있는지 확인하여 자동으로 로드
- **메모 저장**: 새로운 메모 작성 및 저장 (POST)
- **메모 수정**: 기존 메모 수정 (PUT)
- **메모 삭제**: 메모 삭제 기능 (DELETE)
- **에러/성공 처리**: 사용자 친화적인 피드백 제공

## API 엔드포인트

- **GET** `/v1/songs/:id/memo`      // 메모 조회
- **POST** `/v1/songs/:id/memo`     // 메모 생성
- **PUT** `/v1/songs/:id/memo`      // 메모 수정
- **DELETE** `/v1/songs/:id/memo`    // 메모 삭제

## 1. 메모 조회

- **GET** `/v1/songs/{id}/memo`

응답 예시:
```json
{
  "code": 200,
  "v": "v1",
  "status": "OK",
  "data": {
    "id": 1,
    "text": "이 곡 정말 좋아요!",
    "createdAt": "2025-06-26T12:00:00.000Z"
  }
}


## 2. 메모 생성

- **POST** `/v1/songs/{id}/memo`


응답 예시:
```json
{
  "code": 201,
  "v": "v1",
  "status": "Created",
  "data": {
	"id": 2,
	"text": "이 곡 정말 좋아요!",
	"createdAt": "2025-06-26T12:05:00.000Z"
  }
}
```

## 3. 메모 수정

- **PUT** `/v1/songs/{id}/memo`

요청 바디:
```json
{
  "text": "이 곡 정말 좋아요! 수정됨"
}
```
응답 예시:
```json
{
  "code": 200,
  "v": "v1",
  "status": "UPDATED",
  "data": {
	"id": 1,
	"text": "이 곡 정말 좋아요! 수정됨",
	"createdAt": "2025-06-26T12:00:00.000Z"
  }
}
```

## 4. 메모 삭제

- **DELETE** `/v1/songs/{id}/memo`

응답 예시:
```json
{
  "code": 200,
  "v": "v1",
  "status": "DELETED",
  "message": "메모가 삭제되었습니다."
}
```

## 5. 에러/성공 처리

- 요청이 잘못되었을 때(예: text가 비어있음):
- 존재하지 않는 메모 접근 시:
```json
{
  "code": 404,
  "v": "v1",
  "status": "NOT FOUND",
  "message": "존재하지 않는 메모입니다."
}
```


## 6. React 클라이언트 예시


```javascript
import axios from 'axios';

// 메모 조회
const fetchMemo = async (songId) => {
  const res = await axios.get(`/v1/songs/${songId}/memo`);
  return res.data.data;
};

// 메모 생성
const createMemo = async (songId, text) => {
  const res = await axios.post(`/v1/songs/${songId}/memo`, { text });
  return res.data.data;
};

// 메모 수정
const updateMemo = async (songId, text) => {
  const res = await axios.put(`/v1/songs/${songId}/memo`, { text });
  return res.data.data;
};

// 메모 삭제
const deleteMemo = async (songId) => {
  await axios.delete(`/v1/songs/${songId}/memo`);
};