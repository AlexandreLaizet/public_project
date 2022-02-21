# tests/test_lib.py
from public_project.lib import try_me

def test_distance():
    assert try_me(2, 3) == 5
