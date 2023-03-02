<div align="center">
  <h1>🖥Python-Algorithm-Study🖥</h1>
</div>
<br/>

- [Member](#Member)
- [Rule](#Rule)
- [Record](#Record)

---

## Member   
| <img src='https://avatars.githubusercontent.com/u/65546884?s=400&u=77cde868c35574004dbaa9aa3031aab36cfbde3b&v=4' width='120px' height='120px' alt='avatar'/><br/><b>[김태연](https://github.com/taeyeon0319)</b> |  <img src='https://avatars.githubusercontent.com/u/100748980?v=4' width='120px' height='120px' alt='avatar'/><br/><b>[전현정](https://github.com/hjyeeoonng)</b>  |  <img src='https://avatars.githubusercontent.com/u/95211829?v=4' width='120px' height='120px' alt='avatar'/><br/><b>[윤영서](https://github.com/sdfjkj)</b>  |  <img src='https://avatars.githubusercontent.com/u/118758007?v=4' width='120px' height='120px' alt='avatar'/><br/><b>[이수은](https://github.com/sueueue)</b>  |  <img src='https://avatars.githubusercontent.com/u/95170874?v=4' width='120px' height='120px' alt='avatar'/><br/><b>[안정민](https://github.com/102sae)</b>  |  
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: | 

---

## Rule

> [나동빈님의 '이것이 취업을 위한 코딩테스트다'](https://github.com/ndb796/python-for-coding-test)와 백준 문제들로 스터디를 진행한다.
  
- 매주 수요일 15시에 약 2-3시간 온라인 스터디를 진행한다.
- 스터디날까지 해당하는 주차의 이코테 챕터를 읽고 해당 코딩 문제를 풀어 내용을 정리해 Pull Request를 보낸다.
  - 책의 개념과 문제 풀이는 분류하여 Commit 한다.
  - Pull Request 양식을 지키지 않을 시 거절한다.
- PR 제출 마감은 당일 스터디 시작 전까지이다.
- 문제 선정은 매주 온라인 스터디 종료 후 다같이 선정하여 Readme에 등록한다.
- 이코테 완독 후 )) 백준 문제의 답은 스터디 당일날 서로의 풀이를 확인한 후에 다같이 본다.

### Naming

- 이코테 책의 경우, 유형별 폴더 아래의 자신의 닉네임으로된 폴더만 이용합니다.
- 유형별로 개념 정리와 문제 풀이는 분류하여 작성합니다.
  - **ex.** 그리디 챕터 개념정리, 문제풀이의 경우 → >📁`Greedy` -> 📁`김태연` -> 📋`Greedy.md`, 📋`Greedy_거스름돈.py`

- 백준 문제 풀이의 경우, 📁`baekjoon` 폴더 아래의 자신의 닉네임으로 된 폴더만 이용합니다.
- 📋`문제번호_문제제목.py` 으로 통일합니다. 띄어쓰기가 있으면 띄어쓰기를 제외하고 작성합니다.
  - 문제 번호와 문제 제목은 <strong>[Record](#Record)</strong>에서 확인할 수 있습니다.
  - **ex.** 백준 2606번 바이러스 → 📋`2606_바이러스.py`
  - **ex.** 백준 1260번 DFS와 BFS → 📋`1260_DFS와BFS.py`

### Pull Request

- Pull Request 제목은 `[이름] 주차`로 해주세요!
  - 스터디 1주차 펭귄 → `[김태연] 1주차`
- 자신의 닉네임으로 된 브랜치를 딴 후 자신의 닉네임 폴더에 코드를 추가한 후 Pull Request를 보냅니다.
- Pull Request 양식에 따라 작성해야 하며, 제대로 작성하지 않을 시 승인이 되지 않습니다.

### 협업방법(Upstream)

- 협업 시작하기   
  - Fork뜨기    
  - (터미널)git clone [복사한 url 붙여넣기(본인계정 url)]   
  - upstream 설정 : git remote add upstream https://github.com/taeyeon0319/Python-Algorithm-Study.git   
  - (참고*) fork한 본인의 repository([본인계정]/Python-Algorithm-Study)는 origin, 원본 repository(taeyeon0319/Python-Algorithm-Study)는 upstream이라고 한다.      
<br>

- branch 파서 작업하기   
  - 브랜치 생성 : (터미널) git branch [브랜치 이름]   
  - 프랜치 이동 : git checkout [생성한 브랜치 이름]   
  - (참고*) 브랜치 이름은 아무거나 상관없음(예시. develop, KTY, 등등)   
<br>

- 작업 후 push 하기   
   - 작업 내용 저장 : (터미널)git add .   
   - 작업 commit 이름(위 Naming규칙에 따라 작성할 것) : (터미널)git commit -m "commit이름"   
   - 작업 push : (터미널)git push origin [작업 브랜치 이름]   
   - 레포지토리 들어와서 Compare & pull request 라는 초록색 버튼 클릭 -> Create pull request눌러 등록 완료   
<br>

- 최신상태로 업데이트
   - git pull upstream main   
   (또는)
   - git fetch upstream main   
   - git merge upstream main   
---

## Record
<details markdown="1">
<summary><strong>Chapter (2023.01.17 ~ )</strong></summary>

<br/>

| 주차 | 주 | 유형 | 챕터명 | 챕터 |
| :--: | :--: | :--: | :--: | :--: | 
| 1주차 | 01.17 ~ 01.25 | Greedy & Implementation | 그리디 & 구현 | Chap3, 4, 11, 12  | 
| 2주차 | 01.26 ~ 01.31 | DFS & BFS | DFS/BFS | Chap5, 13 | 

// 미예정
| 3주차 | Sorting | 정렬 |
| 4주차 | Binary Search | 이진 탐색 |
| 5주차 | Dynamic Programming | 다이나믹 프로그래밍 |
| 6주차 | Shortest Path | 최단 경로 |
| 7주차 | Graph | 그래프 이론 |
</details>
