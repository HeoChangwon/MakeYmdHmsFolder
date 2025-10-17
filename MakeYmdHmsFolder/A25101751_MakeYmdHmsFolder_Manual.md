# A25101751_MakeYmdHmsFolder 사용 매뉴얼

## 문서 정보
- **문서명**: A25101751_MakeYmdHmsFolder 사용 매뉴얼
- **작성일**: 2025-10-17 13:47
- **작성자**: 허창원  
- **AI 지원**: Claude Code Assistant

## 목차
1. [개요](#개요)
2. [설치 및 준비](#설치-및-준비)
3. [파일 구성](#파일-구성)
4. [사용 방법](#사용-방법)
5. [명령행 옵션](#명령행-옵션)
6. [폴더명 형식](#폴더명-형식)
7. [사용 예시](#사용-예시)
8. [설정 변경](#설정-변경)
9. [문제 해결](#문제-해결)

---

## 개요

`A25101751_MakeYmdHmsFolder`는 현재 날짜와 시간을 기반으로 한 폴더명을 자동으로 생성하는 Python 스크립트입니다.

### 주요 기능
- 6가지 날짜/시간 형식으로 폴더 생성 가능
- 명령행 인자를 통한 유연한 제어
- 한글 경로 및 공백이 포함된 경로 지원
- 원하는 위치에 폴더 생성 가능
- 종료 대기 옵션 제어 가능

### 시스템 요구사항
- Python 3.6 이상
- Windows, Linux, macOS 모두 지원

---

## 설치 및 준비

### Python 설치 확인
명령 프롬프트(cmd)나 터미널에서 다음 명령어를 실행하여 Python이 설치되어 있는지 확인합니다:

```bash
python --version
```

또는

```bash
python3 --version
```

### 파일 배치
1. `A25101751_MakeYmdHmsFolder.py` 파일을 폴더를 생성하고자 하는 위치에 복사합니다.
2. (선택사항) `A25101751_MakeYmdHmsFolder.bat` 파일도 같은 위치에 복사합니다.

---

## 파일 구성

### A25101751_MakeYmdHmsFolder.py
메인 Python 스크립트 파일입니다. 폴더 생성의 모든 로직이 포함되어 있습니다.

### A25101751_MakeYmdHmsFolder.bat
Windows 환경에서 명령행 인자를 쉽게 전달할 수 있도록 도와주는 배치 파일입니다.

---

## 사용 방법

### 방법 1: 더블클릭으로 실행 (가장 간단)

1. `A25101751_MakeYmdHmsFolder.py` 파일을 폴더를 생성하고 싶은 위치에 복사
2. 파일을 더블클릭하여 실행
3. 현재 시간 기준으로 `YYYYMMDD_HHMMSS` 형식의 폴더가 생성됩니다
4. Enter 키를 눌러 종료

### 방법 2: 배치 파일로 실행

1. `A25101751_MakeYmdHmsFolder.bat` 파일을 더블클릭
2. 또는 명령 프롬프트에서 배치 파일 실행:
   ```batch
   A25101751_MakeYmdHmsFolder.bat --mode 3
   ```

### 방법 3: 명령행에서 직접 실행

명령 프롬프트나 터미널을 열고 다음과 같이 실행:

```bash
python A25101751_MakeYmdHmsFolder.py
```

옵션과 함께 실행:

```bash
python A25101751_MakeYmdHmsFolder.py --mode 5 --folder "C:\작업폴더"
```

---

## 명령행 옵션

### --help
스크립트의 사용 방법과 옵션 설명을 표시합니다.

```bash
python A25101751_MakeYmdHmsFolder.py --help
```

### --mode <1-6>
폴더명 형식을 지정합니다. 1부터 6까지의 값을 사용할 수 있습니다.

- **타입**: 정수 (1, 2, 3, 4, 5, 6)
- **기본값**: 6
- **필수 여부**: 선택사항

```bash
python A25101751_MakeYmdHmsFolder.py --mode 3
```

### --folder <경로>
폴더를 생성할 대상 경로를 지정합니다.

- **타입**: 문자열 (경로)
- **기본값**: 현재 폴더 (.)
- **필수 여부**: 선택사항

```bash
python A25101751_MakeYmdHmsFolder.py --folder "D:\MyProjects"
```

경로에 공백이 포함된 경우 반드시 따옴표로 감싸주세요:

```bash
python A25101751_MakeYmdHmsFolder.py --folder "D:\My Documents\Projects"
```

### --nowait-exit
스크립트 종료 전에 사용자 입력을 기다리지 않고 바로 종료합니다.

- **타입**: 플래그 (값 없음)
- **기본값**: False (대기함)
- **필수 여부**: 선택사항

```bash
python A25101751_MakeYmdHmsFolder.py --nowait-exit
```

이 옵션은 배치 파일이나 자동화 스크립트에서 유용합니다.

---

## 폴더명 형식

### Mode 1: YYYY
연도만 표시합니다.

**예시**: `2025`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 1
```

### Mode 2: YYYYMM
연도와 월을 표시합니다.

**예시**: `202510`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 2
```

### Mode 3: YYYYMMDD
연도, 월, 일을 표시합니다.

**예시**: `20251017`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 3
```

### Mode 4: YYYYMMDD_HH
연도, 월, 일, 시간을 표시합니다.

**예시**: `20251017_14`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 4
```

### Mode 5: YYYYMMDD_HHMM
연도, 월, 일, 시간, 분을 표시합니다.

**예시**: `20251017_1430`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 5
```

### Mode 6: YYYYMMDD_HHMMSS (기본값)
연도, 월, 일, 시간, 분, 초를 모두 표시합니다.

**예시**: `20251017_143052`

```bash
python A25101751_MakeYmdHmsFolder.py --mode 6
```

또는 mode를 생략하면 자동으로 mode 6이 적용됩니다:

```bash
python A25101751_MakeYmdHmsFolder.py
```

---

## 사용 예시

### 예시 1: 현재 폴더에 기본 형식으로 폴더 생성

```bash
python A25101751_MakeYmdHmsFolder.py
```

**결과**: 현재 폴더에 `20251017_143052` 같은 폴더가 생성됩니다.

---

### 예시 2: 날짜만 포함된 폴더 생성

```bash
python A25101751_MakeYmdHmsFolder.py --mode 3
```

**결과**: 현재 폴더에 `20251017` 폴더가 생성됩니다.

---

### 예시 3: 특정 폴더에 생성

```bash
python A25101751_MakeYmdHmsFolder.py --mode 5 --folder "C:\Projects"
```

**결과**: `C:\Projects` 폴더 안에 `20251017_1430` 폴더가 생성됩니다.

---

### 예시 4: 한글 경로에 폴더 생성

```bash
python A25101751_MakeYmdHmsFolder.py --mode 3 --folder "D:\내문서\프로젝트"
```

**결과**: `D:\내문서\프로젝트` 폴더 안에 `20251017` 폴더가 생성됩니다.

---

### 예시 5: 대기 없이 즉시 종료

```bash
python A25101751_MakeYmdHmsFolder.py --mode 6 --nowait-exit
```

**결과**: 폴더를 생성한 후 Enter 키 입력을 기다리지 않고 바로 종료됩니다.

---

### 예시 6: 여러 옵션 조합

```bash
python A25101751_MakeYmdHmsFolder.py --mode 4 --folder "D:\Backup Files" --nowait-exit
```

**결과**: `D:\Backup Files` 폴더 안에 `20251017_14` 형식의 폴더가 생성되고 즉시 종료됩니다.

---

### 예시 7: 배치 파일로 실행

**A25101751_MakeYmdHmsFolder.bat** 파일을 편집:

```batch
python A25101751_MakeYmdHmsFolder.py --mode 3 --nowait-exit
```

배치 파일을 더블클릭하면 자동으로 위 명령이 실행됩니다.

---

### 예시 8: 자동화 시나리오

매일 백업 폴더를 생성하는 스케줄러에서 사용:

```batch
@echo off
python A25101751_MakeYmdHmsFolder.py --mode 3 --folder "D:\DailyBackup" --nowait-exit
xcopy "D:\SourceData\*.*" "D:\DailyBackup\20251017\" /E /I /Y
```

---

## 설정 변경

스크립트 파일의 상단에 있는 설정 부분을 편집하여 기본값을 변경할 수 있습니다.

### 편집 방법

1. `A25101751_MakeYmdHmsFolder.py` 파일을 텍스트 편집기로 엽니다.
2. 파일 상단의 다음 부분을 찾습니다:

```python
# ============================================================================
# 기본 설정 (이 부분을 수정하여 기본값 변경 가능)
# ============================================================================
BASE_FILENAME_PREFIX = "A25101751_MakeYmdHmsFolder"
BASE_FILENAME_ABBR = "MYHF"
DEFAULT_MODE = 6  # 기본 폴더명 조합 방식 (6: YYYYMMDD_HHMMSS)
```

3. 원하는 값으로 변경합니다.

### 설정 항목 설명

#### BASE_FILENAME_PREFIX
- **설명**: 파일명의 기본 접두어
- **기본값**: `"A25101751_MakeYmdHmsFolder"`
- **용도**: 스크립트 파일명 식별

#### BASE_FILENAME_ABBR
- **설명**: 결과 파일 및 로그 파일명의 약어
- **기본값**: `"MYHF"`
- **용도**: 로그 파일명 등에 사용 (현재는 로그 파일을 생성하지 않음)

#### DEFAULT_MODE
- **설명**: 기본 폴더명 조합 방식
- **기본값**: `6` (YYYYMMDD_HHMMSS)
- **가능한 값**: 1, 2, 3, 4, 5, 6
- **용도**: --mode 옵션을 생략했을 때 사용되는 기본 형식

### 예시: 기본 mode를 3으로 변경

```python
DEFAULT_MODE = 3  # 기본 폴더명 조합 방식을 YYYYMMDD로 변경
```

변경 후 저장하면 이후부터는 --mode 옵션 없이 실행해도 YYYYMMDD 형식으로 폴더가 생성됩니다.

---

## 문제 해결

### Python이 인식되지 않습니다

**증상**:
```
'python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.
```

**해결 방법**:
1. Python이 설치되어 있는지 확인합니다.
2. `python3` 명령어를 대신 사용해봅니다:
   ```bash
   python3 A25101751_MakeYmdHmsFolder.py
   ```
3. Python을 PATH에 추가하거나 전체 경로로 실행합니다:
   ```bash
   C:\Python39\python.exe A25101751_MakeYmdHmsFolder.py
   ```

---

### 대상 경로가 존재하지 않습니다

**증상**:
```
오류: 대상 경로가 존재하지 않습니다: D:\NonExistent\Folder
```

**해결 방법**:
1. --folder 옵션에 지정한 경로가 실제로 존재하는지 확인합니다.
2. 경로에 오타가 없는지 확인합니다.
3. 경로를 먼저 생성한 후 스크립트를 실행합니다.

---

### 한글이 깨져서 보입니다

**해결 방법 (Windows)**:
1. 명령 프롬프트의 인코딩을 UTF-8로 변경:
   ```batch
   chcp 65001
   ```
2. 배치 파일에서는 자동으로 처리됩니다.

---

### 폴더가 이미 존재합니다

**동작**:
스크립트는 이미 폴더가 존재하더라도 오류를 발생시키지 않습니다. 기존 폴더를 그대로 유지하고 성공 메시지를 표시합니다.

**참고**:
같은 초에 두 번 실행하면 같은 폴더명이 생성되므로 중복될 수 있습니다. Mode 6 (YYYYMMDD_HHMMSS)을 사용하면 이러한 충돌을 최소화할 수 있습니다.

---

### 권한 오류

**증상**:
```
오류: 폴더 생성 실패 - [Errno 13] Permission denied
```

**해결 방법**:
1. 대상 폴더에 쓰기 권한이 있는지 확인합니다.
2. 관리자 권한으로 명령 프롬프트를 실행합니다.
3. 다른 위치에 폴더를 생성해봅니다.

---

## 라이선스 및 저작권

이 스크립트는 사용자의 요구사항에 맞게 자유롭게 수정하여 사용할 수 있습니다.

---

## 버전 정보

- **버전**: 1.0
- **최초 작성일**: 2025-10-17
- **Python 버전**: Python 3.6 이상

---

## 문의 및 지원

스크립트 사용 중 문제가 발생하거나 개선 사항이 있으면 문의해주시기 바랍니다.
