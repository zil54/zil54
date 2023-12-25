import pytest

def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num1) != int:
        raise Exception('We need to do fuzzy math on ints')
    if operator == '+':
         result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I dont know how to do math with '{operator}'")

    if result < 0:
        return 'A negative #'
    elif result < 10:
        return 'A small #'
    elif result < 20:
        return 'A mid-size #'
    else:
        return 'A big #'


class TestFuzzyMath:
    def test_non_int_input_for_num1(self):
        error = None
        try:
            fuzzy_math('hi', '+', 2)
        except Exception as e:
            error = e
        assert error is not None

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as j:
            fuzzy_math(2, '+', 'hi')
        assert 'need to do fuzzy math on ints' in str(j)

    def test_addition_neg_result(self):
        pass

    def test_addition_small_result(self):
        assert 'small' in fuzzy_math(2, '+', 2)



