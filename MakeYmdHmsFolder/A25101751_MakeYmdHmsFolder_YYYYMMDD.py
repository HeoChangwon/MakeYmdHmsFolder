#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
연월일_시분초 형식의 폴더를 생성하는 스크립트

사용법:
    python A25101751_MakeYmdHmsFolder.py [--mode <1-6>] [--folder <경로>] [--nowait-exit]
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

# ============================================================================
# 기본 설정 (이 부분을 수정하여 기본값 변경 가능)
# ============================================================================
BASE_FILENAME_PREFIX = "A25101751_MakeYmdHmsFolder"
BASE_FILENAME_ABBR = "MYHF"
DEFAULT_MODE = 6  # 기본 폴더명 조합 방식 (6: YYYYMMDD_HHMMSS)

# 명령행 인자 없이 실행할 때 사용할 기본 인자
# 명령행 인자가 명시적으로 제공되면 이 값은 무시됩니다.
DEFAULT_COMMAND_ARGS = "--nowait-exit --mode 3"

# ============================================================================
# 메인 로직
# ============================================================================

def get_folder_name(mode):
    """mode에 따라 폴더명을 생성합니다."""
    now = datetime.now()

    folder_formats = {
        1: "%Y",                    # YYYY
        2: "%Y%m",                  # YYYYMM
        3: "%Y%m%d",                # YYYYMMDD
        4: "%Y%m%d_%H",             # YYYYMMDD_HH
        5: "%Y%m%d_%H%M",           # YYYYMMDD_HHMM
        6: "%Y%m%d_%H%M%S"          # YYYYMMDD_HHMMSS
    }

    if mode not in folder_formats:
        print(f"오류: 잘못된 mode 값입니다. (1-6 사이의 값을 사용하세요)")
        return None

    return now.strftime(folder_formats[mode])


def create_folder(target_path, folder_name):
    """폴더를 생성합니다."""
    try:
        full_path = Path(target_path) / folder_name
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"폴더가 생성되었습니다: {full_path}")
        return True
    except Exception as e:
        print(f"오류: 폴더 생성 실패 - {e}")
        return False


def main():
    """메인 함수"""
    # 명령행 인자가 제공되지 않은 경우 기본 인자 사용
    if len(sys.argv) == 1:
        sys.argv.extend(DEFAULT_COMMAND_ARGS.split())

    # 명령행 인자 파서 설정
    parser = argparse.ArgumentParser(
        description=f"{BASE_FILENAME_PREFIX} - 연월일_시분초 형식의 폴더 생성 스크립트",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
폴더명 조합 방식 (--mode):
  1: YYYY
  2: YYYYMM
  3: YYYYMMDD
  4: YYYYMMDD_HH
  5: YYYYMMDD_HHMM
  6: YYYYMMDD_HHMMSS (기본값)

사용 예시:
  python A25101751_MakeYmdHmsFolder.py
  python A25101751_MakeYmdHmsFolder.py --mode 3
  python A25101751_MakeYmdHmsFolder.py --mode 6 --folder "C:\\MyFolder"
  python A25101751_MakeYmdHmsFolder.py --mode 5 --nowait-exit
        """
    )

    parser.add_argument(
        '--mode',
        type=int,
        default=DEFAULT_MODE,
        choices=[1, 2, 3, 4, 5, 6],
        help=f'폴더명 조합 방식 (1-6, 기본값: {DEFAULT_MODE})'
    )

    parser.add_argument(
        '--folder',
        type=str,
        default='.',
        help='대상 폴더 경로 (기본값: 현재 폴더)'
    )

    parser.add_argument(
        '--nowait-exit',
        action='store_true',
        help='스크립트 종료 전에 대기하지 않기'
    )

    # 인자 파싱
    args = parser.parse_args()

    # 폴더명 생성
    folder_name = get_folder_name(args.mode)
    if folder_name is None:
        if not args.nowait_exit:
            input("\n종료하려면 Enter 키를 누르세요...")
        sys.exit(1)

    # 대상 경로 확인
    target_path = Path(args.folder).resolve()
    if not target_path.exists():
        print(f"오류: 대상 경로가 존재하지 않습니다: {target_path}")
        if not args.nowait_exit:
            input("\n종료하려면 Enter 키를 누르세요...")
        sys.exit(1)

    print(f"대상 경로: {target_path}")
    print(f"생성할 폴더명: {folder_name}")
    print(f"Mode: {args.mode}")

    # 폴더 생성
    success = create_folder(target_path, folder_name)

    # 종료 대기
    if not args.nowait_exit:
        input("\n종료하려면 Enter 키를 누르세요...")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
