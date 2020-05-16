# Faker

## **내용**

- 여러 장의 사진과 동영상을 입력받아 동영상에 얼굴을 합성하는 딥페이크 동영상을 제작해주는 웹 사이트
- 폭력이나 성인물 합성을 방지하기 위해 AI를 통한 영상 등급 검열
- OOO을 통한 프론트엔드 제작 및 Spring Boot를 통해 웹서버를 제작하고 Flask를 통해 AI서버를 따로 제작하는 Restful서버 예정 DB NoSQL 이하연이 하고싶다고함(//나는 아님)
- 기간 2020.05.16 ~ (약 2달?) 이 기간은 아마 밀릴 예정입니다.

## 나중에 하고싶은거

- NoSQL 나중에 시간되면

## 페이지

- 로그인 페이지

- 메인화면(다른 동영상?)

- 합성하기

  - 사진에 합성하기 , 동상영상에 합성하기
  - 1. src 사진, 2. des 사진 /

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/845253ec-0368-4928-8a54-85e84ce7c596/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/845253ec-0368-4928-8a54-85e84ce7c596/Untitled.png)

  - 사진 입력하면 사진에 나온 얼굴들 인식해서, 얼굴 선택 할 수 있도록 함 (눈코입잘 나온 사진으로 입력할 수 있도록 유도)
    - 얼굴 사진을 base64 배열로
  - 원본사진을 입력하면백에서 인식할 수 없거나, 처리하기에 부적절한 이미지(판단은 AI가) 라면 다시 입력하도록 유도 (정면이 나온 사진을 입력해주세요)
  - 동영상합성
    - 최대 15초짜리 입력
    - 로딩화면 출력
    - 동영상 검열.. (선정성 폭력성)
      - 선정성 폭력성이 높으면 경고창
    - 1. src 사진은 3장..?? 2. des 동영상 거기서 얼굴 찾아줘서 그 얼굴 선택시 합성?
  
- 내 동영상/ 이미지 관리 페이지 (게시물 페이지)

  - 날짜별, 조회수별 , 합성된 동영상 보여주기, 코멘트, 제목, 좋아요 /
    - 나중에 댓글~
  - CRD

## 프론트엔드

- https://trend.io/
- Vue

## 벡엔드

- Spring Boot 예정
- AI 서버는 플라스크 예정

## 데이터베이스

MySQL

## 일정

- 1주차(16,17일)
  - 기획, git만들기, 환경설정
  - vue 기본 화면 구성(page만들고 레이아웃설정)
  - DB설계(User, Boarder(좋아요 어캐할지)- FK : user, image, 내이미지 - FK - user)
- 2주차(23,24일)
  - Spring 설치, 구조 설계??
  - vue, spring - 로그인/ jwt
  - Flask로 FaceRecognition을 통한 얼굴 위치값 반환 후 그 얼굴 이미지 base64로 전달
- 3주차(30,31일)
  - 합성하기 페이지
  - AI GAN 학습 및 DATASET 활용
- 4주차(6,7일)
  - 합성하기 페이지
  - AI GAN 학습 및 DATASET 활용
- 5주차(13,14일)
  - 메인페이지
  - Deep Fake 제작
- 6주차(20,21일)
  - 내 게시물 관리 페이지
  - Deep Fake 제작
- 7주차(27,28일)
  - 내 게시물 관리페이지
  - 벡 미흡한 부분 붙이기
- 8주차(4,5일)

[감동이야](https://www.notion.so/507bd416c4734bf89913857d729d652c)

### 폴더구조

```jsx
── ai
── backend
── frontend
── study
	├── jsp
		├── readme.md
  ├── hyl

'''복붙용 예시
    ├── manage.py
    ├── api
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── management
    │   │   ├── commands
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── backend
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## **커밋 메시지 스타일**

[링크](https://siyoon210.tistory.com/56)

```
type: subject

body(옵션)

footer(옵션)
```

- type : 어떤 의도로 커밋했는지를 type에 명시합니다. 자세한 사항은 아래서 설명하겠습니다.
- subject : 최대 50글자가 넘지 않도록 하고 마침표는 찍지 않습니다. 영문으로 표기하는 경우 동사(원형)을 가장 앞에 두고 첫글자는 대문자로 표기합니다.
- body: 긴 설명이 필요한 경우에 작성합니다. **어떻게** 했는지가 아니라, **무엇**을 **왜** 했는지 작성합니다. 최대 75글자를 넘기지 않도록 합니다.
- footer : issue tracker ID를 명시하고 싶은 경우에 작성합니다.

### **타입 type**

- **feat** : 새로운 기능 추가
- **fix** : 버그 수정
- **docs** : 문서의 수정
- **style** : (코드의 수정 없이) 스타일(style)만 변경(들여쓰기 같은 포맷이나 세미콜론을 빼먹은 경우)
- **refactor** : 코드를 리펙토링
- **test** : Test 관련한 코드의 추가, 수정
- **chore** : (코드의 수정 없이) 설정을 변경

이런식으로 했으면 좋겠다,,,

## **Git Ignore**

[링크](https://www.gitignore.io/)

여기보고 flask, vue, vuejs, python으로 추가