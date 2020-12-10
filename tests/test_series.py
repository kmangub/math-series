from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series



def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_at_2():
  actual = fibonacci(2)
  value = 1
  assert actual == value

def test_fibonacci_at_5():
  actual = fibonacci(5)
  value = 3
  assert actual == value

def test_fibonacci_at_25():
  actual = fibonacci(25)
  value = 46368
  assert actual == value

def test_lucas_at_1():
  actual = lucas(1)
  value = 2
  assert actual == value

def test_sum_series_at_7():
  actual = sum_series(7)
  value = 8
  assert actual == value

def test_sum_series_with_lucas_arguments_at_3():
  actual = sum_series(3, 2, 1)
  value = 3
  assert actual == value

def test_sum_series_with_optional_arguments_at_5():
  actual = sum_series(5, 3, 5)
  value = 21
  assert actual == value

