# Think of a fixture as a “setup helper” 
# — something that prepares what your test needs before running it.

import pytest

@pytest.fixture
def PreWork():
     print("browser instance")

def test_PostWork(PreWork):
     print("this is first test")

def test_Work(PostWork):
     print("this is second test")     