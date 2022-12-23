

def test_add():
    from python_project_template.calculator.calculator import Calculator
    c = Calculator()
    test_result = c.add(a=1, b=2, c=3)
    expected_result = 6
    assert test_result == expected_result