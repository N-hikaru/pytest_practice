# import pytest
# from bank_account import BankAccount

# @pytest.fixture
# def initial_amount():
#     return BankAccount(1000)

import os
import sys


src_path = "/Users/n-hikaru/Desktop/div/pytest_githubactions/src"

def pytest_sessionstart(session):
    """テスト全体の前処理 """
    print(f"pytest実行中に {src_path} 内のモジュールをインポートできるようにする")
    os.environ["PYTHONPATH"] = src_path
    sys.path.append(src_path)


def pytest_unconfigure(config):
    """テスト全体の後処理"""
    print("環境変数の解除")
    os.environ.pop("PYTHONPATH", None)  # 環境変数を削除
    if src_path in sys.path:
        sys.path.remove(src_path)  # sys.path から削除

