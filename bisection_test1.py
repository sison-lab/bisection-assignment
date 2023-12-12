import bisection;

def example_func(x):
  return 3-x**2

def test_bisection():
    assert bisection.bisection_algorithm(example_func, 0, 2, .01) == (1.734375, -0.008056640625, 7)
