@echo off
chcp 65001 >nul
REM ============================================================================
REM A25101751_MakeYmdHmsFolder.bat
REM Python 스크립트에 인자를 전달하는 배치 파일
REM ============================================================================

REM 현재 배치 파일이 있는 디렉토리로 이동
cd /d "%~dp0"

REM Python 스크립트 실행
REM 아래 예시를 참고하여 필요한 옵션을 추가하세요

REM ============================================================================
REM 사용 예시:
REM ============================================================================
REM
REM 1. 기본 실행 (현재 폴더에 YYYYMMDD_HHMMSS 형식 폴더 생성):
REM    python A25101751_MakeYmdHmsFolder.py
REM
REM 2. mode 3으로 실행 (YYYYMMDD 형식):
REM    python A25101751_MakeYmdHmsFolder.py --mode 3
REM
REM 3. 특정 폴더에 생성:
REM    python A25101751_MakeYmdHmsFolder.py --mode 6 --folder "C:\MyFolder"
REM
REM 4. 종료 대기 없이 실행:
REM    python A25101751_MakeYmdHmsFolder.py --mode 5 --nowait-exit
REM
REM 5. 도움말 보기:
REM    python A25101751_MakeYmdHmsFolder.py --help
REM
REM ============================================================================

REM 아래 줄의 주석을 해제하고 원하는 옵션으로 수정하여 사용하세요
REM python A25101751_MakeYmdHmsFolder.py --mode 6

REM 기본 실행 (모든 인자를 그대로 전달)
python A25101751_MakeYmdHmsFolder.py %*

REM 배치 파일 실행 완료
