---
applyTo: "**/*.test.js"
---


## **테스트 프레임워크**
- **Jest**: JavaScript 테스트 프레임워크로, React 및 Node.js 애플리케이션에 적합합니다.

---

## **테스트 코드 작성 지침**

### **1. 테스트 파일 구조**
- 테스트 파일은 소스 코드와 동일한 디렉토리 구조를 따르며, 파일 이름에 `.test.js` 또는 `.spec.js`를 추가합니다.
  - 예: `user.js` → `user.test.js`
- 모든 테스트 파일은 `/tests` 디렉토리에 저장합니다.


---

### **3. 테스트 작성 규칙**
- **Given-When-Then 패턴**을 따릅니다:
  - **Given**: 테스트의 초기 상태를 설정합니다.
  - **When**: 테스트할 동작을 실행합니다.
  - **Then**: 예상 결과를 검증합니다.

```javascript
describe('User Model', () => {
  it('should create a new user', async () => {
    // Given
    const userData = { name: 'John', email: 'john@example.com' };

    // When
    const user = await User.create(userData);

    // Then
    expect(user.name).toBe('John');
    expect(user.email).toBe('john@example.com');
  });
});
```

---

### **4. 테스트 스타일**
- **독립적 테스트**: 각 테스트는 다른 테스트에 의존하지 않아야 합니다.
- **명확한 설명**: `describe`와 `it` 블록에 테스트의 목적을 명확히 작성합니다.
- **모의(Mock) 객체 사용**: 외부 API 호출이나 데이터베이스 작업은 모의 객체를 사용하여 테스트합니다.

---

### **5. React 컴포넌트 테스트**
- **React Testing Library**를 사용하여 컴포넌트의 렌더링 및 동작을 테스트합니다.
- **Jest Mock**을 사용하여 API 호출을 모의합니다.

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import UserForm from '../components/UserForm';

test('renders the user form and submits data', () => {
  render(<UserForm />);

  // Input fields
  const nameInput = screen.getByLabelText(/name/i);
  const emailInput = screen.getByLabelText(/email/i);

  // Fill out the form
  fireEvent.change(nameInput, { target: { value: 'John' } });
  fireEvent.change(emailInput, { target: { value: 'john@example.com' } });

  // Submit the form
  const submitButton = screen.getByRole('button', { name: /submit/i });
  fireEvent.click(submitButton);

  // Assertions
  expect(screen.getByText(/user created successfully/i)).toBeInTheDocument();
});
```

---

### **6. 테스트 실행**
- 테스트는 `npm test` 명령어로 실행합니다.
- `package.json`에 스크립트를 추가합니다:

