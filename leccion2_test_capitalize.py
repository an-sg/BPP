from leccion2_capitalize import capital_case
import pytest

def test_capital_case():
    assert capital_case('rubén') == 'Rubén'

def test_raise_exception_caputalize():
    with pytest.raises(TypeError):
        capital_case(9)