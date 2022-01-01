import pytest
from calculator_model import *


@pytest.fixture
def calc() -> CalculatorModel:
    return CalculatorModel()


def type_in(calc: CalculatorModel, seq: str) -> None:
    for c in seq:
        calc.type_in(c)


def test_init(calc: CalculatorModel) -> None:
    assert calc.get_display() == "0"


def test_init_then_typing(calc: CalculatorModel) -> None:
    calc.type_in("1")
    assert calc.get_display() == "1"


def test_type_0(calc: CalculatorModel) -> None:
    calc.type_in("0")
    assert calc.get_display() == "0"
    calc.type_in("0")
    assert calc.get_display() == "0"


def test_type_10(calc: CalculatorModel) -> None:
    calc.type_in("1")
    calc.type_in("0")
    assert calc.get_display() == "10"


def test_type_decimal(calc: CalculatorModel) -> None:
    type_in(calc, "1.1")
    assert calc.get_display() == "1.1"


def test_type_decimal_no_zero(calc: CalculatorModel) -> None:
    type_in(calc, ".12")
    assert calc.get_display() == "0.12"


def test_addition(calc: CalculatorModel) -> None:
    type_in(calc, "1")
    calc.type_in("+")
    assert calc.get_display() == "1"
    type_in(calc, "2")
    assert calc.get_display() == "2"
    calc.type_in("=")
    assert calc.get_display() == "3"


def test_multiplication(calc: CalculatorModel) -> None:
    type_in(calc, "2")
    calc.type_in("*")
    assert calc.get_display() == "2"
    type_in(calc, "3")
    assert calc.get_display() == "3"
    calc.type_in("=")
    assert calc.get_display() == "6"


def test_equals_alone(calc: CalculatorModel) -> None:
    calc.type_in("=")
    assert calc.get_display() == "0"


def test_long_add(calc: CalculatorModel) -> None:
    type_in(calc, "123+345=")
    assert calc.get_display() == "468"


def test_number_then_two_equals(calc: CalculatorModel) -> None:
    type_in(calc, "111==")
    assert calc.get_display() == "111"


def test_add_then_several_equals(calc: CalculatorModel) -> None:
    type_in(calc, "2+2=")
    assert calc.get_display() == "4"
    type_in(calc, "=")
    assert calc.get_display() == "6"
    type_in(calc, "=")
    assert calc.get_display() == "8"


def test_mult_then_several_equals(calc: CalculatorModel) -> None:
    type_in(calc, "2*2=")
    assert calc.get_display() == "4"
    type_in(calc, "=")
    assert calc.get_display() == "8"
    type_in(calc, "=")
    assert calc.get_display() == "16"


def test_two_ops_in_a_row(calc: CalculatorModel) -> None:
    type_in(calc, "2+3+")
    assert calc.get_display() == "5"
    type_in(calc, "8=")
    assert calc.get_display() == "13"
    type_in(calc, "=")
    assert calc.get_display() == "21"


def test_two_calcs_in_a_row(calc: CalculatorModel) -> None:
    type_in(calc, "2+3=")
    assert calc.get_display() == "5"
    type_in(calc, "4+5=")
    assert calc.get_display() == "9"


def test_two_dots(calc: CalculatorModel) -> None:
    type_in(calc, "1..2")
    assert calc.get_display() == "1.2"


def test_division(calc: CalculatorModel) -> None:
    type_in(calc, "10/2=")
    assert calc.get_display() == "5"


def test_subtraction(calc: CalculatorModel) -> None:
    type_in(calc, "10-2=")
    assert calc.get_display() == "8"


def test_do_clear(calc: CalculatorModel) -> None:
    type_in(calc, "123C")
    assert calc.get_display() == "0"


def test_do_dot_after_equals(calc: CalculatorModel) -> None:
    type_in(calc, "1+1=.2")
    assert calc.get_display() == "0.2"


def test_replace_op_midway(calc: CalculatorModel) -> None:
    type_in(calc, "2+*")
    assert calc.get_display() == "2"
    type_in(calc, "3")
    assert calc.get_display() == "3"
    type_in(calc, "=")
    assert calc.get_display() == "6"


def test_start_with_op_minus(calc: CalculatorModel) -> None:
    type_in(calc, "-5")
    assert calc.get_display() == "5"
    type_in(calc, "=")
    assert calc.get_display() == "-5"


def test_start_with_op_mult(calc: CalculatorModel) -> None:
    type_in(calc, "*5")
    assert calc.get_display() == "5"
    type_in(calc, "=")
    assert calc.get_display() == "0"


def test_zero_division(calc: CalculatorModel) -> None:
    type_in(calc, "5/0=")
    assert calc.get_display() == "Nan"
