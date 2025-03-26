from base64 import base64_enc

def test_man():
    result = base64_enc("Man")
    assert "TWFu" == result

def test_empty_string():
    result = base64_enc("")
    assert "" == result