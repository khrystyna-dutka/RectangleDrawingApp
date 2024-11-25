import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from app.model import Rectangle

def test_rectangle_creation():
    rect = Rectangle(10, 20, "red")
    assert rect.width == 10
    assert rect.height == 20
    assert rect.color == "red"
