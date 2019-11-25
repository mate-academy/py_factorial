import factorial


def test_0():
    assert factorial.fact(0) == 1


def test_1():
    assert factorial.fact(1) == 1


def test_5():
    assert factorial.fact(5) == 120


def test_source():
    with open("factorial.py", 'rt') as f:
        source = f.read()
        assert "for" not in source
        assert "while" not in source
        assert "math" not in source
        assert "reduce" not in source