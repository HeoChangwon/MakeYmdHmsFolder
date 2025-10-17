# A25101751_MakeYmdHmsFolder - Quick Reference v01

> 날짜/시간 기반 폴더를 자동 생성하는 Python 스크립트 프로젝트

**최종 업데이트**: 2025-10-17 13:55  
**버전**: 1.0  
**상태**: 개발 완료  
**작성자**: 허창원  
**AI 지원**: Claude Code Assistant


---

## 프로젝트 개요

현재 시스템 날짜/시간을 기반으로 YYYYMMDD_HHMMSS 형식의 폴더를 자동 생성하는 Python 스크립트입니다.

### 핵심 기능
- ✅ 6가지 날짜/시간 형식 지원 (YYYY ~ YYYYMMDD_HHMMSS)
- ✅ 명령행 옵션으로 유연한 제어
- ✅ 한글 경로 및 공백 포함 경로 지원
- ✅ Windows 배치 파일 제공
- ✅ 사용자 정의 가능한 기본 설정

---

## 프로젝트 구조

```
D:\Work_Claude\2025\10\A25101751_MakeYmdHmsFolder\
├── MakeYmdHmsFolder\                              # 메인 프로그램 폴더
│   ├── A25101751_MakeYmdHmsFolder.py              # Python 스크립트
│   ├── A25101751_MakeYmdHmsFolder.bat             # Batch 파일
│   ├── A25101751_MakeYmdHmsFolder_Manual.md       # 상세 매뉴얼
│   └── A25101751_MakeYmdHmsFolder_Simple_manual.md # 간단 매뉴얼
│
└── Documents\                                      # 문서 폴더
    ├── 2025\10\                                    # 작업 내역
    │   └── 20251017_1354_MYHF_Work_list.md        # 작업 내역서
    └── Project_overview\                           # 프로젝트 개요
        └── 20251017_1355_MYHF_Quick_Reference_v01.md # 이 파일
```

---

## 핵심 파일

### 1. A25101751_MakeYmdHmsFolder.py
**경로**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder.py`

메인 Python 스크립트로 모든 로직을 포함합니다.

**핵심 코드 위치**:
- 라인 9-12: 사용자 정의 가능한 기본 설정
- 라인 18-34: 폴더명 생성 함수 (`get_folder_name`)
- 라인 37-47: 폴더 생성 함수 (`create_folder`)
- 라인 50-122: 메인 함수 (명령행 인자 처리 및 실행)

**주요 설정값**:
```python
BASE_FILENAME_PREFIX = "A25101751_MakeYmdHmsFolder"
BASE_FILENAME_ABBR = "MYHF"
DEFAULT_MODE = 6  # 기본: YYYYMMDD_HHMMSS
```

### 2. A25101751_MakeYmdHmsFolder.bat
**경로**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder.bat`

Windows 환경에서 Python 스크립트를 쉽게 실행하기 위한 배치 파일입니다.

**핵심 기능**:
- UTF-8 인코딩 설정 (`chcp 65001`)
- 스크립트 디렉토리로 자동 이동
- 모든 명령행 인자를 Python 스크립트로 전달

---

## 빠른 사용법

### 가장 간단한 방법
```bash
# Python 파일을 원하는 폴더에 복사 후 더블클릭
# → 현재 시간 기준 폴더 생성 (예: 20251017_143052)
```

### 명령행 사용
```bash
# 기본 실행
python A25101751_MakeYmdHmsFolder.py

# 날짜만 (YYYYMMDD)
python A25101751_MakeYmdHmsFolder.py --mode 3

# 특정 폴더에 생성
python A25101751_MakeYmdHmsFolder.py --folder "C:\Projects"

# 대기 없이 종료
python A25101751_MakeYmdHmsFolder.py --nowait-exit

# 여러 옵션 조합
python A25101751_MakeYmdHmsFolder.py --mode 5 --folder "D:\Backup" --nowait-exit
```

---

## 폴더명 형식 (Mode)

| Mode | 형식 | 예시 | 사용 시나리오 |
|------|------|------|--------------|
| 1 | YYYY | `2025` | 연간 백업 |
| 2 | YYYYMM | `202510` | 월간 백업 |
| 3 | YYYYMMDD | `20251017` | **일일 백업** (추천) |
| 4 | YYYYMMDD_HH | `20251017_14` | 시간별 백업 |
| 5 | YYYYMMDD_HHMM | `20251017_1430` | 분 단위 백업 |
| 6 | YYYYMMDD_HHMMSS | `20251017_143052` | **기본값, 초 단위** |

