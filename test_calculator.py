from calculator import Calculator


def test_add():
    calc = Calculator()
    res = calc.add(4, 5)
    assert res, 9


def test_mul():
    calc = Calculator()
    res = calc.mul(4, 5)
    assert res, 20


def test_sub():
    calc = Calculator()
    res = calc.sub(4, 5)
    assert res, -1


def test_div():
    calc = Calculator()
    res = calc.div(4, 5)
    assert res, 0.8


def test_add_triple():
    calc = Calculator()
    res = calc.add_triple(4, 5, 6)
    assert res, 15

def test_add_triple1():
    calc = Calculator()
    res = calc.add_triple(4, 5, 6)
    assert res, 15
