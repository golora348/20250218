# Flow Free Solver GUI
`Limbus Company File Mapper`는 `catalog_S1.json` 파일에 정의된 URL 정보를 이용하여 Limbus Company Client의 `__data` 파일들을 사용자가 지정한 위치에 구조화하여 복사하는 Python 스크립트입니다.

<BR>

## 📅 마지막 정상 작동 확인 날짜 및 버전
- **DATE**: 2024-02-18

<BR>

## 🔍 주요 기능
- **자동/수동 경로 지정**  
  `__data` 파일 검색 경로와 `catalog_S1.json` 파일 경로를 자동 또는 수동으로 지정하는 옵션 제공 <BR> <BR>

- **URL 기반 파일 매핑**  
  `catalog_S1.json` 파일 내 URL 정보를 활용하여 `__data` 파일과 매칭 및 복사 작업 수행 <BR> <BR>

- **자동 폴더 생성 및 파일 복사**  
  URL 구조를 기반으로 저장 경로에 자동 폴더 생성 및 `__data` 파일 복사 기능 제공

<BR>

## 💾 다운로드 <BR>
| Program                                | URL                                                | 필수여부 | 비고                                                                                           |
|----------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------------------------------------|
| `Python`            | [Download](https://www.python.org/downloads/release/python-390/)   | 필수     | ◼ Python Script 동작, 파이썬 3.9.0 버전 또는 그 이상 사용 가능 |
| `반디집`             | [Download](https://kr.bandisoft.com/bandizip/)   | 필수     | ◼ (* 다른 압축 프로그램 사용 가능) |

<BR>

## 🛠️ 설치

1. Python 을 설치합니다. <BR> <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR> <BR>

2. **(필수) pycosat Package 설치** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install pycosat` <BR>
or <BR>
`python -m pip install pycosat` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install pycosat --user` <BR>
or <BR>
`python -m pip install pycosat --user` <BR>

<BR>

## ⏩ 사용 방법

### 1. **스크립트 실행**

`Flow Free Solver GUI.py` 를 실행합니다. <BR> <BR>

### 2. **`__data` 파일 검색 경로 지정**  

- 자동 (1번 선택):
  - 스크립트가 기본 경로 (C:\Users\(Your_User_Name)\AppData\LocalLow\Unity\ProjectMoon_LimbusCompany)에서 `__data` 파일을 자동으로 검색합니다. <BR> <BR>
- 수동 (2번 선택):
  - 파일 선택 대화 상자가 열리면, Limbus Company Client의 `__data 파일`이 포함된 최상위 폴더를 직접 선택합니다.

<BR>

### 3. **`catalog_S1.json` 파일 경로 지정**  

- 자동 (1번 선택):
  - 스크립트가 기본 경로 (C:\Users\(Your_User_Name)\AppData\LocalLow\ProjectMoon\LimbusCompany)에서 `catalog_S1.json` 파일을 자동으로 검색합니다. <BR> <BR>
- 수동 (2번 선택):
  - 파일 선택 대화 상자가 열리면, `catalog_S1.json` 파일을 직접 선택합니다.

<BR>

### 4. **처리된 파일 저장 경로 지정**

디렉토리 선택 대화 상자가 열리면, `__data` 파일들을 복사하여 저장할 폴더를 선택합니다.

<BR>

### 5. **처리된 파일 확인**

처리된 파일 저장 경로로 이동하여 처리 된 파일을 확인합니다.

<BR>

## ⚖️ 라이센스
이 프로젝트는 [MIT License](LICENSE)에 따라 라이선스가 부여됩니다.