---

## 명령행 옵션

### 필수 옵션 없음 (모두 선택사항)

| 옵션 | 설명 | 기본값 | 예시 |
|------|------|--------|------|
| `--mode <1-6>` | 폴더명 형식 지정 | 6 | `--mode 3` |
| `--folder <경로>` | 생성 위치 지정 | 현재 폴더 | `--folder "C:\Projects"` |
| `--nowait-exit` | 즉시 종료 | 대기함 | `--nowait-exit` |
| `--help` | 도움말 표시 | - | `--help` |

---

## 기술 스펙

### 시스템 요구사항
- **Python**: 3.6 이상
- **OS**: Windows, Linux, macOS
- **외부 패키지**: 불필요 (표준 라이브러리만 사용)

### 사용된 Python 모듈
| 모듈 | 용도 |
|------|------|
| `os` | 운영체제 인터페이스 |
| `sys` | 시스템 파라미터 및 종료 코드 |
| `argparse` | 명령행 인자 파싱 |
| `datetime` | 날짜/시간 처리 |
| `pathlib` | 크로스 플랫폼 경로 처리 |

### 인코딩
- **Python 스크립트**: UTF-8 (`# -*- coding: utf-8 -*-`)
- **Batch 파일**: UTF-8 (`chcp 65001`)
- **한글 경로**: 완벽 지원

---

## 주요 기능 상세

### 1. 폴더명 생성 로직
```python
def get_folder_name(mode):
    now = datetime.now()
    folder_formats = {
        1: "%Y",                    # YYYY
        2: "%Y%m",                  # YYYYMM
        3: "%Y%m%d",                # YYYYMMDD
        4: "%Y%m%d_%H",             # YYYYMMDD_HH
        5: "%Y%m%d_%H%M",           # YYYYMMDD_HHMM
        6: "%Y%m%d_%H%M%S"          # YYYYMMDD_HHMMSS
    }
    return now.strftime(folder_formats[mode])
```

### 2. 폴더 생성 로직
```python
def create_folder(target_path, folder_name):
    full_path = Path(target_path) / folder_name
    full_path.mkdir(parents=True, exist_ok=True)
    # exist_ok=True → 이미 존재해도 오류 없음
```

### 3. 명령행 인자 파싱
- `argparse` 모듈 사용
- 표준 CLI 규칙 준수
- 상세한 도움말 제공

### 4. 에러 처리
- 잘못된 mode 값 검증
- 경로 존재 여부 확인
- 폴더 생성 실패 예외 처리
- 사용자 친화적 오류 메시지

---

## 사용 시나리오

### 시나리오 1: 일일 백업 폴더
```bash
# 매일 실행하여 날짜별 백업 폴더 생성
python A25101751_MakeYmdHmsFolder.py --mode 3 --folder "D:\Backup"
# 결과: D:\Backup\20251017\
```

### 시나리오 2: 프로젝트 작업 폴더
```bash
# 새 프로젝트 시작 시 타임스탬프 폴더 생성
python A25101751_MakeYmdHmsFolder.py --mode 6 --folder "D:\Projects"
# 결과: D:\Projects\20251017_143052\
```

### 시나리오 3: 로그 폴더 자동 생성
```bash
# 자동화 스크립트에서 사용
python A25101751_MakeYmdHmsFolder.py --mode 5 --folder "D:\Logs" --nowait-exit
# 결과: D:\Logs\20251017_1430\
```

### 시나리오 4: 더블클릭으로 빠른 폴더 생성
1. Python 파일을 자주 사용하는 폴더에 복사
2. 필요할 때마다 더블클릭
3. 현재 시간 기준 폴더가 즉시 생성됨

---

## 문서 참조

### 상세 매뉴얼
**파일**: `A25101751_MakeYmdHmsFolder_Manual.md`
- 전체 기능 상세 설명
- 8가지 사용 예시
- 설정 변경 방법
- 문제 해결 가이드

### 간단 매뉴얼
**파일**: `A25101751_MakeYmdHmsFolder_Simple_manual.md`
- 빠른 시작 가이드
- 명령어 요약 테이블
- 자주 사용하는 명령 모음

