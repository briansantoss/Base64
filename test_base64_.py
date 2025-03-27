import base64
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

@pytest.mark.parametrize('input, expected', test_cases)
def test_encode(input, expected):
    encoded = base64.base64_encode(input)
    assert  encoded == expected, f'Error in encoding: {encoded}'

@pytest.mark.parametrize('expected, input', test_cases)
def test_decode(expected, input):
    decoded = base64.base64_decode(input)
    assert decoded == expected, f'Error in decoding: {decoded}'