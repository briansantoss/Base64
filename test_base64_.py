from base64 import base64_enc
import pytest

test_cases = [
    ('Man', 'TWFu'),
    ("Ma", "TWE="),
    ('abdc', 'YWJkYw=='),
    ('abcdef', 'YWJjZGVm'),
    ('A'*12, 'QUFBQUFBQUFBQUFB'),
    ('1234567890', 'MTIzNDU2Nzg5MA=='),
    ('', ''),
]

@pytest.mark.parametrize('word, expected', test_cases)
def test_encode(word, expected):
    encoded = base64_enc(word)
    assert  encoded == expected, f'Error in encode_test(): {encoded}'