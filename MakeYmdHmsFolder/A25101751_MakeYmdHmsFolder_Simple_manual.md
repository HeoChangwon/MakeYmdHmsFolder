# A25101751_MakeYmdHmsFolder 간단 매뉴얼

## 문서 정보
- **문서명**: A25101751_MakeYmdHmsFolder 간단 매뉴얼
- **작성일**: 2025-10-17 13:48
- **작성자**: 허창원  
- **AI 지원**: Claude Code Assistant

## 빠른 시작

### 1. 가장 간단한 사용법
Python 파일을 원하는 폴더에 복사하고 **더블클릭**하면 끝!

→ 현재 시간 기준 `20251017_143052` 같은 폴더가 생성됩니다.

---

## 폴더명 형식 (Mode)

| Mode | 형식 | 예시 |
|------|------|------|
| 1 | YYYY | `2025` |
| 2 | YYYYMM | `202510` |
| 3 | YYYYMMDD | `20251017` |
| 4 | YYYYMMDD_HH | `20251017_14` |
| 5 | YYYYMMDD_HHMM | `20251017_1430` |
| **6** | **YYYYMMDD_HHMMSS** | `20251017_143052` **(기본값)** |

---

## 명령행 옵션

### --mode <1-6>
폴더명 형식 지정

```bash
python A25101751_MakeYmdHmsFolder.py --mode 3
```

### --folder <경로>
생성할 위치 지정 (기본: 현재 폴더)

```bash
python A25101751_MakeYmdHmsFolder.py --folder "D:\MyFolder"
```

### --nowait-exit
종료 시 대기하지 않음

```bash
python A25101751_MakeYmdHmsFolder.py --nowait-exit
```

### --help
도움말 보기

```bash
python A25101751_MakeYmdHmsFolder.py --help
```

---

## 자주 사용하는 명령어

### 날짜만 포함된 폴더 생성
```bash
python A25101751_MakeYmdHmsFolder.py --mode 3
```
→ `20251017` 폴더 생성

### 특정 위치에 폴더 생성
```bash
python A25101751_MakeYmdHmsFolder.py --folder "C:\Projects"
```
→ `C:\Projects\20251017_143052` 폴더 생성

### 날짜+시분 형식으로 생성
```bash
python A25101751_MakeYmdHmsFolder.py --mode 5
```
→ `20251017_1430` 폴더 생성

### 한글 경로에 생성
```bash
python A25101751_MakeYmdHmsFolder.py --folder "D:\내문서\프로젝트"
```
→ 한글 경로 지원

### 여러 옵션 조합
```bash
python A25101751_MakeYmdHmsFolder.py --mode 3 --folder "D:\Backup" --nowait-exit
```
→ `D:\Backup\20251017` 폴더 생성 후 즉시 종료

---

## 배치 파일 사용법

### 1. 기본 사용
`A25101751_MakeYmdHmsFolder.bat` 더블클릭

### 2. 명령행 인자 전달
```batch
A25101751_MakeYmdHmsFolder.bat --mode 3
```

### 3. 배치 파일 편집하여 자주 쓰는 명령 설정
`A25101751_MakeYmdHmsFolder.bat` 파일을 열어서 다음 부분 수정:

```batch
REM 원하는 옵션으로 수정
python A25101751_MakeYmdHmsFolder.py --mode 3 --nowait-exit
```

---

## 기본값 변경하기

`A25101751_MakeYmdHmsFolder.py` 파일 상단의 설정 부분 편집:

```python
# ============================================================================
# 기본 설정 (이 부분을 수정하여 기본값 변경 가능)
# ============================================================================
BASE_FILENAME_PREFIX = "A25101751_MakeYmdHmsFolder"
BASE_FILENAME_ABBR = "MYHF"
DEFAULT_MODE = 6  # 원하는 mode로 변경 (1-6)
```

**예시**: 기본 mode를 3 (YYYYMMDD)으로 변경
```python
DEFAULT_MODE = 3
```

---

## 문제 해결

### Python이 없다고 나올 때
```bash
python3 A25101751_MakeYmdHmsFolder.py
```
또는 Python 재설치

### 한글이 깨질 때 (Windows)
```batch
chcp 65001
python A25101751_MakeYmdHmsFolder.py
```

### 경로가 없다고 나올 때
--folder 옵션에 지정한 폴더가 실제로 존재하는지 확인

---

## 요약

| 용도 | 명령어 |
|------|--------|
| 기본 실행 | `python A25101751_MakeYmdHmsFolder.py` |
| 날짜만 | `python A25101751_MakeYmdHmsFolder.py --mode 3` |
| 특정 위치 | `python A25101751_MakeYmdHmsFolder.py --folder "경로"` |
| 대기 없이 종료 | `python A25101751_MakeYmdHmsFolder.py --nowait-exit` |
| 도움말 | `python A25101751_MakeYmdHmsFolder.py --help` |

---

**TIP**: 자주 사용하는 명령은 배치 파일에 저장해두고 더블클릭으로 사용하세요!
