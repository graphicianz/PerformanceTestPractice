import pytest
import time

def something(duration=100):
    """
    Function that needs some serious benchmarking.
    """
    #time.sleep(duration)
    # You may return anything you want, like the result of a computation
    tmp = ''
    for i in range(duration):
        tmp += 'x'
    return 123

def test_my_stuff(benchmark):
    # benchmark something
    result = benchmark(something)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 123

def test_my_stuff_different_arg(benchmark):
    # benchmark something, but add some arguments
    result = benchmark(something, 1000000)
    assert result == 123

def test_my_stuff_different_arg2(benchmark):
    # benchmark something, but add some arguments
    result = benchmark(something, 10000)
    assert result == 123