### 작업 내역서
**파일**: `Documents\2025\10\20251017_1354_MYHF_Work_list.md`
- 전체 개발 과정
- 요구사항 충족 여부
- 테스트 시나리오
- 향후 개선 방향

---

## 커스터마이징 가이드

### 기본 Mode 변경
스크립트 상단의 `DEFAULT_MODE` 값을 변경하세요.

```python
# 기본값을 YYYYMMDD로 변경
DEFAULT_MODE = 3
```

### 기본 문자열 변경
프로젝트명이 변경된 경우 다음 값을 수정하세요.

```python
BASE_FILENAME_PREFIX = "NewProjectName"
BASE_FILENAME_ABBR = "NPN"
```

### 배치 파일 자동 실행 설정
`A25101751_MakeYmdHmsFolder.bat` 파일을 편집하여 자주 사용하는 옵션을 설정하세요.

```batch
REM 아래 줄의 주석 해제 후 사용
python A25101751_MakeYmdHmsFolder.py --mode 3 --nowait-exit
```

---

## 문제 해결 치트시트

| 문제 | 해결 방법 |
|------|----------|
| Python 인식 안됨 | `python3` 사용 또는 Python 재설치 |
| 한글 깨짐 (Windows) | `chcp 65001` 실행 후 재시도 |
| 경로 없음 오류 | 대상 폴더가 존재하는지 확인 |
| 권한 오류 | 관리자 권한으로 실행 |
| 폴더 이미 존재 | 정상 동작 (오류 아님) |

---

## 자주 사용하는 명령어 모음

```bash
# 날짜 폴더 (가장 많이 사용)
python A25101751_MakeYmdHmsFolder.py --mode 3

# 특정 위치에 날짜 폴더
python A25101751_MakeYmdHmsFolder.py --mode 3 --folder "D:\Backup"

# 자동화용 (대기 없음)
python A25101751_MakeYmdHmsFolder.py --mode 3 --nowait-exit

# 초 단위 폴더 (중복 방지)
python A25101751_MakeYmdHmsFolder.py --mode 6

# 도움말
python A25101751_MakeYmdHmsFolder.py --help
```

---

## 개발 히스토리

### v1.0 (2025-10-17)
- ✅ 초기 개발 완료
- ✅ 6가지 폴더명 형식 구현
- ✅ 명령행 옵션 4개 구현
- ✅ 한글 경로 지원
- ✅ Batch 파일 제공
- ✅ 상세 매뉴얼 작성
- ✅ 간단 매뉴얼 작성

### 향후 계획
- GUI 버전 개발 (tkinter)
- 설정 파일 지원 (.ini, .json)
- 폴더 생성 후 자동으로 열기 옵션
- 다국어 지원 (영어)
- 생성 이력 로그 (선택 옵션)

---

## 주요 레퍼런스

### Python 공식 문서
- [argparse](https://docs.python.org/3/library/argparse.html) - 명령행 인자 파싱
- [datetime](https://docs.python.org/3/library/datetime.html) - 날짜/시간 처리
- [pathlib](https://docs.python.org/3/library/pathlib.html) - 경로 처리

### 관련 파일
- **메인 스크립트**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder.py`
- **배치 파일**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder.bat`
- **상세 매뉴얼**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder_Manual.md`
- **간단 매뉴얼**: `MakeYmdHmsFolder\A25101751_MakeYmdHmsFolder_Simple_manual.md`

---

## 요약 체크리스트

새로운 Chat 시작 시 다음을 확인하세요:

- [ ] 프로젝트 목적: 날짜/시간 기반 폴더 자동 생성
- [ ] 메인 파일: `A25101751_MakeYmdHmsFolder.py`
- [ ] 기본 Mode: 6 (YYYYMMDD_HHMMSS)
- [ ] 주요 옵션: `--mode`, `--folder`, `--nowait-exit`, `--help`
- [ ] 한글 경로: 지원함
- [ ] 외부 패키지: 불필요
- [ ] 문서: 상세 매뉴얼, 간단 매뉴얼 제공
- [ ] 상태: 개발 완료, 즉시 사용 가능

---

**작성자**: Claude Code  
**문서 타입**: Quick Reference  
**버전**: v01  
**다음 버전 예정**: 사용자 피드백 반영 후 v02 작성 예정
