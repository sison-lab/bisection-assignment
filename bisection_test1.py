import bisection;

def example_func(x):
  return 3-x**2

def test_bisection():
    location, error, number_of_tries = bisection.bisection_algorithm(example_func, 0, 2, .01) == (1.734375, -0.008056640625, 7)
    assert location = 1.734375
    assert error = -0.008056640625
    assert number_of_tries = 7
    assert bisection.bisection_algorithm(example_func, 0, 2, .01) == (1.734375, -0.008056640625, 7)
