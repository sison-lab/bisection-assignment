import bisection;

# Test whether it will work when solution is found exactly in the interior

def example_func(x):
  return 1-x**3

def test_bisection():
    assert bisection.bisection_algorithm(example_func, 0, 4, .01) == (1.734375, -0.008056640625, 7)
