import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from cs4090_cicd_demo.app import add, divide, multiply, sub

def test_multiply():
    assert multiply(3, 4) == 12

def test_add():
    assert add(3, 4) == 7

def test_divide():
    assert divide(6, 3) == 2

def test_sub():
    assert sub(6, 3) == 3
